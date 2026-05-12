# AIPA Governance Demo Walkthrough

This walkthrough explains the MVP demo in plain operational terms.

The goal is to show how AIPA Knowledge Blocks can sit beside MCP-based tool systems and make agent tool use easier to review, explain, and audit.

## Scenario

An AI agent wants to use an MCP server tool.

The platform may already decide whether the tool can be used based on registry settings, identity, access policy, runtime controls, or other platform rules.

The AIPA governance layer does not replace that decision. It records the governance context around the decision.

## Flow

```text
1. Agent requests an MCP tool
        |
2. MCP platform evaluates operational access
        |
3. AIPA Governance Knowledge Block describes the tool context
        |
4. Policy reference and policy fingerprint are attached
        |
5. Execution receipt records the tool-use event
        |
6. Governance record declares oversight, scope, and evidence
        |
7. Verification boundary map defines what can be checked
        |
8. Audit package summary bundles reviewable artifacts
```

## Step 1: Agent requests a tool

Example:

```text
Agent requests filesystem.write_file
```

This request may involve risk because writing files can change project state, overwrite evidence, or affect later execution.

## Step 2: Operational access is evaluated

A ToolHive-style platform may handle practical control questions such as:

- Is this MCP server available?
- Is the user allowed to access it?
- Is the runtime isolated?
- Are platform-level controls in place?

AIPA does not replace those controls.

## Step 3: Knowledge Block describes governance context

The relevant Knowledge Block answers governance questions:

- What is the MCP server?
- What is its purpose?
- What risk tier applies?
- What use is allowed?
- What use is prohibited?
- Is human oversight required?
- What evidence must be retained?

Example file:

```text
examples/aipa-governance/filesystem-governance.kb.json
```

## Step 4: Policy reference is attached

The Knowledge Block includes:

```json
{
  "policy_id": "AIPA-MCP-FS-001",
  "policy_name": "Filesystem Tool Governance Policy",
  "policy_fingerprint": "sha256:placeholder-filesystem-policy-fingerprint"
}
```

The policy fingerprint is a placeholder in this MVP. In a production-grade system, it would identify the exact policy version being referenced.

## Step 5: Execution receipt records the event

The execution receipt captures the basic review trail:

- receipt ID
- timestamp
- agent ID
- MCP server ID
- tool name
- input hash
- output hash
- policy decision
- verification status

Example file:

```text
examples/aipa-governance/sample-execution-receipt.json
```

## Step 6: Governance record declares review context

The governance record declares what governance claims were made about the event.

Example claims:

- policy was referenced
- identity context was declared
- human oversight was required
- human oversight was recorded
- execution boundary was declared

Example file:

```text
examples/aipa-governance/sample-governance-record.json
```

## Step 7: Verification boundary defines what can be checked

The verification boundary map separates declaration from review.

It describes what evidence a reviewer or validator would need before producing one of three outcomes:

- `PASS`
- `FAIL`
- `UNSUPPORTED`

Example file:

```text
examples/aipa-governance/sample-verification-boundary.map.json
```

## Step 8: Audit package bundles the artifacts

The audit package summary gives a reviewer a compact map of what exists, what is missing, and what can be reviewed.

Example file:

```text
examples/aipa-governance/audit-package-summary.json
```

## MVP takeaway

This prototype demonstrates a narrow point:

```text
MCP security and runtime systems can control tool access.
AIPA governance artifacts can make the decision context reviewable.
```

That separation keeps the prototype complementary rather than competitive.
