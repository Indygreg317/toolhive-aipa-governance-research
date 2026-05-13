# Review Handoff Model

This document describes how AIPA governance artifacts can be packaged for review by a separate verification or audit system.

The goal is to keep governance declaration separate from independent review.

## Core distinction

AIPA governance artifacts can declare:

- what action or lifecycle event occurred
- what policy was referenced
- what evidence was recorded
- what human review context applied
- what verification boundary was declared
- what audit package was prepared

A separate reviewer or verification system can evaluate:

- whether the evidence is present
- whether references are internally consistent
- whether the claimed boundary is sufficient
- whether the expected outcome is supported
- whether the result should be `PASS`, `FAIL`, or `UNSUPPORTED`

## Why handoff matters

A governance record should not automatically be treated as proof.

It is a structured declaration that can be reviewed.

A handoff package gives a reviewer or verifier a bounded set of artifacts to inspect without requiring trust in the originating workflow.

## Handoff package contents

A minimal handoff package may include:

- package identifier
- originating governance record reference
- scenario or event type
- policy reference
- policy fingerprint
- evidence references
- expected governance outcome
- unsupported claims
- verification boundary reference
- audit package reference

## Handoff flow

```mermaid
flowchart LR
    A[Governance Record] --> B[Evidence References]
    B --> C[Review Handoff Package]
    C --> D[Independent Reviewer or Verifier]
    D --> E[PASS / FAIL / UNSUPPORTED]
```

## Review boundary

The handoff package should clearly separate:

```text
claims included in the review package
```

from:

```text
claims outside the available evidence boundary
```

If required evidence is not included, the reviewer should return `UNSUPPORTED` rather than inventing certainty.

## Example review questions

A reviewer may ask:

- Does the governance record identify the event being reviewed?
- Is a policy reference present?
- Is a policy fingerprint present?
- Are evidence references present?
- Are unsupported claims listed?
- Does the audit package summarize the review package clearly?
- Does the expected outcome match the available evidence?

## Relationship to v0.1 scenarios

The v0.1 scenario folders already contain the parts needed for basic handoff:

- request or install request
- decision context or trust profile
- execution receipt where applicable
- governance record
- verification boundary map
- audit package summary

v0.2 adds an explicit handoff package shape so those artifacts can be presented to an external reviewer more consistently.

## Non-goals

This model does not provide:

- runtime enforcement
- official platform integration
- cryptographic proof
- external attestation
- production certification
- automatic trust in the originating governance layer

## Summary

The handoff model makes one principle explicit:

```text
Governance records organize claims and evidence.
Review systems evaluate whether the evidence supports the claims.
```

That separation is central to the AIPA governance architecture.
