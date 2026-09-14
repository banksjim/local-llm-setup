# P07-S012: Implement version, missing-source, and deletion workflow

| Property | Value |
|---|---|
| Story ID | P07-S012 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 14 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P07-S011 |
| Unlocks | P07-S013 |
| Preferred route | Interface: WSL coding agent with goagentic owner confirmation for deletion; Provider: controller-selected cloud provider; Model class: high-reliability coding/security; Effort: high; Fallback: disable deletion and retain prior accepted version. |
| Research freshness | Current Git recovery, PostgreSQL transaction, retention, and secure-deletion limitations checked within 30 days. |

## 1. User story

As the owner, I want explicit change, missing-source, and deletion behavior so absence never silently destroys knowledge or originals.

## 2. Bounded objective

Implement lifecycle code under workloads/rag/lifecycle/ and reusable operation operations/windows/p07/P07-S012-document-lifecycle with version comparison, missing marking, reconciliation, retention inventory, and a separate preview/confirm deletion command spanning all layers.

## 3. Learning objective

The deletion checklist teaches the difference between missing, inactive, superseded, and deleted and shows exactly which recoverable copies remain.

## 4. Current research requirements

Confirm current Git object-recovery limits, filesystem/NAS/OneDrive deletion semantics, database transaction behavior, and truthful language for logical versus physical deletion.

## 5. Preconditions and unlock conditions

P07-S011 is Done. Activation resolves retention defaults and test roots. The implementation and non-destructive tests use phase authorization; any real deletion requires a fresh exact preview and owner confirmation.

## 6. In scope

Stable document identity, new immutable versions, unchanged detection, missing status, reappearance, supersession, active-version pointer, retention report, deletion preview token, typed confirmation, post-delete verification, and audit evidence.

## 7. Out of scope and prohibited changes

No inferred deletion from a missing URL/file, automatic original cleanup, broad directory deletion, history rewriting, secure-erasure guarantee, remote deletion, or deletion outside an exact document/version inventory.

## 8. Privilege and human approval

Critical deletion boundary. The owner confirms each real deletion from a preview naming paths, Git effect, index rows, backup status, and recovery limits. LLM-generated approval is invalid.

## 9. Risk rationale

Critical: deletion may remove original private data and cross multiple persistence layers with uncertain physical recovery.

## 10. Execution contract

Ordinary reconciliation can only add versions or statuses. Deletion requires a short-lived hash-bound preview, verified backup/retention prerequisites, owner confirmation matching that hash, layer-by-layer transaction log, and stop-on-drift. Defaults retain immutable originals.

## 11. Automated acceptance tests

Prove unchanged, changed, missing, reappeared, and superseded transitions. Deny absent confirmation, stale preview, mismatched path/hash, broad target, unbacked original, active-version deletion without replacement, remote/history rewrite, and injected failure at each layer. An isolated synthetic delete must either complete with audit evidence or compensate to the prior accepted state.

## 12. Human validation

The owner performs one synthetic deletion rehearsal, explains what remains recoverable, and confirms the UI clearly distinguishes missing from deleted. No real private document must be deleted for acceptance.

## 13. Idempotency and rollback

Reconciliation is idempotent. Repeating a completed delete reports already completed. Before irreversible removal, rollback cancels. After synthetic removal, restore from the rehearsal backup; real recovery is limited to the previewed backup and Git retention.

## 14. Required evidence

The directory evidence/P07-S012/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Transition matrix, retention report, preview schema, at least eight denial results, per-layer failure injections, synthetic confirmation and restore, owner result, deletion audit fields, rollback limits, and security review at evidence/P07-S012/.

## 15. Definition of done

Absence cannot delete; every transition is validated; deletion requires genuine hash-bound confirmation; isolated compensation/restore works; and P07-S013 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S012/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause before deletion confirmation or after the entire transaction/compensation completes. Never pause between destructive layers.
