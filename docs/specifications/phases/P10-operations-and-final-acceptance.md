# P10: Operations and Final Acceptance

**Depends on:** P09

**Required outcome:** A secure, measured, recoverable, documented Windows release that a nonexpert owner can operate and restore without chat history.

**Status:** Planned

## Gate and authorization

P09-S012 must be Done. Research and the targeted lesson may run before privileged authorization. Before P10-S003, the controller must compile one revision-bound P10 activation packet covering every proposed host/service mutation in P10-S003 through P10-S007, P10-S012, P10-S013, and P10-S009; exact targets; versions/digests; ports; data classes; backup destination and encryption; deletion choices; test fixtures; checkpoints; and rollback. The owner gives one bounded privileged-phase authorization. Elevation prompts, backup-destination selection, destructive-choice confirmation, lessons, and acceptance remain genuine owner participation—not repeated approval of unchanged scope. Any material scope, target, risk, or operation change invalidates the authorization.

## Fixed operating architecture

- Compose only the reusable operations accepted in P02–P09; the installer and maintenance commands may orchestrate them but may not reimplement them.
- Treat `H:\ai` as the declared Windows data root and the dedicated `AI-Workbench` Ubuntu distribution as the agent runtime. Never broaden a recursive operation beyond activation-resolved child paths.
- Keep every network listener loopback-only or on the accepted private container network. A release fails if an unexplained listener, route, credential location, or telemetry path exists.
- Pin component versions and container image digests in a machine-readable release manifest. Updates are previewed, backed up, migrated, verified, and independently reversible; a container rollback never pretends to reverse a database migration.
- Maintain a component/data/backup matrix. Configuration, databases, agent state, approved memory, source originals, knowledge repositories, and WSL state each have an explicit backup and restore method. Re-downloadable model blobs may be excluded only when immutable identity and retrieval are proven.
- Use an owner-selected local, OneDrive, NAS, or combined backup destination. The destination must be encrypted where appropriate, separated from the live tree, integrity-checked, and proven through an isolated restore. A continuously attached or synced copy alone is not sufficient recovery evidence.
- Performance profiles are measurements, not guesses: `fast`, `balanced`, `quality`, and `constrained` record model, context, concurrency, keep-alive, GPU/CPU allocation, service budget, latency, throughput, temperature, power, and desktop-headroom results. Normal profiles retain at least 3 GB VRAM headroom and do not silently spill the default model to CPU.
- Every mutating PowerShell command supports preview and exact-target validation; functions use `SupportsShouldProcess` where applicable, but cross-module and external-process behavior is explicitly tested rather than assumed.
- Evidence is sanitized and versioned. No secret, private document content, raw durable memory, recovery key, or backup credential enters this public repository.

## Required release artifacts

| Area | Required artifact family |
|---|---|
| Research and learning | `docs/research/P10/`, `docs/learning/P10/` |
| Operations | `operations/windows/p10/` with preview/apply/verify/rollback boundaries |
| Installer | `installer/windows/Install-LocalAIWorkstation.ps1` and composed modules/configuration |
| Maintenance | Discoverable wrappers under `scripts/windows/` backed by the accepted operations |
| Tests | `tests/p10/` catalog, security, performance, failure, restore, removal, and end-to-end suites |
| Guides | Core Windows guides, operational runbooks, Mermaid diagrams, and `prompts/` |
| Release | Machine-readable manifest, accepted evidence index, residual-risk record, and immutable Git tag |

## Current source baseline

Refresh at activation; direct sources take precedence over this planning snapshot.

