# P07-S014: Build the Langflow personal RAG capstone

| Property | Value |
|---|---|
| Story ID | P07-S014 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 16 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P07-S013 |
| Unlocks | P07-S015 |
| Preferred route | Interface: WSL coding agent plus localhost Langflow/Open WebUI; Provider: controller-selected cloud provider for integration and approved local Ollama model for runtime; Model class: high-reliability coding/local chat; Effort: high; Fallback: direct tested retrieval API while Langflow adapter is corrected. |
| Research freshness | Current Langflow stable run/export/API-key docs and current Open WebUI extension/tool integration docs checked within 7 days. |

## 1. User story

As the owner, I want the accepted retrieval pipeline represented in Langflow and callable from Open WebUI so I can learn visually while using one normal chat interface.

## 2. Bounded objective

Build workloads/rag/langflow/personal-rag.json and reusable operation operations/windows/p07/P07-S014-langflow-capstone to deploy a localhost-only flow that queries the active index, invokes the approved local model, returns structured citations, emits redacted MLflow traces, and is invoked through Open WebUI.

## 3. Learning objective

Reinforce P07-S003 by showing the owner where retrieval, prompt grounding, model generation, citations, and traces appear in the production-like flow.

## 4. Current research requirements

Verify the current stable Langflow run endpoint/export format and Open WebUI integration mechanism at activation; avoid beta APIs unless no stable route exists and the activation packet records the risk/fallback.

## 5. Preconditions and unlock conditions

P07-S013 is Done. Activation resolves flow ID/name, endpoint, authentication, network policy, Open WebUI adapter, model, prompt, citation schema, trace redaction, timeout, and previous configuration checkpoint.

## 6. In scope

Versioned flow JSON, externalized secrets, active-index retriever, grounded prompt, abstention behavior, structured citations, local model, MLflow spans, localhost/private-network binding, Open WebUI adapter, health check, and export/import.

## 7. Out of scope and prohibited changes

No public binding, cloud model, embedded credentials, arbitrary custom-code component without review, Langflow as primary UI/data store, beta API by convenience, uncited confident answers, or private source text in MLflow.

## 8. Privilege and human approval

P07 authorization covers local service configuration and private derived content. The owner performs guided usability validation, not technical approval.

## 9. Risk rationale

High: integration spans Open WebUI, Langflow, Ollama, PGVector, and MLflow and handles private knowledge.

## 10. Execution contract

Import the reviewed flow, inject secrets at runtime, validate only approved network routes, invoke stable run API, map citations into the Open WebUI response, redact before tracing, and preserve the prior Open WebUI/Langflow configuration checkpoint until acceptance.

## 11. Automated acceptance tests

Test grounded answer, unknown-answer abstention, multiple citations, metadata filter, citation link resolution, Open WebUI invocation, flow export/import equivalence, trace redaction, and health restart. Inject Langflow unavailable, model unavailable, DB unavailable, invalid API key, prompt injection in a document, missing citation, timeout, malformed response, and private-text trace; every failure is bounded and does not expose or fabricate.

## 12. Human validation

The owner asks three known and two unknown questions in Open WebUI, opens citations, identifies the flow stages in Langflow, and confirms unknown questions abstain. The checklist asks only about observable usefulness.

## 13. Idempotency and rollback

Redeploying the same flow/config creates no duplicate. Rollback restores the saved Open WebUI adapter and prior Langflow flow while leaving the accepted index intact.

## 14. Required evidence

The directory evidence/P07-S014/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Flow export hash, endpoint/auth/network settings without secrets, prompt/citation schema, integration and nine failure results, trace-redaction scan, restart/import equivalence, owner five-question outcome, rerun, rollback, and cross-provider review at evidence/P07-S014/.

## 15. Definition of done

Open WebUI invokes the local Langflow flow; answers cite or abstain; traces are sanitized; failure modes are bounded; the owner can inspect the flow; and P07-S015 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S014/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause before configuration switch or after health and rollback checkpoints. Never pause with only one side of the Open WebUI/Langflow contract updated.
