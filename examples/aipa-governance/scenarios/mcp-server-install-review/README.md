# MCP Server Install Review Scenario

This scenario demonstrates an end-to-end AIPA governance review path for approving an MCP server install or exposure decision.

## Scenario summary

A developer requests approval to install or expose a filesystem MCP server for use inside an approved project workspace.

The server has high-risk capabilities because it can read, write, and list files. The AIPA governance overlay records the capability block, trust profile, install request, approval decision, governance record, verification boundary, and audit package summary.

## Scenario flow

```text
server-capability-block.json
      |
      v
server-trust-profile.json
      |
      v
install-request.json
      |
      v
approval-decision.json
      |
      v
install-governance-record.json
      |
      v
verification-boundary.map.json
      |
      v
audit-package-summary.json
```

## Review question

Could a reviewer understand why this MCP server was approved for install or exposure, what capabilities it declared, what trust profile applied, what policy was referenced, and what evidence exists for later review?

## Expected result

```text
PASS
```

The scenario should pass because:

- server capabilities are declared
- server trust profile is present
- risk tier is assigned
- policy reference includes a policy fingerprint
- human review is required and recorded
- approved scope is bounded
- verification boundary identifies reviewable evidence

## Boundary

This scenario does not claim live ToolHive integration, live runtime enforcement, cryptographic provenance verification, or external attestation. It is a structured governance demo for review and explanation.
