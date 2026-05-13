# Overlay Reuse Criteria

This document defines criteria for choosing future public repositories where the AIPA governance overlay pattern may be useful.

The goal is to identify good research candidates without creating competitive, misleading, or unsupported claims.

## Purpose

The AIPA overlay pattern is most useful when a project has a visible decision, tool-use, server lifecycle, approval, audit, or evidence boundary.

A good candidate repository should allow AIPA to demonstrate governance context beside the original system without replacing that system.

## Core reuse question

Before creating an overlay for another repository, ask:

```text
Can AIPA add reviewable governance context without modifying, competing with, or overclaiming the underlying project?
```

If the answer is no, the repository is not a good candidate.

## Required criteria

A repository should meet all required criteria before an AIPA overlay is created.

| Criterion | Requirement | Why it matters |
| --- | --- | --- |
| Public visibility | Repository is public or has public documentation. | AIPA should use only public, reviewable information. |
| Governance relevance | The project has decisions, policies, approvals, tool use, agent behavior, data access, security controls, or audit needs. | The overlay must have a real governance surface. |
| Review boundary | There is a clear boundary between what can be reviewed and what remains unsupported. | Prevents unsupported proof claims. |
| Partner-safe framing | The overlay can be described as complementary, not competitive. | Avoids implying replacement, endorsement, or official integration. |
| Evidence artifacts | The project exposes enough public information to build example artifacts. | Enables evidence-bound examples. |
| Non-runtime value | AIPA can demonstrate value without modifying runtime behavior. | Keeps the overlay in the research/governance layer. |

## Strong candidate signals

A repository is a strong candidate when it has several of these signals:

- agent tool-use surface
- MCP server registry or tool registry behavior
- policy engine or authorization layer
- security approval process
- plugin, extension, or connector lifecycle
- audit logs or event records
- human review or approval workflow
- data access controls
- model/tool orchestration
- reproducible examples or scenarios
- public schemas or JSON artifacts
- governance, risk, compliance, or security documentation

## Weak candidate signals

A repository is a weak candidate when:

- there is no clear governance surface
- examples require private data
- the project is mostly UI-only without reviewable decisions
- the overlay would require modifying runtime behavior
- the value proposition sounds like a competing product
- evidence cannot be inspected from public materials
- the project owner strongly restricts derivative examples
- the overlay would imply certification, partnership, or endorsement

## Do-not-use criteria

Do not create an AIPA overlay if any of these are true:

- The overlay would require private, confidential, or non-public data.
- The overlay would imply official endorsement without permission.
- The overlay would be positioned as a replacement for the original project.
- The overlay would claim runtime enforcement that is not implemented.
- The overlay would claim cryptographic proof that is not implemented.
- The overlay would claim compliance certification that is not issued.
- The repository is unrelated to AI, agents, tools, security, governance, data access, or auditability.
- The overlay would be primarily promotional rather than evidence-bound.

## Reuse scoring model

Use this lightweight scoring model before starting a new overlay.

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Governance surface | None | Partial or indirect | Clear decision/tool/policy surface |
| Evidence availability | None | Some public docs | Public examples, schemas, or artifacts |
| Review boundary clarity | None | Can be inferred | Clearly separable review boundary |
| Partner-safe fit | Risky or competitive | Needs careful wording | Clearly complementary |
| Template fit | No fit | Partial fit | Runtime, install, or handoff template applies |
| Unsupported-claim clarity | Hard to separate | Some unsupported claims visible | Unsupported claims are easy to define |

Suggested interpretation:

```text
0–4   Do not pursue.
5–7   Hold for later or research further.
8–10  Possible candidate with careful scope.
11–12 Strong candidate for a lightweight overlay.
```

## Minimum overlay package for a new repository

A lightweight overlay for another repository should include at least:

```text
README or notice
positioning note
one governance scenario
policy reference or policy placeholder
verification boundary map
audit package summary
unsupported claims list
```

A stronger overlay may also include:

```text
reusable template instance
review handoff package
validator manifest entry
partner review note
policy fingerprint example
```

## Public-repo candidate worksheet

Use this worksheet before opening a new research branch.

```text
Repository:
Public URL:
Project category:
Governance surface:
Candidate scenario:
Runtime modification required: yes/no
Private data required: yes/no
Policy or decision boundary:
Evidence artifacts available:
Unsupported claims:
Partner-safe language:
Score:
Recommendation: pursue / hold / do not pursue
```

## Example candidate categories

Good categories for future overlays may include:

- MCP registries and MCP server tooling
- agent-security platforms
- model evaluation frameworks
- AI audit or logging frameworks
- workflow approval tools
- policy-as-code repositories
- governance, risk, and compliance tooling
- data access control systems
- AI plugin or connector ecosystems
- reproducible agent workflow examples

## Partner-safe language

Use language such as:

- independent research overlay
- complementary governance context
- evidence-bound review package
- public example based on available materials
- non-runtime governance layer
- reviewer-facing artifact package

Avoid language such as:

- official integration
- certified by the upstream project
- replacement for the upstream project
- production enforcement
- verified compliance
- cryptographic proof
- endorsed partnership

## Evidence-bound positioning

Each future overlay should make the boundary explicit:

```text
What public evidence exists?
What governance claim is being organized?
What can be reviewed?
What remains unsupported?
```

If those questions cannot be answered clearly, do not build the overlay yet.

## Relationship to templates

The reusable templates should be used only when they fit the candidate repository.

Runtime tool-use template:

```text
Use when reviewing an agent/tool action.
```

Server install overlay template:

```text
Use when reviewing a server, plugin, connector, or tool exposure lifecycle event.
```

Review handoff package template:

```text
Use when a bounded evidence package should be passed to an external reviewer.
```

## Recommended process

```text
1. Identify candidate repository.
2. Score the candidate using the reuse scoring model.
3. Reject candidates that trigger do-not-use criteria.
4. Define one narrow scenario.
5. Identify public evidence artifacts.
6. Define policy reference or placeholder.
7. Define unsupported claims.
8. Create a minimal overlay package.
9. Validate structure where possible.
10. Keep language partner-safe and evidence-bound.
```

## Summary

Overlay reuse should be selective.

The best candidates are public, governance-relevant, evidence-rich, and easy to frame as complementary.

AIPA should only create overlays where it can add clarity without claiming authority over the original project.
