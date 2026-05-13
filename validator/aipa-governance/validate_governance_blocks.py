#!/usr/bin/env python3
"""
AIPA MCP Governance Knowledge Block validator.

This validator checks structural correctness for the AIPA MCP governance
research overlay. It validates example artifacts and scenario folders without
claiming runtime enforcement, cryptographic verification, external attestation,
or live MCP integration.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

VALID_REVIEW_OUTCOMES = {"PASS", "FAIL", "UNSUPPORTED"}
VALID_POLICY_DECISIONS = {"approve", "deny", "escalate"}
VALID_DECISION_OUTPUTS = {"approved", "denied", "escalated"}
VALID_RISK_TIERS = {"low", "medium", "high"}

REQUIRED_KB_FIELDS = {
    "kb_id", "artifact_type", "mcp_server", "risk_tier", "allowed_use",
    "prohibited_use", "human_oversight", "policy_reference", "identity_context",
    "execution_boundary", "evidence_required", "audit_outputs", "validation_logic",
}
REQUIRED_RECEIPT_FIELDS = {
    "receipt_id", "timestamp", "agent_id", "mcp_server_id", "tool_name",
    "input_hash", "output_hash", "policy_decision", "verification_status",
}
REQUIRED_RUNTIME_SCENARIO_FILES = {
    "request.json", "decision-context.json", "execution-receipt.json",
    "governance-record.json", "verification-boundary.map.json", "audit-package-summary.json",
}
REQUIRED_INSTALL_BASE_FILES = {
    "server-capability-block.json", "server-trust-profile.json", "install-request.json",
    "install-governance-record.json", "verification-boundary.map.json", "audit-package-summary.json",
}
REQUIRED_UNSUPPORTED_FILES = {
    "request.json", "governance-record.json", "verification-boundary.map.json", "audit-package-summary.json",
}
REQUIRED_POLICY_BLOCK_FIELDS = {
    "policy_block_id", "artifact_type", "decision_type", "scope", "policy_reference",
    "conditions", "required_evidence", "human_oversight", "decision_output",
}
REQUIRED_TRUST_PROFILE_FIELDS = {
    "trust_profile_id", "artifact_type", "mcp_server", "source_context",
    "capability_summary", "risk_tier", "trust_status", "policy_reference",
    "evidence_references", "review_context",
}
REQUIRED_HANDOFF_FIELDS = {
    "handoff_package_id", "artifact_type", "version", "scenario_type",
    "governance_record_reference", "policy_reference", "expected_governance_outcome",
    "verification_boundary_reference", "audit_package_reference", "evidence_references",
    "unsupported_claims", "review_notes",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def missing(errors: list[str], required: set[str], artifact: dict[str, Any], label: str) -> None:
    for field in sorted(required - artifact.keys()):
        errors.append(f"missing required {label} field: {field}")


def nested(artifact: dict[str, Any], *keys: str) -> Any:
    current: Any = artifact
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def policy_fingerprint(artifact: dict[str, Any]) -> str | None:
    value = nested(artifact, "policy_reference", "policy_fingerprint")
    return value if isinstance(value, str) and value else None


def validate_policy_reference(artifact: dict[str, Any]) -> list[str]:
    ref = artifact.get("policy_reference")
    if not isinstance(ref, dict):
        return ["policy_reference must be an object"]
    if not ref.get("policy_id"):
        return ["policy_reference.policy_id is required"]
    if not ref.get("policy_fingerprint"):
        return ["policy_reference.policy_fingerprint is required"]
    return []


def validate_governance_kb(artifact: dict[str, Any]) -> tuple[str, list[str]]:
    errors: list[str] = []
    missing(errors, REQUIRED_KB_FIELDS, artifact, "Knowledge Block")
    errors.extend(validate_policy_reference(artifact))

    if not nested(artifact, "mcp_server", "server_id"):
        errors.append("mcp_server.server_id is required")

    if artifact.get("risk_tier") == "high":
        if not artifact.get("prohibited_use"):
            errors.append("high-risk tools must define prohibited_use")
        oversight = artifact.get("human_oversight")
        if not isinstance(oversight, dict) or oversight.get("required") is not True:
            errors.append("high-risk tools must require human oversight")

    if not nested(artifact, "execution_boundary", "boundary_id"):
        errors.append("execution_boundary.boundary_id is required")

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_execution_receipt(artifact: dict[str, Any]) -> tuple[str, list[str]]:
    errors: list[str] = []
    missing(errors, REQUIRED_RECEIPT_FIELDS, artifact, "execution receipt")
    if artifact.get("verification_status") not in VALID_REVIEW_OUTCOMES:
        errors.append("verification_status must be PASS, FAIL, or UNSUPPORTED")
    if "policy_reference" in artifact:
        errors.extend(validate_policy_reference(artifact))
    return ("FAIL", errors) if errors else ("PASS", [])


def validate_policy_block(artifact: dict[str, Any]) -> tuple[str, list[str]]:
    errors: list[str] = []
    missing(errors, REQUIRED_POLICY_BLOCK_FIELDS, artifact, "policy block")
    errors.extend(validate_policy_reference(artifact))

    if artifact.get("decision_type") not in VALID_POLICY_DECISIONS:
        errors.append("decision_type must be approve, deny, or escalate")
    if nested(artifact, "scope", "risk_tier") not in VALID_RISK_TIERS:
        errors.append("scope.risk_tier must be low, medium, or high")

    conditions = artifact.get("conditions")
    if not isinstance(conditions, dict):
        errors.append("conditions must be an object")
    else:
        for key in ("required", "prohibited", "escalation_triggers"):
            if not isinstance(conditions.get(key), list):
                errors.append(f"conditions.{key} must be a list")

    if not artifact.get("required_evidence"):
        errors.append("required_evidence must be a non-empty list")

    if nested(artifact, "scope", "risk_tier") == "high":
        if nested(artifact, "human_oversight", "required") is not True:
            errors.append("high-risk policy blocks must require human oversight")

    if nested(artifact, "decision_output", "decision") not in VALID_DECISION_OUTPUTS:
        errors.append("decision_output.decision must be approved, denied, or escalated")
    if nested(artifact, "decision_output", "review_outcome") not in VALID_REVIEW_OUTCOMES:
        errors.append("decision_output.review_outcome must be PASS, FAIL, or UNSUPPORTED")

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_server_trust_profile(artifact: dict[str, Any]) -> tuple[str, list[str]]:
    errors: list[str] = []
    missing(errors, REQUIRED_TRUST_PROFILE_FIELDS, artifact, "server trust profile")
    errors.extend(validate_policy_reference(artifact))

    if not nested(artifact, "mcp_server", "server_id"):
        errors.append("mcp_server.server_id is required")
    if artifact.get("risk_tier") not in VALID_RISK_TIERS:
        errors.append("risk_tier must be low, medium, or high")
    if artifact.get("trust_status") not in {"approved", "denied", "escalated", "unsupported"}:
        errors.append("trust_status must be approved, denied, escalated, or unsupported")
    if not nested(artifact, "capability_summary", "capabilities"):
        errors.append("capability_summary.capabilities must be a non-empty list")
    if artifact.get("risk_tier") == "high" and nested(artifact, "review_context", "review_required") is not True:
        errors.append("high-risk server trust profiles must require review")
    if not artifact.get("evidence_references"):
        errors.append("evidence_references must be a non-empty list")

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_install_governance_record(artifact: dict[str, Any]) -> tuple[str, list[str]]:
    errors: list[str] = []
    required = {
        "governance_record_id", "artifact_type", "created_at", "mcp_server_id",
        "install_decision", "policy_reference", "governance_claims", "human_review",
        "evidence_references", "expected_reviewer_outcome",
    }
    missing(errors, required, artifact, "install governance record")
    errors.extend(validate_policy_reference(artifact))

    if nested(artifact, "install_decision", "decision") not in {"approved", "denied", "escalated"}:
        errors.append("install_decision.decision must be approved, denied, or escalated")
    if nested(artifact, "human_review", "required") is not True:
        errors.append("install governance record must require human review")
    if nested(artifact, "human_review", "review_status") not in {"approved", "denied", "rejected", "escalated", "unsupported"}:
        errors.append("human_review.review_status must be approved, denied, rejected, escalated, or unsupported")
    if not artifact.get("evidence_references"):
        errors.append("evidence_references must be a non-empty list")
    if artifact.get("expected_reviewer_outcome") not in VALID_REVIEW_OUTCOMES:
        errors.append("expected_reviewer_outcome must be PASS, FAIL, or UNSUPPORTED")

    return ("FAIL", errors) if errors else ("PASS", [])


def referenced_paths_from_handoff(artifact: dict[str, Any]) -> list[str]:
    paths: list[str] = []
    for key in ("governance_record_reference", "verification_boundary_reference", "audit_package_reference"):
        value = artifact.get(key)
        if isinstance(value, dict) and isinstance(value.get("path"), str):
            paths.append(value["path"])
    for ref in artifact.get("evidence_references", []):
        if isinstance(ref, dict) and isinstance(ref.get("path"), str):
            paths.append(ref["path"])
    return paths


def validate_review_handoff_package(path: Path, artifact: dict[str, Any]) -> tuple[str, list[str]]:
    errors: list[str] = []
    missing(errors, REQUIRED_HANDOFF_FIELDS, artifact, "review handoff package")
    errors.extend(validate_policy_reference(artifact))

    if artifact.get("expected_governance_outcome") not in VALID_REVIEW_OUTCOMES:
        errors.append("expected_governance_outcome must be PASS, FAIL, or UNSUPPORTED")
    if not isinstance(artifact.get("evidence_references"), list) or not artifact.get("evidence_references"):
        errors.append("evidence_references must be a non-empty list")
    if not isinstance(artifact.get("unsupported_claims"), list):
        errors.append("unsupported_claims must be a list")

    repo_root = path.resolve().parents[2]
    fingerprints = {policy_fingerprint(artifact)}
    fingerprints.discard(None)

    for relative in referenced_paths_from_handoff(artifact):
        referenced_path = repo_root / relative
        if not referenced_path.is_file():
            errors.append(f"referenced path does not exist: {relative}")
            continue
        try:
            referenced_artifact = load_json(referenced_path)
        except (json.JSONDecodeError, OSError) as error:
            errors.append(f"could not inspect referenced artifact {relative}: {error}")
            continue
        fingerprint = policy_fingerprint(referenced_artifact)
        if fingerprint:
            fingerprints.add(fingerprint)

    if not fingerprints:
        errors.append("review handoff package must include at least one policy_fingerprint")
    elif len(fingerprints) > 1:
        errors.append("policy_fingerprint must remain consistent across review handoff package artifacts")

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_runtime_scenario(path: Path) -> tuple[str, list[str]]:
    errors: list[str] = []
    for name in sorted(REQUIRED_RUNTIME_SCENARIO_FILES):
        if not (path / name).is_file():
            errors.append(f"missing required runtime scenario file: {name}")
    if errors:
        return "FAIL", errors

    request = load_json(path / "request.json")
    decision_context = load_json(path / "decision-context.json")
    receipt = load_json(path / "execution-receipt.json")
    governance_record = load_json(path / "governance-record.json")
    boundary_map = load_json(path / "verification-boundary.map.json")
    audit_package = load_json(path / "audit-package-summary.json")

    status, receipt_errors = validate_execution_receipt(receipt)
    if status == "FAIL":
        errors.extend(f"execution-receipt.json: {message}" for message in receipt_errors)

    request_id = request.get("request_id")
    if request_id and len({request_id, decision_context.get("related_request_id"), governance_record.get("related_request_id")}) != 1:
        errors.append("request_id must match across runtime scenario artifacts")

    fingerprints = {policy_fingerprint(decision_context), policy_fingerprint(receipt), policy_fingerprint(governance_record), policy_fingerprint(boundary_map), policy_fingerprint(audit_package)}
    fingerprints.discard(None)
    if not fingerprints:
        errors.append("scenario must include at least one policy_fingerprint")
    elif len(fingerprints) > 1:
        errors.append("policy_fingerprint must remain consistent across runtime scenario artifacts")

    if not boundary_map.get("evidence_inputs"):
        errors.append("verification boundary map must include evidence_inputs")
    if audit_package.get("expected_reviewer_outcome") not in VALID_REVIEW_OUTCOMES:
        errors.append("audit package expected_reviewer_outcome must be PASS, FAIL, or UNSUPPORTED")

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_install_scenario(path: Path) -> tuple[str, list[str]]:
    errors: list[str] = []
    decision_file = None
    if (path / "approval-decision.json").is_file():
        decision_file = "approval-decision.json"
    elif (path / "denial-decision.json").is_file():
        decision_file = "denial-decision.json"

    for name in sorted(REQUIRED_INSTALL_BASE_FILES):
        if not (path / name).is_file():
            errors.append(f"missing required install scenario file: {name}")
    if decision_file is None:
        errors.append("missing required install scenario file: approval-decision.json or denial-decision.json")
    if errors:
        return "FAIL", errors

    capability = load_json(path / "server-capability-block.json")
    trust_profile = load_json(path / "server-trust-profile.json")
    install_request = load_json(path / "install-request.json")
    decision = load_json(path / decision_file)
    install_record = load_json(path / "install-governance-record.json")
    boundary_map = load_json(path / "verification-boundary.map.json")
    audit_package = load_json(path / "audit-package-summary.json")

    status, trust_errors = validate_server_trust_profile(trust_profile)
    if status == "FAIL":
        errors.extend(f"server-trust-profile.json: {message}" for message in trust_errors)
    status, record_errors = validate_install_governance_record(install_record)
    if status == "FAIL":
        errors.extend(f"install-governance-record.json: {message}" for message in record_errors)

    server_ids = {nested(capability, "mcp_server", "server_id"), nested(trust_profile, "mcp_server", "server_id"), install_request.get("mcp_server_id"), install_record.get("mcp_server_id"), nested(audit_package, "governed_install_decision", "mcp_server_id")}
    server_ids.discard(None)
    if not server_ids:
        errors.append("install scenario must include mcp_server_id")
    elif len(server_ids) > 1:
        errors.append("mcp_server_id must remain consistent across install scenario artifacts")

    install_request_id = install_request.get("install_request_id")
    if decision.get("related_install_request_id") != install_request_id:
        errors.append("install decision must reference the install_request_id")
    if install_record.get("related_install_request_id") != install_request_id:
        errors.append("install governance record must reference the install_request_id")

    fingerprints = {policy_fingerprint(trust_profile), policy_fingerprint(decision), policy_fingerprint(install_record), policy_fingerprint(boundary_map), policy_fingerprint(audit_package)}
    fingerprints.discard(None)
    if not fingerprints:
        errors.append("install scenario must include at least one policy_fingerprint")
    elif len(fingerprints) > 1:
        errors.append("policy_fingerprint must remain consistent across install scenario artifacts")

    if nested(audit_package, "governed_install_decision", "risk_tier") == "high":
        if nested(install_record, "human_review", "required") is not True:
            errors.append("high-risk install scenario must require human review")
        if nested(install_record, "human_review", "review_status") not in {"approved", "denied", "rejected", "escalated", "unsupported"}:
            errors.append("high-risk install scenario must include human review status")

    if not boundary_map.get("evidence_inputs"):
        errors.append("install verification boundary map must include evidence_inputs")
    if nested(audit_package, "governed_install_decision", "expected_reviewer_outcome") not in VALID_REVIEW_OUTCOMES:
        errors.append("audit package expected reviewer outcome must be PASS, FAIL, or UNSUPPORTED")

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_unsupported_scenario(path: Path) -> tuple[str, list[str]]:
    errors: list[str] = []
    for name in sorted(REQUIRED_UNSUPPORTED_FILES):
        if not (path / name).is_file():
            errors.append(f"missing required unsupported scenario file: {name}")
    if errors:
        return "FAIL", errors

    request = load_json(path / "request.json")
    governance_record = load_json(path / "governance-record.json")
    boundary_map = load_json(path / "verification-boundary.map.json")
    audit_package = load_json(path / "audit-package-summary.json")

    if governance_record.get("related_request_id") != request.get("request_id"):
        errors.append("governance record must reference the request_id")

    fingerprints = {policy_fingerprint(governance_record), policy_fingerprint(boundary_map), policy_fingerprint(audit_package)}
    fingerprints.discard(None)
    if not fingerprints:
        errors.append("unsupported scenario must include at least one policy_fingerprint")
    elif len(fingerprints) > 1:
        errors.append("policy_fingerprint must remain consistent across unsupported scenario artifacts")

    if not boundary_map.get("evidence_inputs"):
        errors.append("unsupported verification boundary map must include evidence_inputs")
    if nested(audit_package, "governed_review", "expected_reviewer_outcome") != "UNSUPPORTED":
        errors.append("unsupported scenario expected reviewer outcome must be UNSUPPORTED")
    if not audit_package.get("unsupported_items"):
        errors.append("unsupported scenario must include unsupported_items")

    return ("FAIL", errors) if errors else ("PASS", [])


def validate_scenario_folder(path: Path) -> tuple[str, list[str]]:
    if (path / "install-request.json").is_file():
        return validate_install_scenario(path)
    if (path / "governance-record.json").is_file() and not (path / "decision-context.json").is_file():
        return validate_unsupported_scenario(path)
    return validate_runtime_scenario(path)


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
    if artifact_type == "review_handoff_package":
        return validate_review_handoff_package(path, artifact)
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
