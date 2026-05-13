# Review Handoff Index

This index explains what an external reviewer receives in an AIPA governance handoff package and how to inspect it.

It complements the [Review Handoff Model](./review-handoff-model.md).

The model explains the concept.

This index maps the artifacts.

## Purpose

A review handoff package should make a governance review package easy to inspect without requiring trust in the originating workflow.

The reviewer should be able to answer:

- What event or scenario is being reviewed?
- What governance record declared the claim?
- What policy reference applies?
- What policy fingerprint anchors the policy state?
- What evidence artifacts are available?
- What verification boundary was declared?
- What audit package summarizes the review?
- What claims remain unsupported?
- What outcome is expected?

## Core principle

```text
Governance artifacts organize claims and evidence.
Review systems decide whether evidence supports the claims.
```

A handoff package is not proof by itself.

It is a structured review envelope.

## Primary handoff artifact

The root handoff example is:

```text
examples/aipa-governance/review-handoff-package.json
```

The template-instantiated scenario also includes a scenario-local handoff package:

```text
examples/aipa-governance/scenarios/template-instantiated-example/review-handoff-package.json
```

Reusable starter template:

```text
templates/aipa-governance/review-handoff-package.template.json
```

## Handoff package fields

| Field | Reviewer question | Expected use |
| --- | --- | --- |
| `handoff_package_id` | Which package is being reviewed? | Identifies the review envelope. |
| `artifact_type` | Is this a handoff package? | Should be `review_handoff_package`. |
| `version` | Which handoff shape is used? | Helps compare package versions. |
| `scenario_type` | What kind of event is reviewed? | Runtime tool use, server install, or unsupported boundary. |
| `governance_record_reference` | Which governance declaration is being reviewed? | Points to the governance record. |
| `policy_reference` | Which policy applies? | Declares policy family, name, and fingerprint. |
| `expected_governance_outcome` | What result does the package expect? | `PASS`, `FAIL`, or `UNSUPPORTED`. |
| `verification_boundary_reference` | What can be reviewed from available evidence? | Points to the boundary map. |
| `audit_package_reference` | Where is the review summarized? | Points to the audit package summary. |
| `evidence_references` | What supporting artifacts are included? | Points to request, receipt, policy, trust, or decision artifacts. |
| `unsupported_claims` | What should not be treated as proven? | Lists claims outside the evidence boundary. |
| `review_notes` | What should the reviewer focus on? | Provides scope and expectation notes. |

## Reviewer path

Use this order when inspecting a handoff package:

```text
1. Open review-handoff-package.json.
2. Confirm scenario_type and expected_governance_outcome.
3. Open governance_record_reference.path.
4. Confirm the governance record identifies the event being reviewed.
5. Compare policy_reference.policy_fingerprint across linked artifacts.
6. Open verification_boundary_reference.path.
7. Confirm evidence_inputs, reviewable claims, and unsupported claims.
8. Open audit_package_reference.path.
9. Confirm the audit package summarizes the same event and expected outcome.
10. Open evidence_references paths.
11. Decide whether evidence supports PASS, FAIL, or UNSUPPORTED.
```

## Artifact-to-question map

| Artifact | Main review question |
| --- | --- |
| `request.json` or `install-request.json` | What was requested? |
| `decision-context.json` | What policy and context shaped the decision? |
| `execution-receipt.json` | What execution evidence was recorded? |
| `server-trust-profile.json` | What server trust context was declared? |
| `approval-decision.json` or `denial-decision.json` | Why was a server lifecycle event approved or denied? |
| `governance-record.json` or `install-governance-record.json` | What governance claim was declared? |
| `verification-boundary.map.json` | What can and cannot be verified from the provided evidence? |
| `audit-package-summary.json` | What should the reviewer conclude from the package? |
| `review-handoff-package.json` | What bundle is being handed to the reviewer? |

## Policy fingerprint check

The reviewer should compare policy fingerprints across linked artifacts.

Common locations:

```text
policy_reference.policy_fingerprint
```

Expected behavior:

```text
same review package -> same policy fingerprint
```

Exception:

```text
explicit policy transition declared
```

If fingerprints conflict without a declared transition, the package should not be treated as a clean `PASS`.

## Unsupported claims check

Unsupported claims should be explicit.

Examples:

- live runtime enforcement
- cryptographic proof
- external registry verification
- runtime replay
- dependency-state attestation
- source provenance outside the included evidence

If a reviewer cannot verify a claim from the available evidence, the correct result is usually:

```text
UNSUPPORTED
```

not an invented `PASS`.

## Outcome interpretation

### PASS

Use `PASS` when the evidence is present, internally consistent, and sufficient inside the declared boundary.

### FAIL

Use `FAIL` when required evidence is missing, inconsistent, or contradicts the declared policy context.

### UNSUPPORTED

Use `UNSUPPORTED` when the package asks the reviewer to verify something outside the available evidence boundary.

## Example: root handoff package

The root handoff example demonstrates a package around an MCP filesystem governance review.

Key references:

```text
examples/aipa-governance/review-handoff-package.json
examples/aipa-governance/mcp-server-install-governance-record.json
examples/aipa-governance/sample-verification-boundary.map.json
examples/aipa-governance/audit-package-summary.json
```

Reviewer focus:

- Are referenced paths present?
- Does the policy fingerprint align across referenced artifacts?
- Does the expected outcome match the evidence?
- Are unsupported claims listed?

## Example: template-instantiated handoff package

The template-instantiated scenario demonstrates a scenario-local runtime tool-use handoff package.

Key references:

```text
examples/aipa-governance/scenarios/template-instantiated-example/review-handoff-package.json
examples/aipa-governance/scenarios/template-instantiated-example/governance-record.json
examples/aipa-governance/scenarios/template-instantiated-example/verification-boundary.map.json
examples/aipa-governance/scenarios/template-instantiated-example/audit-package-summary.json
```

Reviewer focus:

- Does the filesystem write stay inside the declared workspace boundary?
- Is high-risk human review recorded?
- Is the policy fingerprint consistent?
- Are runtime replay and external attestation correctly left unsupported?

## Validation support

The validator checks review handoff packages for:

- required fields
- expected outcome value
- evidence reference presence
- unsupported claims list
- referenced path existence
- policy fingerprint consistency across referenced artifacts when fingerprints are present

Run:

```bash
python validator/aipa-governance/run_demo_validation.py
```

or validate a handoff artifact directly:

```bash
python validator/aipa-governance/validate_governance_blocks.py \
  examples/aipa-governance/review-handoff-package.json
```

## What the handoff index does not claim

This index does not provide:

- runtime enforcement
- official ToolHive or Stacklok integration
- cryptographic proof
- external attestation
- production certification
- automatic trust in the originating governance layer

## Summary

The handoff index gives reviewers a repeatable path through the evidence package.

It makes the boundary legible:

```text
what is declared
what is evidenced
what is unsupported
what outcome is justified
```
