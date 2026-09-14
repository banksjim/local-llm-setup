# P09-S007: Implement durable promotion and correction

| Property | Value |
|---|---|
| Story ID | P09-S007 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 8 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P09-S006 |
| Unlocks | P09-S008 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: controller-selected cloud provider; Model class: high-reliability security/data; Effort: high; Fallback: leave all candidates quarantined and durable writes disabled. |
| Research freshness | Current transaction, authentication, anti-replay, selected-framework, and deletion docs checked within 7 days. |

## 1. User story
As the owner, I want only my fresh, explicit inbox decision to create or change durable memory.
## 2. Bounded objective
Implement workloads/agents/memory/decisions/ and operations/ubuntu/p09/P09-S007-memory-decisions/ for hash-bound approve/edit/merge/restrict/reject/defer/correct/delete transactions.
## 3. Learning objective
Not applicable — P09-S003 covers decisions and history.
## 4. Current research requirements
Verify cryptographic token, transaction isolation, CSRF/session, framework write, and purge semantics against selected versions.
## 5. Preconditions and unlock conditions
P09-S006 is Done. Activation fixes token lifetime/signing key reference, state machine, dual confirmation for Restricted/delete, ledger/outbox transaction, retry, and audit schema.
## 6. In scope
Owner authentication; decision token bound to candidate hash/action/target/policy/expiry; one-time use; immutable versions; owner edits/merges; correction/supersession; reject/defer/purge; outbox; and non-content audit.
## 7. Out of scope and prohibited changes
No agent/deterministic/bulk promotion, chat phrase as approval, stale decision, silent conflict resolution, destructive history rewrite, candidate recall, or secret/restricted value in audit/trace.
## 8. Privilege and human approval
Covered by revision-bound P09 authorization. Each durable decision is owner participation through the authenticated inbox, not a new phase approval.
## 9. Risk rationale
Critical: this is the sole write authority for durable private memory. Revision-bound authorization, isolated rehearsal, cross-provider review, and P09-S012 owner acceptance are mandatory.
## 10. Execution contract
Rehearse every transition in isolation; issue fresh preview tokens; re-read/hash candidate at commit; transact ledger/outbox/state/audit; consume token; reconcile interruptions; verify correction/delete; run concurrency/replay/failure tests; and cross-provider review.
## 11. Automated acceptance tests
Reject forged/expired/replayed/wrong-action/wrong-target/wrong-policy tokens, changed/expired candidate, agent request, bulk request, duplicate click, concurrent conflict, partial transaction, secret, and unauthorized Restricted/delete. Prove exactly-once commit, immutable history, purge tombstone, recovery, rollback, and zero candidate recall.
## 12. Human validation
Deferred to P09-S012; automated fixtures cannot fabricate owner acceptance.
## 13. Idempotency and rollback
Decision token is exactly once; retry returns the recorded result. Failed commits change nothing. Rollback disables decision writes and reconciles outbox without deleting accepted ledger versions.
## 14. Required evidence
evidence/P09-S007/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, transition-matrix.json, anti-replay-results.json, concurrency-results.json, reconciliation.json, and purge-results.json.
## 15. Definition of done
Only a current authenticated owner decision changes durable state; all transitions are exactly once, versioned, recoverable, and independently reviewed.
## 16. Pause-safe boundaries
Update evidence/P09-S007/checkpoint.json after each transition/failure/reconciliation gate; never pause with an unclassified ledger/outbox transaction or decision writes enabled after a hard failure.
