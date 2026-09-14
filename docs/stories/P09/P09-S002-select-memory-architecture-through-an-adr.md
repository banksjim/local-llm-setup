# P09-S002: Select memory architecture through an ADR

| Property | Value |
|---|---|
| Story ID | P09-S002 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 2 |
| Status | Planned |
| Step | Review |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P09-S001 |
| Unlocks | P09-S003 |
| Preferred route | Interface: goagentic guided decision; Provider: different cloud provider from P09-S001 reviewer; Model class: high-reliability architecture; Effort: high; Fallback: select the framework-neutral LangGraph/PostgreSQL baseline if no candidate clears every gate. |
| Research freshness | P09-S001 sources and candidate releases rechecked within 24 hours. |

## 1. User story
As the owner, I want a clear recommendation and reversible architecture decision without being made responsible for technical correctness.
## 2. Bounded objective
Create docs/decisions/P09-S002-memory-architecture.md fixing the selected framework/components, canonical ledger, projection, encryption, resource allocation, migration seams, and rejected alternatives.
## 3. Learning objective
Not applicable — the selected architecture is taught in P09-S003.
## 4. Current research requirements
Revalidate the winning and fallback versions, licenses, breaking changes, local-model path, and every claimed self-hosted capability.
## 5. Preconditions and unlock conditions
P09-S001 is Done with no unresolved material contradiction. The decision packet translates engineering differences into privacy, cost, maintenance, and usability consequences.
## 6. In scope
Threat model; authoritative ledger versus derived projection; framework adapter; storage/encryption/key recovery; candidate retention; deletion/backup semantics; resource budget; observability; upgrade/migration; exit criteria; and pilot agent.
## 7. Out of scope and prohibited changes
No deployment, technical vote by the owner, cloud dependency, auto-promotion, opaque sole store, self-editing agent identity, or use of private data.
## 8. Privilege and human approval
No privileged mutation. The owner chooses only among explained privacy/cost/operator tradeoffs and confirms the proposed P09 scope; engineering validity requires cross-provider review.
## 9. Risk rationale
High: an incorrect architecture could expose or corrupt future sensitive memory across agents.
## 10. Execution contract
Apply gates before weighted scoring; recommend one design; map every SYS-MEM invariant; provide data-flow and trust-boundary diagrams; prove a migration/export seam with synthetic data; obtain cross-provider review; then record the owner's preference without attributing technical certification to them.
## 11. Automated acceptance tests
Validate ADR fields, source hashes, gate results, complete invariant mapping, resource arithmetic, migration fixture, threat mitigations, and rollback. Reject any design whose OSS path cannot run locally or whose durable data cannot be independently exported.
## 12. Human validation
The owner records understood privacy, cost, and operating tradeoffs and accepts, rejects, or requests clarification. The LLM cannot author that response.
## 13. Idempotency and rollback
Re-running without new evidence produces no change. Supersession requires a new ADR linked to this one; rollback restores no service because none is deployed.
## 14. Required evidence
evidence/P09-S002/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, invariant-map.json, threat-model.json, migration-fixture.json, and owner-decision.md.
## 15. Definition of done
One design clears all gates, maps every invariant, has an exit path, passes cross-provider review, and receives a genuine owner tradeoff decision.
## 16. Pause-safe boundaries
Update evidence/P09-S002/checkpoint.json after gates, draft ADR, reviews, and owner decision; pause before recording a final decision if any material issue is open.
