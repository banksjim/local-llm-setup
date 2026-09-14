# P09-S006: Implement the reviewed inbox

| Property | Value |
|---|---|
| Story ID | P09-S006 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 7 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P09-S005 |
| Unlocks | P09-S007 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: controller-selected cloud provider; Model class: high-reliability full-stack; Effort: high; Fallback: authenticated local CLI/TUI with the identical decision API. |
| Research freshness | Selected framework and current local UI/auth/accessibility guidance checked within 7 days. |

## 1. User story
As the owner, I want one clear local inbox to inspect every proposed memory before it can become durable.
## 2. Bounded objective
Implement workloads/agents/memory/inbox/ and operations/windows/p09/P09-S006-memory-inbox/Open-MemoryInbox.ps1 as an authenticated loopback UI backed by a typed read/decision-preview API. `goagentic next` may direct the owner to this story operation; P09 does not invent an uncontracted controller subcommand.
## 3. Learning objective
Not applicable — inbox concepts were learned in P09-S003 and practiced in P09-S012.
## 4. Current research requirements
Confirm framework APIs, current secure-session/CSRF guidance, accessibility, and supported Open WebUI link/prompt integration without embedding secrets.
## 5. Preconditions and unlock conditions
P09-S005 is Done. Activation fixes loopback port, session authentication, fields/actions, sort/filter, accessibility criteria, TTL display, and decision-preview schema.
## 6. In scope
Pending/deferred queue; bounded source context; class/namespace/sensitivity/expiry; duplicate/conflict links; approve/edit/merge/reject/defer/restrict/purge previews; one-at-a-time decisions; keyboard access; disable/close; and no-content audit.
## 7. Out of scope and prohibited changes
No bulk approval, automatic action, chat-based approval, raw transcript, candidate recall, LAN/public bind, stored browser token, framework admin console exposure, or decision commit before P09-S007.
## 8. Privilege and human approval
Covered by P09 authorization. The UI previews but cannot yet commit durable promotion; no repeated phase approval is requested.
## 9. Risk rationale
High: the UI reveals bounded private candidate content and proposes consequential actions, though commit is not yet enabled.
## 10. Execution contract
Build authenticated loopback UI and typed API; enforce owner session, CSRF and anti-clickjacking; render every required field; make previews hash-bound; test accessibility, expiry/conflicts, session timeout, restart, no-op deploy, and cleanup; cross-provider review.
## 11. Automated acceptance tests
Prove anonymous/LAN/cross-user/CSRF/replay access fails; candidate values never enter URL/log/MLflow/Git; no bulk control exists; stale/expired/changed candidates cannot preview; all actions and keyboard paths render; service outage and restart fail safely.
## 12. Human validation
Deferred to P09-S012; automated accessibility checks and independent review cover implementation here.
## 13. Idempotency and rollback
Same configuration is a no-op. Rollback unregisters the launcher/UI and restores the API checkpoint without deleting candidates.
## 14. Required evidence
evidence/P09-S006/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, ui-contract.json, auth-security-results.json, accessibility-results.json, leak-scan.json, and launcher-results.json.
## 15. Definition of done
The owner-only inbox clearly previews all actions, leaks no candidate values, has no bulk/auto promotion, is accessible/recoverable, and cannot commit early.
## 16. Pause-safe boundaries
Update evidence/P09-S006/checkpoint.json after API, auth, UI, accessibility, restart, and review gates; disable the UI before pausing on any access or leak failure.
