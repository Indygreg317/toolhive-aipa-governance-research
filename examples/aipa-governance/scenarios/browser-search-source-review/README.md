# Browser Search Source Review Scenario

This scenario demonstrates an end-to-end AIPA governance review path for a browser/search MCP tool-use event.

## Scenario summary

An AI agent uses a browser/search MCP tool to gather public source material for a governance research note.

The action is treated as medium risk because search results may be incomplete, stale, misinterpreted, or insufficiently cited. The governance overlay records the request, decision context, execution receipt, governance record, verification boundary, and audit package summary.

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

Could a reviewer understand what the agent searched for, what source-quality rules applied, whether citations were required, what evidence was captured, and what claims remain outside the verification boundary?

## Expected result

```text
PASS
```

The scenario should pass because:

- search purpose is declared
- source-quality policy is referenced
- policy fingerprint is present
- source URLs or source identifiers are recorded
- output summary is linked to evidence
- verification boundary separates cited claims from unsupported claims

## Boundary

This scenario does not claim that external source content is permanently available, complete, or independently true. It only demonstrates a reviewable governance package around browser/search tool use.
