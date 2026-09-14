# P08-S010: Perform personal-agent owner acceptance

| Property | Value |
|---|---|
| Story ID | P08-S010 |
| Phase | P08 — Practical Personal Agents |
| Sequence | 12 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Approval |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P08-S009 |
| Unlocks | P09-S001 |
| Preferred route | Interface: Open WebUI with goagentic evidence capture; Provider: accepted local Ollama profiles; Model class: P08-qualified primary/fast routes; Effort: owner-paced; Fallback: pause, disable the affected preset, and return a bounded correction to its implementation story. |
| Research freshness | P08-S009 evaluation and P08-S001 safety resources must be unexpired; recheck current emergency and cited official resources within 24 hours. |

## 1. User story

As the owner, I want guided hands-on acceptance so I can decide whether each agent is understandable, useful, comfortable, and ready for personal use.

## 2. Bounded objective

Run an owner-paced acceptance session for all five private Open WebUI agents and record the outcome at evidence/P08-S010/owner-acceptance.md without asking the owner to certify technical correctness.

## 3. Learning objective

The owner can select the right agent/model, recognize its visible scope and memory status, use citations and uncertainty, export or delete a session safely, identify an inappropriate request, and know how to pause/disable/report a problem.

## 4. Current research requirements

Confirm UI instructions match the installed Open WebUI version and all safety/resource links are current. No new recommendation is introduced during acceptance without returning to P08-S001/P08-S009.

## 5. Preconditions and unlock conditions

P08-S009 is Done with no unresolved High/Critical finding. An isolated synthetic rehearsal has validated the complete acceptance sequence, expected UI state, cleanup, and rollback without owner data. The acceptance packet shows enabled presets, model routes, disclosures, automated results, known limitations, safe synthetic prompts, expected behavior, privacy choices, rollback command, and owner decisions requested.

## 6. In scope

Open WebUI selection and disclosure; one ordinary scenario per agent; primary-versus-fast daily check-in comparison; citation inspection; explicit export then cleanup; session deletion; one mild boundary request per agent; pause/disable workflow; and accept, reject, or needs-change decision per agent.

## 7. Out of scope and prohibited changes

No technical architecture review, deliberately traumatic crisis exercise, unsafe physical activity, real investment/tax/legal decision, financial credential/account, required sensitive disclosure, automatic pass, P09 memory, or widening permissions during the session.

## 8. Privilege and human approval

This is the human gate. Each agent is enabled for personal use only after the owner explicitly accepts it. Critical activates only the review/decision requirement; it does not authorize new system changes.

## 9. Risk rationale

Critical: this gate authorizes ongoing use in emotionally, physically, or financially consequential contexts. The explicit revision-bound P08 phase authorization, isolated rehearsal, cross-provider review from P08-S009, and genuine owner acceptance in this story are mandatory.

## 10. Execution contract

Show a plain-language result packet; guide one short scenario at a time; state expected boundary before testing it; stop immediately on discomfort; capture only the owner's decision and optional notes; verify export/deletion/disable; route failures to the smallest owning story; and never reinterpret silence as approval.

## 11. Automated acceptance tests

Before owner participation, rehearse the full sequence with isolated synthetic accounts/sessions and inject a failed preset, failed export, interrupted session, and rollback. Before each owner scenario, verify exact preset/config/model hash, private binding, no-memory status, correct disclosure, hard-suite pass, enabled source matrix, redacted tracing, clean rollback, and evidence form. Afterward verify export/delete/disable events match owner choices and no raw prompt was added to Git/evidence.

## 12. Human validation

For each agent, the owner records accept, reject, or needs change for usefulness, tone, clarity, boundaries, speed, citations where applicable, and comfort. The owner confirms the daily model choice and demonstrates pause/disable once. No technical judgment is required.

## 13. Idempotency and rollback

Reruns preserve prior decisions and retest only changed agents unless the owner requests the full session. Rejection disables the preset; rollback restores the pre-acceptance enabled set and removes test sessions/exports selected for cleanup.

## 14. Required evidence

evidence/P08-S010/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, owner-acceptance.md, per-agent-decisions.json, ui-version-check.json, privacy-cleanup.json, and routing-outcomes.json.

## 15. Definition of done

Every agent is explicitly accepted or disabled with a routed correction; the owner can operate and stop the system; no technical responsibility was shifted to the owner; evidence is genuine; and only accepted agents unlock P09 consideration.

## 16. Pause-safe boundaries

Update evidence/P08-S010/checkpoint.json after each agent with owner decision, enabled state, cleanup result, and exact next scenario. A pause leaves unaccepted presets disabled and never infers consent.
