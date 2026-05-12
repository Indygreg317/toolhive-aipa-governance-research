# AIPA Governance Scenarios

This directory contains end-to-end scenario packages for the AIPA MCP governance research overlay.

Each scenario is designed to show a complete governance review path from an MCP tool-use request, MCP server lifecycle decision, or verification boundary question to an audit package summary.

## Current scenarios

| Scenario | Status | Expected outcome | Purpose |
| --- | --- | --- | --- |
| [Filesystem Write Review](./filesystem-write-review/) | MVP complete | PASS | Demonstrates how a high-risk filesystem write request can be represented through request, decision context, execution receipt, governance record, verification boundary, and audit package artifacts. |
| [MCP Server Install Review](./mcp-server-install-review/) | MVP complete | PASS | Demonstrates a successful governance path for approving an MCP server install or exposure decision. |
| [Denied MCP Server Install](./mcp-server-install-denied/) | MVP failure-mode example | FAIL | Demonstrates how an MCP server install request can be denied when trust context, approved scope, or required evidence is insufficient. |
| [Unsupported Verification Boundary](./unsupported-verification-boundary/) | MVP boundary example | UNSUPPORTED | Demonstrates how a reviewer should avoid false certainty when required external evidence is outside the available verification boundary. |

## Runtime tool-use scenario artifact pattern

Runtime tool-use scenarios generally follow this structure:

```text
README.md
request.json
decision-context.json
execution-receipt.json
governance-record.json
verification-boundary.map.json
audit-package-summary.json
```

## MCP server install scenario artifact pattern

Install review scenarios generally follow this structure:

```text
README.md
server-capability-block.json
server-trust-profile.json
install-request.json
approval-decision.json or denial-decision.json
install-governance-record.json
verification-boundary.map.json
audit-package-summary.json
```

## Unsupported verification scenario artifact pattern

Unsupported verification scenarios generally follow this structure:

```text
README.md
request.json
governance-record.json
verification-boundary.map.json
audit-package-summary.json
```

## Review flow

```text
request or server lifecycle event
  -> decision context, trust profile, or governance record
  -> approval, denial, escalation, or unsupported boundary decision
  -> governance record
  -> verification boundary
  -> audit package summary
```

## Why scenarios matter

The root examples show individual artifact types.

Scenarios show how those artifacts work together in a reviewable governance package.

A reviewer should be able to open a scenario folder and understand:

- what the agent or user requested
- what policy context applied
- whether human oversight was required
- what evidence was recorded
- what boundary separates declaration from review
- what the expected audit outcome is

## Planned scenarios

Future scenario packages may include:

- browser/search source review
- database read-only query review
- database bulk export escalation
- cross-tool agent workflow review
- human override review

## Boundary

These scenarios are explanatory governance packages. They do not claim live runtime enforcement, official integration, cryptographic proof, or external attestation.
