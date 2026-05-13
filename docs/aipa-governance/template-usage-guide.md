# Template Usage Guide

This guide explains how to create a new AIPA governance overlay scenario from the reusable templates.

The goal is repeatability.

A reviewer should be able to copy a template, replace placeholders, preserve policy consistency, declare unsupported claims, and run validation without guessing how the overlay package is supposed to work.

## Scope

This guide applies to the templates in:

```text
templates/aipa-governance/
```

Current templates include:

```text
runtime-tool-use-overlay.template.json
server-install-overlay.template.json
review-handoff-package.template.json
```

## Boundary

The templates describe governance context, evidence expectations, review boundaries, and audit package structure.

They do not provide:

- runtime enforcement
- official ToolHive or Stacklok integration
- certification
- external attestation
- cryptographic proof
- production policy behavior

## Step 1: Choose the correct template

Use the runtime tool-use template when the scenario is about an agent or MCP tool action.

Examples:

- filesystem write
- browser or search request
- database read-only query
- data export request
- tool action requiring human oversight

Use the server install template when the scenario is about a server lifecycle decision.

Examples:

- MCP server install review
- MCP server exposure review
- server denial decision
- server trust profile review

Use the review handoff template when the goal is to package artifacts for an external reviewer or verifier.

Examples:

- review handoff package for a PASS scenario
- handoff package for a denied install
- handoff package for an UNSUPPORTED verification boundary

## Step 2: Create a scenario folder

Create a new folder under:

```text
examples/aipa-governance/scenarios/{scenario-name}/
```

Use lowercase words separated by hyphens.

Example:

```text
examples/aipa-governance/scenarios/template-instantiated-example/
```

## Step 3: Copy the template content

Copy the appropriate template into your new scenario folder as a planning artifact or use it to create the required concrete artifacts.

For runtime tool-use scenarios, create:

```text
request.json
decision-context.json
execution-receipt.json
governance-record.json
verification-boundary.map.json
audit-package-summary.json
```

For server install scenarios, create:

```text
server-capability-block.json
server-trust-profile.json
install-request.json
approval-decision.json or denial-decision.json
install-governance-record.json
verification-boundary.map.json
audit-package-summary.json
```

For handoff packages, create:

```text
review-handoff-package.json
```

## Step 4: Replace placeholder identifiers

Replace every placeholder value before treating the scenario as a concrete example.

Common placeholders include:

```text
placeholder-mcp-server-id
Placeholder MCP Server
placeholder.tool_name
AIPA-MCP-PLACEHOLDER-001
sha256:placeholder-policy-fingerprint
placeholder-governance-record-id
placeholder-verification-boundary-id
placeholder-audit-package-id
```

Do not leave placeholder identifiers in finalized example artifacts.

## Step 5: Assign the governed action or lifecycle event

For runtime tool-use scenarios, define:

- MCP server ID
- MCP server name
- tool name
- tool category
- operation type
- risk tier

For server lifecycle scenarios, define:

- MCP server ID
- MCP server name
- server category
- requested lifecycle event
- risk tier
- trust status

## Step 6: Define policy reference and fingerprint

Every governed scenario should include a policy reference.

Minimum shape:

```json
{
  "policy_id": "AIPA-MCP-FS-001",
  "policy_name": "Filesystem Tool Governance Policy",
  "policy_fingerprint": "sha256:placeholder-filesystem-policy-fingerprint"
}
```

For v0.3, the policy fingerprint is a consistency anchor.

It is not a cryptographic proof claim.

## Step 7: Keep policy fingerprints consistent

Artifacts inside the same scenario package should use the same policy fingerprint unless a policy transition is explicitly declared.

Check the fingerprint across:

- decision context
- execution receipt
- governance record
- verification boundary map
- audit package summary
- review handoff package
- policy block or trust profile when referenced

If fingerprints conflict, the scenario should not be treated as a clean `PASS` package.

## Step 8: Declare allowed and prohibited use

Every concrete governance overlay should declare both:

```text
allowed use
```

and:

