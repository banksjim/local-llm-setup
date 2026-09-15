# P10-S003: Finalize security and privacy controls

| Property | Value |
|---|---|
| Story ID | P10-S003 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 3 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P10-S002 |
| Unlocks | P10-S004 |
| Preferred route | Interface: Codex CLI in Windows and AI-Workbench through goagentic; Provider: high-reliability cloud provider; Model class: security implementation; Effort: high; Fallback: Anthropic architecture/security model with cross-provider review and identical activation packet. |
| Research freshness | P10-S001 unexpired; relevant Microsoft, Rancher, Ollama, Open WebUI, OWASP, and selected-component security guidance checked within 7 days. |

## 1. User story
As the owner, I want the accepted workstation security boundaries enforced and measured before it is tuned or declared operable.
## 2. Bounded objective
Implement `operations/windows/p10/P10-S003-security/` with `Get-SecurityBaseline.ps1`, `Set-SecurityBaseline.ps1`, `Test-SecurityBaseline.ps1`, and `Restore-SecurityBaseline.ps1`, plus `tests/p10/security/` fixtures.
## 3. Learning objective
Not applicable — P10-S002 covers the owner-facing concepts.
## 4. Current research requirements
Revalidate listener, firewall, WSL networking, Windows ACL, Rancher settings, credential-store, telemetry, repository-ignore, container secret, and agent-tool guidance for exact accepted versions.
## 5. Preconditions and unlock conditions
P10-S002 is Done. The controller derives Critical risk and presents the revision-bound P10 phase preview including before-state capture, exact mutations, isolated rehearsal, and rollback; owner authorization is recorded.
## 6. In scope
Listener inventory and allowlist; loopback/private-network enforcement; least-privilege ACLs; ignored secret files; redaction; container/user identity; WSL mount boundary; telemetry inventory; credential-location assertions; agent/RAG/memory deny-by-default checks; and Windows Defender Firewall rules owned by this project.
## 7. Out of scope and prohibited changes
No router changes, public ingress, disabling Windows security, exporting credentials, moving private data, unrelated firewall/ACL edits, security-product purchase, or unsupported hardening.
## 8. Privilege and human approval
Covered by the active P10 privileged-phase authorization. The owner handles elevation; scope drift requires a new preview and authorization.
## 9. Risk rationale
Critical: this crosses network, access-control, credential, and whole-workstation security boundaries. P10 phase authorization, synthetic/isolated rehearsal, cross-provider review, and P10-S011 final owner acceptance are mandatory.
## 10. Execution contract
Capture signed before-state; validate exact paths/rules/processes; rehearse with synthetic fixtures; apply one reversible control group at a time; verify from Windows, WSL, and container perspectives; redact before evidence emission; stop on unknown listener, inherited ACL ambiguity, or credential exposure.
## 11. Automated acceptance tests
Expected-listener count is nonzero and exact; all AI endpoints reject nonapproved interfaces; private container services are unreachable from host/LAN where prohibited; ACL and secret-negative fixtures pass; Git/private-content scans pass; telemetry is off or explicitly documented; agent capability negatives pass; no unrelated firewall/ACL entry changes; no-op second run and full rollback restore the captured fixture state.
## 12. Human validation
Owner reviews a plain-language exposure summary and confirms only expected local interfaces are available; no technical certification is requested.
## 13. Idempotency and rollback
Second apply makes no change. Rollback removes only story-owned rules/settings and restores captured prior values without weakening pre-existing controls or deleting data.
## 14. Required evidence
Commit operations/tests plus `evidence/P10-S003/activation.json`, `before-state.json`, `mutation-plan.json`, `listener-matrix.json`, `test-results.json`, `second-run.json`, `rollback.json`, `owner-summary.md`, `cross-provider-review.md`, and `checkpoint.json`.
## 15. Definition of done
Every expected boundary is enforced from all relevant perspectives, unexplained exposure is zero, failure/rollback/no-op tests pass, owner summary and independent cross-provider review are accepted, and P10-S004 unlocks.
## 16. Pause-safe boundaries
Pause before elevation and after each verified control group or completed rollback; never pause with a temporary broad rule or weakened ACL active.
