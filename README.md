# ToolHive AIPA Governance Research Fork

> **Announcement:** [AIPA MCP Governance Research Prototype](./ANNOUNCEMENT.md)  
> Independent AIPA research fork exploring governance context, execution receipts, verification boundaries, and audit evidence for MCP-based agent workflows.

This repository is an independent AIPA research fork of ToolHive.

It explores how AIPA Governance Knowledge Blocks can describe governance context, verification boundaries, execution receipts, and audit evidence requirements for MCP-based agent workflows.

## Important notice

This fork does not claim endorsement, approval, partnership, or official integration with Stacklok, ToolHive, or any related project.

The original ToolHive project remains the upstream open-source project:

```text
https://github.com/stacklok/toolhive
```

This fork adds a separate AIPA governance research overlay. It does not replace ToolHive runtime behavior, registry behavior, policy enforcement, or platform controls.

## Core thesis

Security and runtime systems can control what agents are allowed to do.

Governance artifacts can explain why an action was allowed, under what policy, with what oversight, and what evidence exists for later review.

## v0.1 milestone

The current research milestone is documented here:

- [AIPA v0.1 Milestone Notes](./docs/aipa-governance/v0.1-milestone.md)
- [Scenario Outcomes](./docs/aipa-governance/scenario-outcomes.md)

v0.1 demonstrates governance review packages across:

```text
PASS
FAIL
UNSUPPORTED
```

## AIPA governance overlay

The AIPA research materials are located in:

```text
docs/aipa-governance/
schemas/aipa-governance/
examples/aipa-governance/
validator/aipa-governance/
```

Start here:

- [AIPA Governance Notice](./AIPA-GOVERNANCE-NOTICE.md)
- [AIPA Governance Overlay README](./docs/aipa-governance/README.md)
- [AIPA v0.1 Milestone Notes](./docs/aipa-governance/v0.1-milestone.md)
- [Scenario Outcomes](./docs/aipa-governance/scenario-outcomes.md)
- [Demo Walkthrough](./docs/aipa-governance/demo-walkthrough.md)
- [Artifact Flow](./docs/aipa-governance/artifact-flow.md)
- [ToolHive-Style Governance Overlay Lifecycle](./docs/aipa-governance/toolhive-overlay-lifecycle.md)
- [Approval and Denial Policy Model](./docs/aipa-governance/approval-denial-model.md)
- [Scenario Index](./examples/aipa-governance/scenarios/README.md)
- [Roadmap](./docs/aipa-governance/roadmap.md)
- [Positioning](./docs/aipa-governance/positioning.md)
- [Verification Boundaries](./docs/aipa-governance/verification-boundaries.md)
- [Partnership-Safe Language](./docs/aipa-governance/partnership-safe-language.md)

## End-to-end scenarios

The fork currently includes six review scenarios:

- [Filesystem Write Review Scenario](./examples/aipa-governance/scenarios/filesystem-write-review/)  
  Demonstrates runtime/tool-use governance for a scoped filesystem change request.

- [Browser Search Source Review Scenario](./examples/aipa-governance/scenarios/browser-search-source-review/)  
  Demonstrates source identifiers, citation requirements, and unsupported-claim boundaries for browser/search use.

- [Database Read-Only Query Review Scenario](./examples/aipa-governance/scenarios/database-readonly-query-review/)  
  Demonstrates scoped read-only database access, approved query scope, result handling, and evidence capture.

- [MCP Server Install Review Scenario](./examples/aipa-governance/scenarios/mcp-server-install-review/)  
  Demonstrates server lifecycle approval governance for an MCP server install or exposure decision.

- [Denied MCP Server Install Scenario](./examples/aipa-governance/scenarios/mcp-server-install-denied/)  
  Demonstrates governance-supported denial when trust context, approved scope, or required evidence is insufficient.

- [Unsupported Verification Boundary Scenario](./examples/aipa-governance/scenarios/unsupported-verification-boundary/)  
  Demonstrates evidence-bound review when required external proof is outside the available verification boundary.

## Example artifacts

The MVP includes governance examples for three MCP server/tool categories:

- [Filesystem MCP governance example](./examples/aipa-governance/filesystem-governance.kb.json)
- [Browser/search MCP governance example](./examples/aipa-governance/browser-search-governance.kb.json)
- [Database MCP governance example](./examples/aipa-governance/database-governance.kb.json)

It also includes:

- [Sample execution receipt](./examples/aipa-governance/sample-execution-receipt.json)
- [Sample governance record](./examples/aipa-governance/sample-governance-record.json)
- [Sample verification boundary map](./examples/aipa-governance/sample-verification-boundary.map.json)
- [Audit package summary](./examples/aipa-governance/audit-package-summary.json)
- [Server trust profile](./examples/aipa-governance/server-trust-profile.json)
- [MCP server install governance record](./examples/aipa-governance/mcp-server-install-governance-record.json)
- [Tool approval policy block](./examples/aipa-governance/tool-approval-policy-block.json)
- [Tool denial policy block](./examples/aipa-governance/tool-denial-policy-block.json)
- [Tool escalation policy block](./examples/aipa-governance/tool-escalation-policy-block.json)

## Schemas

The MVP schemas are located in:

- [MCP Governance Knowledge Block schema](./schemas/aipa-governance/mcp-governance-kb.schema.json)
- [Execution Receipt schema](./schemas/aipa-governance/execution-receipt.schema.json)
- [Verification Boundary Map schema](./schemas/aipa-governance/verification-boundary-map.schema.json)
- [Server Trust Profile schema](./schemas/aipa-governance/server-trust-profile.schema.json)
- [Tool Approval Policy schema](./schemas/aipa-governance/tool-approval-policy.schema.json)

## Validator

The prototype includes a minimal validator:

```text
validator/aipa-governance/validate_governance_blocks.py
```

Example usage:

```bash
python validator/aipa-governance/validate_governance_blocks.py \
  examples/aipa-governance/filesystem-governance.kb.json \
  examples/aipa-governance/sample-execution-receipt.json
```

Run the demo validation set:

```bash
python validator/aipa-governance/run_demo_validation.py
```

The validator uses three outcomes:

```text
PASS
FAIL
UNSUPPORTED
```

## What this fork is not

This fork is not:

- a replacement for ToolHive
- an official Stacklok or ToolHive integration
- a competing MCP runtime
- a commercial clone
- a claim of partnership or endorsement

## Research status

This is a v0.1 research prototype milestone.

The current focus is clarity, artifact structure, scenario coverage, validation semantics, and partnership-safe positioning rather than runtime integration.

## License

This fork preserves the upstream project license. See [LICENSE](./LICENSE).
