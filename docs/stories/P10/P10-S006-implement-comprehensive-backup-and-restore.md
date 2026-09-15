# P10-S006: Implement comprehensive backup and restore

| Property | Value |
|---|---|
| Story ID | P10-S006 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 6 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P10-S005 |
| Unlocks | P10-S007 |
| Preferred route | Interface: Codex CLI plus owner-selected backup destination through goagentic; Provider: high-reliability cloud provider; Model class: data recovery implementation; Effort: high; Fallback: Anthropic recovery-capable model with cross-provider review and isolated restore rehearsal. |
| Research freshness | Current source-component consistency, WSL export/import, encryption, and owner-selected local/OneDrive/NAS backup documentation checked within 7 days. |

## 1. User story
As the owner, I want a tested, private backup set that can rebuild the useful system rather than merely copy files.
## 2. Bounded objective
Implement `operations/windows/p10/P10-S006-backup/Backup-LocalAI.ps1`, `Restore-LocalAI.ps1`, and `Test-LocalAIBackup.ps1`; `config/backup/windows-backup-policy.yaml`; and `tests/p10/backup/`.
## 3. Learning objective
Not applicable — P10-S002 covers backup versus proven restore; the owner receives destination-specific instructions during participation.
## 4. Current research requirements
Verify application-consistent export/stop requirements, WSL VHD/tar export semantics, Rancher snapshot limits, database dump/restore, encryption/key recovery, OneDrive or NAS atomicity/versioning, path-length/filesystem behavior, and integrity tooling.
## 5. Preconditions and unlock conditions
P10-S005 is Done. Owner selects an available destination and retention class from explained privacy/cost/recovery tradeoffs. Activation resolves capacity, encryption, key-recovery location, RPO/RTO targets, included/excluded data, and isolated restore root beneath `H:\ai\tmp\restore-tests`.
## 6. In scope
Controller state/evidence; configuration and version manifests; databases; Open WebUI data; agent workspace/state; approved durable memory ledger; knowledge-base Git repositories and non-Git original source tree; extraction records; WSL `AI-Workbench`; selected Rancher state; logs needed for recovery; and cryptographic manifests. Re-downloadable model blobs may be excluded only with immutable retrieval records.
## 7. Out of scope and prohibited changes
No public storage, secret in repository/evidence, assumed sync-as-backup, restore over live data during proof, destructive retention before verified generations, backing up temporary caches by default, or claiming an untested destination is supported.
## 8. Privilege and human approval
Covered by P10 authorization. Owner supplies/unlocks the destination and recovery-key mechanism and confirms any UI prompt; credentials are never requested in chat or evidence. Live replacement restore requires separate action confirmation within the approved workflow.
## 9. Risk rationale
Critical: original documents, private knowledge, memory, databases, and an entire WSL runtime could be lost or exposed. P10 phase authorization, isolated restore rehearsal, cross-provider review, and P10-S011 final owner acceptance are mandatory.
## 10. Execution contract
Quiesce or consistently export each source; stage locally; hash before transfer; encrypt where policy requires; copy to an exact destination; verify manifest after transfer; apply retention only after a valid new generation; disconnect/offline the removable path when applicable; restore into isolation; prove services and data; sanitize evidence.
## 11. Automated acceptance tests
The matrix has a nonzero row for every P10 data class; changed-file and consistent-database backups work; interrupted copy leaves no valid marker; corruption, wrong key, insufficient space, unavailable destination, unsafe live target, traversal, symlink escape, and stale generation are rejected. Isolated restore matches hashes and passes controller, WSL, database, agent, RAG, memory, and UI smoke probes; a second backup is incremental/no-op as designed.
## 12. Human validation
Owner locates the encrypted backup generation and separate recovery instructions, confirms destination access, and opens the isolated restored Open WebUI/knowledge-base sample. The owner judges usability, not architecture.
## 13. Idempotency and rollback
Incomplete generations never become current. Repeated backup reuses unchanged content safely. Restore never overwrites live state without exact target plus confirmation; rollback removes only the isolated restore or restores the captured live pre-restore point.
## 14. Required evidence
Commit operations/config/tests plus `evidence/P10-S006/activation.json`, sanitized data matrix, capacity plan, backup manifest without private filenames/content where sensitive, integrity results, failure fixtures, isolated restore results, RPO/RTO result, retention result, human validation, cross-provider review, and `checkpoint.json`.
## 15. Definition of done
Every required data class is protected or explicitly reproducible, encryption/recovery is proven, failure cases fail closed, an isolated full restore passes functional checks, owner validation is genuine, and P10-S007 unlocks.
## 16. Pause-safe boundaries
Pause after a consistent source export, completed invalid staging cleanup, verified generation, or isolated restore checkpoint; never pause while live services are quiesced without recording restart state.
