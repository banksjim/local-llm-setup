# P10-S002: Learn routine operation and incident boundaries

| Property | Value |
|---|---|
| Story ID | P10-S002 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 2 |
| Status | Planned |
| Step | Learning |
| Hold reason | Dependency |
| Risk | Low |
| Actor | Human + LLM |
| Dependencies | P10-S001 |
| Unlocks | P10-S003 |
| Preferred route | Interface: goagentic guided lesson in the owner’s chosen coding interface; Provider: controller-selected cloud provider; Model class: clear instructional; Effort: medium; Fallback: equivalent cloud assistant using the same committed lesson and scoring rubric. |
| Research freshness | Accepted P10-S001 pack and P01–P09 command/evidence interfaces checked within 7 days. |

## 1. User story
As the owner, I want focused operational training so I can recognize normal behavior, inspect health, and stop safely without learning unrelated platform internals.
## 2. Bounded objective
Create and complete `docs/learning/P10/routine-operations-and-incidents.md`, a 60–90 minute lesson using accepted P01–P09 operations—not final P10 runbooks that do not yet exist.
## 3. Learning objective
Explain Windows versus WSL versus container responsibility; demonstrate `goagentic next/status/pause/resume`; identify model/service health; interpret a sanitized log; distinguish update preview from apply; explain backup versus proven restore; and choose stop/escalate for ambiguous, destructive, credential, exposure, or data-loss conditions.
## 4. Current research requirements
Use the accepted P10-S001 baseline and actual accepted command help. Recheck changed UI labels or commands; do not teach a planned command as implemented.
## 5. Preconditions and unlock conditions
P10-S001 is Done; lesson, answer key, synthetic incident cards, and pass rubric are committed. Owner controls pacing and may pause without penalty.
## 6. In scope
Short concept sections, safe demonstrations, five scenario decisions, a command-location exercise, knowledge check, remediation loop, and personal quick-reference notes.
## 7. Out of scope and prohibited changes
No workstation mutation, destructive rehearsal, secret handling, exhaustive container/PowerShell education, technical certification, or final acceptance.
## 8. Privilege and human approval
The owner must genuinely complete the lesson; an LLM cannot supply or fabricate answers. No privileged approval is needed.
## 9. Risk rationale
Low: read-only learning with synthetic examples.
## 10. Execution contract
Teach one bounded concept at a time; require the owner to perform safe lookups and answer in their own words; score against the committed rubric; remediate only missed concepts; record no sensitive personal answer text.
## 11. Automated acceptance tests
Lesson lint confirms all seven objectives, five incident cards, expected/unsafe choices, stop conditions, current links, 60–90 minute estimate, scoring threshold, and retry path. Evidence schema rejects LLM-authored human completion.
## 12. Human validation
Owner achieves at least 80%, correctly stops all destructive/exposure scenarios, and locates the next/status/pause/resume instructions without this chat. Missed items are retaught and retested.
## 13. Idempotency and rollback
Reopening does not erase prior attempts. Only a new genuine attempt changes completion; Git reversion restores lesson content, not human history.
## 14. Required evidence
Commit the lesson and `evidence/P10-S002/activation.json`, `attempt.json`, `scenario-results.json`, `human-validation.md`, `remediation.json`, and `checkpoint.json`; store results, not sensitive free-form answers.
## 15. Definition of done
All objectives are covered, the owner passes the rubric and safety-critical scenarios, genuine evidence exists, and P10-S003 unlocks.
## 16. Pause-safe boundaries
Pause between modules or scenarios; resume at the next incomplete item from the checkpoint.
