# ToolHive-Style Governance Overlay Lifecycle

This document describes how AIPA governance artifacts can sit beside a ToolHive-style MCP server lifecycle.

The purpose is not to replace MCP runtime controls, registry controls, or platform policy enforcement. The purpose is to make the governance context around MCP server approval, installation, execution, and audit easier to review.

## Lifecycle overview

```text
Discover MCP server
      |
      v
Assess capability and trust profile
      |
      v
Approve, deny, or escalate install
      |
      v
Install or make available under policy
      |
      v
Execute MCP tool under runtime controls
      |
      v
Generate execution receipt
      |
      v
Create governance record
      |
      v
Bundle audit package
```

## Where AIPA artifacts fit

| Lifecycle stage | AIPA artifact | Purpose |
| --- | --- | --- |
| Discover MCP server | MCP server capability Knowledge Block | Describes the server, tool surface, purpose, and governance-relevant capabilities. |
| Assess server | Server trust profile | Records source, maintainer, provenance notes, risk tier, dependency notes, and review status. |
| Approve or deny | Tool approval / denial policy block | Describes the policy logic used to allow, deny, or escalate server or tool use. |
| Install | MCP server install governance record | Declares why the server was approved, under what policy, and what evidence was retained. |
| Execute | Execution receipt | Records event-level evidence for a specific tool-use event. |
| Review | Verification boundary map | Separates governance declaration from reviewable evidence. |
| Audit | Audit package summary | Bundles related artifacts into a compact review package. |

## Core distinction

ToolHive-style infrastructure can answer operational control questions:

- Is the server available?
- Is access allowed?
- What runtime boundary applies?
- What policy or identity controls are active?
- What operational logs exist?

AIPA governance artifacts answer review questions:

- Why was this MCP server trusted enough to install or expose?
- What capabilities did it declare?
- What risk tier was assigned?
- What policy was referenced?
- What policy fingerprint identifies the policy version?
- Was approval, denial, or escalation recorded?
- What evidence would a reviewer need later?

## Install governance flow

```text
server capability block
      |
      v
server trust profile
      |
      v
approval / denial policy block
      |
      v
install governance record
      |
      v
runtime execution receipts
      |
      v
audit package summary
```

## Example install decision

A server may be approved for installation when:

- its purpose is documented
- its tool surface is declared
- its source or registry context is recorded
- its risk tier is assigned
- prohibited use is described
- human approval is recorded if required
- a policy fingerprint is attached

A server may be denied or escalated when:

- its maintainer or source is unknown
- its tool surface is too broad
- it requests sensitive permissions without justification
- it lacks required evidence
- its risk tier exceeds allowed policy limits
- human oversight is required but absent

## Policy fingerprint role

A policy fingerprint identifies the policy version used for the governance decision.

In this MVP, policy fingerprints are placeholders. Future work may define canonical policy forms and deterministic hash generation.

## Server trust profile role

The server trust profile is not a security verdict by itself. It is a governance artifact that records trust-relevant context for review.

It may include:

- server identifier
- source registry
- maintainer field
- capability summary
- declared tool names
- risk tier
- approval status
- evidence references
- policy fingerprint
- review notes

## Boundary

This lifecycle model does not claim official ToolHive or Stacklok integration. It is an independent AIPA research model for governance context around MCP server lifecycle events.
