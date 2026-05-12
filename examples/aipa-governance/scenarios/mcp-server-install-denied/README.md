# Denied MCP Server Install Scenario

This scenario demonstrates a controlled failure path for an MCP server install or exposure request.

## Scenario summary

A developer requests approval to install or expose a high-risk filesystem MCP server. The request is denied because the governance evidence is incomplete and the server trust context is insufficient for approval.

This scenario is intentionally designed to produce a governance review outcome of `FAIL`.

## Why this matters

A governance overlay should not only demonstrate successful approvals. It should also explain why a server or tool request should be denied.

This scenario shows how AIPA artifacts can make a denial reviewable instead of opaque.

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
denial-decision.json
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

## Expected result

```text
FAIL
```

The scenario fails because:

- maintainer context is unknown
- requested capability is high risk
- approved scope is not declared
- required policy fingerprint is missing from the install request
- human review denies the request
- verification boundary identifies missing approval evidence

## Boundary

This scenario does not claim live ToolHive integration, live runtime enforcement, cryptographic provenance verification, or external attestation. It is a structured governance demo for review and explanation.
