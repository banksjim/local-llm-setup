# P08-S006: Build the fitness-coach agent

| Property | Value |
|---|---|
| Story ID | P08-S006 |
| Phase | P08 — Practical Personal Agents |
| Sequence | 8 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P08-S011 |
| Unlocks | P08-S007 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: controller-selected cloud provider; Model class: high-reliability safety implementation; Effort: high; Fallback: disable the preset and provide links to current official guidance only. |
| Research freshness | Current CDC/HHS physical-activity guidance and source revisions checked within 24 hours; runtime and model docs within 7 days. |

## 1. User story

As the owner, I want an educational fitness coach that helps structure safe activity plans while recognizing when a qualified professional is needed.

## 2. Bounded objective

Implement workloads/agents/personal/fitness_coach/ and operation operations/windows/p08/P08-S006-fitness-coach/; register a private Open WebUI preset on the accepted primary model.

## 3. Learning objective

Not applicable — P08-S010 covers safe use and escalation expectations.

## 4. Current research requirements

Use current official public-health guidance as the baseline; record revision dates and population applicability. Verify model/runtime behavior and do not use influencer, supplement-vendor, or scraped wellness content as authority.

## 5. Preconditions and unlock conditions

P08-S011 is Done. Activation fixes model profile, current official sources, input schema for goals/experience/equipment/constraints, escalation rules, no-tool policy, and session retention.

## 6. In scope

Versioned official source cards under workloads/agents/personal/fitness_coach/sources/; educational activity concepts; owner-stated goals, constraints, equipment, experience, preferences, and time; conservative progressive plans; recovery reminders; uncertainty; current-source citations; plan revision; and explicit Markdown export confirmation.

## 7. Out of scope and prohibited changes

No diagnosis, symptom interpretation, treatment, rehabilitation, nutrition prescription, eating-disorder coaching, medication/supplement advice, medical clearance, wearable/account integration, emergency action, RAG until P08-S008, durable memory, or silent write.

## 8. Privilege and human approval

Covered by P08 activation. Each export requires preview/confirmation. Requests involving symptoms, injury, chronic-condition uncertainty, pregnancy, medication, disordered eating, or urgent illness follow the deterministic escalation policy.

## 9. Risk rationale

High: incorrect or overconfident physical guidance can cause injury or delay appropriate care.

## 10. Execution contract

Use structured intake without diagnosis; select only approved educational patterns; apply deterministic exclusion/escalation checks before generation and output validation after it; cite official guidance; label assumptions; avoid false precision; register privately; and cross-provider review.

## 11. Automated acceptance tests

Test golden conservative-plan fixtures plus beginner and experienced goals, limited equipment/time, disability/chronic-condition uncertainty, injury/pain/chest-pain/fainting, medication/supplement, eating-disorder, rapid-weight-loss, youth/pregnancy, prompt injection, unsafe intensity, invented citations, no-memory disclosure, export controls, redaction, restart, rollback, and no-op rerun. Hard safety decisions use code fixtures, not only an LLM judge.

## 12. Human validation

Deferred to P08-S010. The owner judges usefulness of a low-risk synthetic plan, not medical correctness.

## 13. Idempotency and rollback

Same configuration is a no-op. Rollback disables/removes the preset and graph, restores runtime configuration, and preserves owner-approved exports.

## 14. Required evidence

evidence/P08-S006/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, source-applicability.json, safety-matrix.json, citation-results.json, and open-webui-registration.json.

## 15. Definition of done

The agent produces conservative educational plans for supported cases, escalates excluded cases, cites current official sources, holds privacy/role boundaries, and passes independent review.

## 16. Pause-safe boundaries

Update evidence/P08-S006/checkpoint.json after sources, graph, safety, citation, preset, and review gates. Disable the preset before pausing on any health-safety or citation failure.
