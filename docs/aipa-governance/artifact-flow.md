# Artifact Flow

This document shows how the MVP artifacts relate to one another.

## High-level map

```text
MCP Server / Tool
      |
      v
MCP Governance Knowledge Block
      |
      v
Policy Reference + Policy Fingerprint
      |
      v
Execution Receipt
      |
      v
Governance Record
      |
      v
Verification Boundary Map
      |
      v
Audit Package Summary
```

## Artifact responsibilities

| Artifact | Responsibility |
| --- | --- |
| MCP Governance Knowledge Block | Describes the governed tool, risk tier, allowed use, prohibited use, oversight, evidence, and validation logic. |
| Policy Reference | Identifies the policy and policy fingerprint associated with the governance decision. |
| Execution Receipt | Records the event-level evidence for a specific tool-use event. |
| Governance Record | Declares the governance claims around the event. |
| Verification Boundary Map | Defines what evidence can be reviewed and what PASS, FAIL, or UNSUPPORTED means. |
| Audit Package Summary | Bundles related artifacts into a compact review object. |

## Filesystem example

```text
filesystem-governance.kb.json
      |
      v
sample-execution-receipt.json
      |
      v
sample-governance-record.json
      |
      v
sample-verification-boundary.map.json
      |
      v
audit-package-summary.json
```

## Design principle

Each artifact should do one job.

The Knowledge Block describes governance context.
The receipt records execution evidence.
The governance record declares review claims.
The boundary map defines what can be checked.
The audit package summarizes the review bundle.

## Why this matters

A single log line is rarely enough for governance review. A reviewer usually needs policy context, identity context, evidence references, oversight records, and a clear statement of what can or cannot be verified.

This artifact flow gives MCP-based systems a path from tool use to reviewable governance evidence without changing the underlying runtime.
