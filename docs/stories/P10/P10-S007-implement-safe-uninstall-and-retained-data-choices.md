# P10-S007: Implement safe uninstall and retained-data choices

| Property | Value |
|---|---|
| Story ID | P10-S007 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 7 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P10-S006 |
| Unlocks | P10-S012 |
| Preferred route | Interface: Codex CLI on Windows through goagentic; Provider: high-reliability cloud provider; Model class: destructive-operation safety; Effort: high; Fallback: Anthropic security/recovery model with cross-provider review and disposable-target rehearsal. |
| Research freshness | Current official uninstall, factory-reset, data-location, WSL unregister, package-manager, and model-removal guidance checked within 7 days. |

## 1. User story
As the owner, I want removal to distinguish software from my irreplaceable data and show exactly what will happen before anything is deleted.
## 2. Bounded objective
Implement `operations/windows/p10/P10-S007-removal/Get-RemovalPlan.ps1`, `Uninstall-LocalAIComponent.ps1`, and `Test-RemovalState.ps1`, `config/removal/data-classes.yaml`, and `tests/p10/removal/`.
## 3. Learning objective
Not applicable — P10-S002 covers destructive stop boundaries; this story provides a plain-language choice sheet.
## 4. Current research requirements
Resolve actual uninstall effects and retained paths for every accepted component. Explicitly distinguish Rancher application uninstall, factory reset, snapshots/cache, and WSL distributions; distinguish Ollama application versus model/data removal.
## 5. Preconditions and unlock conditions
P10-S006 has a verified restorable generation. Activation resolves the exact component inventory, story-owned artifacts, discovered unknown files, retention choice, before-state, and disposable rehearsal roots.
## 6. In scope
Independent choices for application binaries, services, containers/images/volumes, models, WSL runtime, caches/logs, configuration, databases, agent state, memory, knowledge repositories, original documents, backups, and project-owned firewall/settings entries; default is retain all user/private data.
## 7. Out of scope and prohibited changes
No broad recursive delete, wildcard/computed target without canonical containment check, removing WSL/Rancher prerequisites installed separately unless explicitly selected, deleting backup/recovery keys with the live copy, unrelated package removal, or automatic treatment of unknown files.
## 8. Privilege and human approval
Covered by P10 authorization, but the owner must make the retention choices and confirm the exact final plan immediately before destructive apply. This is participation; any new target or broader scope invalidates the plan.
## 9. Risk rationale
Critical: a faulty target can destroy original documents, private repositories, memory, backups, WSL data, or unrelated host content. P10 phase authorization, disposable removal rehearsal, cross-provider review, and P10-S011 final owner acceptance are mandatory.
## 10. Execution contract
Inventory first; canonicalize and containment-check every literal target; classify known/unknown ownership; generate a counts/sizes/recoverability preview; require backup validity for selected private-data deletion; use product uninstall interfaces before file cleanup; stop services; delete only confirmed rows; verify retained/deleted sets; write sanitized tombstone evidence.
## 11. Automated acceptance tests
Dry-run never mutates; default retains every private/user data class; traversal, root, drive root, unresolved variable, symlink/junction escape, unknown file, active service, missing backup, stale plan, and mismatched hash are rejected. Disposable install removal deletes only selected owned artifacts, retains sentinels and prerequisites, supports partial interruption/resume, and a second run no-ops.
## 12. Human validation
Owner reviews a plain-language disposable plan, chooses retain/remove per data class, and verifies sentinel files remain after rehearsal. No live private data is removed for acceptance.
## 13. Idempotency and rollback
Plans bind to a before-state hash and expire on drift. Software removal rollback reinstalls the pinned version and configuration where supported; data deletion is not called reversible and requires a proven backup restore path before confirmation.
## 14. Required evidence
Commit operations/config/tests plus `evidence/P10-S007/activation.json`, sanitized inventory, choice record, exact plan, containment checks, dry-run, negative fixtures, disposable rehearsal, retained/deleted verification, second run, recovery result, human validation, cross-provider review, and `checkpoint.json`.
## 15. Definition of done
Every component/data class has an explicit default and effect, all destructive negative cases fail closed, disposable rehearsal preserves unknown/user data, recovery claims are honest, and P10-S012 unlocks.
## 16. Pause-safe boundaries
Pause before final confirmation and after each product-level removal plus verification. Finish or restore an atomic unit before pausing; never leave a broadened target cached for resume.
