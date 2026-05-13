# Reusable Governance Overlay Template

This document describes a reusable AIPA governance overlay pattern for MCP-style server registries, agent-security runtimes, and tool-control platforms.

The template is intentionally platform-neutral.

It does not claim official integration, endorsement, runtime enforcement, certification, or replacement behavior.

## Purpose

The reusable overlay template helps a reviewer create a consistent governance package around tool use or server lifecycle events.

It answers five questions:

1. What tool, server, or lifecycle event is being governed?
2. What policy context applies?
3. What evidence is required?
4. What boundary can be reviewed?
5. What claims remain unsupported?

## Template structure

A reusable overlay package should include:

```text
1. governance knowledge block
2. policy reference
3. execution or lifecycle receipt
4. governance record
5. verification boundary map
6. audit package summary
7. optional review handoff package
```

## Minimal artifact set

For runtime tool use:

```text
request.json
decision-context.json
execution-receipt.json
governance-record.json
verification-boundary.map.json
audit-package-summary.json
```

For MCP server install or exposure review:

```text
server-capability-block.json
server-trust-profile.json
install-request.json
approval-decision.json or denial-decision.json
install-governance-record.json
verification-boundary.map.json
audit-package-summary.json
```

For external review handoff:

```text
review-handoff-package.json
```

## Required fields

Each overlay package should declare:

- governed server or tool identifier
- risk tier
- policy reference
- policy fingerprint
- allowed use
- prohibited use
- human oversight requirement
- evidence inputs
- reviewable claims
- unsupported claims
- expected governance outcome

## Outcome model

The template uses three governance review outcomes:

```text
PASS
FAIL
UNSUPPORTED
```

`PASS` means the required evidence is present and internally consistent inside the declared boundary.

`FAIL` means required evidence is missing, inconsistent, or violates the declared policy context.

`UNSUPPORTED` means the claim cannot be evaluated with the available evidence or falls outside the declared verification boundary.

## Policy fingerprint rule

Artifacts inside the same overlay package should use the same policy fingerprint unless the package explicitly declares a policy transition.

The current v0.2 template treats fingerprints as consistency anchors, not cryptographic proof.

## Review boundary rule

A governance record should not be treated as proof by itself.

It is a structured declaration.

A verification boundary map defines what can and cannot be reviewed from the available evidence.

## Platform-neutral wording

Use terms such as:

- MCP governance overlay
- ToolHive-style registry
- agent-security runtime
- compatible governance layer
- independent review package
- complementary governance context

Avoid terms such as:

- official integration
- certified by Stacklok
- ToolHive replacement
- production enforcement
- cryptographic proof
- commercial clone

## Template workflow

```text
1. Identify the tool, server, or lifecycle event.
2. Assign risk tier and policy reference.
3. Attach policy fingerprint.
4. Declare allowed and prohibited use.
5. Define human oversight requirement.
6. Identify evidence inputs.
7. Create governance record.
8. Create verification boundary map.
9. Create audit package summary.
10. Optionally create review handoff package.
11. Run validator.
```

## Reuse target

This template can be adapted for:

- filesystem tool use
- browser or search tool use
- database query review
- MCP server install review
- denied tool or server requests
- unsupported verification boundary cases
- future MCP or agent-tool categories

## Non-goals

This template does not provide:

- runtime sandboxing
- access control
- production policy enforcement
- cryptographic attestation
- external verification service
- official ToolHive or Stacklok integration

## Summary

The reusable overlay template turns an ad hoc governance example into a repeatable review package.

It keeps AIPA positioned as a complementary governance layer that organizes policy context, review boundaries, and audit evidence without competing with MCP runtime or security systems.
