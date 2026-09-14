# P01-S002: Learn the goagentic operating model

| Property | Value |
|---|---|
| Story ID | P01-S002 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 3 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P01-S001 |
| Unlocks | P01-S003 |
| Preferred route | Interface: interactive Codex or Claude Code session; Provider: OpenAI or Anthropic; Model class: general-purpose guide; Effort: low; Fallback: switch provider if the primary interface is unavailable; no model may substitute for human evidence. |
| Research freshness | Current project specifications; external sources are not required. |

## 1. User story

As the workstation owner, I want this story to teach the owner the state, step, hold, lease, evidence, pause, resume, review, and authorization concepts needed for controller acceptance, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Teach the owner the state, step, hold, lease, evidence, pause, resume, review, and authorization concepts needed for controller acceptance.

## 3. Learning objective

Given synthetic story scenarios, the owner can identify Status, Step, Hold reason, active guard, required evidence, and the one safe next action; distinguish `pause` from inspection-only `resume`; explain when review or human evidence blocks progress; and state why only exact `goagentic go` with valid authorization may execute work after trust is established.

## 4. Current research requirements

Use the exact committed revisions of the master program, story contract, P01 phase, and controller specification accepted by P01-S001. Record their Git commit and paths. External sources are not required because the lesson teaches this project's own operating contract rather than a changeable product.

## 5. Preconditions and unlock conditions

P01-S001. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

A project-specific lesson, a short scenario exercise, and `evidence/P01-S002/owner-learning.md` recording the owner's own answers about Status, Step, Hold reason, lease ownership, evidence, `pause`, `resume`, review, human gates, and `goagentic go` authorization.

## 7. Out of scope and prohibited changes

General project-management or AI-agent coursework; executing a real program story; changing controller or GitHub state; accepting paraphrased LLM answers as the owner's evidence; and marking completion without the owner performing the explain-back.

## 8. Privilege and human approval

Required human learning — the owner completes the exercise and supplies the explain-back. This is evidence under the P01 phase authorization, not a new approval, and the LLM cannot manufacture it.

## 9. Risk rationale

The lesson is Low risk because it changes only a learning-evidence file and asks the owner to reason about synthetic scenarios. It grants no authorization and performs no program mutation.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the currently accepted P01 mutation guard—the bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the guard; and route to review or human validation. The owner completes the exercise and accurately explains why resume does not execute and why only goagentic go authorizes work.

## 11. Automated acceptance tests

The owner completes the exercise and accurately explains why resume does not execute and why only goagentic go authorizes work. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

The owner answers the scenarios in their own words, demonstrates the exact next-command choice, and records completion. The guiding LLM may score and explain but may not generate or rewrite the owner's answers.

## 13. Idempotency and rollback

The lesson can be repeated without changing controller state. A later attempt appends or supersedes the prior scored exercise rather than rewriting the owner's original answers; rollback reverts only the learning-evidence commit.

## 14. Required evidence

Lesson revision; linked controller and story-contract revisions; interface/provider/model/effort used for guidance; the owner's ungenerated answers; scored scenarios for pause versus resume versus authorization; completion timestamp; and the owner's explicit acknowledgement that conversational “go” is not controller authorization.

## 15. Definition of done

The owner correctly classifies every scenario, explains why `resume` cannot execute work, identifies genuine human evidence, and invokes no mutating command. The signed learning record is committed and P01-S003 alone becomes eligible for activation.

## 16. Pause-safe boundaries

Pause between lesson modules or scenarios and before the owner signs the evidence. Preserve answered scenarios exactly; never pause while transforming or scoring an answer without first saving the original.
