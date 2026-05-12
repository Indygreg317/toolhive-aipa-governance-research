# Approval and Denial Policy Model

This document describes how AIPA approval and denial policy blocks can support MCP server and tool governance decisions.

The goal is to make approval, denial, and escalation decisions reviewable without replacing the runtime or platform policy system.

## Decision outcomes

The MVP policy block model uses three governance decision outcomes:

```text
approve
deny
escalate
```

These outcomes are governance records. They are not runtime enforcement by themselves.

## Why policy blocks matter

A runtime may determine whether a tool can execute.

A governance policy block explains the decision logic used to approve, deny, or escalate a server or tool request for review.

## Approval

An approval policy block describes when a server or tool can be approved.

Example approval conditions:

- server capability is declared
- server trust profile is present
- policy fingerprint is attached
- target scope is bounded
- sensitive operations require human review
- audit evidence requirements are declared

## Denial

A denial policy block describes when a server or tool should not be approved.

Example denial conditions:

- missing policy fingerprint
- missing server trust profile
- unknown source or maintainer
- tool surface exceeds allowed risk tier
- sensitive capability lacks review requirement
- requested operation is prohibited

## Escalation

An escalation policy block describes when the decision requires human review or additional evidence.

Example escalation conditions:

- high-risk tool category
- filesystem write access
- database bulk export
- ambiguous source trust
- policy fingerprint mismatch
- requested use exceeds standard scope

## Policy fingerprint

Every policy block should include a policy fingerprint.

In this MVP, fingerprints are placeholders. Future work may define canonical policy formats and deterministic hashing.

## Relationship to governance records

A policy block can be referenced by:

- server trust profile
- install governance record
- execution receipt
- governance record
- verification boundary map
- audit package summary

## Boundary

Policy blocks are review artifacts. They are not claims of live runtime enforcement, official integration, or external attestation.
