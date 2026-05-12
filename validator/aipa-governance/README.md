# AIPA Governance Validator

This directory contains a minimal validator for the AIPA MCP governance research overlay.

The validator checks whether example governance artifacts contain the required MVP fields and whether their validation status uses the expected AIPA outcomes. It also supports basic scenario-folder validation for end-to-end demo packages.

## Outcomes

The validator reports one of three outcomes:

```text
PASS
FAIL
UNSUPPORTED
```

## What it checks

For MCP Governance Knowledge Blocks, the validator checks that:

- required Knowledge Block fields are present
- every MCP server has a governance Knowledge Block identifier
- high-risk tools define prohibited use
- high-risk tools require human oversight or explain why not
- tools define an execution or verification boundary
- policy references include a policy fingerprint

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

For scenario folders, the validator checks that the folder contains:

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

## Run the validator directly

From the repository root:

```bash
python validator/aipa-governance/validate_governance_blocks.py \
  examples/aipa-governance/filesystem-governance.kb.json \
  examples/aipa-governance/browser-search-governance.kb.json \
  examples/aipa-governance/database-governance.kb.json \
  examples/aipa-governance/sample-execution-receipt.json
```

## Validate a scenario folder

From the repository root:

```bash
python validator/aipa-governance/validate_governance_blocks.py \
  examples/aipa-governance/scenarios/filesystem-write-review
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

It also validates the filesystem write review scenario folder.

## MVP limitation

This validator does not perform runtime enforcement, cryptographic verification, external attestation, or live MCP integration. It only validates the shape, required governance fields, and basic internal consistency of the MVP example artifacts and scenario packages.
