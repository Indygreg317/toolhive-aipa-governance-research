#!/usr/bin/env python3
"""
Minimal AIPA MCP Governance Knowledge Block validator.

This validator is intentionally small. It checks the MVP rules for example
Knowledge Blocks and execution receipts. It does not replace runtime policy
enforcement or external verification.
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


def validate_artifact(path: Path) -> tuple[str, list[str]]:
    artifact = load_json(path)
    artifact_type = artifact.get("artifact_type")

    if artifact_type == "mcp_governance_knowledge_block":
        return validate_governance_kb(artifact)

    if "receipt_id" in artifact:
        return validate_execution_receipt(artifact)

    return "UNSUPPORTED", [f"unsupported artifact type in {path.name}"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AIPA MCP governance example artifacts.")
    parser.add_argument("paths", nargs="+", help="JSON artifact file paths to validate")
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
