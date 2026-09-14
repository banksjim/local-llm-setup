# P09-S009: Integrate memory with the life-planning agent

| Property | Value |
|---|---|
| Story ID | P09-S009 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 10 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P09-S008 |
| Unlocks | P09-S010 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: controller-selected cloud provider; Model class: high-reliability agent integration; Effort: high; Fallback: restore the accepted stateless P08 life planner and disable capture/recall. |
| Research freshness | Current LangGraph Store/selected adapter, P08 runtime/Open WebUI, local model, and MLflow docs checked within 7 days. |

## 1. User story
As the owner, I want approved memory piloted in the life-planning agent without weakening its existing safety or privacy.
## 2. Bounded objective
Implement workloads/agents/personal/life_planner/memory/ and operations/windows/p09/P09-S009-life-planner-memory/ for optional candidate capture and purpose-bound approved recall.
## 3. Learning objective
Not applicable — operation is practiced in P09-S012.
## 4. Current research requirements
Verify exact adapter, Open WebUI disclosure/preset, LangGraph context, model, trace-redaction, and outage behavior against installed versions.
## 5. Preconditions and unlock conditions
P09-S008 and P08-S010 life-planner acceptance are Done. Activation fixes eligible memory types, namespaces, recall intents, limits, capture default off, disclosure, evaluation baseline, and rollback hash.
## 6. In scope
Explicit per-chat capture toggle; owner identity from trusted session; candidate API; read-only recall before planning; provenance/correction/conflict display; no-result/outage disclosure; private preset update; MLflow decision-only traces; and instant disable.
## 7. Out of scope and prohibited changes
No other agent, candidate recall, automatic promotion, memory-derived authority, hidden personalization, raw trace, autonomous action, P08 boundary change, or memory required for safe use.
## 8. Privilege and human approval
Covered by P09 authorization. Capture stays off until P09-S012 owner acceptance; promotion remains an inbox action.
## 9. Risk rationale
Critical: private cross-session context enters an owner-facing agent. Revision-bound authorization, isolated rehearsal, cross-provider review, and P09-S012 owner acceptance are mandatory.
## 10. Execution contract
Rehearse with synthetic owner/agent; add trusted identity/context; retrieve only explicit purposes; frame memory as untrusted; cite provenance/status; capture to quarantine; expose disclosure/disable; inject outage/poisoning; compare stateless baseline; restart/rollback/no-op; and cross-provider review.
## 11. Automated acceptance tests
Test capture off/on/do-not-learn, candidate invisibility, approved/corrected/conflicting/expired/deleted/Restricted memory, cross-agent/owner denial, injection in memory, false recall, empty result, outage/timeout, stale policy, trace leak, model route, restart, instant disable, rollback, and unchanged P08 hard tests.
## 12. Human validation
Deferred to P09-S012; no LLM may fabricate the owner's usefulness/privacy judgment.
## 13. Idempotency and rollback
Same preset/graph version is no-op. Rollback atomically restores P08 stateless graph/preset, disables capture/recall, and preserves ledger for administration.
## 14. Required evidence
evidence/P09-S009/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, integration-manifest.json, disclosure-results.json, outage-results.json, baseline-comparison.json, and p08-regression.json.
## 15. Definition of done
The pilot uses only approved scoped memory, candidates remain quarantined, failures degrade visibly/statelessly, P08 protections regress zero, and review resolves.
## 16. Pause-safe boundaries
Update evidence/P09-S009/checkpoint.json after synthetic, recall, capture, outage, regression, preset, and review gates; restore stateless mode before pausing on a hard failure.
