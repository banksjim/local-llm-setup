# P10-S015: Write the operations, recovery, and troubleshooting guides

| Property | Value |
|---|---|
| Story ID | P10-S015 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 11 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P10-S014 |
| Unlocks | P10-S008 |
| Preferred route | Interface: coding agent through goagentic; Provider: high-reliability cloud provider; Model class: operations/recovery documentation; Effort: high; Fallback: different cloud provider reviews every destructive/recovery instruction against test evidence. |
| Research freshness | Accepted local results and pinned-component operational documentation checked within 7 days. |

## 1. User story
As the owner, I want tested runbooks with clear stop conditions so I can recover safely when normal operation fails.
## 2. Bounded objective
Create `docs/guides/windows/OPERATIONS.md`, `PERFORMANCE-TUNING.md`, `SECURITY-AND-PRIVACY.md`, `TROUBLESHOOTING.md`, `UPDATE-AND-ROLLBACK.md`, `BACKUP-AND-RESTORE.md`, `UNINSTALL.md`, and `INCIDENTS.md`, mapped only to accepted commands and evidence.
## 3. Learning objective
Not applicable — these are references for previously taught workflows; owner validates findability, not memorization.
## 4. Current research requirements
Refresh official operational guidance for pinned versions and use accepted P10 measurements for workstation-specific claims. Record version/date and distinguish documented, measured, inferred, and unsupported behavior.
## 5. Preconditions and unlock conditions
P10-S014 and operational producer stories are Done; exact commands, symptoms, failure/restore evidence, privilege boundaries, and known limitations are stable.
## 6. In scope
Daily start/stop/status/logs; profile selection and safe thermal/VRAM interpretation; exposure/credential/privacy checks; symptom-to-diagnosis decision trees; Windows/WSL/Rancher/Ollama/Open WebUI/service failures; update/migration and rollback; backup/restore; uninstall/retention; disk pressure; model OOM/queue/CPU spill; RAG/agent/memory faults; emergency stop; and escalation/evidence collection.
## 7. Out of scope and prohibited changes
No untested repair, destructive shortcut, generic scraped advice, secret/raw private logs, disabling safeguards, unsupported hardware tuning, unattended mutation, live workstation change during authoring, or promise that backup/rollback can do what tests did not prove.
## 8. Privilege and human approval
Documentation edits need no approval. Every documented privileged, restore, update, removal, access-control, or publication action visibly retains its owning authorization/confirmation requirement.
## 9. Risk rationale
High: these instructions will be used under stress and can invoke Critical recovery/destructive operations.
## 10. Execution contract
For every procedure state symptom/goal, context, prerequisites, data/privilege impact, least-invasive diagnosis, exact wrapper, expected result, abort criteria, recovery, evidence, and escalation. Never conflate diagnosis with repair; link rather than copy implementation; put irreversible boundaries before commands.
## 11. Automated acceptance tests
All eight guides exist; every accepted maintenance wrapper appears in exactly one authoritative procedure and all cross-links resolve; activation symptom matrix has no uncovered row; commands match help/operation map; each mutating procedure has privilege/data warning, preview, expected result, abort/rollback/escalation; dangerous-command and broad-path scans pass; local claims link test evidence; sources are fresh; no secret/private content appears.
## 12. Human validation
Using only these guides, owner completes one benign diagnosis and correctly locates safe update, restore, uninstall-retention, exposure, and emergency-stop paths, identifying where each asks for confirmation.
## 13. Idempotency and rollback
Unchanged evidence yields no semantic rewrite. Git reversion restores documents; command examples inherit the underlying operation’s no-op/rollback rules.
## 14. Required evidence
Commit eight guides plus `evidence/P10-S015/activation.json`, runbook/symptom/command/evidence maps, link/command/warning/freshness/privacy scans, changed-file list, owner usability result, cross-provider review, and `checkpoint.json`.
## 15. Definition of done
Every supported routine, symptom, failure, and recovery path has a tested discoverable procedure with explicit safety boundaries; owner findability passes; P10-S008 unlocks.
## 16. Pause-safe boundaries
Pause after a complete runbook plus validation; never leave a renamed command/guide or a destructive procedure without its warning and stop path.
