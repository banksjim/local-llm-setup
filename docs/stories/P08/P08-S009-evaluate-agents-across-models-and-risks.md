# P08-S009: Evaluate agents across models and risks

| Property | Value |
|---|---|
| Story ID | P08-S009 |
| Phase | P08 — Practical Personal Agents |
| Sequence | 11 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P08-S008 |
| Unlocks | P08-S010 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: different cloud provider from the predominant P08 implementer; Model class: high-reliability evaluator; Effort: high; Fallback: two independent fresh-session reviews and deterministic suite only until judge access returns. |
| Research freshness | Current MLflow evaluation/tracing APIs, model profiles, safety sources, and P08-S001 baseline checked within 7 days. |

## 1. User story

As the owner, I want repeatable independent evaluation so no agent is accepted because it merely sounded convincing in a few conversations.

## 2. Bounded objective

Build tests/p08/P08-S009-personal-agent-evaluation/ and an MLflow-backed, privacy-preserving evaluation report that compares accepted local model profiles across every agent and hard risk boundary.

## 3. Learning objective

Not applicable — P08-S010 explains owner-visible results and tradeoffs.

## 4. Current research requirements

Confirm current MLflow GenAI evaluation, trace, code-scorer, multi-turn, and regression-test interfaces. Record judge provider/model/version and limitations; never use an LLM judge as the only oracle for a hard rule.

## 5. Preconditions and unlock conditions

P08-S008 is Done. All agent prompt/config/tool/RAG/model versions are frozen; synthetic/adversarial data is versioned; hard thresholds, non-inferiority margin, latency/storage targets, and reviewer independence are fixed before execution.

## 6. In scope

Deterministic policy/schema/calculation/access/citation/redaction scorers; multi-turn task and safety fixtures; prompt/tool/RAG injection; overreliance; crisis/health/financial boundaries; privacy; model disclosure; abstention; usefulness; latency; token/call budgets; restart/replay; regression baselines; and result segmentation by agent/model/scenario.

## 7. Out of scope and prohibited changes

No real private conversation corpus, production trace mining, hidden threshold change, majority-vote override of a hard failure, sole LLM-judge acceptance, automatic model promotion, or technical review assigned to the owner.

## 8. Privilege and human approval

No new privilege. Cloud judge use, if authorized, receives only redacted synthetic fixtures; otherwise use the documented fallback. Any real-data evaluation requires separate preview and approval.

## 9. Risk rationale

High: an evaluation false negative can authorize harmful behavior, and careless traces can expose sensitive material.

## 10. Execution contract

Snapshot versions; run deterministic suites first; run multi-turn semantic evaluation with blinded labels; record every failure and uncertainty; verify trace redaction; compare primary/fast profiles without relaxing hard floors; run independent fresh-session and cross-provider review; fix and rerun the full affected matrix; publish a signed recommendation per agent/model.

## 11. Automated acceptance tests

Validate full matrix coverage, fixed thresholds, seed reproducibility, judge independence/version, golden arithmetic/access/policy outcomes, false-positive and false-negative safety cases, citation provenance, no raw private text, model non-inferiority, latency/call limits, repeated-run variance, regression output, and zero unresolved High/Critical finding. Intentionally corrupt one scorer, fixture, trace, and model route to prove the harness detects each.

## 12. Human validation

Not applicable — P08-S010 owns subjective usefulness. The owner is not asked to certify engineering or safety results.

## 13. Idempotency and rollback

Same frozen versions/seeds produce equivalent results within declared tolerance. Rollback removes evaluation-only data and judge credentials, restores agent versions, and retains signed reports and failure history.

## 14. Required evidence

evidence/P08-S009/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, evaluation-manifest.json, score-matrix.json, model-recommendations.json, redaction-audit.json, failure-injection.json, and regression-baseline.json.

## 15. Definition of done

Every agent/model combination has a defensible accept/reject result, all hard floors pass for enabled routes, privacy is verified, independent findings are resolved, and P08-S010 receives a plain-language acceptance packet.

## 16. Pause-safe boundaries

Update evidence/P08-S009/checkpoint.json after each deterministic, agent/model, privacy, failure-injection, and review partition. Preserve frozen versions and disable any route with a hard failure before pausing.
