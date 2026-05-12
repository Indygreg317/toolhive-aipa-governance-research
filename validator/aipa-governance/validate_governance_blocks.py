#!/usr/bin/env python3
"""
AIPA MCP Governance Knowledge Block validator.

This validator checks MVP rules for example Knowledge Blocks, execution
receipts, policy blocks, server trust profiles, install governance records,
and scenario folders. It does not replace runtime policy enforcement,
cryptographic verification, external attestation, or live MCP integration.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

VALID_VERIFICATION_STATUSES = {"PASS", "FAIL", "UNSUPPORTED"}
VALID_POLICY_DECISIONS = {"approve", "deny", "escalate"}
VALID_DECISION_OUTPUTS = {"approved", "denied", "escalated"}
VALID_RISK_TIERS = {"low", "medium", "high"}

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
REQUIRED_RUNTIME_SCENARIO_FILES = {
    "request.json",
    "decision-context.json",
    "execution-receipt.json",
    "governance-record.json",
    "verification-boundary.map.json",
    "audit-package-summary.json",
}
REQUIRED_INSTALL_SCENARIO_FILES = {
    "server-capability-block.json",
    "server-trust-profile.json",
    "install-request.json",
    "approval-decision.json",
    "install-governance-record.json",
    "verification-boundary.map.json",
    "audit-package-summary.json",
}
REQUIRED_POLICY_BLOCK_FIELDS = {
    "policy_block_id",
    "artifact_type",
    "decision_type",
    "scope",
    "policy_reference",
    "conditions",
    "required_evidence",
    "human_oversight",
    "decision_output",
}
REQUIRED_SERVER_TRUST_PROFILE_FIELDS = {
    "trust_profile_id",
    "artifact_type",
    "mcp_server",
    "source_context",
    "capability_summary",
    "risk_tier",
    "trust_status",
    "policy_reference",
    "evidence_references",
    "review_context",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def add_missing_field_errors(errors: list[str], required: set[str], artifact: dict[str, Any], label: str) -> None:
    missing = sorted(required - artifact.keys())
    for field in missing:
        errors.append(f"missing required {label} field: {field}")


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


def get_nested_value(artifact: dict[str, Any], *keys: str) -> Any:
    current: Any = artifact
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def validate_governance_kb(artifact: dict[str, Any]) -> tuple[str, list[str]]:
    errors: list[str] = []

    add_missing_field_errors(errors, REQUIRED_KB_FIELDS, artifact, "Knowledge Block")
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

    add_missing_field_errors(errors, REQUIRED_RECEIPT_FIELDS, artifact, "execution receipt")

    status = artifact.get("verification_status")
    if status not in VALID_VERIFICATION_STATUSES:
        errors.append("verification_status must be PASS, FAIL, or UNSUPPORTED")

    if "policy_reference" in artifact:
        errors.extend(validate_policy_reference(artifact))

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_policy_block(artifact: dict[str, Any]) -> tuple[str, list[str]]:
    errors: list[str] = []

    add_missing_field_errors(errors, REQUIRED_POLICY_BLOCK_FIELDS, artifact, "policy block")
    errors.extend(validate_policy_reference(artifact))

    decision_type = artifact.get("decision_type")
    if decision_type not in VALID_POLICY_DECISIONS:
        errors.append("decision_type must be approve, deny, or escalate")

    scope = artifact.get("scope")
    if not isinstance(scope, dict):
        errors.append("scope must be an object")
    else:
        if scope.get("risk_tier") not in VALID_RISK_TIERS:
            errors.append("scope.risk_tier must be low, medium, or high")

    conditions = artifact.get("conditions")
    if not isinstance(conditions, dict):
        errors.append("conditions must be an object")
    else:
        for key in ("required", "prohibited", "escalation_triggers"):
            if not isinstance(conditions.get(key), list):
                errors.append(f"conditions.{key} must be a list")

    required_evidence = artifact.get("required_evidence")
    if not isinstance(required_evidence, list) or not required_evidence:
        errors.append("required_evidence must be a non-empty list")

    human_oversight = artifact.get("human_oversight")
    risk_tier = get_nested_value(artifact, "scope", "risk_tier")
    operation_type = get_nested_value(artifact, "scope", "operation_type")
    if not isinstance(human_oversight, dict):
        errors.append("human_oversight must be an object")
    elif risk_tier == "high" or operation_type in {"write", "delete", "bulk_export"}:
        if human_oversight.get("required") is not True:
            errors.append("high-risk or sensitive policy blocks must require human oversight")

    decision_output = artifact.get("decision_output")
    if not isinstance(decision_output, dict):
        errors.append("decision_output must be an object")
    else:
        if decision_output.get("decision") not in VALID_DECISION_OUTPUTS:
            errors.append("decision_output.decision must be approved, denied, or escalated")
        if decision_output.get("review_outcome") not in VALID_VERIFICATION_STATUSES:
            errors.append("decision_output.review_outcome must be PASS, FAIL, or UNSUPPORTED")

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_server_trust_profile(artifact: dict[str, Any]) -> tuple[str, list[str]]:
    errors: list[str] = []

    add_missing_field_errors(errors, REQUIRED_SERVER_TRUST_PROFILE_FIELDS, artifact, "server trust profile")
    errors.extend(validate_policy_reference(artifact))

    mcp_server = artifact.get("mcp_server")
    if not isinstance(mcp_server, dict) or not mcp_server.get("server_id"):
        errors.append("server trust profile must include mcp_server.server_id")

    if artifact.get("risk_tier") not in VALID_RISK_TIERS:
        errors.append("risk_tier must be low, medium, or high")

    trust_status = artifact.get("trust_status")
    if trust_status not in {"approved", "denied", "escalated", "unsupported"}:
        errors.append("trust_status must be approved, denied, escalated, or unsupported")

    capability_summary = artifact.get("capability_summary")
    if not isinstance(capability_summary, dict):
        errors.append("capability_summary must be an object")
    else:
        capabilities = capability_summary.get("capabilities")
        if not isinstance(capabilities, list) or not capabilities:
            errors.append("capability_summary.capabilities must be a non-empty list")

    review_context = artifact.get("review_context")
    if not isinstance(review_context, dict):
        errors.append("review_context must be an object")
    elif artifact.get("risk_tier") == "high":
        if review_context.get("review_required") is not True:
            errors.append("high-risk server trust profiles must require review")
        if not review_context.get("review_status"):
            errors.append("review_context.review_status is required")

    evidence_references = artifact.get("evidence_references")
    if not isinstance(evidence_references, list) or not evidence_references:
        errors.append("evidence_references must be a non-empty list")

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_install_governance_record(artifact: dict[str, Any]) -> tuple[str, list[str]]:
    errors: list[str] = []

    required = {
        "governance_record_id",
        "artifact_type",
        "created_at",
        "mcp_server_id",
        "install_decision",
        "policy_reference",
        "governance_claims",
        "human_review",
        "evidence_references",
        "expected_reviewer_outcome",
    }
    add_missing_field_errors(errors, required, artifact, "install governance record")
    errors.extend(validate_policy_reference(artifact))

    install_decision = artifact.get("install_decision")
    if not isinstance(install_decision, dict):
        errors.append("install_decision must be an object")
    elif install_decision.get("decision") not in {"approved", "denied", "escalated"}:
        errors.append("install_decision.decision must be approved, denied, or escalated")

    human_review = artifact.get("human_review")
    if not isinstance(human_review, dict):
        errors.append("human_review must be an object")
    else:
        if human_review.get("required") is not True:
            errors.append("install governance record must require human review in this MVP")
        if human_review.get("review_status") not in {"approved", "denied", "rejected", "escalated"}:
            errors.append("human_review.review_status must be approved, denied, rejected, or escalated")

    evidence_references = artifact.get("evidence_references")
    if not isinstance(evidence_references, list) or not evidence_references:
        errors.append("evidence_references must be a non-empty list")

    expected = artifact.get("expected_reviewer_outcome")
    if expected not in VALID_VERIFICATION_STATUSES:
        errors.append("expected_reviewer_outcome must be PASS, FAIL, or UNSUPPORTED")

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_runtime_scenario_folder(path: Path) -> tuple[str, list[str]]:
    errors: list[str] = []

    missing_files = sorted(name for name in REQUIRED_RUNTIME_SCENARIO_FILES if not (path / name).is_file())
    for name in missing_files:
        errors.append(f"missing required runtime scenario file: {name}")

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
        get_nested_value(governance_record, "identity_context", "agent_id"),
        get_nested_value(boundary_map, "identity_context", "agent_id"),
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


def validate_install_scenario_folder(path: Path) -> tuple[str, list[str]]:
    errors: list[str] = []

    missing_files = sorted(name for name in REQUIRED_INSTALL_SCENARIO_FILES if not (path / name).is_file())
    for name in missing_files:
        errors.append(f"missing required install scenario file: {name}")

    if errors:
        return "FAIL", errors

    capability = load_json(path / "server-capability-block.json")
    trust_profile = load_json(path / "server-trust-profile.json")
    install_request = load_json(path / "install-request.json")
    approval_decision = load_json(path / "approval-decision.json")
    install_record = load_json(path / "install-governance-record.json")
    boundary_map = load_json(path / "verification-boundary.map.json")
    audit_package = load_json(path / "audit-package-summary.json")

    trust_status, trust_errors = validate_server_trust_profile(trust_profile)
    if trust_status == "FAIL":
        errors.extend(f"server-trust-profile.json: {message}" for message in trust_errors)

    record_status, record_errors = validate_install_governance_record(install_record)
    if record_status == "FAIL":
        errors.extend(f"install-governance-record.json: {message}" for message in record_errors)

    mcp_server_ids = {
        get_nested_value(capability, "mcp_server", "server_id"),
        get_nested_value(trust_profile, "mcp_server", "server_id"),
        install_request.get("mcp_server_id"),
        install_record.get("mcp_server_id"),
        get_nested_value(audit_package, "governed_install_decision", "mcp_server_id"),
    }
    mcp_server_ids.discard(None)
    if not mcp_server_ids:
        errors.append("install scenario must include mcp_server_id")
    elif len(mcp_server_ids) > 1:
        errors.append("mcp_server_id must remain consistent across install scenario artifacts")

    install_request_id = install_request.get("install_request_id")
    if approval_decision.get("related_install_request_id") != install_request_id:
        errors.append("approval decision must reference the install_request_id")
    if install_record.get("related_install_request_id") != install_request_id:
        errors.append("install governance record must reference the install_request_id")

    policy_fingerprints = {
        get_policy_fingerprint(trust_profile),
        get_policy_fingerprint(approval_decision),
        get_policy_fingerprint(install_record),
        get_policy_fingerprint(boundary_map),
        get_policy_fingerprint(audit_package),
    }
    policy_fingerprints.discard(None)
    if not policy_fingerprints:
        errors.append("install scenario must include at least one policy_fingerprint")
    elif len(policy_fingerprints) > 1:
        errors.append("policy_fingerprint must remain consistent across install scenario artifacts")

    risk_tier = get_nested_value(audit_package, "governed_install_decision", "risk_tier")
    if risk_tier == "high":
        human_review = install_record.get("human_review", {})
        if human_review.get("required") is not True:
            errors.append("high-risk install scenario must require human review")
        if human_review.get("review_status") not in {"approved", "denied", "rejected", "escalated"}:
            errors.append("high-risk install scenario must include human review status")

    evidence_inputs = boundary_map.get("evidence_inputs")
    if not isinstance(evidence_inputs, list) or not evidence_inputs:
        errors.append("install verification boundary map must include evidence_inputs")

    expected_outcome = get_nested_value(audit_package, "governed_install_decision", "expected_reviewer_outcome")
    if expected_outcome not in VALID_VERIFICATION_STATUSES:
        errors.append("audit package governed_install_decision.expected_reviewer_outcome must be PASS, FAIL, or UNSUPPORTED")

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_scenario_folder(path: Path) -> tuple[str, list[str]]:
    if (path / "install-request.json").is_file():
        return validate_install_scenario_folder(path)
    return validate_runtime_scenario_folder(path)


def validate_artifact(path: Path) -> tuple[str, list[str]]:
    if path.is_dir():
        return validate_scenario_folder(path)

    artifact = load_json(path)
    artifact_type = artifact.get("artifact_type")

    if artifact_type == "mcp_governance_knowledge_block":
        return validate_governance_kb(artifact)

    if artifact_type == "server_trust_profile":
        return validate_server_trust_profile(artifact)

    if artifact_type == "tool_approval_policy_block":
        return validate_policy_block(artifact)

    if artifact_type == "mcp_server_install_governance_record":
        return validate_install_governance_record(artifact)

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
