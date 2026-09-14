# P08-S005: Build the life-planning agent

| Property | Value |
|---|---|
| Story ID | P08-S005 |
| Phase | P08 — Practical Personal Agents |
| Sequence | 6 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P08-S004 |
| Unlocks | P08-S011 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: controller-selected cloud provider; Model class: high-reliability agent implementation; Effort: high; Fallback: disable preset and retain only approved Markdown templates. |
| Research freshness | P08-S001 baseline and current runtime/preset documentation checked within 7 days. |

## 1. User story

As the owner, I want a life-planning agent that converts my stated priorities into realistic, revisable plans while leaving decisions and commitments with me.

## 2. Bounded objective

Implement workloads/agents/personal/life_planner/ and operation operations/windows/p08/P08-S005-life-planner/; register a private Open WebUI preset on the accepted primary model.

## 3. Learning objective

Not applicable — targeted operating practice occurs in P08-S010.

## 4. Current research requirements

Reconfirm current agent/runtime APIs and review selected planning templates for accessibility, coercive patterns, hidden assumptions, and unsupported health/financial claims.

## 5. Preconditions and unlock conditions

P08-S004 is Done. Activation fixes model profile, structured goal/constraint schema, read-only/no-tool policy, session retention, allowed templates, and export root.

## 6. In scope

Goal clarification, priorities, constraints, options, milestones, dependencies, tradeoffs, uncertainty, user-selected next actions, progress reflection, plan revision, and previewed Markdown export to an approved owner-controlled location.

## 7. Out of scope and prohibited changes

No calendar/message/task-system action, autonomous commitments, health/financial/legal direction, surveillance, guilt/shame tactics, arbitrary file access, RAG, cross-session inference, durable memory, or silent export.

## 8. Privilege and human approval

Covered by the P08 activation packet. Each export is a separate in-session preview/confirm decision and may write only the approved path.

## 9. Risk rationale

High: advice can materially influence personal choices and the optional export writes private content.

## 10. Execution contract

Use a bounded LangGraph workflow for clarify, reflect, draft, challenge assumptions, owner choose, and optional export; enforce deterministic export policy and schema; show model/data/memory status; distinguish facts from planning suggestions; register privately; and review with a different provider.

## 11. Automated acceptance tests

Test vague/conflicting goals, unrealistic timelines, user disagreement, missing constraints, protected/sensitive attributes, prompt injection, professional-advice drift, coercion, action requests, no-memory disclosure, export deny/preview/approve/path traversal/replay, thread isolation, restart, rollback, and second-run no-op.

## 12. Human validation

Deferred to P08-S010, where the owner judges usefulness and tone using non-sensitive or deliberately chosen content.

## 13. Idempotency and rollback

Configuration reruns are no-ops. Exports are content-addressed and never overwrite without approval. Rollback unregisters the preset/graph and restores runtime configuration without deleting owner-approved exports.

## 14. Required evidence

evidence/P08-S005/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, planning-fixtures.json, export-policy-results.json, prompt-version.json, and open-webui-registration.json.

## 15. Definition of done

The agent creates practical owner-controlled plans, resists role/capability escape, writes only with explicit confirmation, discloses no durable memory, and passes independent review.

## 16. Pause-safe boundaries

Update evidence/P08-S005/checkpoint.json after workflow, export, preset, test, and review gates. Disable the preset before pausing on any privacy, coercion, or write-control failure.
