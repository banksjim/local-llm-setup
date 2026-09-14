# P07-S003: Learn Langflow for visual RAG

| Property | Value |
|---|---|
| Story ID | P07-S003 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 4 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P07-S018 |
| Unlocks | P07-S004 |
| Preferred route | Interface: goagentic learn; Provider: controller-selected cloud provider; Model class: economical tutor with screen-guidance capability; Effort: medium; Fallback: alternate provider using the committed lesson and screenshots. |
| Research freshness | Current Langflow stable documentation and maintained tutorials checked within 7 days. |

## 1. User story

As the owner, I want a focused Langflow lesson so I can inspect, run, export, and troubleshoot the capstone flow without learning every Langflow feature.

## 2. Bounded objective

Create and complete docs/learning/p07/P07-S003-langflow-visual-rag.md using workloads/rag/fixtures/langflow/learning-flow.json, which accepts a question, retrieves supplied fixture text, and returns an answer with a source identifier.

## 3. Learning objective

Identify components, connections, inputs/outputs, secrets, vector retrieval, model calls, run logs, flow export/import, and the stable API boundary. Explain why Langflow is a visual learning/admin surface rather than the authoritative data store or primary user interface.

## 4. Current research requirements

Use current official Langflow documentation for installation-independent concepts, flow export, the stable run endpoint, API-key handling, and troubleshooting. Include one short overview and one substantive current tutorial.

## 5. Preconditions and unlock conditions

P07-S018 is Done and its synthetic Langflow service is healthy. P07-S004 waits for genuine completion.

## 6. In scope

A 45–90 minute guided lesson, one synthetic flow, one export/import exercise, one deliberate broken connection, one missing-secret failure, and four owner knowledge questions.

## 7. Out of scope and prohibited changes

No private corpus, production flow, internet exposure, stored credentials, arbitrary custom component code, or full Langflow administration course.

## 8. Privilege and human approval

Human participation is required, but no additional privileged authorization is needed. The owner judges usability, not implementation correctness.

## 9. Risk rationale

Low: synthetic data in a prepared local learning surface.

## 10. Execution contract

The lesson guides the owner to trace data through the graph, run it, inspect citations, export it, import a copy, diagnose the two injected faults, and state what belongs outside the flow file.

## 11. Automated acceptance tests

Validate lesson/source freshness; the fixture flow export parses; imported and original flows produce the same fixture source ID; the missing-secret and broken-edge cases fail with named messages; and all four owner responses are present.

## 12. Human validation

The owner successfully locates input, retriever, model, output, and run API; fixes or explains both injected faults; and answers at least 3/4 questions after feedback.

## 13. Idempotency and rollback

Resume returns to the last exercise checkpoint. Synthetic flow copies use unique IDs and can be removed without affecting later production flow state.

## 14. Required evidence

The directory evidence/P07-S003/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Lesson revision, current sources, sanitized screenshots or state captures, export hash, test results, owner answers, score, and completion attestation at evidence/P07-S003/.

## 15. Definition of done

The owner demonstrates the targeted Langflow skills, evidence is genuine, and P07-S004 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S003/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause after every concept and before import/export or fault injection. The controller records the exact next exercise.
