# P01-S014: Complete owner controller acceptance drill

| Property | Value |
|---|---|
| Story ID | P01-S014 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 15 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P01-S013 |
| Unlocks | P02-S001 |
| Preferred route | Interface: interactive Codex or Claude Code session plus the built controller; Provider: OpenAI or Anthropic; Model class: general-purpose guide; Effort: medium; Fallback: switch cloud provider while retaining the same accepted checklist; no model may substitute for owner actions or evidence. |
| Research freshness | Not applicable — acceptance uses the built controller and approved specification. |

## 1. User story

As the workstation owner, I want this story to guide the owner through zero-context start, lesson, execution, pause, restart, resume, review, rejection, and completion, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Guide the owner through zero-context start, lesson, execution, pause, restart, resume, review, rejection, and completion.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P01-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Not applicable — acceptance uses the built controller, its recorded versions, and the owner-approved specification; it makes no new current-product recommendation.

## 5. Preconditions and unlock conditions

P01-S013. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

A scripted owner drill using disposable stories and fixtures for zero-context entry, reading one next action, learning hold, exact authorization, safe pause, application restart, machine reboot, resume reconciliation, rejected bypass, independent-review handoff, human completion, and final status.

## 7. Out of scope and prohibited changes

Starting P02 workstation work, substituting simulated LLM statements for owner actions, bypassing a failed drill step, using real credentials or private data in fixtures, changing acceptance criteria during the drill, and granting Controller Core Trusted with unresolved High or Critical findings.

## 8. Privilege and human approval

Required human validation — the owner performs the drill and explicitly accepts or rejects Controller Core Trusted. This is acceptance evidence under the existing P01 authorization, not another approval of unchanged mutations.

## 9. Risk rationale

The story is Critical because owner acceptance grants the controller authority to guide later privileged workstation operations. The drill uses disposable state, but it crosses the program trust boundary and therefore requires genuine owner actions, reboot recovery, isolated rehearsal, and explicit acceptance.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the currently accepted P01 mutation guard—the bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the guard; and route to review or human validation. The owner completes every step without relying on this chat; the accepted baseline is tagged Controller Core Trusted.

## 11. Automated acceptance tests

The owner completes every step without relying on this chat; the accepted baseline is tagged Controller Core Trusted. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

The owner personally performs every marked drill action, records pass or fail without LLM substitution, and explicitly accepts or rejects the Controller Core Trusted transition.

## 13. Idempotency and rollback

The drill can restart from a new disposable fixture without altering the prior signed record. Cleanup removes only drill-owned state; rollback withholds the trust-stage change and restores the pre-drill controller state while preserving failure evidence.

## 14. Required evidence

Accepted drill revision; controller commit and review verdict; each owner action with timestamp; pre/post restart and reboot checkpoints; denied bypass output; resume no-mutation proof; disposable-state inventory and cleanup; failed or repeated steps; explicit owner acceptance or rejection; and trust-stage result.

## 15. Definition of done

The owner completes every drill step without this chat, returns after both application restart and reboot, receives the same safe state, observes a bypass denial, confirms `resume` did not execute, and explicitly accepts the controller. Only then is Controller Core Trusted recorded and P02-S001 unblocked.

## 16. Pause-safe boundaries

Pause at the checklist's declared boundaries, including the deliberate pause/restart step, after each owner result is recorded, and before the trust-stage decision. Never skip forward after a failed or ambiguous step.
