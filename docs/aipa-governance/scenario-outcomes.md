# Scenario Outcomes

This document summarizes the expected governance outcomes for the AIPA MCP governance research overlay scenarios.

## Outcome meanings

### PASS

`PASS` means the scenario contains enough reviewable evidence to support the declared governance conclusion within the current boundary.

### FAIL

`FAIL` means the scenario contains enough reviewable evidence to support denial or failure of the declared governance request.

A `FAIL` governance outcome does not mean the scenario folder is structurally invalid. It means the scenario is a deliberate failure-mode example.

### UNSUPPORTED

`UNSUPPORTED` means the available evidence is insufficient to determine `PASS` or `FAIL` inside the current verification boundary.

This outcome is used when a claim depends on external evidence, runtime proof, source provenance, dependency state, or attestation that is not available inside the review package.

## Scenario table

| Scenario | Path | Expected outcome | Review focus |
| --- | --- | --- | --- |
| Filesystem Write Review | `examples/aipa-governance/scenarios/filesystem-write-review/` | PASS | Runtime tool-use governance for a scoped filesystem change request. |
| Browser Search Source Review | `examples/aipa-governance/scenarios/browser-search-source-review/` | PASS | Source identifiers, citation requirements, source-quality limits, and unsupported-claim boundaries. |
| Database Read-Only Query Review | `examples/aipa-governance/scenarios/database-readonly-query-review/` | PASS | Scoped read-only database access, approved query scope, result handling, and evidence capture. |
| MCP Server Install Review | `examples/aipa-governance/scenarios/mcp-server-install-review/` | PASS | Server lifecycle approval governance, server trust profile, policy fingerprint, and human review. |
| Denied MCP Server Install | `examples/aipa-governance/scenarios/mcp-server-install-denied/` | FAIL | Governance-supported denial due to insufficient trust context, missing approved scope, or insufficient evidence. |
| Unsupported Verification Boundary | `examples/aipa-governance/scenarios/unsupported-verification-boundary/` | UNSUPPORTED | Evidence-bound review when required external proof is outside the available verification boundary. |

## Structural validation versus governance outcome

The validator checks whether an artifact or scenario is structurally reviewable.

The validation manifest records the expected governance outcome.

This distinction allows examples like:

```text
structural validation: PASS
governance outcome: FAIL
```

or:

```text
structural validation: PASS
governance outcome: UNSUPPORTED
```

That distinction is important because the repository should be able to test failure modes without treating them as broken files.

## Current v0.1 coverage

v0.1 covers:

- tool-use approval
- source-review approval
- scoped database query approval
- server lifecycle approval
- server lifecycle denial
- unsupported verification boundary handling

Together these examples demonstrate that governance review can represent more than a binary allow or deny model.
