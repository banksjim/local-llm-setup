# P09-S011: Prove memory backup, restore, export, and deletion

| Property | Value |
|---|---|
| Story ID | P09-S011 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 12 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P09-S010 |
| Unlocks | P09-S012 |
| Preferred route | Interface: goagentic restore rehearsal with WSL test runner and guided local inspection; Provider: controller-selected cloud provider; Model class: high-reliability operations; Effort: high; Fallback: keep live system disabled and restore the last verified snapshot. |
| Research freshness | Current selected storage/framework, encryption, backup, secure-deletion, and migration docs checked within 7 days. |

## 1. User story
As the owner, I want proof that I can recover, move, inspect, and truly delete my memory without resurrecting it.
## 2. Bounded objective
Create operations/windows/p09/P09-S011-memory-data-lifecycle/ and run isolated backup/restore, canonical export/import, scoped deletion, retention, key recovery, projection rebuild, and framework-exit rehearsals.
## 3. Learning objective
The owner learns only how to locate an export, recognize its manifest, and initiate restore/delete safely; this targeted operation is part of validation.
## 4. Current research requirements
Resolve exact backup consistency, key custody/recovery, secure-deletion limits on SSD/snapshots, and framework migration constraints; state limitations plainly.
## 5. Preconditions and unlock conditions
P09-S010 is Done. Activation fixes synthetic corpus/counts/hashes, isolated restore target, backup/key locations, retention, deletion propagation, rollback, and owner observation steps.
## 6. In scope
Consistent ledger/projection/config backup; secret/key manifest without key material; isolated restore; projection rebuild; portable JSONL export; clean import into adapter baseline; candidate expiry; one-record/namespace/all-content deletion; backup aging; and tombstone non-resurrection.
## 7. Out of scope and prohibited changes
No destructive test on live owner data, claim of physical SSD erasure, unencrypted backup, key in backup/Git/evidence, deletion of non-P09 data, final NAS/OneDrive choice, or reliance on projection-only export.
## 8. Privilege and human approval
Covered by P09 authorization. The owner performs the explicit local export inspection and confirms the isolated target; no additional approval unless targets change.
## 9. Risk rationale
Critical: restore/deletion/key operations can lose or expose private data. Revision-bound authorization, isolated rehearsal, cross-provider review, genuine owner validation here, and final owner acceptance in P09-S012 are mandatory.
## 10. Execution contract
Inventory/hash synthetic live state; quiesce or snapshot consistently; back up; restore into validated isolated path; compare ledger/policies/behavior; rebuild projection; export/import baseline; exercise scoped deletion and backup aging; attempt resurrection; recover key; clean only isolated data; review.
## 11. Automated acceptance tests
Match record/version/decision/tombstone counts and hashes; verify authorization, provenance, Restricted exclusions, key separation, corrupt/wrong-key/partial backup failure, cross-version migration, projection rebuild, deletion from live/cache/projection/eligible backups, no resurrection, target guards, no-op rerun, and unchanged live system.
## 12. Human validation
The owner inspects only the synthetic export manifest, identifies scope/date/encryption status, and confirms the guided restore/delete controls are understandable. The LLM cannot author the observation.
## 13. Idempotency and rollback
Backup is content-addressed; repeated restore to same empty target matches. Destructive drills are isolated. Rollback removes only rehearsal targets and returns live capture/recall to its pre-test state.
## 14. Required evidence
evidence/P09-S011/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, backup-manifest.json, restore-comparison.json, export-import.json, deletion-results.json, key-recovery.json, and human-validation.md.
## 15. Definition of done
Restore/export/import/rebuild/key recovery work, deletion does not resurrect content, live state is unchanged, owner evidence is genuine, and review resolves.
## 16. Pause-safe boundaries
Update evidence/P09-S011/checkpoint.json before each backup/restore/delete and after verification; never pause mid-restore/deletion or with keys/rehearsal data unaccounted.
