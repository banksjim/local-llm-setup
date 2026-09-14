# P04-S011: Connect Open WebUI document extraction and vector storage

| Property | Value |
|---|---|
| Story ID | P04-S011 |
| Phase | P04 — Open WebUI and Supporting AI Services |
| Sequence | 11 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P04-S010 |
| Unlocks | P04-S012 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: qualified local Ollama worker or OpenAI or Anthropic cloud; Model class: current implementation model; Effort: medium; Fallback: current Terra or Sonnet-class cloud route, then Sol or Sonnet-class diagnosis if verification fails. |
| Research freshness | Current Open WebUI document-extraction and vector-database documentation, Docling Serve API, and PGVector image contract checked within 7 days. |

## 1. User story

As the workstation owner, I want Open WebUI to use the private Docling service and PostgreSQL with PGVector for disposable document fixtures, so that document extraction and retrieval foundations are verified without pretending the later knowledge-base system already exists.

## 2. Bounded objective

Configure and verify only Open WebUI document extraction and vector-storage foundations.

## 3. Learning objective

Not applicable — P04-S002 covers the service-boundary concepts and P07 provides the dedicated ingestion and RAG learning gates.

## 4. Current research requirements

Record the exact Open WebUI settings contract, Docling endpoints and limits, PGVector compatibility, versions, image digests, primary-source URLs, and any unsupported integration claim. Training memory is not evidence.

## 5. Preconditions and unlock conditions

P04-S010 is Done; Docling, PostgreSQL/PGVector, and Open WebUI health checks pass; the P04 phase authorization still matches the preview.

## 6. In scope

Create operations/windows/p04/P04-S011-connect-open-webui-document-extraction-and-vector-storage with settings export/import, the accepted P03 embedding profile and dimension, Docling 2.x-compatible parameter JSON, a three-page synthetic PDF fixture, extraction assertions, disposable vector collection, retrieval query, database-row and network-boundary probes, and settings-only rollback. Store sanitized evidence under evidence/P04-S011/.

## 7. Out of scope and prohibited changes

Do not ingest owner documents, create a durable knowledge base, add web scraping, publish Docling or PostgreSQL ports, substitute an embedding model or dimension different from the accepted P03 profile, enable GPU Docling, or alter SearXNG and speech settings.

## 8. Privilege and human approval

No new approval is required while the revision-bound P04 authorization remains valid; stop for a new preview if the settings API, database target, or network boundary differs.

## 9. Risk rationale

Document extraction handles untrusted content and the vector database is durable; an incorrect endpoint or cleanup could expose data or delete unrelated collections.

## 10. Execution contract

Back up Open WebUI settings; prove all three services healthy; create the disposable fixture and uniquely named collection; apply only extraction/vector settings; convert, index, retrieve, and inspect storage; run negative limit and network tests; remove the fixture collection; verify unrelated state; record evidence and release the lease.

## 11. Automated acceptance tests

Assert one fixture and one unique disposable collection. Verify Docling/API version and parameter compatibility, expected headings and tables, the exact accepted embedding model and dimension on both indexing and query, retrieval of a seeded fact with source attribution, rows only in the fixture collection, enforced file/page/time limits, no published Docling/PostgreSQL port, cleanup of the fixture, and zero change to search, speech, or owner data. A model/dimension mismatch must fail before indexing.

## 12. Human validation

Not applicable — synthetic content, deterministic assertions, database inspection, and independent review are sufficient for this infrastructure connection.

## 13. Idempotency and rollback

Second apply reports no settings change and uses a fresh unique fixture collection. Rollback restores the pre-story settings export and removes only the named disposable collection; it never drops a database, role, volume, or unknown collection.

## 14. Required evidence

Commit the operation and fixture plus activation.json, change-inventory.json, extraction assertions, retrieval results, database inventory before and after, network negatives, test-results.json, rollback.json, review.md, and explicit not-applicable human record under evidence/P04-S011/.

## 15. Definition of done

The extraction, retrieval, isolation, limit, cleanup, idempotency, and rollback checks pass; no owner data or unrelated setting changed; independent review has no unresolved material finding; P04-S012 unlocks.

## 16. Pause-safe boundaries

Pause after settings backup, fixture creation, extraction, indexing, retrieval, cleanup, rollback test, and evidence commit. Finish or roll back the active fixture transaction and record the next command in evidence/P04-S011/checkpoint.json.
