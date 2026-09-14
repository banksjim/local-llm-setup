# P06-S014: Perform first-agent owner acceptance

| Property | Value |
|---|---|
| Story ID | P06-S014 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 14 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P06-S013 |
| Unlocks | P07-S001 |
| Preferred route | Interface: goagentic guided acceptance using VS Code/WSL, the agent CLI, and localhost MLflow UI; Provider: owner's accepted cloud assistant for guidance while the tested agent uses its qualified route; Model class: economical tutor plus recorded agent model; Effort: medium; Fallback: current Sol- or Sonnet-class guide, never unattended substitution. |
| Research freshness | Not applicable — validation uses the implemented agent. |

## 1. User story

As the workstation owner, I want this story to have the owner inspect code, run the agent, interrupt and resume it, view traces, and reject an unsafe action, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Have the owner inspect code, run the agent, interrupt and resume it, view traces, and reject an unsafe action.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P06-S011; this story introduces no separate learning objective.

## 4. Current research requirements

Not applicable — validation uses the accepted agent build and recorded dependency versions and makes no new product recommendation.

## 5. Preconditions and unlock conditions

P06-S013. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create a blank owner packet from P06-S013 results covering code navigation, provider/model identification, safe fixture task, tool trace, process-stop/resume, approval denial, MCP call, skill invocation, MLflow failure inspection, and rollback observation. Use only tagged synthetic state and store genuine results under `evidence/P06-S014/`.

## 7. Out of scope and prohibited changes

Do not repair defects inside acceptance, use private data, enter credentials into evidence, broaden tools, coach the required answers, infer approval, or mark completion from automated evidence alone.

## 8. Privilege and human approval

The existing P06 authorization covers the pretested synthetic acceptance operations. The owner must personally perform and sign every task; any repair or scope change becomes a separately previewed story.

## 9. Risk rationale

Acceptance exercises the integrated agent, persistent state, MCP, skills, and observability; it may reveal defects but uses synthetic data and cannot silently repair them.

## 10. Execution contract

Validate prerequisite hashes; generate a packet with blank owner fields; preflight tagged fixtures; guide one task at a time without supplying answers; stop and file a defect on discrepancy; let the owner record observations; clean tagged state; verify only packet completeness/authorship; and reconcile controller state.

## 11. Automated acceptance tests

Assert nonzero checklist items, accepted prerequisite references, blank pre-handoff fields, isolated fixture/thread IDs, and cleanup plan. After handoff, verify genuine owner entries and signature exist. Fail on omitted task, prefilled answer, failed required item, unresolved defect, untagged state, incomplete cleanup, or zero checklist rows.

## 12. Human validation

The owner inspects the code, identifies provider/model/tool authority, completes the fixture task, stops and resumes it, denies an unsafe proposal, calls MCP and the skill, locates the failure trace, observes cleanup, and signs `evidence/P06-S014/human-acceptance.md`. The LLM cannot author observations or signature.

## 13. Idempotency and rollback

Each attempt uses new tagged fixtures/threads and preserves earlier signed records. Cleanup removes only those tags; rollback restores the pre-acceptance configuration and never deletes accepted agent code or unrelated traces.

## 14. Required evidence

Commit blank and signed packets plus `evidence/P06-S014/` activation, prerequisite hashes, task/trace/thread IDs, defect list, cleanup and rollback proof, checkpoint, and review; exclude credentials and raw private content.

## 15. Definition of done

Every owner task passes, evidence is genuine, no material defect remains, tagged state is cleaned, review resolves, and P07-S001 unlocks.

## 16. Pause-safe boundaries

Pause between owner tasks only after saving tagged state, never during recording or config replacement. Record next task, thread/trace IDs, model/provider, and cleanup state in `evidence/P06-S014/checkpoint.json`.
