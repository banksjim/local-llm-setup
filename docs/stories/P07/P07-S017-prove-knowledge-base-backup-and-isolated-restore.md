# P07-S017: Prove knowledge-base backup and isolated restore

| Property | Value |
|---|---|
| Story ID | P07-S017 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 19 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P07-S016 |
| Unlocks | P08-S001 |
| Preferred route | Interface: goagentic restore rehearsal plus WSL test runner; Provider: controller-selected cloud provider; Model class: high-reliability operations; Effort: high; Fallback: retain original system untouched and block P08. |
| Research freshness | Current Git bundle/LFS, PostgreSQL backup/restore, archive integrity, Rancher volume, and Windows filesystem guidance checked within 7 days. |

## 1. User story

As the owner, I want a clean-room restore proof so the accepted knowledge base is not dependent on one working directory, database, or chat session.

## 2. Bounded objective

Implement reusable operation operations/windows/p07/P07-S017-kb-backup-restore, create a provider-neutral local recovery package, restore it into isolated roots/services, and prove manifests, Git/assets, flow/config, database/index, and known-answer retrieval match.

## 3. Learning objective

Teach the owner what is backed up, what is recreated, where secrets are excluded, how to launch a restore, and how to recognize a usable result. Durable OneDrive/NAS selection remains P10.

## 4. Current research requirements

Verify current backup/restore commands and compatibility for Git and LFS if used, PostgreSQL/pgvector, container volumes, Langflow export, model/profile inventory, permissions, and checksum tooling.

## 5. Preconditions and unlock conditions

P07-S016 is Done. Activation names source roots, isolated restore roots, test DB/ports/service names, recovery-package location, free-space requirement, encryption decision for private local backup, secret-recreation steps, cleanup, and pre-restore active-system hashes.

## 6. In scope

Immutable snapshots, normalized records, manifests, knowledge Git objects/LFS, flow/config/profile exports, database schema/logical dump, checksums, inventory, restore script, secret placeholders/recreation instructions, isolated services, comparison, retrieval, and cleanup preview.

## 7. Out of scope and prohibited changes

No raw secrets, OAuth tokens, cookies, cloud publication, OneDrive/NAS commitment, overwrite of the accepted live system, restore into existing roots, unsupported secure-erasure promise, or deletion before comparison succeeds.

## 8. Privilege and human approval

Critical: this copies all private knowledge and creates isolated services. Covered by the revision-bound phase preview; the owner confirms the private local package location and performs a guided usability check.

## 9. Risk rationale

Critical: the operation spans all private originals and persistence layers; a wrong target could overwrite or expose the live corpus.

## 10. Execution contract

Preflight exact paths/free space and assert restore targets are new/empty; quiesce or take consistent application-level snapshots; package with inventory/checksums and no secrets; restore under distinct names/ports; recreate least-privilege secrets; verify all layers; run known-answer/abstention set; leave live system untouched; then preview cleanup.

## 11. Automated acceptance tests

Verify package checksums and inventory; snapshot/version/manifest counts; Git fsck and commit hash; every asset/LFS object; schema/profile/flow hashes; DB row/collection/active-pointer counts; citation resolution; known-answer and abstention parity; no secret/token; no live-root mutation. Failure injection covers insufficient space, existing target, corrupt archive, missing LFS object, incompatible DB/extension, missing manifest, wrong model dimension, absent secret, and interrupted restore; each resumes safely or fails cleanly.

## 12. Human validation

Using the restored Open WebUI/Langflow path, the owner asks three accepted questions, opens citations, checks one source and visual asset, and confirms the recovery checklist is understandable. No technical certification is requested.

## 13. Idempotency and rollback

Rerun against a completed restore verifies and reports no change; a new rehearsal uses a new isolated ID. Rollback stops/removes only isolated services and story-owned restore roots after evidence and owner confirmation; the package and live system remain.

## 14. Required evidence

The directory evidence/P07-S017/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Source/package/restore inventories and hashes, free-space/path preflight, secret scan, all nine denial results, interrupted-resume result, Git/DB/flow/citation parity, live-system no-change proof, owner usability result, cleanup/rollback proof, and two technical reviews at evidence/P07-S017/.

## 15. Definition of done

An isolated restore reproduces the accepted knowledge base and cited answers; all corruption/target guards pass; the live system is unchanged; the owner can use the restored path; and P08-S001 is eligible for activation.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S017/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause after package checksum completion or after a complete restore stage with durable inventory. Never pause during live consistency capture, database restore transaction, pointer swap, or cleanup mutation.
