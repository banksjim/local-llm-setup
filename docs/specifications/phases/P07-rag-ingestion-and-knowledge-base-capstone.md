# P07: RAG, Ingestion, and Knowledge-Base Capstone

**Depends on:** P06  
**Required outcome:** One private, reproducible knowledge base built from nine source categories, exposed through a cited Langflow retrieval flow and recoverable without the source applications.
**Status:** Planned

## Phase boundary

P07 builds the ingestion and retrieval system described by [SYS-RAG](../systems/RAG-INGESTION.md). It does not build personal agents, durable agent memory, generalized web crawling, a public knowledge service, or the final workstation backup program. The first knowledge base is a proof of the reusable design; later knowledge bases receive separate IDs, configurations, repositories, and indexes.

The phase may not begin until P06 is accepted and `goagentic` has produced a revision-bound activation preview. One owner approval authorizes the previewed privileged operations for this phase. Material changes to targets, mounts, credentials, exposure, deletion behavior, or risk invalidate that authorization.

## Owner responsibilities

The LLM owns engineering design, current-source research, implementation, testing, and technical review. The owner is asked only to:

- complete the targeted RAG and Langflow learning gates;
- authorize the phase preview and any separately identified access boundary;
- authenticate Google Workspace and any explicitly approved private website without disclosing credentials to the LLM;
- stage three examples for each supported category when requested; and
- judge source fidelity, citation usefulness, and restore usability using guided checklists.

The owner is never asked to certify code, architecture, security, or test completeness.

## Fixed acceptance inventory

The nine categories are PDF, DOCX, XLSX, PPTX, Markdown, public/authorized website URL, Google Docs URL, Google Sheets URL, and Google Slides URL. Final acceptance uses three owner-selected inputs in each category, for 27 inputs total. Private inputs and generated private content never enter this public playbook repository.

## Story sequence

| Seq. | Story | Step | Risk |
|---:|---|---|---|
| 1 | [P07-S001: Refresh RAG and ingestion tool guidance](../../stories/P07/P07-S001-refresh-rag-and-ingestion-tool-guidance.md) | Research | Low |
| 2 | [P07-S002: Learn RAG concepts and failure modes](../../stories/P07/P07-S002-learn-rag-concepts-and-failure-modes.md) | Learning | Low |
| 3 | [P07-S018: Deploy the private Langflow learning service](../../stories/P07/P07-S018-deploy-private-langflow-learning-service.md) | Implementation | High |
| 4 | [P07-S003: Learn Langflow for visual RAG](../../stories/P07/P07-S003-learn-langflow-for-visual-rag.md) | Learning | Low |
| 5 | [P07-S004: Define multi-knowledge-base registry and schemas](../../stories/P07/P07-S004-define-multi-knowledge-base-registry-and-schemas.md) | Implementation | Medium |
| 6 | [P07-S019: Initialize the private knowledge-base roots and Git repository](../../stories/P07/P07-S019-initialize-private-knowledge-base-roots-and-git-repository.md) | Implementation | High |
| 7 | [P07-S005: Implement private source intake and immutable snapshots](../../stories/P07/P07-S005-implement-private-source-intake-and-immutable-snapshots.md) | Implementation | Critical |
| 8 | [P07-S006: Implement Docling conversion and lossless archive](../../stories/P07/P07-S006-implement-docling-conversion-and-lossless-archive.md) | Implementation | High |
| 9 | [P07-S007: Implement deterministic YAML frontmatter and filing](../../stories/P07/P07-S007-implement-deterministic-yaml-frontmatter-and-filing.md) | Implementation | Medium |
| 10 | [P07-S008: Implement Crawl4AI one-off web intake](../../stories/P07/P07-S008-implement-crawl4ai-one-off-web-intake.md) | Implementation | High |
| 11 | [P07-S009: Implement guarded authenticated web intake](../../stories/P07/P07-S009-implement-guarded-authenticated-web-intake.md) | Implementation | Critical |
| 12 | [P07-S010: Implement Google Docs, Sheets, and Slides intake](../../stories/P07/P07-S010-implement-google-docs-sheets-and-slides-intake.md) | Implementation | Critical |
| 13 | [P07-S011: Implement visual asset preservation and enrichment](../../stories/P07/P07-S011-implement-visual-asset-preservation-and-enrichment.md) | Implementation | High |
| 14 | [P07-S012: Implement version, missing-source, and deletion workflow](../../stories/P07/P07-S012-implement-version-missing-source-and-deletion-workflow.md) | Implementation | Critical |
| 15 | [P07-S013: Implement chunking, embeddings, and transactional indexing](../../stories/P07/P07-S013-implement-chunking-embeddings-and-transactional-indexing.md) | Implementation | High |
| 16 | [P07-S014: Build the Langflow personal RAG capstone](../../stories/P07/P07-S014-build-the-langflow-personal-rag-capstone.md) | Implementation | High |
| 17 | [P07-S015: Run synthetic ingestion acceptance suite](../../stories/P07/P07-S015-run-synthetic-ingestion-acceptance-suite.md) | Testing | High |
| 18 | [P07-S016: Run owner-provided 27-document acceptance](../../stories/P07/P07-S016-run-owner-provided-27-document-acceptance.md) | Human Validation | Critical |
| 19 | [P07-S017: Prove knowledge-base backup and isolated restore](../../stories/P07/P07-S017-prove-knowledge-base-backup-and-isolated-restore.md) | Testing | Critical |

## Completion gate

P07 is complete only when every non-superseded story is Done; the 27-input matrix has an outcome for every cell; unchanged reingestion is byte-stable; failed jobs cannot change the active index; private and secret scans are clean; cited retrieval passes the versioned evaluation set; and a clean-room restore reproduces the accepted corpus and query results. Defects create correction stories and block P08.
