# P04-S014: Perform service-stack owner acceptance and restore drill

| Property | Value |
|---|---|
| Story ID | P04-S014 |
| Phase | P04 — Open WebUI and Supporting AI Services |
| Sequence | 14 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P04-S013 |
| Unlocks | P05-S001 |
| Preferred route | Interface: goagentic-guided session in the designated cloud IDE or CLI; Provider: owner's active OpenAI or Anthropic subscription; Model class: current economical validation model; Effort: medium; Fallback: pause for the owner or switch to the current Sol or Sonnet-class route when a drill fails. |
| Research freshness | Not applicable — owner validation uses the accepted P04 versions and P04-S013 evidence. |

## 1. User story

As the workstation owner, I want to use the service stack and observe a guided isolated restore, so that I can confirm it is understandable, usable, and recoverable before integrations expand.

## 2. Bounded objective

Have the owner complete normal Open WebUI workflows, identify service boundaries, and perform the human steps of one isolated restore drill.

## 3. Learning objective

Demonstrate that the owner can start and stop the stack, locate health and backup status, distinguish restart from data deletion, and recognize when to stop and request diagnosis.

## 4. Current research requirements

Not applicable — the packet makes no new product claim. Version drift or changed UI labels block and return to P04-S001 or the owning implementation story.

## 5. Preconditions and unlock conditions

P04-S013 is Done with a clean baseline; the owner is present; the isolated target is empty; no live-volume restore is proposed.

## 6. In scope

Create evidence/P04-S014/human-acceptance.md and a guided checklist for chat, vision, sourced search, synthetic upload/retrieval, in-chat dictation, trace inspection, health interpretation, stack restart, backup selection, isolated restore observation, and safe-stop response.

## 7. Out of scope and prohibited changes

Do not restore into live volumes, use private owner documents, repair defects during acceptance, change service settings, expose ports, enable cloud services, or let the LLM write the owner's answers or sign-off.

## 8. Privilege and human approval

P04 phase authorization covers the already-previewed restart and isolated restore operations. The owner performs GUI, microphone, interpretation, and sign-off actions; changed targets or repair work require a new story and preview.

## 9. Risk rationale

The owner handles a backup and observes service restart and restore; using the wrong target could overwrite durable stack data, so isolation is mandatory.

## 10. Execution contract

Validate the P04-S013 baseline; generate a checklist with blank owner fields; guide one task at a time; stop on discrepancy; let the owner record observations; verify the isolated restore through read-only comparison; clean the isolated target; reconcile evidence and controller state without modifying failed work.

## 11. Automated acceptance tests

Assert nonzero checklist items and validate prerequisite results, empty isolated target, packet schema, blank owner fields, evidence timestamps, restore checksum references, and cleanup. Fail if the target is not isolated and empty, any required owner response is absent, a restore comparison differs, cleanup is incomplete, or the validator matches zero checklist items. After handoff, verify only that genuine owner-authored responses exist; automation may not infer acceptance.

## 12. Human validation

The owner personally completes every checklist item, describes one failure boundary and safe response, confirms usability and acceptable latency, observes the isolated restore, and signs evidence/P04-S014/human-acceptance.md. Any failed required item blocks completion.

## 13. Idempotency and rollback

Repeating acceptance creates a new dated owner record and a new empty isolated target. Cleanup removes only that isolated target and synthetic fixtures; accepted services and live data remain unchanged.

## 14. Required evidence

Commit the blank checklist and genuine completed human-acceptance.md plus activation.json, P04-S013 reference, isolated-target preflight, sanitized task results, restore comparison, cleanup proof, defect list, rollback.json, and review.md under evidence/P04-S014/.

## 15. Definition of done

Every required owner task passes, owner evidence is genuine, the isolated restore and cleanup are verified, no defect or review finding remains unresolved, baseline services are healthy, and P05-S001 unlocks.

## 16. Pause-safe boundaries

Pause between checklist tasks, after baseline restart, after isolated restore verification and cleanup, and after owner evidence commit. Never pause while recording audio, a service is intentionally stopped, or an isolated restore is incomplete; record the next command in evidence/P04-S014/checkpoint.json.
