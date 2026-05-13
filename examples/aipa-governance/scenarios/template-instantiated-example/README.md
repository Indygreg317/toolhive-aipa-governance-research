# Template-Instantiated Example Scenario

This scenario demonstrates how the reusable runtime tool-use overlay template can be instantiated into a concrete AIPA governance review package.

The example is intentionally simple.

It models a high-risk filesystem write request where an assistant proposes creating a generated report inside an approved project workspace.

## Expected outcome

```text
PASS
```

The expected outcome is `PASS` because:

- the requested write is inside the approved workspace
- the policy reference is present
- the policy fingerprint is consistent across artifacts
- human review is required and recorded
- execution evidence is represented by input and output hashes
- unsupported claims are explicitly declared

## Artifact set

```text
request.json
decision-context.json
execution-receipt.json
governance-record.json
verification-boundary.map.json
audit-package-summary.json
review-handoff-package.json
```

## Template source

This scenario is derived from:

```text
templates/aipa-governance/runtime-tool-use-overlay.template.json
```

It follows the guidance in:

```text
docs/aipa-governance/template-usage-guide.md
```

## Boundary

This scenario does not claim live runtime enforcement, official ToolHive integration, external attestation, cryptographic proof, or production certification.

It is a concrete governance review package for demonstrating template reuse.
