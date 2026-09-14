# P08-S002: Learn practical agent design and boundaries

| Property | Value |
|---|---|
| Story ID | P08-S002 |
| Phase | P08 — Practical Personal Agents |
| Sequence | 2 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P08-S001 |
| Unlocks | P08-S003 |
| Preferred route | Interface: Open WebUI or browser lesson with goagentic evidence capture; Provider: controller-selected value cloud model; Model class: teaching; Effort: medium; Fallback: alternate vetted resource from P08-S001. |
| Research freshness | Use only P08-S001-vetted resources still current at lesson time; recheck changed pages and videos within 24 hours. |

## 1. User story

As the owner, I want focused training on the exact personal-agent choices I will operate so I can make informed subjective decisions without learning unrelated framework internals.

## 2. Bounded objective

Deliver a 60–90 minute, pauseable module at docs/learning/p08/P08-S002-practical-personal-agents.md covering agent versus chatbot, graph state, tools/skills/RAG, trust boundaries, guardrails, privacy, citations, model tradeoffs, and escalation behavior.

## 3. Learning objective

The owner can explain what each layer controls, identify a tool request that requires approval, distinguish a thread checkpoint from durable memory, critique one unsafe agent response, and choose whether a proposed personal-agent interaction feels appropriate.

## 4. Current research requirements

Revalidate the selected official pages, short concept video, and hands-on video. Substitute material if it is obsolete, inaccessible, poorly rated, promotional without evidence, or inconsistent with the P08-S001 baseline.

## 5. Preconditions and unlock conditions

P08-S001 is Done and its resource vetting passes. The lesson packet includes time estimate, objectives, links, exercises, answer key, glossary, and pause points.

## 6. In scope

Project-specific concepts; a diagram of Open WebUI to LangGraph to Ollama/tools/RAG/MLflow; examples for all five agents; crisis/medical/financial boundaries; prompt-injection exercise; privacy and memory choices; short knowledge check; and owner reflection.

## 7. Out of scope and prohibited changes

No general VS Code, Python, container, psychotherapy, medicine, investing, or LangGraph course; no implementation; no technical review assigned to the owner; and no pass based only on watching a video.

## 8. Privilege and human approval

No privileged action. The owner controls pacing and may pause or repeat any section.

## 9. Risk rationale

Low: education only; the gate prevents implementation before the owner understands operational boundaries.

## 10. Execution contract

Present concepts in short sections; demonstrate one synthetic conversation; run the exercises; give immediate corrective feedback; record only completion and owner-authored notes; and ask the owner to attest understanding or request more explanation.

## 11. Automated acceptance tests

Validate lesson structure, resource vetting, all five objective mappings, answer-key completeness, time budget, accessibility, and absence of implementation side effects. Score the knowledge check, but do not manufacture owner answers.

## 12. Human validation

The owner completes the exercises and explicitly records “understood,” “needs reinforcement,” or “skip—already understood” for each module. A skip requires a short knowledge check, not redundant training.

## 13. Idempotency and rollback

Reruns preserve completion evidence and reopen only changed or failed objectives. Rollback removes generated progress artifacts without changing implementation state.

## 14. Required evidence

evidence/P08-S002/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, module-progress.json, knowledge-check.json, and owner-attestation.md.

## 15. Definition of done

Every objective is completed or validly skipped, gaps are remediated, the owner attests to the boundaries, and P08-S003 is unlocked.

## 16. Pause-safe boundaries

Update evidence/P08-S002/checkpoint.json at each module boundary with completion, unresolved questions, and exact resume section. Never infer completion after interruption.
