# P09-S012: Perform memory owner acceptance

| Property | Value |
|---|---|
| Story ID | P09-S012 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 13 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Approval |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P09-S011 |
| Unlocks | P10-S001 |
| Preferred route | Interface: Open WebUI plus the P09-S006 local inbox operation; Provider: accepted local Ollama profiles; Model class: P09-qualified runtime with value cloud facilitator only for guidance; Effort: owner-paced; Fallback: disable capture/recall and restore the P08 stateless life planner. |
| Research freshness | Installed UI/runtime instructions and P09-S010/S011 results checked within 24 hours; no new product claim is introduced. |

## 1. User story
As the owner, I want guided acceptance so I can decide whether reviewed memory is transparent, useful, controllable, and comfortable.
## 2. Bounded objective
Run one owner-paced life-planning memory cycle—capture, review, edit/approve/reject, recall, correct, restrict, export, delete, restart, disable—and record genuine decisions at evidence/P09-S012/owner-acceptance.md.
## 3. Learning objective
The owner can see memory status/provenance, operate the inbox, prevent capture, correct/delete/export memory, recognize stateless fallback, and disable memory.
## 4. Current research requirements
Recheck only version-specific UI steps and accepted safety/resource links; route any design change back to the owning story.
## 5. Preconditions and unlock conditions
P09-S011 is Done; no High/Critical finding remains. The full sequence, cleanup, and rollback pass an isolated synthetic rehearsal. Packet shows exact versions, disclosures, known limits, safe prompts, expected results, and choices.
## 6. In scope
Synthetic plus optional owner-chosen low-sensitivity memory; capture-off/on; `do not learn`; candidate inbox; approve/edit/reject/defer; recall provenance; correction; Restricted denial; export manifest; scoped deletion; restart; outage/stateless disclosure; disable; and accept/reject/needs-change.
## 7. Out of scope and prohibited changes
No technical certification, forced sensitive disclosure, crisis/medical/financial memory, bulk approval, cloud transfer, hidden capture, other P08 agent, unsafe destructive live test, or inferred consent.
## 8. Privilege and human approval
This is owner participation under the revision-bound P09 authorization. Capture and recall become enabled for personal use only after explicit final acceptance; silence is never consent.
## 9. Risk rationale
Critical: this authorizes persistent personal context in ongoing use. Revision-bound authorization, isolated rehearsal, cross-provider review, and genuine owner acceptance are mandatory.
## 10. Execution contract
Present plain-language results; verify stateless baseline/rollback; guide one action at a time; state expected privacy effect; stop on discomfort; record decision only; clean test data; route defects to smallest owning story; never fabricate observations.
## 11. Automated acceptance tests
Before each step verify exact hashes, private binding, policy, hard-suite pass, trace redaction, backup, and rollback. Afterward prove ledger/action/audit match owner choices, deleted content is absent, disabled memory makes no calls, and no private value entered Git/evidence.
## 12. Human validation
The owner rates usefulness, accuracy, transparency, inbox clarity, control, speed, and comfort; demonstrates correction/delete/disable; and records accept, reject, or needs change. No technical judgment is required.
## 13. Idempotency and rollback
Rerun preserves decisions and retests changed behavior only. Rejection atomically disables capture/recall and restores the accepted P08 stateless preset while retaining owner-accessible export/deletion controls.
## 14. Required evidence
evidence/P09-S012/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, owner-acceptance.md, action-outcomes.json, privacy-cleanup.json, disable-results.json, and routing-outcomes.json.
## 15. Definition of done
The owner explicitly accepts memory or it remains disabled with corrections routed; controls are demonstrated; evidence is genuine and private-value-free; P10 unlocks only after acceptance.
## 16. Pause-safe boundaries
Update evidence/P09-S012/checkpoint.json after each owner action with decision, enabled state, cleanup, and exact next step; unaccepted memory remains disabled during every pause.
