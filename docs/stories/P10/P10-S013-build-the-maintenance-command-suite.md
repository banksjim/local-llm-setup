# P10-S013: Build the maintenance command suite

| Property | Value |
|---|---|
| Story ID | P10-S013 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 9 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P10-S012 |
| Unlocks | P10-S014 |
| Preferred route | Interface: Codex CLI on Windows through goagentic; Provider: controller-selected cloud provider; Model class: PowerShell integration; Effort: high; Fallback: Anthropic coding model with cross-provider review of destructive wrappers. |
| Research freshness | P10-S001 and accepted component health/lifecycle interfaces refreshed within 7 days. |

## 1. User story
As the owner, I want memorable maintenance scripts so routine operation and recovery do not require reconstructing internal commands.
## 2. Bounded objective
Create `scripts/windows/LocalAIWorkstation.psm1` and wrappers `Get-LocalAIStatus.ps1`, `Start-LocalAI.ps1`, `Stop-LocalAI.ps1`, `Get-LocalAILogs.ps1`, `Get-LocalAIUpdatePlan.ps1`, `Update-LocalAI.ps1`, `Backup-LocalAI.ps1`, `Restore-LocalAI.ps1`, `Undo-LocalAIChange.ps1`, and `Uninstall-LocalAI.ps1`.
## 3. Learning objective
Not applicable — P10-S002 teaches boundaries and P10-S014/S015 document use.
## 4. Current research requirements
Revalidate the exact health, lifecycle, log, backup, restore, rollback, and removal entry points for pinned components; changed interfaces return to owning operations.
## 5. Preconditions and unlock conditions
P10-S012 is Done; P10-S003 through S007 operations are accepted; each wrapper has exactly one authoritative delegate, risk class, approval behavior, expected output schema, and help example.
## 6. In scope
Discoverable help; safe defaults; status/start/stop; redacted log bundle; update preview/apply; backup/restore; rollback; removal preview/apply; shared configuration; structured output; exact target display; and controller evidence integration.
## 7. Out of scope and prohibited changes
No duplicated installer/component logic, hidden mutation, unattended scheduling, automatic update/restore/removal, GUI, new destination, raw logs/secrets, broad delete, or bypass of controller authorization.
## 8. Privilege and human approval
Read-only status/help/preview requires none. Mutating wrappers enforce the owning operation’s active authorization, `ShouldProcess`, exact plan binding, and human participation; `-Force` never bypasses controller authorization or data-class confirmation.
## 9. Risk rationale
High: wrappers expose multi-service update, restore, rollback, and removal; they must preserve Critical controls even though the wrapper code is small.
## 10. Execution contract
Parse/validate first; provide `-WhatIf`/preview where meaningful; show target and impact; delegate once; preserve exit/result schema; redact at source; stop on ambiguity; record planned versus actual result. Test external-process and cross-module preview explicitly.
## 11. Automated acceptance tests
All ten wrappers exist, parse/analyze, expose help/examples and expected parameters, use shared module, map one-to-one to accepted operations, reject bad targets/config/authorization, redact fixture secrets, preserve structured output/exit behavior, perform zero mutation in preview, handle mocked success/failure/interruption, no-op on repeat where applicable, and contain no duplicate core logic.
## 12. Human validation
From a fresh shell, owner runs help, status, redacted log preview, update preview, backup preview, and uninstall preview, then identifies which commands mutate and where they stop for confirmation.
## 13. Idempotency and rollback
Read-only/preview wrappers never mutate. Mutating wrappers inherit the accepted operation’s no-op, checkpoint, and rollback contract and add no independent state.
## 14. Required evidence
Commit module/wrappers/tests plus `evidence/P10-S013/activation.json`, command catalog, ownership map, help validation, static/negative/preview/failure/no-op results, redaction scan, owner validation, cross-provider review, and `checkpoint.json`.
## 15. Definition of done
Every accepted routine/recovery workflow has one understandable tested wrapper, safety is neither duplicated nor weakened, owner usability passes, and P10-S014 unlocks.
## 16. Pause-safe boundaries
Pause between wrapper implementations/tests and at delegated operation checkpoints; never pause inside atomic restore/migration/removal.
