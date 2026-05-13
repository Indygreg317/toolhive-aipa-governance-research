# Policy Fingerprint Evolution

This document defines the v0.2 policy fingerprint direction for the AIPA MCP governance research overlay.

The goal is to make policy references more reviewable without claiming cryptographic proof, runtime enforcement, or official integration.

## Current v0.1 behavior

In v0.1, policy fingerprints are placeholder identifiers attached to governance artifacts.

They help reviewers see which policy version a governance claim intends to reference.

Examples include:

```text
policy_id: AIPA-MCP-FS-001
policy_fingerprint: sha256:placeholder-filesystem-policy-fingerprint
```

At v0.1, the fingerprint is treated as a review anchor, not as verified cryptographic evidence.

## v0.2 evolution

v0.2 begins moving fingerprints from simple placeholders toward consistent policy anchors.

A policy fingerprint should be used to answer three review questions:

1. Which policy was referenced?
2. Which policy version or state was intended?
3. Do related artifacts point to the same policy anchor?

The first validation target is internal consistency.

If a governance record, policy block, verification boundary map, audit package, and handoff package all claim to belong to the same review package, their policy fingerprints should align unless a declared policy transition is present.

## Minimum policy reference shape

A policy reference should include:

```json
{
  "policy_id": "AIPA-MCP-FS-001",
  "policy_name": "Filesystem Tool Governance Policy",
  "policy_fingerprint": "sha256:placeholder-filesystem-policy-fingerprint"
}
```

`policy_id` identifies the policy family.

`policy_name` helps humans review the package.

`policy_fingerprint` anchors the intended policy state.

## Review rules

For v0.2, validators and reviewers should apply these rules:

- Every governed artifact should include a policy reference when it declares or evaluates policy context.
- Every policy reference should include a policy fingerprint.
- Artifacts inside the same review package should use the same fingerprint unless a policy transition is explicitly declared.
- A missing fingerprint should produce `FAIL` for structural validation.
- A conflicting fingerprint should produce `FAIL` for internal consistency.
- A fingerprint that cannot be independently recomputed should remain a review anchor, not a proof claim.

## Policy transitions

Future versions may support explicit policy transitions.

A transition-aware package may include fields such as:

```json
{
  "previous_policy_fingerprint": "sha256:previous-policy-state",
  "current_policy_fingerprint": "sha256:current-policy-state",
  "transition_reason": "policy updated before execution",
  "transition_mode": "declared_override",
  "human_review_required": true
}
```

This is not part of the current enforcement model.

For now, the v0.2 validator focuses on consistency among declared fingerprints.

## Boundary

This document does not claim:

- live policy enforcement
- cryptographic verification of policy contents
- external registry attestation
- official ToolHive or Stacklok integration
- production certification

The policy fingerprint is a governance review anchor.

It helps reviewers detect missing, mismatched, or unsupported policy context.

## Summary

v0.2 policy fingerprint evolution means:

```text
Policy fingerprints move from placeholder labels toward consistency anchors.
```

That is enough to improve reviewability while keeping the project safely inside a research-overlay boundary.
