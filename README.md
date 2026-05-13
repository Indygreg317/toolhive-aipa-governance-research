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

## Research milestones

Current milestone documents:

- [AIPA v0.1 Milestone Notes](./docs/aipa-governance/v0.1-milestone.md)
- [AIPA v0.2 Milestone Notes](./docs/aipa-governance/v0.2-milestone.md)
- [Scenario Outcomes](./docs/aipa-governance/scenario-outcomes.md)
- [v0.1 Demo Walkthrough](./docs/aipa-governance/v0.1-demo-walkthrough.md)
- [Architecture Diagrams](./docs/aipa-governance/architecture-diagrams.md)
- [Partner Review Package](./docs/aipa-governance/partner-review-package.md)
- [Review Handoff Model](./docs/aipa-governance/review-handoff-model.md)
- [Review Handoff Index](./docs/aipa-governance/review-handoff-index.md)
- [Policy Fingerprint Evolution](./docs/aipa-governance/policy-fingerprint-evolution.md)
- [Reusable Governance Overlay Template](./docs/aipa-governance/reusable-overlay-template.md)
- [Template Usage Guide](./docs/aipa-governance/template-usage-guide.md)
- [v0.2 Roadmap](./docs/aipa-governance/v0.2-roadmap.md)
- [v0.3 Roadmap](./docs/aipa-governance/v0.3-roadmap.md)

v0.1 demonstrates governance review packages across:

```text
PASS
FAIL
UNSUPPORTED
```

v0.2 adds:

```text
partner reviewability
architecture clarity
review handoff boundaries
policy fingerprint consistency
reusable governance overlay templates
milestone alignment
```

v0.3 is planned to focus on:

```text
template instantiation
template usage guidance
validator hardening
policy fingerprint examples
review handoff indexing
overlay reuse criteria
```

## AIPA governance overlay

The AIPA research materials are located in:

```text
docs/aipa-governance/
schemas/aipa-governance/
examples/aipa-governance/
templates/aipa-governance/
validator/aipa-governance/
```

Recommended reviewer path:

```text
1. Read the README.
2. Read the v0.1 milestone notes.
3. Read the v0.2 milestone notes.
4. Open the v0.1 demo walkthrough.
5. Review the architecture diagrams.
6. Read the partner review package.
7. Read the review handoff model.
8. Read the review handoff index.
9. Read the policy fingerprint evolution notes.
10. Read the reusable overlay template.
11. Read the template usage guide.
12. Run the demo validator.
13. Inspect the scenario index.
14. Review PASS, FAIL, and UNSUPPORTED examples.
15. Read the v0.3 roadmap for planned next-phase work.
```

Start here:

- [AIPA Governance Notice](./AIPA-GOVERNANCE-NOTICE.md)
- [AIPA Governance Overlay README](./docs/aipa-governance/README.md)
- [AIPA v0.1 Milestone Notes](./docs/aipa-governance/v0.1-milestone.md)
- [AIPA v0.2 Milestone Notes](./docs/aipa-governance/v0.2-milestone.md)
- [Scenario Outcomes](./docs/aipa-governance/scenario-outcomes.md)
- [v0.1 Demo Walkthrough](./docs/aipa-governance/v0.1-demo-walkthrough.md)
- [Architecture Diagrams](./docs/aipa-governance/architecture-diagrams.md)
- [Partner Review Package](./docs/aipa-governance/partner-review-package.md)
- [Review Handoff Model](./docs/aipa-governance/review-handoff-model.md)
- [Review Handoff Index](./docs/aipa-governance/review-handoff-index.md)
- [Policy Fingerprint Evolution](./docs/aipa-governance/policy-fingerprint-evolution.md)
- [Reusable Governance Overlay Template](./docs/aipa-governance/reusable-overlay-template.md)
- [Template Usage Guide](./docs/aipa-governance/template-usage-guide.md)
- [v0.2 Roadmap](./docs/aipa-governance/v0.2-roadmap.md)
- [v0.3 Roadmap](./docs/aipa-governance/v0.3-roadmap.md)
- [Demo Walkthrough](./docs/aipa-governance/demo-walkthrough.md)
- [Artifact Flow](./docs/aipa-governance/artifact-flow.md)
- [ToolHive-Style Governance Overlay Lifecycle](./docs/aipa-governance/toolhive-overlay-lifecycle.md)
- [Approval and Denial Policy Model](./docs/aipa-governance/approval-denial-model.md)
- [Scenario Index](./examples/aipa-governance/scenarios/README.md)
- [Reusable Overlay Templates](./templates/aipa-governance/README.md)
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
- [Review handoff package example](./examples/aipa-governance/review-handoff-package.json)
- [Policy fingerprint example](./examples/aipa-governance/policy-fingerprint-example.json)

## Reusable templates

The v0.2 reusable overlay templates are located in:

- [Template README](./templates/aipa-governance/README.md)
- [Runtime tool-use overlay template](./templates/aipa-governance/runtime-tool-use-overlay.template.json)
- [Server install overlay template](./templates/aipa-governance/server-install-overlay.template.json)
- [Review handoff package template](./templates/aipa-governance/review-handoff-package.template.json)

To use these templates, read:

- [Template Usage Guide](./docs/aipa-governance/template-usage-guide.md)

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

In v0.2 and v0.3, the validator also checks review handoff packages, scenario references, and policy fingerprint consistency across supported review packages.

## What this fork is not

This fork is not:

- a replacement for ToolHive
- an official Stacklok or ToolHive integration
- a competing MCP runtime
- a commercial clone
- a claim of partnership or endorsement

## Research status

This repository currently contains:

```text
v0.1 stable research milestone
v0.2 partner-reviewable research milestone
v0.3 roadmap planning
```

The current focus is:

```text
clarity
scenario coverage
partner-safe positioning
reviewability
validation semantics
policy fingerprint consistency
reusable governance overlay templates
external review boundaries
future template instantiation and validator hardening
```

## License

This fork preserves the upstream project license. See [LICENSE](./LICENSE).
