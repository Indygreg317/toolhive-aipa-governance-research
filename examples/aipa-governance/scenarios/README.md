# AIPA Governance Scenarios

This directory contains end-to-end scenario packages for the AIPA MCP governance research overlay.

Each scenario is designed to show a complete governance review path from an MCP tool-use request to an audit package summary.

## Current scenarios

| Scenario | Status | Purpose |
| --- | --- | --- |
| [Filesystem Write Review](./filesystem-write-review/) | MVP complete | Demonstrates how a high-risk filesystem write request can be represented through request, decision context, execution receipt, governance record, verification boundary, and audit package artifacts. |

## Scenario artifact pattern

Each scenario should follow this structure:

```text
README.md
request.json
decision-context.json
execution-receipt.json
governance-record.json
verification-boundary.map.json
audit-package-summary.json
```

## Review flow

```text
request
  -> decision context
  -> execution receipt
  -> governance record
  -> verification boundary
  -> audit package summary
```

## Why scenarios matter

The root examples show individual artifact types.

Scenarios show how those artifacts work together in a reviewable governance package.

A reviewer should be able to open a scenario folder and understand:

- what the agent requested
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
- unsupported verification boundary review

## Boundary

These scenarios are explanatory governance packages. They do not claim live runtime enforcement, official integration, cryptographic proof, or external attestation.
