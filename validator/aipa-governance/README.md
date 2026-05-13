# AIPA Governance Validator

This directory contains a minimal validator for the AIPA MCP governance research overlay.

The validator checks whether example governance artifacts contain the required MVP fields and whether their validation status uses the expected AIPA outcomes. It also supports scenario-folder validation for end-to-end demo packages.

The current v0.1 validation manifest covers all six shipped scenario folders.

## Outcome model

The AIPA governance overlay uses three governance outcomes:

```text
PASS
FAIL
UNSUPPORTED
```

The demo validation path separates two concepts:

```text
structural validation
expected governance outcome
```

Structural validation answers:

```text
Is the artifact or scenario shaped correctly enough to review?
```

Expected governance outcome answers:

```text
What should the review conclusion be?
```

This matters because a structurally valid `FAIL` scenario should not break CI when `FAIL` is the expected governance outcome.

Likewise, a structurally valid `UNSUPPORTED` scenario should not break CI when `UNSUPPORTED` is the expected governance outcome.

## What it checks

### MCP Governance Knowledge Blocks

For MCP Governance Knowledge Blocks, the validator checks that:

- required Knowledge Block fields are present
- every MCP server has a governance Knowledge Block identifier
- high-risk tools define prohibited use
- high-risk tools require human oversight or explain why not
- tools define an execution or verification boundary
- policy references include a policy fingerprint

### Execution receipts

For execution receipts, the validator checks that required receipt fields are present:

- receipt_id
- timestamp
- agent_id
- mcp_server_id
- tool_name
- input_hash
- output_hash
- policy_decision
- verification_status

It also checks that `verification_status` is one of:

```text
PASS
FAIL
UNSUPPORTED
```

### Server trust profiles

For server trust profiles, the validator checks that:

- required trust profile fields are present
- mcp_server.server_id is declared
- risk_tier is low, medium, or high
- trust_status is approved, denied, escalated, or unsupported
- policy_reference includes a policy_fingerprint
- capability_summary includes capabilities
- high-risk server profiles require review
- evidence_references are present

### Approval, denial, and escalation policy blocks

For policy blocks, the validator checks that:

- required policy block fields are present
- decision_type is approve, deny, or escalate
- policy_reference includes a policy_fingerprint
- scope.risk_tier is low, medium, or high
- conditions.required, conditions.prohibited, and conditions.escalation_triggers are lists
- required_evidence is present
- high-risk or sensitive operation policy blocks require human oversight
- decision_output.decision is approved, denied, or escalated
- decision_output.review_outcome is PASS, FAIL, or UNSUPPORTED

### Install governance records

For MCP server install governance records, the validator checks that:

- required install governance record fields are present
- policy_reference includes a policy_fingerprint
- install_decision.decision is approved, denied, or escalated
- human_review is present
- evidence_references are present
- expected_reviewer_outcome is PASS, FAIL, or UNSUPPORTED

### Runtime tool-use scenario folders

For runtime tool-use scenario folders, the validator checks that the folder contains:

- request.json
- decision-context.json
- execution-receipt.json
- governance-record.json
- verification-boundary.map.json
- audit-package-summary.json

It also performs basic consistency checks:

- request IDs match across request, decision context, and governance record
- agent IDs remain consistent across scenario artifacts
- policy fingerprints remain consistent across scenario artifacts
- audit package tool identity matches the execution receipt
- high-risk or write operations include human oversight
- verification boundary maps include evidence inputs
- audit package expected reviewer outcome is PASS, FAIL, or UNSUPPORTED

### MCP server install scenario folders

For MCP server install scenario folders, the validator checks that the folder contains:

- server-capability-block.json
- server-trust-profile.json
- install-request.json
- approval-decision.json or denial-decision.json
- install-governance-record.json
- verification-boundary.map.json
- audit-package-summary.json

It also performs basic consistency checks:

- mcp_server_id remains consistent across install artifacts
- approval or denial decision references the install request
- install governance record references the install request
- policy fingerprints remain consistent across trust, decision, governance, boundary, and audit artifacts
- high-risk server installs include human review
- verification boundary maps include evidence inputs
- expected reviewer outcome is PASS, FAIL, or UNSUPPORTED

### Unsupported verification boundary scenarios

For unsupported verification boundary scenarios, the validator expects the artifact package to demonstrate that required evidence is outside the available review boundary.

The governance outcome should be `UNSUPPORTED`, not `PASS` or `FAIL`.

## Run the validator directly

From the repository root:

```bash
python validator/aipa-governance/validate_governance_blocks.py \
  examples/aipa-governance/filesystem-governance.kb.json \
  examples/aipa-governance/browser-search-governance.kb.json \
  examples/aipa-governance/database-governance.kb.json \
  examples/aipa-governance/sample-execution-receipt.json
```

## Validate a runtime tool-use scenario folder

From the repository root:

```bash
python validator/aipa-governance/validate_governance_blocks.py \
  examples/aipa-governance/scenarios/filesystem-write-review
```

## Validate an MCP server install scenario folder

From the repository root:

```bash
python validator/aipa-governance/validate_governance_blocks.py \
  examples/aipa-governance/scenarios/mcp-server-install-review
```

## Run the demo validation set

From the repository root:

```bash
python validator/aipa-governance/run_demo_validation.py
```

The runner uses:

```text
examples/aipa-governance/validation-manifest.json
```

It validates the manifest artifacts and all listed scenario folders, including expected `PASS`, `FAIL`, and `UNSUPPORTED` governance outcomes.

## MVP limitation

This validator does not perform runtime enforcement, cryptographic verification, external attestation, or live MCP integration. It only validates the shape, required governance fields, and basic internal consistency of the MVP example artifacts and scenario packages.
