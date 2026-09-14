# P08-S001: Research current personal-agent patterns and safety

| Property | Value |
|---|---|
| Story ID | P08-S001 |
| Phase | P08 — Practical Personal Agents |
| Sequence | 1 |
| Status | Planned |
| Step | Research |
| Hold reason | Dependency |
| Risk | Low |
| Actor | LLM |
| Dependencies | P07-S017 |
| Unlocks | P08-S002 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: controller-selected cloud provider; Model class: research-capable; Effort: high; Fallback: second cloud provider for disputed safety or integration claims. |
| Research freshness | Official and primary sources checked during activation; product/tool facts no older than 7 days and public-health/consumer guidance checked for current revision. |

## 1. User story

As the owner, I want a current evidence baseline so agent design is based on today's supported interfaces and safety guidance rather than stale model knowledge.

## 2. Bounded objective

Create docs/research/p08/P08-S001-personal-agent-safety-baseline.md and a machine-readable decision inventory covering LangChain/LangGraph, Open WebUI, Ollama, MLflow, OWASP agentic threats, US crisis routing, adult physical-activity guidance, and consumer financial education.

## 3. Learning objective

Not applicable — P08-S002 converts the accepted research into targeted owner learning.

## 4. Current research requirements

Use official docs and primary authorities first. Record URL, title, publisher, checked-at UTC, version/revision, claim supported, license, and contradictory evidence. Vet one current short conceptual video and one current hands-on tutorial for P08-S002 by publisher authority, recency, technical accuracy, accessibility, and absence of unsafe claims.

## 5. Preconditions and unlock conditions

P07-S017 is Done. The activation packet identifies accepted P03 models, P04 service versions, P06 agent contracts, P07 retrieval contract, owner region, and research cutoff.

## 6. In scope

Current agent/runtime APIs; Open WebUI private model presets and supported integration path; deterministic/model guardrails; human interrupts; checkpoint semantics; tool budgets; prompt-injection defenses; trace redaction; evaluation; mental-wellness, fitness, and financial-education boundaries; and applicable current official resources.

## 7. Out of scope and prohibited changes

No service change, model pull, package install, private-data access, clinical/legal interpretation, scraped advice site, social-media recommendation as authority, or implementation decision unsupported by evidence.

## 8. Privilege and human approval

No privileged action. Public read-only research is allowed; authenticated/private sources require separate authorization.

## 9. Risk rationale

Low: repository documentation only, but weak research could cause unsafe downstream design.

## 10. Execution contract

Refresh sources; reproduce important claims from primary documentation; compare at least two viable Open WebUI integration patterns; define rejected alternatives and exit criteria; identify version-sensitive assumptions; create a research expiry trigger; and obtain a fresh-session technical review.

## 11. Automated acceptance tests

Validate source metadata, URL reachability, age rules, primary-source coverage, contradiction log, license fields, named versions, and explicit conclusions. Fail on unsupported recommendations, missing owner-region handling, generic “latest” claims, or a learning resource without a vetting record.

## 12. Human validation

Not applicable — the owner is not asked to validate technical research. P08-S002 asks only whether the selected learning material is usable.

## 13. Idempotency and rollback

Repeated research preserves prior citations and appends superseding evidence. Rollback restores the prior document and leaves a reasoned supersession record.

## 14. Required evidence

evidence/P08-S001/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, sources.json, contradictions.json, and learning-material-vetting.json.

## 15. Definition of done

The baseline is current, reproducible, source-backed, independently reviewed, and provides explicit inputs to P08-S002 and P08-S003.

## 16. Pause-safe boundaries

Update evidence/P08-S001/checkpoint.json after each source family with claims accepted, unresolved contradictions, checked-at times, and exact next query. Pause only between source families.
