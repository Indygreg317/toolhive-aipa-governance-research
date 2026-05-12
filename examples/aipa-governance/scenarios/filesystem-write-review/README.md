# Filesystem Write Review Scenario

This scenario demonstrates one complete AIPA governance review path for an MCP filesystem tool-use event.

## Scenario summary

An AI agent requests permission to write a documentation file inside an approved project workspace.

The action is not inherently blocked, but it is treated as high risk because filesystem write access can modify project state. The AIPA governance layer records the policy context, oversight requirement, execution receipt, governance record, verification boundary, and audit package summary.

## Scenario flow

```text
request.json
      |
      v
decision-context.json
      |
      v
execution-receipt.json
      |
      v
governance-record.json
      |
      v
verification-boundary.map.json
      |
      v
audit-package-summary.json
```

## Review question

Could a reviewer understand why the filesystem write was allowed, what policy was referenced, whether human oversight was required, and what evidence exists for later review?

## Expected result

```text
PASS
```

The scenario should pass because:

- the file path is inside the approved workspace
- the operation has a policy reference
- the policy reference includes a policy fingerprint
- the write operation includes human review
- the execution receipt contains input and output hashes
- the verification boundary defines review evidence

## Boundary

This scenario does not claim live ToolHive integration, live runtime enforcement, cryptographic proof, or external attestation. It is a structured governance demo for review and explanation.
