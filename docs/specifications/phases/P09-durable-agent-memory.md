# P09: Durable Agent Memory

**Depends on:** P08

**Required outcome:** A currently selected OSS or composable memory system provides owner-reviewed promotion, provenance, namespaces, restriction, export/deletion, and one proven life-planning-agent integration.

**Status:** Planned

## Gate

P08-S010 must be Done with the life-planning agent accepted. P09-S001 research, P09-S002 architecture selection, and P09-S003 learning may run before privileged authorization. Before deployment, the controller presents one revision-bound P09 packet covering exact versions/digests, local models, service/data/secret paths, ports and private networks, database and projection identities, memory classes/retention, capture defaults, source-context handling, encryption/key recovery, deletion/backup semantics, test fixtures, failure injection, and rollback. Material change invalidates the authorization.

## Fixed execution sequence

| Seq. | Story | Step | Risk |
|---:|---|---|---|
| 1 | [P09-S001: Research and score current OSS memory frameworks](../../stories/P09/P09-S001-research-and-score-current-oss-memory-frameworks.md) | Research | Medium |
| 2 | [P09-S002: Select memory architecture through an ADR](../../stories/P09/P09-S002-select-memory-architecture-through-an-adr.md) | Review | High |
| 3 | [P09-S003: Learn the selected memory framework and concepts](../../stories/P09/P09-S003-learn-the-selected-memory-framework-and-concepts.md) | Learning | Low |
| 4 | [P09-S013: Deploy the selected private memory foundation](../../stories/P09/P09-S013-deploy-the-selected-private-memory-foundation.md) | Implementation | Critical |
| 5 | [P09-S004: Implement memory storage and provenance schema](../../stories/P09/P09-S004-implement-memory-storage-and-provenance-schema.md) | Implementation | Critical |
| 6 | [P09-S005: Implement candidate-memory capture](../../stories/P09/P09-S005-implement-candidate-memory-capture.md) | Implementation | High |
| 7 | [P09-S006: Implement the reviewed inbox](../../stories/P09/P09-S006-implement-the-reviewed-inbox.md) | Implementation | High |
| 8 | [P09-S007: Implement durable promotion and correction](../../stories/P09/P09-S007-implement-durable-promotion-and-correction.md) | Implementation | Critical |
| 9 | [P09-S008: Implement namespace and restricted-memory enforcement](../../stories/P09/P09-S008-implement-namespace-and-restricted-memory-enforcement.md) | Implementation | Critical |
| 10 | [P09-S009: Integrate memory with the life-planning agent](../../stories/P09/P09-S009-integrate-memory-with-one-accepted-personal-agent.md) | Implementation | Critical |
| 11 | [P09-S010: Evaluate memory quality and poisoning resistance](../../stories/P09/P09-S010-evaluate-memory-quality-and-poisoning-resistance.md) | Testing | Critical |
| 12 | [P09-S011: Prove memory backup, restore, export, and deletion](../../stories/P09/P09-S011-prove-memory-backup-restore-export-and-deletion.md) | Testing | Critical |
| 13 | [P09-S012: Perform memory owner acceptance](../../stories/P09/P09-S012-perform-memory-owner-acceptance.md) | Human Validation | Critical |

Story IDs remain stable when newly discovered work is inserted; Sequence controls execution order.

## Completion

All 13 stories are Done; the exact selected framework and license are recorded; capture defaults off until accepted; only genuine owner decisions promote memory; private evidence remains outside the public repository; every Critical story has authorization, isolated rehearsal, recovery, cross-provider review, and owner-acceptance coverage; all system invariants pass; and no unresolved High/Critical finding remains.
