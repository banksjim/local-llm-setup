# P07-S005: Implement private source intake and immutable snapshots

| Property | Value |
|---|---|
| Story ID | P07-S005 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 7 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P07-S019 |
| Unlocks | P07-S006 |
| Preferred route | Interface: WSL coding agent through goagentic deployment; Provider: controller-selected cloud provider; Model class: high-reliability coding; Effort: high; Fallback: second provider plus isolated rehearsal. |
| Research freshness | Current file-signature, safe-copy, hashing, Windows volume, container-mount, and malware-handling guidance checked within 30 days. |

## 1. User story

As the owner, I want authorized inputs copied into append-only managed storage so originals survive conversion errors and never enter Git.

## 2. Bounded objective

Implement the intake module under workloads/rag/ingestion/ and reusable operation operations/windows/p07/P07-S005-private-source-intake with intake, inspect, resume, and quarantine commands that create content-addressed snapshots and atomic manifests under one approved knowledge-source root.

## 3. Learning objective

Not applicable — this implements the preservation boundary taught in P07-S002.

## 4. Current research requirements

Resolve safe atomic-replace semantics on NTFS/container mounts, supported file signatures, cryptographic hash choice, maximum-size defaults, and current Rancher Desktop mount behavior.

## 5. Preconditions and unlock conditions

P07-S019 is Done. The activation packet names the exact KB ID, source root, intake staging root, mount, limits, service identity, and rollback point. Phase authorization must cover these targets; any different root requires a new preview.

## 6. In scope

PDF, DOCX, XLSX, PPTX, and Markdown file intake; staged copy; signature/extension validation; size/time limits; pre/post hash verification; duplicate reuse; stable document and immutable version IDs; atomic manifests; quarantine; restart; and read-only inventory.

## 7. Out of scope and prohibited changes

No conversion, web/Google fetching, Office macro execution, external-link traversal, archive extraction, legacy formats, deletion, Git add, database write, unrelated H-drive access, or agent access to private content.

## 8. Privilege and human approval

Covered by the revision-bound P07 authorization because it writes private originals and configures a narrow mount. The owner only satisfies an elevation prompt if required and stages files; no technical review is requested.

## 9. Risk rationale

Critical: this crosses the original-data boundary. A path or copy defect could lose or expose originals across host/container storage.

## 10. Execution contract

Copy into a unique staging file, refuse symlinks/reparse escapes, validate type and limits, hash staged bytes, atomically place a read-only content-addressed snapshot, rehash it, then atomically write the manifest and mark snapshotted. An interrupted or mismatched copy remains quarantined. Existing snapshots are never overwritten.

## 11. Automated acceptance tests

Use synthetic fixtures to prove five types ingest; duplicate bytes reuse one snapshot; same logical source with changed bytes creates a new version; interrupted copy, wrong signature, oversized file, path escape, symlink/reparse point, read-only destination, hash mismatch, macro-enabled file, and injected manifest-write failure never produce snapshotted state. Assert zero originals appear in either Git repository.

## 12. Human validation

The owner stages one harmless test file and confirms the guided intake view shows its logical name, hash prefix, status, and managed location without displaying content. Engineering correctness remains LLM-reviewed.

## 13. Idempotency and rollback

Repeated intake of identical bytes creates no new snapshot or manifest version. Rollback removes only story-created synthetic/staging artifacts and configuration; real immutable snapshots are preserved and merely deregistered pending a separate deletion approval.

## 14. Required evidence

The directory evidence/P07-S005/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Resolved roots/mounts, identity and ACL summary, snapshot tree with synthetic names, test count and outcomes, interruption logs, hash comparison, Git exclusion scan, second-run result, rollback rehearsal, owner test result, and review at evidence/P07-S005/.

## 15. Definition of done

Every positive and denial test passes; the mount cannot reach unrelated paths; originals are append-only and outside Git; the owner test succeeds; and P07-S006 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S005/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause before copy or after manifest commit. If interrupted mid-copy, resume quarantines or completes from staging only after full revalidation.
