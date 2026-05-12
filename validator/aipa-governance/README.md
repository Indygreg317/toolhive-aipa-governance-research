# AIPA Governance Validator

This directory contains a minimal validator for the AIPA MCP governance research overlay.

The validator is intentionally small. It checks whether example governance artifacts contain the required MVP fields and whether their validation status uses the expected AIPA outcomes.

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

## Run the validator directly

From the repository root:

```bash
python validator/aipa-governance/validate_governance_blocks.py \
  examples/aipa-governance/filesystem-governance.kb.json \
  examples/aipa-governance/browser-search-governance.kb.json \
  examples/aipa-governance/database-governance.kb.json \
  examples/aipa-governance/sample-execution-receipt.json
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

## MVP limitation

This validator does not perform runtime enforcement, cryptographic verification, external attestation, or live MCP integration. It only validates the shape and required governance fields of the MVP example artifacts.