```text
prohibited use
```

Allowed use explains the approved scope.

Prohibited use explains what the governance package does not allow.

For high-risk tool or server actions, make human oversight explicit.

## Step 9: Declare evidence inputs

Evidence inputs should identify what a reviewer can inspect.

Examples:

- request intent
- policy reference
- policy fingerprint
- input hash
- output hash
- server trust profile
- install request
- approval or denial decision
- human review record
- verification boundary map

A scenario should not claim more certainty than the available evidence supports.

## Step 10: Separate reviewable and unsupported claims

Reviewable claims are claims that can be inspected from the provided artifacts.

Unsupported claims are claims outside the available evidence boundary.

Examples of unsupported claims:

- live runtime enforcement
- external registry verification
- cryptographic package provenance
- external attestation
- runtime replay
- complete source truth

Unsupported claims should remain `UNSUPPORTED` instead of being treated as proof.

## Step 11: Set expected governance outcome

Use one of three outcomes:

```text
PASS
FAIL
UNSUPPORTED
```

Use `PASS` when required evidence is present and internally consistent inside the declared boundary.

Use `FAIL` when required evidence is missing, inconsistent, or violates the declared policy context.

Use `UNSUPPORTED` when the requested claim cannot be evaluated from the available evidence.

## Step 12: Create the verification boundary map

The verification boundary map should answer:

- what is being reviewed
- what evidence is available
- what policy reference applies
- what claims are reviewable
- what claims are unsupported
- what outcome model applies

The boundary map is what prevents governance declarations from becoming unsupported proof claims.

## Step 13: Create the audit package summary

The audit package summary should give reviewers a compact view of the scenario.

It should include:

- related artifact paths
- governed action or lifecycle event
- policy reference
- evidence status
- expected reviewer outcome
- unsupported items
- notes about review scope

## Step 14: Create an optional review handoff package

A review handoff package is useful when a scenario needs to be passed to an external reviewer or verifier.

It should reference:

- governance record
- policy reference
- verification boundary map
- audit package summary
- evidence artifacts
- unsupported claims
- expected governance outcome

## Step 15: Add the scenario to the manifest when appropriate

If the new scenario is intended to be part of the demo validation set, add it to:

```text
examples/aipa-governance/validation-manifest.json
```

Do not add unfinished or placeholder-only scenarios to the manifest.

The manifest should include:

- path
- artifact or scenario type
- expected structural status
- expected governance outcome

## Step 16: Run validation

Run:

```bash
python validator/aipa-governance/run_demo_validation.py
```

For direct artifact or folder checks, run:

```bash
python validator/aipa-governance/validate_governance_blocks.py path/to/artifact-or-scenario
```

Validation checks structural correctness.

It does not prove runtime enforcement, cryptographic integrity, external attestation, or production compliance.

## Common mistakes

Avoid these mistakes:

- leaving placeholder identifiers in finalized examples
- using multiple policy fingerprints in one scenario without declaring a transition
- omitting unsupported claims
- treating governance records as proof by themselves
- claiming official integration or endorsement
- putting incomplete examples into the validation manifest
- using `PASS` when evidence is missing
- using `FAIL` when the correct answer is `UNSUPPORTED`

## Done checklist

Before calling a scenario complete, verify:

```text
[ ] scenario folder has the required artifacts
[ ] all placeholder identifiers were replaced
[ ] policy reference is present
[ ] policy fingerprint is present
[ ] policy fingerprint is consistent across related artifacts
[ ] allowed use is declared
[ ] prohibited use is declared
[ ] evidence inputs are declared
[ ] reviewable claims are declared
[ ] unsupported claims are declared
[ ] expected governance outcome is PASS, FAIL, or UNSUPPORTED
[ ] verification boundary map exists
[ ] audit package summary exists
[ ] handoff package exists when needed
[ ] validation runs successfully when included in the manifest
```

## Summary

The reusable templates should produce evidence-bound governance packages.

A good template-instantiated scenario should be clear, reviewable, internally consistent, and honest about what remains unsupported.
