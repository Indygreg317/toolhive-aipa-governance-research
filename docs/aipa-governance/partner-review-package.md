# Partner Review Package

This document is written for external maintainers, security engineers, governance researchers, and ecosystem reviewers who want to understand the AIPA MCP governance research overlay without reading the entire repository.

## Project summary

This repository is an independent AIPA research fork exploring how governance artifacts can sit beside MCP-style agent workflows.

It is designed to show how governance context can be represented around:

- agent tool-use requests
- MCP server install or exposure decisions
- execution receipts
- policy references
- human review requirements
- verification boundaries
- audit package summaries

## Short description

The AIPA governance overlay is a complementary research layer for MCP-style workflows.

It does not replace runtime controls. It explains the review context around decisions.

```text
Runtime and security layers control what happens.
Governance artifacts explain why it was allowed, denied, or left unsupported.
```

## What this project is

This project is:

- an independent research prototype
- a governance artifact model
- a scenario-based explanation layer
- a validator-backed documentation package
- a partner-safe exploration of MCP governance context
- a possible reference pattern for future governance overlays

## What this project is not

This project is not:

- an official ToolHive or Stacklok integration
- a replacement for ToolHive
- a competing MCP runtime
- a security product
- a production certification system
- a cryptographic proof system
- an external attestation service
- a claim of endorsement or partnership

## Why it may matter to MCP and agent-security ecosystems

MCP-style systems can expose powerful tool-use surfaces for agents.

Runtime and security layers can answer operational questions such as:

- Is the tool available?
- Is access allowed?
- What runtime boundary applies?
- What policy control is active?

Governance layers answer review questions such as:

- Why was this tool or server allowed?
- What policy was referenced?
- What evidence was recorded?
- Was human review required?
- Which claims are reviewable?
- Which claims are outside the verification boundary?
- What should an auditor inspect later?

This distinction is the core value of the overlay.

## Reviewable outcome model

The repository demonstrates three governance outcomes:

```text
PASS
FAIL
UNSUPPORTED
```

`PASS` means the available evidence supports the declared governance conclusion inside the current boundary.

`FAIL` means the available evidence supports denial or failure of the declared governance request.

`UNSUPPORTED` means the available evidence is insufficient to determine `PASS` or `FAIL` inside the current boundary.

The important distinction is:

```text
structural validation is separate from governance outcome
```

A scenario can be structurally valid while its expected governance outcome is `FAIL` or `UNSUPPORTED`.

## Included v0.1 scenarios

The current milestone includes six scenario packages:

| Scenario | Expected outcome | Purpose |
| --- | --- | --- |
| Filesystem Write Review | PASS | Demonstrates runtime tool-use governance for a scoped filesystem change request. |
| Browser Search Source Review | PASS | Demonstrates source identifiers, citation requirements, and unsupported-claim boundaries. |
| Database Read-Only Query Review | PASS | Demonstrates scoped database query governance and result handling. |
| MCP Server Install Review | PASS | Demonstrates server lifecycle approval governance. |
| Denied MCP Server Install | FAIL | Demonstrates governance-supported denial when required evidence is insufficient. |
| Unsupported Verification Boundary | UNSUPPORTED | Demonstrates honest uncertainty when evidence is outside the available review boundary. |

## How to review the repository quickly

Recommended review path:

```text
1. Read README.md.
2. Read docs/aipa-governance/v0.1-milestone.md.
3. Read docs/aipa-governance/v0.1-demo-walkthrough.md.
4. Review docs/aipa-governance/architecture-diagrams.md.
5. Run python validator/aipa-governance/run_demo_validation.py.
6. Inspect examples/aipa-governance/scenarios/README.md.
7. Open one PASS, one FAIL, and one UNSUPPORTED scenario.
```

## Complementary positioning

The overlay is designed to be complementary to runtime and security systems.

A compatible MCP runtime or agent-security system could continue to own:

- runtime enforcement
- server execution
- tool access
- identity controls
- platform policy controls
- operational logging

The AIPA overlay focuses on:

- governance context
- reviewable policy references
- execution receipts
- verification boundary maps
- audit package summaries
- human review records
- expected governance outcomes

## Partner-safe integration direction

A future partner-safe integration path could look like:

```text
MCP runtime emits event
        |
        v
AIPA-compatible adapter creates governance artifacts
        |
        v
Verifier or reviewer inspects evidence package
        |
        v
Audit package records PASS / FAIL / UNSUPPORTED outcome
```

This is a research direction, not a current integration claim.

## What feedback would be useful

Useful reviewer feedback includes:

- Are the boundaries clear enough?
- Is the non-competitive positioning clear?
- Are the scenario packages understandable?
- Are the governance artifacts useful or too abstract?
- Are the PASS / FAIL / UNSUPPORTED outcomes understandable?
- Are important MCP governance cases missing?
- Would this kind of overlay be useful beside an agent-security runtime?

## Current boundary statement

This repository should be read as:

```text
an independent, open research prototype for governance context around MCP-style agent workflows
```

It should not be read as:

```text
an official integration, replacement runtime, certification product, or endorsement claim
```

## Summary for maintainers

The project is intentionally narrow:

```text
It does not try to control execution.
It tries to make execution decisions more reviewable.
```

That is the partner-safe contribution of the AIPA MCP governance research overlay.
