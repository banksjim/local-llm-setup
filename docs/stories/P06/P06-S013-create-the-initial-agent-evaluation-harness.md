# P06-S013: Create the initial agent evaluation harness

| Property | Value |
|---|---|
| Story ID | P06-S013 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 13 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P06-S012 |
| Unlocks | P06-S014 |
| Preferred route | Interface: goagentic using Codex or Claude Code inside AI-Workbench; Provider: OpenAI or Anthropic for evaluation design with qualified Ollama candidates; Model class: strong evaluation/coding model; Effort: high; Fallback: current Sol- or Sonnet-class route with independent rubric review. |
| Research freshness | Current MLflow evaluation guidance checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to build deterministic and model-scored evaluations for task success, tool choice, groundedness, safety, cost, and latency, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Build deterministic and model-scored evaluations for task success, tool choice, groundedness, safety, cost, and latency.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P06-S011; this story introduces no separate learning objective.

## 4. Current research requirements

Current MLflow evaluation guidance checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S012. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create `tests/p06/agent-evaluation/` with versioned datasets for task success, tool selection/arguments, grounded fixture citation, authority denial, injection resistance, latency, and resource/cost proxy; deterministic scorers, separately labeled model-judge scorers, repetitions, confidence summaries, threshold manifest, and MLflow comparison operation.

## 7. Out of scope and prohibited changes

Do not build a coding harness/factory, use private conversations, tune on the acceptance set, silently change thresholds, let one model judge itself without disclosure, make safety depend on an LLM score, or trigger unbounded cloud cost.

## 8. Privilege and human approval

No new approval is required within the P06 evaluation budget and fixtures. A new paid provider, higher budget, private dataset, or changed safety threshold requires a revised preview.

## 9. Risk rationale

Evaluation can route cloud/local calls, consume quota, and falsely certify safety if datasets, thresholds, repetitions, or judges are biased or mutable.

## 10. Execution contract

Freeze datasets and thresholds before candidate runs; implement deterministic scorers first; add optional model judgment with recorded judge/prompt; estimate and cap calls; run deterministic fake, qualified local, and approved cloud comparisons with fixed repetitions; inject scorer/judge/timeout failures; store MLflow links and immutable result manifest; rerun and review.

## 11. Automated acceptance tests

Assert nonzero examples per metric and negative safety category. Verify dataset/threshold hashes precede runs, deterministic scorer unit tests, fixed repetitions, judge identity, confidence/variance, cost cap, and comparable model settings; reject self-modified thresholds, dataset leakage, missing failures, judge-only safety, partial-run pass, and zero fixtures.

## 12. Human validation

Not applicable — evaluation uses synthetic/versioned fixtures and independently reviewable scoring; no owner preference is accepted here.

## 13. Idempotency and rollback

Rerun creates a new immutable result keyed by dataset/config hashes and never overwrites thresholds. Rollback removes only tagged runs/results and restores harness files; prior traces and agents remain.

## 14. Required evidence

Commit harness/datasets/config plus `evidence/P06-S013/` activation, hashes, scorer tests, run matrix, model/judge identities, cost/latency/resource results, failure injection, MLflow links, rollback, checkpoint, and review.

## 15. Definition of done

Frozen evaluations reproducibly compare accepted local/cloud routes, deterministic safety thresholds pass independently of judges, costs are bounded, failures cannot produce a pass, review resolves, and P06-S014 unlocks.

## 16. Pause-safe boundaries

Pause before model calls, after each complete candidate/repetition set, or after result commit. Never pause with mutable thresholds; record hashes, spend, completed matrix cells, and next run in `evidence/P06-S013/checkpoint.json`.
