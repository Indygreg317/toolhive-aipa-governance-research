# ToolHive AIPA Governance Research Fork

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
- [Demo Walkthrough](./docs/aipa-governance/demo-walkthrough.md)
- [Artifact Flow](./docs/aipa-governance/artifact-flow.md)
- [Positioning](./docs/aipa-governance/positioning.md)
- [Verification Boundaries](./docs/aipa-governance/verification-boundaries.md)
- [Partnership-Safe Language](./docs/aipa-governance/partnership-safe-language.md)

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

## Schemas

The MVP schemas are located in:

- [MCP Governance Knowledge Block schema](./schemas/aipa-governance/mcp-governance-kb.schema.json)
- [Execution Receipt schema](./schemas/aipa-governance/execution-receipt.schema.json)
- [Verification Boundary Map schema](./schemas/aipa-governance/verification-boundary-map.schema.json)

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

This is an early MVP research prototype.

The current focus is clarity, artifact structure, and partnership-safe positioning rather than runtime integration.

## License

This fork preserves the upstream project license. See [LICENSE](./LICENSE).
