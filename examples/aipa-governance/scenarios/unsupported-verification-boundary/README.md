# Unsupported Verification Boundary Scenario

This scenario demonstrates an `UNSUPPORTED` review outcome for the AIPA MCP governance research overlay.

## Scenario summary

An MCP server governance record declares that an external dependency state, runtime replay, and source provenance can be verified. However, the required evidence is not available inside the current review boundary.

The request is not treated as a clean `PASS` or a clear `FAIL`. Instead, the reviewer must return `UNSUPPORTED` because the available evidence is insufficient to verify the declared claim.

## Why this matters

A governance system should not force false certainty.

`PASS` means the required evidence supports the claim.

`FAIL` means the required evidence contradicts the claim or required evidence is missing for a rule that must be satisfied.

`UNSUPPORTED` means the system cannot verify the claim with the available boundary and evidence.

## Scenario flow

```text
request.json
      |
      v
governance-record.json
      |
      v
verification-boundary.map.json
      |
      v
audit-package-summary.json
```

## Expected result

```text
UNSUPPORTED
```

The scenario is unsupported because:

- external attestation is referenced but not provided
- runtime replay evidence is unavailable
- dependency state cannot be reconstructed
- source provenance evidence is outside the review boundary
- the policy fingerprint exists but cannot be resolved to a canonical policy artifact

## Boundary

This scenario does not claim live ToolHive integration, live runtime enforcement, cryptographic provenance verification, or external attestation. It demonstrates when a reviewer should avoid making a stronger claim than the evidence supports.
