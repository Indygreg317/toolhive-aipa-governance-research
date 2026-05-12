#!/usr/bin/env python3
"""
AIPA MCP Governance Knowledge Block validator.

This validator checks MVP rules for example Knowledge Blocks, execution
receipts, and scenario folders. It does not replace runtime policy enforcement,
cryptographic verification, external attestation, or live MCP integration.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

VALID_VERIFICATION_STATUSES = {"PASS", "FAIL", "UNSUPPORTED"}
REQUIRED_KB_FIELDS = {
    "kb_id",
    "artifact_type",
    "mcp_server",
    "risk_tier",
    "allowed_use",
    "prohibited_use",
    "human_oversight",
    "policy_reference",
    "identity_context",
    "execution_boundary",
    "evidence_required",
    "audit_outputs",
    "validation_logic",
}
REQUIRED_RECEIPT_FIELDS = {
    "receipt_id",
    "timestamp",
    "agent_id",
    "mcp_server_id",
    "tool_name",
    "input_hash",
    "output_hash",
    "policy_decision",
    "verification_status",
}
REQUIRED_SCENARIO_FILES = {
    "request.json",
    "decision-context.json",
    "execution-receipt.json",
    "governance-record.json",
    "verification-boundary.map.json",
    "audit-package-summary.json",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_policy_reference(artifact: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    policy_reference = artifact.get("policy_reference")
    if not isinstance(policy_reference, dict):
        return ["policy_reference must be an object"]
    if not policy_reference.get("policy_fingerprint"):
        errors.append("policy_reference.policy_fingerprint is required")
    return errors


def get_policy_fingerprint(artifact: dict[str, Any]) -> str | None:
    policy_reference = artifact.get("policy_reference")
    if isinstance(policy_reference, dict):
        value = policy_reference.get("policy_fingerprint")
        return value if isinstance(value, str) else None
    return None


def validate_governance_kb(artifact: dict[str, Any]) -> tuple[str, list[str]]:
    errors: list[str] = []

    missing = sorted(REQUIRED_KB_FIELDS - artifact.keys())
    for field in missing:
        errors.append(f"missing required Knowledge Block field: {field}")

    errors.extend(validate_policy_reference(artifact))

    mcp_server = artifact.get("mcp_server", {})
    if not isinstance(mcp_server, dict) or not mcp_server.get("server_id"):
        errors.append("Every MCP server must have a governance Knowledge Block with mcp_server.server_id")

    risk_tier = artifact.get("risk_tier")
    prohibited_use = artifact.get("prohibited_use")
    human_oversight = artifact.get("human_oversight")

    if risk_tier == "high":
        if not isinstance(prohibited_use, list) or not prohibited_use:
            errors.append("Every high-risk tool must define prohibited_use")
        if not isinstance(human_oversight, dict):
            errors.append("Every high-risk tool must define human_oversight")
        else:
            oversight_required = human_oversight.get("required")
            exception_rationale = human_oversight.get("exception_rationale")
            if oversight_required is not True and not exception_rationale:
                errors.append("Every high-risk tool must require human oversight or explain why not")

    execution_boundary = artifact.get("execution_boundary")
    if not isinstance(execution_boundary, dict) or not execution_boundary.get("boundary_id"):
        errors.append("Every tool must define a verification boundary using execution_boundary.boundary_id")

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_execution_receipt(artifact: dict[str, Any]) -> tuple[str, list[str]]:
    errors: list[str] = []

    missing = sorted(REQUIRED_RECEIPT_FIELDS - artifact.keys())
    for field in missing:
        errors.append(f"missing required execution receipt field: {field}")

    status = artifact.get("verification_status")
    if status not in VALID_VERIFICATION_STATUSES:
        errors.append("verification_status must be PASS, FAIL, or UNSUPPORTED")

    if "policy_reference" in artifact:
        errors.extend(validate_policy_reference(artifact))

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_scenario_folder(path: Path) -> tuple[str, list[str]]:
    errors: list[str] = []

    missing_files = sorted(name for name in REQUIRED_SCENARIO_FILES if not (path / name).is_file())
    for name in missing_files:
        errors.append(f"missing required scenario file: {name}")

    if errors:
        return "FAIL", errors

    request = load_json(path / "request.json")
    decision_context = load_json(path / "decision-context.json")
    receipt = load_json(path / "execution-receipt.json")
    governance_record = load_json(path / "governance-record.json")
    boundary_map = load_json(path / "verification-boundary.map.json")
    audit_package = load_json(path / "audit-package-summary.json")

    receipt_status, receipt_errors = validate_execution_receipt(receipt)
    if receipt_status == "FAIL":
        errors.extend(f"execution-receipt.json: {message}" for message in receipt_errors)

    request_id = request.get("request_id")
    decision_request_id = decision_context.get("related_request_id")
    governance_request_id = governance_record.get("related_request_id")
    if request_id and len({request_id, decision_request_id, governance_request_id}) != 1:
        errors.append("request_id must match across request, decision context, and governance record")

    agent_ids = {
        request.get("agent_id"),
        receipt.get("agent_id"),
        governance_record.get("identity_context", {}).get("agent_id"),
        boundary_map.get("identity_context", {}).get("agent_id"),
    }
    agent_ids.discard(None)
    if len(agent_ids) > 1:
        errors.append("agent_id must remain consistent across scenario artifacts")

    policy_fingerprints = {
        get_policy_fingerprint(decision_context),
        get_policy_fingerprint(receipt),
        get_policy_fingerprint(governance_record),
        get_policy_fingerprint(boundary_map),
        get_policy_fingerprint(audit_package),
    }
    policy_fingerprints.discard(None)
    if not policy_fingerprints:
        errors.append("scenario must include at least one policy_fingerprint")
    elif len(policy_fingerprints) > 1:
        errors.append("policy_fingerprint must remain consistent across scenario artifacts")

    governed_tool_use = audit_package.get("governed_tool_use", {})
    if governed_tool_use.get("mcp_server_id") != receipt.get("mcp_server_id"):
        errors.append("audit package mcp_server_id must match execution receipt")
    if governed_tool_use.get("tool_name") != receipt.get("tool_name"):
        errors.append("audit package tool_name must match execution receipt")

    risk_tier = governed_tool_use.get("risk_tier")
    operation_type = governed_tool_use.get("operation_type")
    oversight_record = governance_record.get("oversight_record", {})
    if risk_tier == "high" or operation_type in {"write", "delete", "bulk_export"}:
        if oversight_record.get("required") is not True:
            errors.append("high-risk scenario or write operation must require human oversight")
        if oversight_record.get("review_status") not in {"approved", "rejected", "escalated"}:
            errors.append("human oversight record must include review_status")

    evidence_inputs = boundary_map.get("evidence_inputs")
    if not isinstance(evidence_inputs, list) or not evidence_inputs:
        errors.append("verification boundary map must include evidence_inputs")

    expected_outcome = audit_package.get("expected_reviewer_outcome")
    if expected_outcome not in VALID_VERIFICATION_STATUSES:
        errors.append("audit package expected_reviewer_outcome must be PASS, FAIL, or UNSUPPORTED")

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_artifact(path: Path) -> tuple[str, list[str]]:
    if path.is_dir():
        return validate_scenario_folder(path)

    artifact = load_json(path)
    artifact_type = artifact.get("artifact_type")

    if artifact_type == "mcp_governance_knowledge_block":
        return validate_governance_kb(artifact)

    if "receipt_id" in artifact:
        return validate_execution_receipt(artifact)

    return "UNSUPPORTED", [f"unsupported artifact type in {path.name}"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AIPA MCP governance example artifacts and scenario folders.")
    parser.add_argument("paths", nargs="+", help="JSON artifact file paths or scenario folders to validate")
    args = parser.parse_args()

    exit_code = 0
    for raw_path in args.paths:
        path = Path(raw_path)
        try:
            status, messages = validate_artifact(path)
        except json.JSONDecodeError as error:
            status = "FAIL"
            messages = [f"invalid JSON: {error}"]
        except OSError as error:
            status = "FAIL"
            messages = [f"could not read file: {error}"]

        print(f"{status}: {path}")
        for message in messages:
            print(f"  - {message}")

        if status == "FAIL":
            exit_code = 1

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
