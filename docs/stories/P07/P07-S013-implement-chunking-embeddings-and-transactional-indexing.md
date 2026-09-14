# P07-S013: Implement chunking, embeddings, and transactional indexing

| Property | Value |
|---|---|
| Story ID | P07-S013 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 15 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P07-S012 |
| Unlocks | P07-S014 |
| Preferred route | Interface: WSL coding agent plus local Ollama/PostgreSQL; Provider: controller-selected cloud provider for code and approved local embedding model at runtime; Model class: high-reliability coding; Effort: high; Fallback: exact-search small corpus and previous accepted embedding profile. |
| Research freshness | Current selected embedding model card/license, Ollama embedding API, LangChain PostgreSQL package, PostgreSQL, and pgvector docs/releases checked within 7 days. |

## 1. User story

As the owner, I want versioned chunks and transactional indexes so retrieval is reproducible and a failed reindex cannot replace a working corpus.

## 2. Bounded objective

Implement indexing under workloads/rag/indexing/ and reusable operation operations/windows/p07/P07-S013-transactional-indexing with content-aware chunk profiles, stable chunk IDs, local embeddings, least-privilege storage, transaction-specific Git refs, shadow collections, paired Git/index publication, cited retrieval, and named full reindex.

## 3. Learning objective

Not applicable — chunking and embeddings were learned in P07-S002; this story implements and measures them.

## 4. Current research requirements

Resolve model digest, dimension, query/document prefixes, context limit, license, normalization, distance metric, Python adapter/API stability, pgvector release, and measured HNSW/IVFFlat/exact-search tradeoffs.

## 5. Preconditions and unlock conditions

P07-S012 is Done. Activation names the dedicated P04 database/schema/role, localhost network, model/profile, shadow naming, evaluation thresholds, resource budget, and rollback collection. The role cannot access OpenWebUI or MLflow databases.

## 6. In scope

Heading/table-aware chunks, overlap rules, stable identifiers, metadata, batch/retry limits, embedding dimension checks, transaction-specific Git ref, shadow index, reconciliation journal, paired accepted-Git and active-index pointers, exact-versus-approximate comparison, citation resolver, inactive retention, and reindex command.

## 7. Out of scope and prohibited changes

No cloud embeddings, direct source-file indexing, shared database credentials, silent model/profile change, destructive in-place rebuild, arbitrary SQL identifiers, active collection deletion, or model-judge-only acceptance.

## 8. Privilege and human approval

P07 authorization covers local model/database writes within named identities and schemas. Credential values remain in secret storage and are not exposed to the LLM.

## 9. Risk rationale

High: multiple local services and private derived content are changed; incorrect publication can corrupt retrieval, but originals remain safe.

## 10. Execution contract

Validate derivative/profile first; create a candidate commit on a transaction-specific Git ref; hard-fail dimension mismatch before vector writes; write deterministic chunk IDs to a named shadow collection; validate counts, referential integrity, duplicate absence, known-answer retrieval, exact-search recall, and citations; journal and update the accepted Git ref plus active-index pointer; reconcile or restore both on a partial finalization; retain prior Git and index states.

## 11. Automated acceptance tests

Golden fixtures prove stable chunks, tables/headings, metadata filters, known answers, citation resolution, unchanged reingest, changed document, and named reindex. Inject model unavailable, dimension mismatch, partial batch, duplicate ID, DB disconnect, bad identifier, orphan chunk, low recall, index-pointer failure, Git-ref failure, and failure between the two final updates; reconciliation must restore or complete the pair, and the prior accepted pair must remain usable.

## 12. Human validation

The owner asks three guided synthetic questions and confirms citations open the expected Markdown sections. The LLM owns metric and transaction review.

## 13. Idempotency and rollback

Same accepted version/profile produces no new active collection or duplicate vectors. Rollback atomically restores the previous active pointer and removes only the failed shadow after evidence is retained.

## 14. Required evidence

The directory evidence/P07-S013/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Model/profile/dimension/license, database grants, stable chunk hashes, exact/approximate recall, all ten failure results, active-pointer history, counts/referential checks, owner citation result, rerun result, rollback rehearsal, and review at evidence/P07-S013/.

## 15. Definition of done

Stable chunks and citations work; measured retrieval meets thresholds; every injected failure preserves the old active index; and P07-S014 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S013/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause before shadow build or after verified pointer swap. A partially built shadow may be resumed only after profile and source-commit revalidation.
