# P07-S015: Run synthetic ingestion acceptance suite

| Property | Value |
|---|---|
| Story ID | P07-S015 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 17 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P07-S014 |
| Unlocks | P07-S016 |
| Preferred route | Interface: WSL test runner through goagentic; Provider: controller-selected cloud provider; Model class: high-reliability test/review; Effort: high; Fallback: second provider diagnoses failures without weakening thresholds. |
| Research freshness | Current pinned stack health, security notices, and test-tool documentation checked within 7 days. |

## 1. User story

As the owner, I want a public-safe end-to-end acceptance suite so defects are found before any private 27-document test.

## 2. Bounded objective

Create and run tests/p07/P07-S015-synthetic-ingestion-acceptance for all nine categories, including mocked Google/authenticated sources, atomic publication, retrieval, citations, observability, restart, and rollback.

## 3. Learning objective

Not applicable — this is an engineering quality gate; the owner is not asked to interpret test output.

## 4. Current research requirements

Recheck security advisories and compatibility for every pinned runtime. Record deviations from P07-S001 and create a correction story for any material change.

## 5. Preconditions and unlock conditions

P07-S014 is Done. Activation inventories fixtures, expected hashes/counts, service versions, network boundaries, test database/KB IDs, thresholds, and cleanup targets. It must assert nine categories before running.

## 6. In scope

Positive pipeline tests, denial/failure matrix from P07-S004 through S014, clean-start run, restart/resume, repeated run, concurrency/lease behavior, private-data canaries, active-index preservation, Git integrity, resource/cost measurement, and rollback.

## 7. Out of scope and prohibited changes

No real private documents, live credentials, public endpoints, weakened assertions, zero-test success, production KB mutation, or acceptance based only on an LLM narrative.

## 8. Privilege and human approval

P07 authorization covers the isolated synthetic services. No owner participation is required; a qualified second-provider review examines the evidence.

## 9. Risk rationale

High: the suite exercises multiple services and destructive simulations, but only inside named disposable test roots and databases.

## 10. Execution contract

Verify isolation and fixture inventory, snapshot service state, run positive matrix, run every required denial/failure family, restart mid-job, rerun unchanged, inspect Git/database/manifests/traces, execute rollback, then rerun a smoke set. Any skipped required test blocks completion.

## 11. Automated acceptance tests

Assert exactly 27 positive inputs—three in each of nine category groups—with controlled local HTTP/OAuth mocks for remote categories. Aggregate all prior named negative tests; prove zero canary leaks, zero orphan active chunks, zero duplicate unchanged commits/vectors, valid citations, byte-stable derivatives, paired Git/index recovery on every publication fault, bounded resource use, and successful post-rollback smoke. Report test counts; zero is failure.

## 12. Human validation

Not applicable — the owner receives a plain-language summary only. A fresh qualified LLM and a second provider perform technical review.

## 13. Idempotency and rollback

Second full run over unchanged fixtures yields identical hashes/counts and no new accepted commit/index. Rollback removes only disposable test services, roots, DB objects, and profiles; fixtures and evidence remain.

## 14. Required evidence

The directory evidence/P07-S015/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Version inventory, isolation proof, expected/actual category matrix, total positive/negative/skipped counts, failure-injection results, canary scan, Git/DB integrity, hashes, restart/rerun/rollback outcomes, resource measurements, and two reviews at evidence/P07-S015/.

## 15. Definition of done

All required tests execute and pass with no skips; isolation and rollback are proven; both technical reviews have no unresolved material defect; and P07-S016 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S015/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause only between test groups after state/evidence flush. A destructive simulation must complete or compensate before pausing.