- [Microsoft WSL commands and export/import](https://learn.microsoft.com/windows/wsl/basic-commands)
- [Microsoft WSL FAQ](https://learn.microsoft.com/windows/wsl/faq)
- [PowerShell confirmation and ShouldProcess](https://learn.microsoft.com/powershell/scripting/developer/cmdlet/requesting-confirmation-from-cmdlets)
- [PSScriptAnalyzer usage](https://learn.microsoft.com/powershell/utility-modules/psscriptanalyzer/using-scriptanalyzer)
- [Rancher Desktop installation and removal](https://docs.rancherdesktop.io/getting-started/installation/)
- [Rancher Desktop rdctl reference](https://docs.rancherdesktop.io/references/rdctl-command-reference/)
- [Open WebUI update and migration warning](https://docs.openwebui.com/getting-started/updating/)
- [Ollama context-length guidance](https://docs.ollama.com/context-length)
- [Ollama concurrency and keep-alive guidance](https://docs.ollama.com/faq)
- [NVIDIA System Management Interface](https://docs.nvidia.com/deploy/nvidia-smi/)
- [CISA ransomware backup and recovery guidance](https://www.cisa.gov/stopransomware/ransomware-guide)

## Story sequence

| Seq. | Story | Step | Risk |
|---:|---|---|---|
| 1 | [P10-S001: Refresh operational and security guidance](../../stories/P10/P10-S001-refresh-operational-and-security-guidance.md) | Research | Low |
| 2 | [P10-S002: Learn routine operation and incident boundaries](../../stories/P10/P10-S002-learn-routine-operation-and-incident-boundaries.md) | Learning | Low |
| 3 | [P10-S003: Finalize security and privacy controls](../../stories/P10/P10-S003-finalize-security-and-privacy-controls.md) | Implementation | Critical |
| 4 | [P10-S004: Tune RTX 4090 and workstation performance](../../stories/P10/P10-S004-tune-rtx-4090-and-workstation-performance.md) | Testing | High |
| 5 | [P10-S005: Implement update, rollback, and migration workflow](../../stories/P10/P10-S005-implement-update-rollback-and-migration-workflow.md) | Implementation | Critical |
| 6 | [P10-S006: Implement comprehensive backup and restore](../../stories/P10/P10-S006-implement-comprehensive-backup-and-restore.md) | Implementation | Critical |
| 7 | [P10-S007: Implement safe uninstall and retained-data choices](../../stories/P10/P10-S007-implement-safe-uninstall-and-retained-data-choices.md) | Implementation | Critical |
| 8 | [P10-S012: Assemble the idempotent PowerShell installer](../../stories/P10/P10-S012-assemble-the-idempotent-powershell-installer.md) | Implementation | Critical |
| 9 | [P10-S013: Build the maintenance command suite](../../stories/P10/P10-S013-build-the-maintenance-command-suite.md) | Implementation | High |
| 10 | [P10-S014: Write the core operator and usage guides](../../stories/P10/P10-S014-write-the-core-operator-and-usage-guides.md) | Implementation | Medium |
| 11 | [P10-S015: Write the operations, recovery, and troubleshooting guides](../../stories/P10/P10-S015-write-the-operations-recovery-and-troubleshooting-guides.md) | Implementation | High |
| 12 | [P10-S008: Validate the complete deliverable catalog](../../stories/P10/P10-S008-validate-the-complete-deliverable-catalog.md) | Testing | High |
| 13 | [P10-S009: Run full automated end-to-end verification](../../stories/P10/P10-S009-run-full-automated-end-to-end-verification.md) | Testing | Critical |
| 14 | [P10-S010: Perform independent final architecture review](../../stories/P10/P10-S010-perform-independent-final-architecture-review.md) | Review | Critical |
| 15 | [P10-S011: Complete final owner acceptance and baseline](../../stories/P10/P10-S011-complete-final-owner-acceptance-and-baseline.md) | Human Validation | Critical |

Story IDs are stable; Sequence controls execution.

## Completion

All 15 non-superseded stories are Done; every required artifact is present; tests account for all expected cases without silent skips; an isolated restore and removal rehearsal pass; author and final reviewer differ; the owner completes the guided acceptance without technical certification; residual risks are explicit; and the accepted release is tagged. No workstation implementation begins merely because this specification exists.
