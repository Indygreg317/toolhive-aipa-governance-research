# Database Read-Only Query Review Scenario

This scenario demonstrates an end-to-end AIPA governance review path for a database MCP read-only query.

## Scenario summary

An AI agent requests permission to run a read-only query against an approved reporting database.

The action is treated as medium risk because database access can expose sensitive or excessive information even when no write operation occurs. The AIPA governance overlay records query intent, scope, policy context, result-handling requirements, execution evidence, verification boundary, and audit package summary.

## Scenario flow

```text
request.json
      |
      v
decision-context.json
      |
      v
execution-receipt.json
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

## Review question

Could a reviewer understand why the query was allowed, what scope applied, whether the query was read-only, what data-handling limits applied, and what evidence exists for later review?

## Expected result

```text
PASS
```

The scenario should pass because:

- database purpose is declared
- query is declared read-only
- approved table/view scope is declared
- policy reference includes a policy fingerprint
- result handling requirements are recorded
- execution receipt includes input and output hashes
- verification boundary identifies unsupported claims

## Boundary

This scenario does not claim live database enforcement, data-classification accuracy, cryptographic proof, or external attestation. It demonstrates a reviewable governance package around read-only database MCP tool use.
