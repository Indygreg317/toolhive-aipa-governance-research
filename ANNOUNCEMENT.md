# AIPA MCP Governance Research Prototype

This repository is now a presentable independent research prototype exploring how AIPA Governance Knowledge Blocks can describe governance context around MCP-based agent workflows.

## Core thesis

Security and runtime systems can control what agents are allowed to do.

Governance artifacts can explain why an action was allowed, under what policy, with what oversight, and what evidence exists for later review.

## What this prototype includes

- AIPA Governance Knowledge Blocks
- MCP governance examples for filesystem, browser/search, and database tools
- policy references and policy fingerprint placeholders
- execution receipts
- governance records
- verification boundary maps
- audit package summaries
- end-to-end filesystem write review scenario
- local validator
- scenario-folder validation
- GitHub Actions validation workflow

## Why it matters

As AI agents gain access to more tools, teams will need more than runtime access controls. They will also need reviewable governance context around tool-use decisions.

This prototype explores one possible structure for that governance layer.

The goal is not to replace MCP runtimes or agent-security platforms. The goal is to make tool-use decisions easier to explain, review, and audit.

## Boundary

This is not an official Stacklok or ToolHive integration.

It is not a replacement runtime, competing MCP platform, commercial clone, or endorsement claim.

It is an independent AIPA research prototype focused on governance context, audit evidence, and verification boundaries for MCP-based tool use.

## Current review path

Start here:

- [README.md](./README.md)
- [AIPA-GOVERNANCE-NOTICE.md](./AIPA-GOVERNANCE-NOTICE.md)
- [AIPA governance README](./docs/aipa-governance/README.md)
- [Demo walkthrough](./docs/aipa-governance/demo-walkthrough.md)
- [Filesystem write review scenario](./examples/aipa-governance/scenarios/filesystem-write-review/)
- [Validator README](./validator/aipa-governance/README.md)

## Validation

The current demo validation command is:

```bash
python validator/aipa-governance/run_demo_validation.py
```

The GitHub Actions workflow also runs this validation for AIPA overlay changes.

## AIPA

AIPA stands for AI Partnership Association.

This work is part of a broader effort to explore governance records, execution receipts, verification boundaries, and audit-ready structures for trustworthy AI deployment.
