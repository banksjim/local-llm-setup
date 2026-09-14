# P07-S019: Initialize the private knowledge-base roots and Git repository

| Property | Value |
|---|---|
| Story ID | P07-S019 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 6 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P07-S004 |
| Unlocks | P07-S005 |
| Preferred route | Interface: Windows controller with WSL coding agent; Provider: controller-selected cloud provider; Model class: high-reliability operations; Effort: high; Fallback: restore the pre-story filesystem checkpoint and keep the KB uninitialized. |
| Research freshness | Current Git, Git LFS if proposed, Windows ACL, NTFS path, Rancher mount, and private-remote visibility guidance checked within 30 days. |

## 1. User story

As the owner, I want the first knowledge base initialized with explicit private roots and a hardened local Git repository so later stories never invent storage or publication policy.

## 2. Bounded objective

Implement reusable operation operations/windows/p07/P07-S019-initialize-private-kb to create one registry entry, H:\ai\knowledge-sources\<kb-id>, H:\ai\knowledge-repos\<kb-id>, the required subtrees, and an initialized local Git repository with privacy guards and no remote.

## 3. Learning objective

Not applicable — the four-layer storage model is taught in P07-S002; this story implements its first instance.

## 4. Current research requirements

Verify current Git initialization/default-branch behavior, safe.directory implications, Git LFS availability only if proposed, Windows ACL inheritance, case sensitivity, path limits, and Rancher mount behavior. Do not infer remote privacy from repository naming.

## 5. Preconditions and unlock conditions

P07-S004 is Done. The activation packet resolves the owner-approved KB ID/display name, exact roots, expected empty/nonexistent state, ACL principals, Git identity source, default branch, allowed generated subtrees, and rollback checkpoint.

## 6. In scope

One KB registry record; source subtrees for snapshots, normalized records, manifests, staging, and quarantine; repository subtrees for documents, assets, schemas, flows, tests, and metadata; local Git initialization; deny-by-default ignore/validation policy; README privacy notice; ACL validation; and no-remote assertion.

## 7. Out of scope and prohibited changes

No source ingestion, content conversion, database/index, service deployment, remote creation, GitHub publication, Git LFS activation without an accepted need and restore plan, private data, deletion of preexisting paths, or access outside the two resolved roots.

## 8. Privilege and human approval

The revision-bound P07 authorization covers creation of the exact H-drive roots and local repository. If either target already exists or permissions differ from preview, stop for reconciliation rather than overwrite.

## 9. Risk rationale

High: host storage, ACLs, registry state, and a future private-data Git boundary are established across Windows and Rancher; wrong paths or visibility could affect multiple later services.

## 10. Execution contract

Preflight absolute resolved paths, volume identity, free space, collisions, ACL inheritance, and Git identity; create only missing directories; initialize Git with the resolved branch; install privacy checks; create a public-safe synthetic seed commit; verify no remote and no source-root path can be added; then record the registry atomically.

## 11. Automated acceptance tests

Prove exact roots and subtrees, expected ACLs, clean Git status, seed commit, no remote, source/repository separation, and repeat no-op. Failure injection denies path traversal, symlink/reparse escape, wrong volume, existing nonempty target, invalid KB ID, case-colliding ID, public remote, source-file git add, secret/private canary, insufficient space, bad ACL, and partial registry write; rollback must leave preexisting data untouched.

## 12. Human validation

Not applicable — the owner is shown a plain-language root and privacy summary, but technical acceptance is automated and cross-provider reviewed.

## 13. Idempotency and rollback

The same KB ID/config returns the existing verified instance without another commit. Before real content exists, rollback removes only story-created empty roots and synthetic seed state after exact ownership checks; it never removes a preexisting path.

## 14. Required evidence

The directory evidence/P07-S019/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md plus resolved path/volume/ACL inventory, Git config and seed hash, remote absence, twelve denial results, second-run no-op, and rollback rehearsal.

## 15. Definition of done

The registry and both private roots exist at exact approved locations; the repository is clean, guarded, and has no remote; denials and rollback pass; and P07-S005 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S019/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation. Pause before root creation or after the complete seed commit and registry transaction; partial initialization must reconcile or roll back first.
