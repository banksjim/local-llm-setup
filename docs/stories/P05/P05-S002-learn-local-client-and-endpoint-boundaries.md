# P05-S002: Learn local client and endpoint boundaries

| Property | Value |
|---|---|
| Story ID | P05-S002 |
| Phase | P05 — Desktop and Development Tool Integrations |
| Sequence | 2 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P05-S001 |
| Unlocks | P05-S003 |
| Preferred route | Interface: goagentic-guided session in the designated cloud IDE or CLI; Provider: owner's active OpenAI or Anthropic subscription; Model class: current economical teaching or validation model; Effort: medium; Fallback: pause for the owner or switch to the current Sol or Sonnet-class route when explanation quality fails. |
| Research freshness | Current P05 research record. |

## 1. User story

As the workstation owner, I want this story to teach which UI, CLI, endpoint, port, and model manager is used for each workflow, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Teach which UI, CLI, endpoint, port, and model manager is used for each workflow.

## 3. Learning objective

Complete the targeted concepts and demonstrate them through the acceptance exercise.

## 4. Current research requirements

Current P05 research record. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P05-S001. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify the client-boundary lesson, endpoint and credential map, model-store diagram, switching exercise, chat versus inline versus MCP worksheet, answer rubric, and owner response. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P05-S002/.

## 7. Out of scope and prohibited changes

Do not weaken WSL isolation, overwrite unrelated editor settings, share Windows and Ubuntu credentials, enable cloud transcription or cleanup, silently replace a hosted model, expose a local endpoint to the LAN, or install an optional integration without owner opt-in.

## 8. Privilege and human approval

The owner completes the learning exercise and writes their answers, but no privileged authorization is requested and no system mutation is allowed in P05-S002.

## 9. Risk rationale

This learning gate has no mutation; misunderstanding endpoints or credentials blocks client setup.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce docs/learning/p05/P05-S002-learn-local-client-and-endpoint-boundaries.md; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: the owner maps every supported interface to its process boundary, endpoint, port, model store, credential store, and switching method, and distinguishes chat, inline completion, MCP, and model replacement.

## 11. Automated acceptance tests

Assert that expected fixtures and checklist items are nonzero; validate the lesson or acceptance packet schema, prerequisite automated results, evidence paths, timestamps, and blank owner-answer fields before handoff. After handoff, verify only that genuine owner-authored evidence exists and matches the rubric; automation must not generate, infer, or change the owner's answers.

## 12. Human validation

The owner completes the guided exercise without answer substitution, explains the result in their own words, and records completion in evidence/P05-S002/human-validation.md.

## 13. Idempotency and rollback

A repeat run refreshes docs/learning/p05/P05-S002-learn-local-client-and-endpoint-boundaries.md without duplicate records. Rollback restores its pre-story Git version and removes only unaccepted evidence/P05-S002/ evidence.

## 14. Required evidence

Commit docs/learning/p05/P05-S002-learn-local-client-and-endpoint-boundaries.md or its versioned result plus evidence/P05-S002/activation.json, evidence/P05-S002/change-inventory.json, evidence/P05-S002/test-results.json, evidence/P05-S002/rollback.json, and evidence/P05-S002/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and genuine owner-authored human validation.

## 15. Definition of done

P05-S002 is Done only when the owner maps every supported interface to its process boundary, endpoint, port, model store, credential store, and switching method, and distinguishes chat, inline completion, MCP, and model replacement; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P05-S002/checkpoint.json.
