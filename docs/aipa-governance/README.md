# AIPA MCP Governance Knowledge Blocks

This directory contains an independent AIPA research overlay for describing governance context around MCP-based agent tool use.

This work is intended to complement ToolHive-style MCP registries and agent-security runtimes. It does not replace runtime isolation, authorization, registry controls, policy enforcement, or security monitoring.

## Core thesis

Security controls what agents can do.

Governance records explain why those actions were allowed, under what policy, with what oversight, and how they can be reviewed or verified.

## What this adds

The overlay introduces example artifacts for:

- MCP Governance Knowledge Blocks
- tool risk context
- execution policy references
- execution receipts
- governance records
- verification boundary maps
- audit package summaries

## What this does not claim

This is not an official Stacklok or ToolHive integration. It is not a replacement runtime, not a competing security product, and not an endorsement claim. It is a research prototype showing how AIPA governance artifacts could sit beside MCP security infrastructure.

## MVP examples

The first examples cover three MCP server categories:

1. Filesystem MCP server
2. Browser/search MCP server
3. Database MCP server

Each example describes allowed use, prohibited use, risk tier, human oversight expectations, policy references, identity context, evidence requirements, audit outputs, and PASS/FAIL/UNSUPPORTED validation logic.
