# AIPA MCP Governance Overlay Architecture Diagrams

This document provides simple architecture diagrams for the AIPA MCP governance research overlay.

The diagrams are explanatory. They do not claim official integration, runtime enforcement, certification, attestation, or endorsement.

## 1. Runtime layer versus governance layer

MCP-style runtime and security systems control operational behavior.

AIPA governance artifacts explain the decision context around that behavior.

```mermaid
flowchart LR
    A[Agent or User Request] --> B[MCP Runtime or Agent Security Layer]
    B --> C[MCP Server or Tool]
    B --> D[AIPA Governance Overlay]
    D --> E[Governance Record]
    D --> F[Execution Receipt]
    D --> G[Verification Boundary Map]
    D --> H[Audit Package Summary]
```

Key point:

```text
Runtime controls execution.
Governance records explain review context.
```

## 2. Governance artifact flow

This is the general artifact flow used across the v0.1 scenario packages.

```mermaid
flowchart TD
    A[Request] --> B[Decision Context]
    B --> C[Execution Receipt]
    C --> D[Governance Record]
    D --> E[Verification Boundary Map]
    E --> F[Audit Package Summary]
```

In server lifecycle scenarios, the flow may include server-specific artifacts.

```mermaid
flowchart TD
    A[Server Capability Block] --> B[Server Trust Profile]
    B --> C[Install Request]
    C --> D[Approval or Denial Decision]
    D --> E[Install Governance Record]
    E --> F[Verification Boundary Map]
    F --> G[Audit Package Summary]
```

## 3. PASS, FAIL, and UNSUPPORTED outcomes

The overlay separates structural validity from governance outcome.

```mermaid
flowchart TD
    A[Review Package] --> B{Is package structurally reviewable?}
    B -- No --> C[Structural Validation Error]
    B -- Yes --> D{What does the evidence support?}
    D -- Supports approval or valid claim --> E[PASS]
    D -- Supports denial or invalid claim --> F[FAIL]
    D -- Evidence outside boundary --> G[UNSUPPORTED]
```

Key point:

```text
A FAIL governance outcome does not mean the scenario files are broken.
It means the evidence supports denial or failure of the governance request.
```

## 4. Verification boundary model

Governance records can declare claims.

Verification boundary maps identify which claims are reviewable with available evidence.

```mermaid
flowchart LR
    A[Governance Claim] --> B[Available Evidence]
    B --> C{Inside Verification Boundary?}
    C -- Yes --> D[Reviewable Claim]
    C -- No --> E[Unsupported Claim]
    D --> F[PASS or FAIL]
    E --> G[UNSUPPORTED]
```

The boundary prevents the system from claiming more certainty than the evidence supports.

## 5. Server install governance lifecycle

This diagram shows how a server install or exposure decision can be represented as a governance package.

```mermaid
flowchart TD
    A[Discover MCP Server] --> B[Create Capability Block]
    B --> C[Create Server Trust Profile]
    C --> D[Evaluate Policy Block]
    D --> E{Decision}
    E -- Approve --> F[Install Governance Record]
    E -- Deny --> G[Denied Install Governance Record]
    E -- Escalate --> H[Escalation Record]
    F --> I[Audit Package]
    G --> I
    H --> I
```

Key point:

```text
Approval, denial, and escalation can all be represented as governance outcomes.
```

## 6. External verifier handoff concept

AIPA governance artifacts can package evidence for an independent verifier without requiring the verifier to trust the originating governance layer.

```mermaid
flowchart LR
    A[AIPA Governance Record] --> B[Evidence References]
    B --> C[Verifier Handoff Package]
    C --> D[Independent Verification System]
    D --> E[PASS / FAIL / UNSUPPORTED Result]
```

This supports a separation between:

```text
governance declaration
```

and:

```text
independent verification
```

## 7. Audit package composition

Audit packages summarize related artifacts so reviewers do not need to reconstruct the chain manually.

```mermaid
flowchart TD
    A[Knowledge Block] --> G[Audit Package]
    B[Policy Reference] --> G
    C[Execution Receipt] --> G
    D[Governance Record] --> G
    E[Verification Boundary Map] --> G
    F[Human Review Record] --> G
    G --> H[Reviewer]
```

## 8. Reusable overlay pattern

The AIPA overlay pattern can be reused across compatible public repositories when the positioning is partner-safe and non-competitive.

```mermaid
flowchart TD
    A[Public AI Infrastructure Repo] --> B[Identify Governance Surface]
    B --> C[Add AIPA Governance Notice]
    C --> D[Add Schemas]
    D --> E[Add Examples]
    E --> F[Add Scenarios]
    F --> G[Add Validator]
    G --> H[Document Boundaries]
    H --> I[Partner Review Package]
```

## Diagram summary

The architecture can be summarized as:

```text
Runtime systems execute.
Governance artifacts explain.
Verification boundaries constrain certainty.
Audit packages make review practical.
```

That is the core architectural position of the AIPA MCP governance research overlay.
