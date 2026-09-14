# P03-S002: Learn local inference, parameters, quantization, and context

| Property | Value |
|---|---|
| Story ID | P03-S002 |
| Phase | P03 — Local Inference and Model Foundation |
| Sequence | 2 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P03-S001 |
| Unlocks | P03-S003 |
| Preferred route | Interface: goagentic-guided session in the designated cloud IDE or CLI; Provider: owner's active OpenAI or Anthropic subscription; Model class: current economical teaching or validation model; Effort: medium; Fallback: pause for the owner or switch to the current Sol or Sonnet-class route when explanation quality fails. |
| Research freshness | Current P03 research and official Ollama guidance. |

## 1. User story

As the workstation owner, I want this story to teach what B means, how quantization, context, and KV cache affect quality and VRAM, and how to choose a task profile, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Teach what B means, how quantization, context, and KV cache affect quality and VRAM, and how to choose a task profile.

## 3. Learning objective

Complete the targeted concepts and demonstrate them through the acceptance exercise.

## 4. Current research requirements

Current P03 research and official Ollama guidance. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P03-S001. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify the lesson, two sizing worksheets, answer rubric, and owner response record; no Ollama setting or model is changed. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P03-S002/.

## 7. Out of scope and prohibited changes

Do not install containers or desktop clients, expose Ollama to the LAN, delete existing models, change BIOS or GPU drivers, accept floating model tags, or route unqualified controller work to a local model.

## 8. Privilege and human approval

The owner completes the learning exercise and writes their answers, but no privileged authorization is requested and no system mutation is allowed in P03-S002.

## 9. Risk rationale

This human learning gate has no system mutation; incorrect answers block installation.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce docs/learning/p03/P03-S002-learn-local-inference-parameters-quantization-and-context.md; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: the owner correctly explains B, quantization, context, KV cache, VRAM headroom, and chooses a profile from two sizing scenarios.

## 11. Automated acceptance tests

Assert that expected fixtures and checklist items are nonzero; validate the lesson or acceptance packet schema, prerequisite automated results, evidence paths, timestamps, and blank owner-answer fields before handoff. After handoff, verify only that genuine owner-authored evidence exists and matches the rubric; automation must not generate, infer, or change the owner's answers.

## 12. Human validation

The owner completes the guided exercise without answer substitution, explains the result in their own words, and records completion in evidence/P03-S002/human-validation.md.

## 13. Idempotency and rollback

A repeat run refreshes docs/learning/p03/P03-S002-learn-local-inference-parameters-quantization-and-context.md without duplicate records. Rollback restores its pre-story Git version and removes only unaccepted evidence/P03-S002/ evidence.

## 14. Required evidence

Commit docs/learning/p03/P03-S002-learn-local-inference-parameters-quantization-and-context.md or its versioned result plus evidence/P03-S002/activation.json, evidence/P03-S002/change-inventory.json, evidence/P03-S002/test-results.json, evidence/P03-S002/rollback.json, and evidence/P03-S002/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and genuine owner-authored human validation.

## 15. Definition of done

P03-S002 is Done only when the owner correctly explains B, quantization, context, KV cache, VRAM headroom, and chooses a profile from two sizing scenarios; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P03-S002/checkpoint.json.
