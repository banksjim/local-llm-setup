# P03-S011: Complete model selection human acceptance

| Property | Value |
|---|---|
| Story ID | P03-S011 |
| Phase | P03 — Local Inference and Model Foundation |
| Sequence | 11 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P03-S010 |
| Unlocks | P04-S001 |
| Preferred route | Interface: goagentic-guided session in the designated cloud IDE or CLI; Provider: owner's active OpenAI or Anthropic subscription; Model class: current economical teaching or validation model; Effort: medium; Fallback: pause for the owner or switch to the current Sol or Sonnet-class route when explanation quality fails. |
| Research freshness | Not applicable — validation uses measured candidate outputs. |

## 1. User story

As the workstation owner, I want this story to let the owner compare responsiveness and output quality for representative personal tasks, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Let the owner compare responsiveness and output quality for representative personal tasks.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P03-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Not applicable — validation uses the accepted, measured candidate outputs and makes no new current-product recommendation.

## 5. Preconditions and unlock conditions

P03-S010. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify owner task packet, randomized model labels where practical, response and latency scorecard, preference decision, and genuine owner acceptance record; model files are read-only. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P03-S011/.

## 7. Out of scope and prohibited changes

Do not install containers or desktop clients, expose Ollama to the LAN, delete existing models, change BIOS or GPU drivers, accept floating model tags, or route unqualified controller work to a local model.

## 8. Privilege and human approval

No new approval is required while the revision-bound P03 phase authorization still matches the work. The owner must personally perform the named GUI, authentication, elevation, microphone, preference, or acceptance actions; changed scope stops for a new preview.

## 9. Risk rationale

Acceptance changes the owner-approved model baseline but performs only bounded inference and preference recording.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce evidence/P03-S011/human-acceptance.md; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: the owner completes the same chat, vision, coding, and agent tasks on primary and fast profiles and records preference, acceptable latency, and any disqualifying behavior.

## 11. Automated acceptance tests

Assert that expected fixtures and checklist items are nonzero; validate the lesson or acceptance packet schema, prerequisite automated results, evidence paths, timestamps, and blank owner-answer fields before handoff. After handoff, verify only that genuine owner-authored evidence exists and matches the rubric; automation must not generate, infer, or change the owner's answers.

## 12. Human validation

The owner runs the blinded or randomized chat, vision, coding, and agent tasks, scores quality and responsiveness without answer substitution, records the preferred primary and fast profiles plus any disqualification, and signs evidence/P03-S011/human-validation.md. The LLM may prepare the packet but cannot score or sign it.

## 13. Idempotency and rollback

Tests use synthetic or owner-approved fixtures and leave accepted services and configuration unchanged. Rollback removes story-created fixtures and restores the pre-test snapshot recorded in evidence/P03-S011/rollback.json.

## 14. Required evidence

Commit the genuine owner-authored evidence/P03-S011/human-acceptance.md, the accepted primary/fast/embedding selection record, referenced benchmark and VRAM-headroom results, rejected-candidate rationale, and evidence/P03-S011/activation.json, change-inventory.json, test-results.json, rollback.json, and review.md. Include exact model tags or digests, context settings, timestamps, and sanitized observations.

## 15. Definition of done

P03-S011 is Done only when the owner completes the same chat, vision, coding, and agent tasks on primary and fast profiles and records preference, acceptable latency, and any disqualifying behavior; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P03-S011/checkpoint.json.
