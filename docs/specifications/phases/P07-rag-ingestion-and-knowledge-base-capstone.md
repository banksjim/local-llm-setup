# P07: RAG, Ingestion, and Knowledge-Base Capstone

**Depends on:** P06  
**Required outcome:** A reproducible multi-format ingestion pipeline and substantial private RAG knowledge base with grounded evaluation.  
**Status:** Planned

## Gate

Dependencies and owner authorization are required. Research and design may occur earlier; implementation cannot cross this gate.

## Story sequence

| Seq. | Story | Step | Risk |
|---:|---|---|---|
| 1 | [P07-S001: Refresh RAG and ingestion tool guidance](../../stories/P07/P07-S001-refresh-rag-and-ingestion-tool-guidance.md) | Research | Low |
| 2 | [P07-S002: Learn RAG concepts and failure modes](../../stories/P07/P07-S002-learn-rag-concepts-and-failure-modes.md) | Learning | Low |
| 3 | [P07-S003: Learn Langflow for visual RAG](../../stories/P07/P07-S003-learn-langflow-for-visual-rag.md) | Learning | Low |
| 4 | [P07-S004: Define multi-knowledge-base registry and schemas](../../stories/P07/P07-S004-define-multi-knowledge-base-registry-and-schemas.md) | Implementation | Medium |
| 5 | [P07-S005: Implement private source intake and immutable snapshots](../../stories/P07/P07-S005-implement-private-source-intake-and-immutable-snapshots.md) | Implementation | High |
| 6 | [P07-S006: Implement Docling conversion and lossless archive](../../stories/P07/P07-S006-implement-docling-conversion-and-lossless-archive.md) | Implementation | High |
| 7 | [P07-S007: Implement deterministic YAML frontmatter and filing](../../stories/P07/P07-S007-implement-deterministic-yaml-frontmatter-and-filing.md) | Implementation | Medium |
| 8 | [P07-S008: Implement Crawl4AI one-off web intake](../../stories/P07/P07-S008-implement-crawl4ai-one-off-web-intake.md) | Implementation | High |
| 9 | [P07-S009: Implement guarded authenticated web intake](../../stories/P07/P07-S009-implement-guarded-authenticated-web-intake.md) | Implementation | Critical |
| 10 | [P07-S010: Implement Google Docs, Sheets, and Slides intake](../../stories/P07/P07-S010-implement-google-docs-sheets-and-slides-intake.md) | Implementation | High |
| 11 | [P07-S011: Implement visual asset preservation and enrichment](../../stories/P07/P07-S011-implement-visual-asset-preservation-and-enrichment.md) | Implementation | High |
| 12 | [P07-S012: Implement version, missing-source, and deletion workflow](../../stories/P07/P07-S012-implement-version-missing-source-and-deletion-workflow.md) | Implementation | High |
| 13 | [P07-S013: Implement chunking, embeddings, and transactional indexing](../../stories/P07/P07-S013-implement-chunking-embeddings-and-transactional-indexing.md) | Implementation | High |
| 14 | [P07-S014: Build the Langflow personal RAG capstone](../../stories/P07/P07-S014-build-the-langflow-personal-rag-capstone.md) | Implementation | High |
| 15 | [P07-S015: Run synthetic ingestion acceptance suite](../../stories/P07/P07-S015-run-synthetic-ingestion-acceptance-suite.md) | Testing | High |
| 16 | [P07-S016: Run owner-provided 27-document acceptance](../../stories/P07/P07-S016-run-owner-provided-27-document-acceptance.md) | Human Validation | Critical |
| 17 | [P07-S017: Prove knowledge-base backup and isolated restore](../../stories/P07/P07-S017-prove-knowledge-base-backup-and-isolated-restore.md) | Testing | Critical |

## Completion

All non-superseded stories are Done; human evidence is genuine; findings resolve; rollback exists; and the outcome is demonstrated.

