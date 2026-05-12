# AIPA MCP Governance Roadmap

This roadmap describes future work for the AIPA MCP governance research overlay.

The roadmap is intentionally scoped as research and demonstration work. It does not claim official ToolHive or Stacklok integration.

## Current MVP

The current MVP includes:

- AIPA governance positioning documents
- partnership-safe language guidance
- MCP Governance Knowledge Block schema
- execution receipt schema
- verification boundary map schema
- filesystem, browser/search, and database governance examples
- sample execution receipt
- sample governance record
- sample verification boundary map
- sample audit package summary
- minimal validator
- validator README
- validation manifest
- demo validation runner
- end-to-end filesystem write review scenario

## Near-term work

### 1. Scenario expansion

Add complete scenario packages for:

- browser/search source review
- database read-only query review
- database bulk export escalation
- high-risk human override review
- unsupported verification boundary review

### 2. Validator expansion

Extend the validator to support:

- governance records
- verification boundary maps
- audit package summaries
- scenario folder validation
- manifest-level expected outcomes
- consistency checks across artifacts

Example consistency checks:

- same agent_id across request, receipt, and governance record
- same policy_fingerprint across decision context, receipt, governance record, and boundary map
- high-risk operation includes human oversight
- audit package references existing files

### 3. Schema hardening

Improve schemas for:

- governance records
- audit package summaries
- decision contexts
- tool-use requests
- scenario manifests

### 4. Documentation polish

Add clearer docs for:

- how to read a scenario
- how to run validation
- what PASS, FAIL, and UNSUPPORTED mean
- where AIPA governance ends and runtime/platform control begins

## Medium-term work

### 1. Registry metadata mapping

Explore how governance Knowledge Blocks could reference MCP server registry metadata without becoming a registry replacement.

Possible fields:

- server identifier
- tool name
- risk tier
- owner or maintainer field
- approved use category
- evidence requirements
- policy reference

### 2. Policy fingerprint examples

Add non-cryptographic placeholder examples first, then document how real policy fingerprints could be generated later.

Future policy fingerprint work may include:

- canonical JSON policy form
- hash generation guidance
- version references
- change notes
- policy lineage metadata

### 3. Verification boundary examples

Add examples showing the difference between:

- declared governance context
- reviewable evidence
- unsupported verification claims

### 4. Audit package bundling

Add a simple bundling script or manifest model that groups related artifacts into a review set.

## Future research directions

### 1. External verifier handoff

Define a neutral handoff format that lets governance records be reviewed by separate verification systems.

### 2. Runtime-adjacent metadata

Explore how governance metadata could be emitted beside runtime logs without changing core runtime behavior.

### 3. Multi-agent workflows

Extend the artifact model to cover workflows where multiple agents, tools, or identity contexts participate in a chain.

### 4. Human oversight records

Add richer examples for:

- human approval
- human rejection
- human override
- escalation rationale
- reviewer identity context

### 5. Failure mode library

Document common failure cases:

- missing policy fingerprint
- identity drift
- missing oversight record
- path boundary violation
- cross-tool continuity gap
- unsupported verification claim

## Explicit non-goals

This research overlay is not intended to become:

- a replacement for ToolHive
- a competing MCP runtime
- an official integration claim
- a platform endorsement claim
- a security product clone
- a runtime enforcement engine

## Guiding principle

Keep the governance layer complementary.

MCP platforms can control tool execution.

AIPA governance artifacts can make the surrounding decision context easier to explain, review, and audit.
