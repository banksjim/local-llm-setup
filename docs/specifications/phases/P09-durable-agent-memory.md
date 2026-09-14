# P09: Durable Agent Memory

**Depends on:** P08  
**Required outcome:** A selected OSS memory system with reviewed promotion, namespaces, provenance, restriction, and one proven agent integration.  
**Status:** Planned

## Gate

Dependencies and owner authorization are required. Research and design may occur earlier; implementation cannot cross this gate.

## Story sequence

| Seq. | Story | Step | Risk |
|---:|---|---|---|
| 1 | [P09-S001: Research and score current OSS memory frameworks](../../stories/P09/P09-S001-research-and-score-current-oss-memory-frameworks.md) | Research | Medium |
| 2 | [P09-S002: Select memory architecture through an ADR](../../stories/P09/P09-S002-select-memory-architecture-through-an-adr.md) | Review | High |
| 3 | [P09-S003: Learn the selected memory framework and concepts](../../stories/P09/P09-S003-learn-the-selected-memory-framework-and-concepts.md) | Learning | Low |
| 4 | [P09-S004: Implement memory storage and provenance schema](../../stories/P09/P09-S004-implement-memory-storage-and-provenance-schema.md) | Implementation | High |
| 5 | [P09-S005: Implement candidate-memory capture](../../stories/P09/P09-S005-implement-candidate-memory-capture.md) | Implementation | High |
| 6 | [P09-S006: Implement the reviewed inbox](../../stories/P09/P09-S006-implement-the-reviewed-inbox.md) | Implementation | High |
| 7 | [P09-S007: Implement durable promotion and correction](../../stories/P09/P09-S007-implement-durable-promotion-and-correction.md) | Implementation | Critical |
| 8 | [P09-S008: Implement namespace and restricted-memory enforcement](../../stories/P09/P09-S008-implement-namespace-and-restricted-memory-enforcement.md) | Implementation | Critical |
| 9 | [P09-S009: Integrate memory with one accepted personal agent](../../stories/P09/P09-S009-integrate-memory-with-one-accepted-personal-agent.md) | Implementation | High |
| 10 | [P09-S010: Evaluate memory quality and poisoning resistance](../../stories/P09/P09-S010-evaluate-memory-quality-and-poisoning-resistance.md) | Testing | Critical |
| 11 | [P09-S011: Prove memory backup, restore, export, and deletion](../../stories/P09/P09-S011-prove-memory-backup-restore-export-and-deletion.md) | Testing | Critical |
| 12 | [P09-S012: Perform memory owner acceptance](../../stories/P09/P09-S012-perform-memory-owner-acceptance.md) | Human Validation | Critical |

## Completion

All non-superseded stories are Done; human evidence is genuine; findings resolve; rollback exists; and the outcome is demonstrated.

