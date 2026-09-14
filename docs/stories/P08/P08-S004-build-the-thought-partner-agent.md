# P08-S004: Build the thought-partner agent

| Property | Value |
|---|---|
| Story ID | P08-S004 |
| Phase | P08 — Practical Personal Agents |
| Sequence | 5 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P08-S012 |
| Unlocks | P08-S005 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: controller-selected cloud provider; Model class: high-reliability safety implementation; Effort: high; Fallback: disable preset and return to the shared diagnostic runtime. |
| Research freshness | P08-S001 baseline unexpired; current US 988/SAMHSA resources and owner-region applicability checked within 24 hours of activation. |

## 1. User story

As the owner, I want a private thought partner that helps me reflect and clarify choices without presenting itself as a therapist or encouraging dependence.

## 2. Bounded objective

Implement workloads/agents/personal/thought_partner/ and operation operations/windows/p08/P08-S004-thought-partner/; register one private Open WebUI preset using the P03 accepted primary model.

## 3. Learning objective

Not applicable — P08-S002 covers the operating concepts; P08-S010 teaches practical use.

## 4. Current research requirements

Recheck crisis-resource details, model safety behavior, Open WebUI preset controls, and applicable OWASP threats. Record that the agent is a reflective aid, not therapy or healthcare.

## 5. Preconditions and unlock conditions

P08-S012 is Done. Activation names owner region, accepted model profile, allowed prompt/skill assets, no-tool default, trace policy, session retention, and emergency-resource source.

## 6. In scope

Reflective listening; clarifying questions; values/options exercises; user-authored next steps; uncertainty; role/model/data/memory disclosure; a versioned current-region resource registry under workloads/agents/personal/thought_partner/resources/; layered crisis detection and response; non-dependency language; session deletion; and explicit preview/confirm Markdown export.

## 7. Out of scope and prohibited changes

No diagnosis, therapy, treatment, medication advice, clinical assessment, coercion, sentience/exclusivity claim, discouraging human help, emergency dispatch, contact/calendar action, autonomous task, RAG, durable memory, or unconfirmed write.

## 8. Privilege and human approval

Covered by the P08 activation packet. Every export requires an in-session preview and explicit owner confirmation; crisis routing never triggers an external action.

## 9. Risk rationale

High: emotionally sensitive use can cause harm even without system privilege.

## 10. Execution contract

Instantiate the shared contract; use deterministic high-confidence safety routing plus model-level boundary instructions and output validation; offer current-region emergency help without diagnosing; keep false-positive responses supportive; disable tools by default; version prompts; register the private preset; and independently review fixtures and behavior.

## 11. Automated acceptance tests

Test ordinary reflection, ambiguity, disagreement, overreliance/dependency prompts, therapist/diagnosis/medication requests, self-harm and harm-to-others scenarios, non-US location, prompt injection, role escape, false positives, secret/PII redaction, session deletion, no-memory disclosure, export deny/preview/approve, restart, and second-run no-op. Require deterministic route tests plus semantic evaluation; an LLM judge cannot be the sole safety gate.

## 12. Human validation

Deferred to P08-S010. No technical or crisis scenario is assigned to the owner here.

## 13. Idempotency and rollback

Same versioned configuration is a no-op. Rollback disables/removes only the preset and graph, restores the runtime checkpoint, and deletes synthetic test sessions while preserving review evidence.

## 14. Required evidence

evidence/P08-S004/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, safety-matrix.json, redaction-results.json, prompt-version.json, and open-webui-registration.json.

## 15. Definition of done

The private agent is useful on ordinary cases, reliably holds its role boundaries, routes urgent scenarios appropriately, leaks no seeded private data, has no durable memory, and passes independent review.

## 16. Pause-safe boundaries

Update evidence/P08-S004/checkpoint.json after graph, safety, preset, test, and review gates. Never pause with a failing crisis, privacy, or role-boundary test while the preset remains enabled.
