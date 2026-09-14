# P09-S003: Learn the selected memory framework and concepts

| Property | Value |
|---|---|
| Story ID | P09-S003 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 3 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P09-S002 |
| Unlocks | P09-S013 |
| Preferred route | Interface: browser/Open WebUI lesson through goagentic; Provider: controller-selected value cloud model; Model class: teaching; Effort: medium; Fallback: alternate P09-S001-vetted resource. |
| Research freshness | Official selected-framework docs and vetted concept/hands-on videos checked within 24 hours. |

## 1. User story
As the owner, I want focused training on the memory system I will actually operate before it is deployed.
## 2. Bounded objective
Deliver docs/learning/p09/P09-S003-durable-memory.md as a 60–90 minute pauseable module with a synthetic retain/review/recall/correct/delete exercise.
## 3. Learning objective
The owner can distinguish thread context, candidate, durable ledger, projection, and RAG; explain why review is mandatory; identify poisoning; and use review, correction, deletion, disable, and restore controls.
## 4. Current research requirements
Vet one short conceptual and one thorough hands-on video plus official docs for recency, ratings/authority, exact selected version, accessibility, and technical accuracy.
## 5. Preconditions and unlock conditions
P09-S002 is Done. The lesson reflects the accepted ADR and contains objectives, diagram, glossary, exercises, answer key, time boxes, and pause points.
## 6. In scope
Project-specific memory concepts, selected framework, privacy, provenance, conflicts, retention, restricted data, failure behavior, owner inbox, and safe operating actions.
## 7. Out of scope and prohibited changes
No general database/AI course, implementation, private memory, technical certification by the owner, or pass based only on watching videos.
## 8. Privilege and human approval
No privilege. The owner controls pacing and may use prior-learning credit only with an evidence-linked retention and delta check.
## 9. Risk rationale
Low: education and synthetic exercises only.
## 10. Execution contract
Teach in short modules; run synthetic examples; provide feedback; record only genuine answers and completion; allow “needs reinforcement”; and block deployment until all objectives pass or are validly credited.
## 11. Automated acceptance tests
Validate resource vetting, version alignment, every objective/exercise/answer mapping, time/accessibility, and no mutation. Never fabricate owner responses.
## 12. Human validation
The owner completes or validly skips each module, performs the exercise, and attests understanding or requests reinforcement.
## 13. Idempotency and rollback
Reruns retain completed unchanged modules and reopen only deltas/failures. Rollback removes learning progress only.
## 14. Required evidence
evidence/P09-S003/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, learning-material-vetting.json, module-progress.json, knowledge-check.json, and owner-attestation.md.
## 15. Definition of done
All objectives are demonstrated, owner evidence is genuine, current selected-framework material is used, and P09-S013 is unlocked.
## 16. Pause-safe boundaries
Update evidence/P09-S003/checkpoint.json at every module boundary with exact resume point; never infer completion after interruption.
