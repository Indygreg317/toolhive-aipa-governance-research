# Verification Boundaries

A verification boundary separates governance declarations from review evidence.

A governance record can declare scope, policy, identity context, continuity assumptions, oversight requirements, and expected evidence. A verification boundary map describes which parts of that declaration can be checked and what evidence is required.

## Boundary model

The MVP uses three outcomes:

- `PASS`: required evidence is present and matches the declared rule.
- `FAIL`: required evidence is missing, inconsistent, or violates the declared rule.
- `UNSUPPORTED`: the validator does not yet support the artifact, rule, or evidence type.

## Example boundary fields

- boundary_id
- governed_artifact_id
- verifier_scope
- evidence_inputs
- policy_reference
- policy_fingerprint
- identity_context
- continuity_assumptions
- unsupported_conditions

## Why boundaries matter

A governance artifact should not be treated as proof by itself. It should make claims legible and link those claims to evidence that can be reviewed separately.

## MVP limitation

This prototype does not perform live runtime replay or external attestation. It defines the shape of governance evidence and a small validation model for example artifacts.
