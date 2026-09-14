# P09-S010: Evaluate memory quality and poisoning resistance

| Property | Value |
|---|---|
| Story ID | P09-S010 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 11 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P09-S009 |
| Unlocks | P09-S011 |
| Preferred route | Interface: WSL test runner through goagentic; Provider: different cloud provider from the pilot implementer; Model class: high-reliability evaluator; Effort: high; Fallback: deterministic suite plus two fresh-session reviews while model judging is unavailable. |
| Research freshness | Current memory benchmarks, OWASP memory poisoning, MLflow GenAI evaluation, and selected-framework docs checked within 7 days. |

## 1. User story
As the owner, I want rigorous measurement so convincing anecdotes cannot hide false, stale, leaked, or poisoned recall.
## 2. Bounded objective
Build tests/p09/P09-S010-memory-evaluation/ and a redacted MLflow evaluation comparing stateless versus memory-enabled life planning across fixed synthetic multi-session fixtures.
## 3. Learning objective
Not applicable — results are explained during P09-S012.
## 4. Current research requirements
Verify benchmark licenses/methods, current threat taxonomy, MLflow APIs, and evaluator limitations. External benchmarks supplement but never replace project-specific tests.
## 5. Preconditions and unlock conditions
P09-S009 is Done. Dataset, seeds, versions, hard thresholds, non-inferiority margin, evaluator identity/cost, and privacy rules are frozen before execution.
## 6. In scope
Capture precision/recall; durable recall precision/recall; false/stale/conflict recall; provenance; owner-decision fidelity; namespace/Restricted isolation; poisoning/prompt injection; correction/deletion; utility; latency/token/storage; outage; variance; and P08 regressions.
## 7. Out of scope and prohibited changes
No real private corpus, production conversation traces, vendor score substitution, threshold tuning after results, sole LLM-judge gate, automatic promotion, or enabled failed route.
## 8. Privilege and human approval
Covered by P09 authorization. Cloud judges, if authorized, receive only synthetic redacted cases; no real value leaves the machine.
## 9. Risk rationale
Critical: evaluation gates a privacy-sensitive feature where false negatives can expose or distort memory. Revision-bound authorization, isolated synthetic evaluation, cross-provider review, and P09-S012 owner acceptance are mandatory.
## 10. Execution contract
Snapshot versions; run deterministic gates first; execute blinded repeated multi-session trials; compare stateless baseline; segment failures; verify redaction; corrupt fixtures/scorers to prove detection; resolve findings and rerun full affected matrix; cross-provider review.
## 11. Automated acceptance tests
Require zero cross-boundary/candidate/secret/deleted recall; zero policy change from memory; exact owner-decision/correction/deletion behavior; fixed minimum recall/provenance and maximum false/stale rates; no P08 hard regression; bounded latency/storage; reproducible variance. An LLM judge cannot override a deterministic failure.
## 12. Human validation
Not applicable — subjective benefit and comfort are P09-S012; technical/safety evidence is independently reviewed.
## 13. Idempotency and rollback
Same frozen inputs yield results within declared tolerance. Rollback removes evaluation-only records/credentials and disables memory on hard failure while preserving signed reports.
## 14. Required evidence
evidence/P09-S010/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, evaluation-manifest.json, score-matrix.json, poisoning-results.json, redaction-audit.json, variance.json, and recommendation.json.
## 15. Definition of done
All hard floors pass, benefit exceeds the fixed non-inferiority rule, privacy is verified, no High/Critical finding remains, and a plain-language packet is ready.
## 16. Pause-safe boundaries
Update evidence/P09-S010/checkpoint.json after each deterministic/model/scenario/privacy/review partition; disable memory before pausing on any hard failure.
