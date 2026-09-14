# P08-S011: Build the daily-check-in agent

| Property | Value |
|---|---|
| Story ID | P08-S011 |
| Phase | P08 — Practical Personal Agents |
| Sequence | 7 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P08-S005 |
| Unlocks | P08-S006 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: controller-selected cloud provider; Model class: high-reliability implementation; Effort: high; Fallback: use the accepted primary model if the fast local profile misses any safety threshold. |
| Research freshness | P08-S001 baseline and current accepted fast-model evaluation checked within 7 days. |

## 1. User story

As the owner, I want a brief daily check-in agent that helps me reflect and choose a next action quickly without pretending to remember prior days.

## 2. Bounded objective

Implement workloads/agents/personal/daily_checkin/ and operation operations/windows/p08/P08-S011-daily-check-in/; register a private Open WebUI preset using the accepted fast model only if it meets the same safety floor as the primary model.

## 3. Learning objective

Not applicable — use and model choice are covered in P08-S010.

## 4. Current research requirements

Recheck fast-model tool/instruction reliability, runtime APIs, and current safety resources. Do not infer suitability from parameter count or speed alone.

## 5. Preconditions and unlock conditions

P08-S005 is Done. Activation defines a maximum interaction length, accepted model profiles, concise check-in schema, no-tool default, session retention, and optional approved export root.

## 6. In scope

Short mood/energy/priority reflection, one achievable next action, explicit uncertainty, role/model/data/memory disclosure, inherited crisis boundary, optional owner-confirmed Markdown check-in export, and automatic fallback to primary model on failed qualification.

## 7. Out of scope and prohibited changes

No reminders, notifications, scheduled automation, streak pressure, scoring the owner, diagnosis, therapy, autonomous action, RAG, cross-day recall, durable memory, or silent record.

## 8. Privilege and human approval

Covered by P08 activation. Each saved check-in requires preview/confirmation; model fallback is shown to the owner and recorded without exposing content.

## 9. Risk rationale

High: repeated emotionally relevant interactions and private records amplify small safety or privacy failures.

## 10. Execution contract

Build a bounded short-turn graph; inherit thought-partner safety; cap questions and calls; qualify fast and primary profiles on identical fixtures; select fast only if every hard safety/privacy threshold passes; register privately; version configuration; and cross-provider review.

## 11. Automated acceptance tests

Test ordinary/low-energy/frustrated responses, crisis and overreliance prompts, brevity, repeated-day non-memory, model disclosure/fallback, export deny/preview/approve/replay, PII redaction, role injection, no tools, thread isolation, restart, and no-op rerun. Fail if the fast model is merely faster but less safe.

## 12. Human validation

Deferred to P08-S010; the owner compares fast and primary experience without being asked to assess technical safety.

## 13. Idempotency and rollback

Same configuration is a no-op; export never overwrites silently. Rollback disables the preset, restores runtime/model routing, and preserves only owner-approved exports.

## 14. Required evidence

evidence/P08-S011/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, model-comparison.json, safety-matrix.json, export-policy-results.json, and open-webui-registration.json.

## 15. Definition of done

The agent is brief, helpful, non-coercive, safe on both ordinary and urgent fixtures, uses the fast model only after qualification, and has no silent durable record.

## 16. Pause-safe boundaries

Update evidence/P08-S011/checkpoint.json after each model, safety, export, preset, and review gate. Disable the fast profile immediately on any hard-threshold failure.
