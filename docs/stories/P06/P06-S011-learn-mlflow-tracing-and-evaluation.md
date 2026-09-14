# P06-S011: Learn MLflow tracing and evaluation

| Property | Value |
|---|---|
| Story ID | P06-S011 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 11 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P06-S010 |
| Unlocks | P06-S012 |
| Preferred route | Interface: goagentic lesson using the localhost MLflow UI and P06 workspace; Provider: OpenAI or Anthropic with qualified Ollama exercises; Model class: economical observability tutor; Effort: medium; Fallback: current Sol- or Sonnet-class tutor. |
| Research freshness | Current official MLflow GenAI resources selected at activation. |

## 1. User story

As the workstation owner, I want this story to teach traces, spans, inputs, outputs, decisions, redaction, datasets, and evaluations needed here, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Teach traces, spans, inputs, outputs, decisions, redaction, datasets, and evaluations needed here.

## 3. Learning objective

Complete the targeted concepts and demonstrate them through the acceptance exercise.

## 4. Current research requirements

Current official MLflow GenAI resources selected at activation. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S010. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create `docs/learning/p06/P06-S011-mlflow-tracing-evaluation.md`, a sanitized fixture trace, span/trace/run glossary, decision and failure hunt, redaction exercise, deterministic-versus-model scorer exercise, cost caveat, and blank owner rubric.

## 7. Out of scope and prohibited changes

Do not enable LangSmith/cloud MLflow, ingest private prompts, teach general MLOps, create production monitoring, use a model judge as safety authority, or expose MLflow beyond loopback.

## 8. Privilege and human approval

No new authorization is required. The owner navigates the local UI and records findings personally; the LLM cannot fabricate clicks, observations, or answers.

## 9. Risk rationale

Only synthetic traces are used, but misunderstanding redaction or evaluator limits could expose private agent data or create false quality confidence.

## 10. Execution contract

Generate a sanitized trace from accepted current MLflow APIs; teach traces/spans versus experiment runs, metadata, decisions, failures, redaction, datasets, deterministic/custom/model scorers, repetitions, and cost; guide a UI hunt and scorer comparison; collect owner explain-back.

## 11. Automated acceptance tests

Assert the fixture trace, expected spans, redaction cases, scorer examples, and blank rubric. Verify the owner task references visible IDs and exact expected locations. Fail on private input, cloud endpoint, missing failure span, unlabeled model judgment, prefilled answers, or zero exercises.

## 12. Human validation

The owner locates the model and tool spans, explains one decision and failure, distinguishes trace from run, identifies a redacted field, compares deterministic and model scoring, and writes `evidence/P06-S011/human-validation.md`. The LLM cannot author it.

## 13. Idempotency and rollback

Repeat uses a new synthetic trace tagged to the attempt and leaves prior owner evidence intact. Rollback deletes only unaccepted fixture traces and lesson files.

## 14. Required evidence

Commit lesson/fixtures plus `evidence/P06-S011/` activation, source/version record, trace IDs, redaction and scorer results, blank rubric, genuine human evidence, cleanup, checkpoint, and review.

## 15. Definition of done

The owner meets every targeted observability rubric item, the fixture contains required spans without sensitive content, evidence resolves, and P06-S012 unlocks.

## 16. Pause-safe boundaries

Pause between modules, after fixture emission/cleanup, or before owner handoff; record trace IDs and next UI task in `evidence/P06-S011/checkpoint.json`.
