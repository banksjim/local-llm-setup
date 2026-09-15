# P10-S009: Run full automated end-to-end verification

| Property | Value |
|---|---|
| Story ID | P10-S009 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 13 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P10-S008 |
| Unlocks | P10-S010 |
| Preferred route | Interface: Codex CLI across Windows and AI-Workbench through goagentic; Provider: high-reliability cloud provider; Model class: systems verification; Effort: high; Fallback: Anthropic architecture/testing model with cross-provider result review and isolated destructive fixtures. |
| Research freshness | Fixed release-candidate sources and health interfaces rechecked within 7 days; no new product decision is allowed. |

## 1. User story
As the owner, I want one reproducible system test that proves the pieces work together under normal, restart, failure, and recovery conditions.
## 2. Bounded objective
Create `tests/p10/Invoke-EndToEndVerification.ps1`, `tests/p10/end-to-end-matrix.yaml`, and a sanitized release-candidate report covering every master acceptance criterion.
## 3. Learning objective
Not applicable — technical verification is independently reviewed and translated for P10-S011.
## 4. Current research requirements
Confirm exact health endpoints/commands for pinned versions and record deviations from P10-S001. Expired or changed behavior blocks rather than being guessed.
## 5. Preconditions and unlock conditions
P10-S008 is Done; P10 authorization remains valid; backup/restore and removal disposable targets are available; no private source content is required in public evidence; test matrix has nonzero expected cases and owner-approved downtime window.
## 6. In scope
Preflight/storage; installer dry-run/fixture apply/no-op; security/listeners; Rancher/container services; native Ollama and GPU placement; model roles/profiles; Open WebUI chat/vision/STT/web search; Docling; tool integrations; VS Code/WSL; agent/tool/MCP/human-interrupt; MLflow redaction; RAG citations/abstention; personal-agent boundaries; candidate/durable memory; restart/persistence; backup/isolated restore; update failure rollback; removal rehearsal; and zero-context controller resume.
## 7. Out of scope and prohibited changes
No production private-data deletion, public exposure, real crisis/medical/financial action, paid external call, unapproved update, fabricated human result, or repair inside the test runner.
## 8. Privilege and human approval
Covered by P10 authorization and owner-approved test window. Owner handles bounded elevation/UI/restart prompts. Scope or target drift stops the run.
## 9. Risk rationale
Critical: the test deliberately exercises the whole workstation, restarts, failure paths, and isolated destructive operations. P10 phase authorization, isolated/disposable rehearsal targets, cross-provider review, and P10-S011 final owner acceptance are mandatory.
## 10. Execution contract
Bind run to candidate hash and matrix; capture before-state; execute dependency-ordered groups; assign pass/fail/warning/justified-not-applicable to every expected case; never convert fail to warning; checkpoint/restart safely; automatically restore controlled settings; stop on exposure, data-integrity, unknown mutation, thermal, credential, or rollback failure.
## 11. Automated acceptance tests
Every matrix case has an executed result and evidence pointer; zero/omitted groups fail. All master criteria pass, no unexplained listener/secret/private-content leak occurs, normal profiles keep required headroom, citations and abstention meet accepted thresholds, durable memory respects owner-only promotion, two restart cycles preserve state, failed update restores, corrupt backup is rejected, isolated restore works, disposable uninstall preserves sentinels, installer and maintenance reruns no-op, and post-run state equals expected baseline.
## 12. Human validation
Owner performs only the named UI/voice/usability observations already required by owning stories; this runner links genuine records and cannot create them.
## 13. Idempotency and rollback
Rerunning the same candidate uses fresh run IDs but equivalent criteria. Fixture mutations are destroyed or restored; live bounded settings return to captured baseline; recovery failure blocks completion.
## 14. Required evidence
Commit runner/matrix plus `evidence/P10-S009/activation.json`, before/after state, case inventory, per-group results, sanitized logs, restart checkpoints, failure/restore results, privacy scan, final report, cross-provider review, and `checkpoint.json`.
## 15. Definition of done
Every applicable case passes without waiver, justified not-applicable cases are independently accepted, post-state is correct, cross-provider review is clean, and P10-S010 unlocks.
## 16. Pause-safe boundaries
Pause between test groups or after verified recovery. Never pause mid-migration/restore/removal or with stress load, broadened access, or services intentionally quiesced.
