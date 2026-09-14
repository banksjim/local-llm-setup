# P07-S002: Learn RAG concepts and failure modes

| Property | Value |
|---|---|
| Story ID | P07-S002 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 2 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P07-S001 |
| Unlocks | P07-S018 |
| Preferred route | Interface: goagentic learn; Provider: controller-selected cloud provider; Model class: economical tutor; Effort: medium; Fallback: alternate provider using the same committed lesson. |
| Research freshness | Lesson sources regenerated from P07-S001 and checked within 7 days; videos checked for availability and current applicability. |

## 1. User story

As the owner, I want targeted RAG training so I can understand what the system is doing and make meaningful quality judgments without needing a general machine-learning course.

## 2. Bounded objective

Create and complete docs/learning/p07/P07-S002-rag-foundations.md, evidence/P07-S002/knowledge-check.md, and a recorded practical exercise using a small synthetic corpus.

## 3. Learning objective

Explain ingestion, parsing, chunking, embeddings, similarity search, metadata filters, reranking, grounding, citations, evaluation, and the difference between source truth, Markdown derivatives, and indexes. Recognize retrieval failure, extraction failure, unsupported answers, stale indexes, and privacy leakage.

## 4. Current research requirements

Use the P07-S001 baseline. Include one current concise conceptual video, one current deeper tutorial, and current official documentation; label optional material. Replace broken or materially stale resources before activation.

## 5. Preconditions and unlock conditions

P07-S001 is Done and the lesson artifact is committed. The owner may pause and resume. P07-S003 unlocks only after genuine owner responses and the practical exercise are recorded.

## 6. In scope

A 45–90 minute, project-specific lesson; a diagram of the four-layer data model; five scenario questions; and a hands-on comparison of good retrieval, missing evidence, and a misleading fluent answer.

## 7. Out of scope and prohibited changes

No broad data-science curriculum, production implementation, credentials, private documents, service mutation, or LLM-generated answers impersonating the owner.

## 8. Privilege and human approval

No privileged approval is needed. Human participation is required; the LLM cannot manufacture completion or require the owner to review code.

## 9. Risk rationale

Low: learning artifacts and synthetic data only.

## 10. Execution contract

goagentic learn P07-S002 presents one section at a time, records progress after each section, asks the owner to explain concepts in their own words, gives corrective feedback, and stores only completion and answers—not unrelated conversation.

## 11. Automated acceptance tests

Validate that the lesson covers all eleven named concepts, sources are current, the diagram renders, the synthetic exercise has expected retrieval results, all five questions have owner-authored responses, and the evidence record contains timestamps and artifact hashes.

## 12. Human validation

The owner completes the exercise and scores at least 4/5 after feedback, including correctly refusing to trust an answer with no supporting citation. A failed check routes to a focused refresher, not a full restart.

## 13. Idempotency and rollback

Resume starts at the last completed section. Repeating the lesson preserves prior attempts and creates a new attempt record. Rollback removes generated learning state but never falsifies a completed record.

## 14. Required evidence

The directory evidence/P07-S002/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Lesson revision, source list, owner answers, score, feedback, exercise result, progress checkpoints, and completion attestation at evidence/P07-S002/.

## 15. Definition of done

The owner meets the knowledge and practical criteria; evidence is genuine; and P07-S018 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S002/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Every lesson section is a durable checkpoint. No timer or session restart converts incomplete learning to Done.
