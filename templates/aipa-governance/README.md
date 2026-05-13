# AIPA Governance Overlay Templates

This directory contains copyable starter templates for building AIPA governance overlay packages around MCP-style tool use and server lifecycle events.

These templates are platform-neutral and partner-safe.

They are not official ToolHive or Stacklok integration artifacts.

## Templates

- `runtime-tool-use-overlay.template.json`
- `server-install-overlay.template.json`
- `review-handoff-package.template.json`

## How to use

Copy the relevant template into a new scenario folder and replace placeholder values.

Suggested folders:

```text
examples/aipa-governance/scenarios/{scenario-name}/
```

Then create the required artifacts referenced by the template and run:

```bash
python validator/aipa-governance/run_demo_validation.py
```

## Template boundary

The templates describe governance context, evidence requirements, review boundaries, and audit package structure.

They do not perform runtime enforcement, certification, external attestation, or cryptographic verification.
