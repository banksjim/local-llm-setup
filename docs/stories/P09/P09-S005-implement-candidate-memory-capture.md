# P09-S005: Implement candidate-memory capture

| Property | Value |
|---|---|
| Story ID | P09-S005 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 6 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P09-S004 |
| Unlocks | P09-S006 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: controller-selected cloud provider; Model class: high-reliability agent implementation; Effort: high; Fallback: deterministic explicit-owner candidate form with model extraction disabled. |
| Research freshness | Selected extraction/local-model, structured-output, PII/secret, and framework docs checked within 7 days. |

## 1. User story
As the owner, I want agents to propose bounded candidate memories without allowing those proposals to affect future answers.
## 2. Bounded objective
Implement workloads/agents/memory/capture/ and operations/ubuntu/p09/P09-S005-candidate-capture/ with per-agent/conversation controls, structured extraction, quarantine, dedup/conflict hints, TTL, and `do not learn` enforcement.
## 3. Learning objective
Not applicable — P09-S003 covers capture and quarantine.
## 4. Current research requirements
Verify local extraction model reliability, structured-output APIs, framework auto-retain disablement, and current secret/PII detection limitations.
## 5. Preconditions and unlock conditions
P09-S004 is Done. Activation fixes eligible assertion types, minimal turn window, local model, thresholds, denylist, TTL, rate/budget limits, and capture default off.
## 6. In scope
Explicit capture toggle; `do not learn`; minimum context; typed candidate; source hash/excerpt; secret/PII/sensitivity checks; duplicate/conflict hints; quarantine; TTL; limits; and sanitized events.
## 7. Out of scope and prohibited changes
No durable promotion, candidate recall, full transcript storage, hidden capture, health/financial details without Restricted warning, cloud model, tool/RAG content capture, or self-editing prompt/identity.
## 8. Privilege and human approval
Covered by P09 authorization. Capture remains off until P09-S012 acceptance and is always owner-disableable.
## 9. Risk rationale
High: private conversation fragments may enter temporary quarantine, but they cannot influence agents or become durable without review.
## 10. Execution contract
Implement deterministic pre/post filters around structured local extraction; quarantine only valid candidates; deduplicate by content/provenance; flag conflicts without resolving; enforce TTL and limits; verify candidate invisibility to recall; and cross-provider review.
## 11. Automated acceptance tests
Test stable preference, transient chatter, negation, sarcasm, ambiguity, correction, duplicate, contradiction, prompt/tool/RAG injection, passwords/tokens/account numbers, health/financial sensitivity, capture-off, `do not learn`, expiry, model failure, oversize, rate limit, redaction, and zero recall of candidates.
## 12. Human validation
Not applicable — the owner reviews real behavior only in P09-S012.
## 13. Idempotency and rollback
Same source hash/config does not duplicate a candidate. Rollback disables capture and purges story-tagged synthetic candidates while leaving the ledger intact.
## 14. Required evidence
evidence/P09-S005/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, extraction-matrix.json, secret-pii-results.json, dedup-conflict-results.json, expiry-results.json, and invisibility-results.json.
## 15. Definition of done
Only eligible bounded candidates enter quarantine, secrets are rejected, controls/TTL work, candidates cannot be recalled, and review resolves.
## 16. Pause-safe boundaries
Update evidence/P09-S005/checkpoint.json after filter, model, quarantine, expiry, and review gates; disable capture before pausing on any privacy or invisibility failure.
