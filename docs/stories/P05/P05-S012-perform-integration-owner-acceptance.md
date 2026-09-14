# P05-S012: Perform integration owner acceptance

| Property | Value |
|---|---|
| Story ID | P05-S012 |
| Phase | P05 — Desktop and Development Tool Integrations |
| Sequence | 12 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P05-S011 |
| Unlocks | P06-S001 |
| Preferred route | Interface: goagentic-guided session in the designated cloud IDE or CLI; Provider: owner's active OpenAI or Anthropic subscription; Model class: current economical teaching or validation model; Effort: medium; Fallback: pause for the owner or switch to the current Sol or Sonnet-class route when explanation quality fails. |
| Research freshness | Not applicable — validation is experiential. |

## 1. User story

As the workstation owner, I want this story to have the owner complete normal VS Code, Codex, Claude, Open WebUI, and dictation tasks, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Have the owner complete normal VS Code, Codex, Claude, Open WebUI, and dictation tasks.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P05-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Not applicable — owner validation is experiential against the accepted integration inventory and makes no new product recommendation.

## 5. Preconditions and unlock conditions

P05-S011. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify an owner checklist, provider and model identification task, representative VS Code, Codex, Claude, Open WebUI, and dictation tasks, pause and resume drill, one settings restore drill, defect record, and genuine sign-off. Include LM Studio live only with recorded opt-in; otherwise require the owner to locate its optional guide and explain that it is not installed. Store evidence under evidence/P05-S012/.

## 7. Out of scope and prohibited changes

Do not weaken WSL isolation, overwrite unrelated editor settings, share Windows and Ubuntu credentials, enable cloud transcription or cleanup, silently replace a hosted model, expose a local endpoint to the LAN, or install an optional integration without owner opt-in.

## 8. Privilege and human approval

No new approval is required while the revision-bound P05 phase authorization still matches the work. The owner must personally perform the named GUI, authentication, elevation, microphone, preference, or acceptance actions; changed scope stops for a new preview.

## 9. Risk rationale

Human acceptance exercises all integrations and a restore path; it can reveal but must not silently repair defects.

## 10. Execution contract

Create a blank owner packet from the accepted P05-S011 matrix; mark LM Studio live or guide-only from the recorded opt-in; verify the rollback checkpoint; guide but do not answer each task; stop and open a defect for any failure; let the owner sign the result; reconcile controller state without repairing acceptance failures inside this story.

## 11. Automated acceptance tests

Assert that expected fixtures and checklist items are nonzero; validate the lesson or acceptance packet schema, prerequisite automated results, evidence paths, timestamps, and blank owner-answer fields before handoff. Fail if any required workflow is omitted, the optional LM Studio disposition is missing, a provider boundary differs from the accepted design, owner evidence is absent, or the validator matches zero checklist items. After handoff, verify only that genuine owner-authored evidence exists and matches the rubric; automation must not generate, infer, or change the owner's answers.

## 12. Human validation

The owner identifies the active provider and model, completes VS Code local chat, Codex cloud and local, Claude cloud and local, Open WebUI, and Windows dictation tasks, runs the pause and resume drill, restores one integration, and records the result in evidence/P05-S012/human-validation.md. With no LM Studio opt-in, the owner instead locates its guide and confirms it is not installed. The LLM cannot author the answers.

## 13. Idempotency and rollback

Tests use synthetic or owner-approved fixtures and leave accepted services and configuration unchanged. Rollback removes story-created fixtures and restores the pre-test snapshot recorded in evidence/P05-S012/rollback.json.

## 14. Required evidence

Commit the genuine owner-authored evidence/P05-S012/human-acceptance.md, the completed VS Code/Codex/Claude Code workflow checklist, endpoint and model-profile observations, desktop-dictation result, optional-track disposition, and evidence/P05-S012/activation.json, change-inventory.json, test-results.json, rollback.json, and review.md. Include exact client and extension versions, timestamps, and sanitized observations without credentials or dictated content.

## 15. Definition of done

P05-S012 is Done only when all required owner tasks, provider identification, pause/resume, and restore pass; LM Studio passes live only when opted in or is correctly verified as guide-only; genuine owner evidence exists; independent review has no unresolved material finding; and P06-S001 unlocks.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P05-S012/checkpoint.json.
