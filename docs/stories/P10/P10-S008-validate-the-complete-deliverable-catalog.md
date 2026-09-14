# P10-S008: Validate the complete deliverable catalog

| Property | Value |
|---|---|
| Story ID | P10-S008 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 12 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P10-S015 |
| Unlocks | P10-S009 |
| Preferred route | Controller-selected quality route with cross-provider review; local models may run deterministic checks after qualification. |
| Research freshness | Accepted source and version records from P10-S012 through P10-S015; recheck any item whose freshness window expired. |

## 1. User story

As the workstation owner, I want the complete installer, maintenance, documentation, diagram, and prompt catalog validated as one release candidate, so that missing or inconsistent deliverables are found before end-to-end acceptance.

## 2. Bounded objective

Validate the outputs of P10-S012 through P10-S015 against the master deliverable matrix without authoring missing content inside this testing story; failures create bounded correction work and block P10-S009.

## 3. Learning objective

Not applicable — this testing story verifies already taught and documented workflows and introduces no separate owner-operated concept.

## 4. Current research requirements

Use the accepted source and version records from the four producing stories. If any declared freshness window expired, recheck only the affected claims before validation; otherwise no new product selection is permitted.

## 5. Preconditions and unlock conditions

P10-S015 and its producing chain are accepted; the release-candidate revision is fixed; the deliverable matrix, Git, controller, route, lease, and freshness checks pass.

## 6. In scope

Completeness, navigation, consistency, command validation, source freshness, platform labeling, diagram validation, prompt inventory, terminology, privacy, and traceability across the complete deliverable set.

## 7. Out of scope and prohibited changes

Silently writing missing guides or scripts during testing, new architecture, workstation mutation, waiving failed checks, public/private data movement, and declaring implementation evidence from documentation alone.

## 8. Privilege and human approval

Not applicable — validation is read-only against the versioned release candidate and sanitized evidence. Any discovered fix executes under its producing story's approval rules.

## 9. Risk rationale

The tests are read-only, but a false pass could expose the owner to unsafe installation or recovery instructions across the entire workstation. Independent review and failure-on-omission make High risk appropriate.

## 10. Execution contract

Freeze the candidate revision; generate the expected catalog from the master requirements; compare expected and actual artifacts; run every applicable static and safe command check; emit actionable failures; and make no repair in the reviewer context.

## 11. Automated acceptance tests

The PowerShell installer and every maintenance entry point pass parsing, analysis, help, dry-run, fixture idempotency, rollback-contract, exact-path, and secret checks. Every required guide, Mermaid diagram, model and usage table, integration instruction, and Codex prompt exists; links, commands, freshness metadata, terminology, and cross-document references validate.

## 12. Human validation

Not applicable — P10-S014 and P10-S015 contain usability checks, and P10-S011 performs final owner acceptance; this story is the independent automated catalog gate.

## 13. Idempotency and rollback

Repeated validation of the same revision produces the same result and never mutates workstation or deliverables. Rollback is removal or reversion of generated test evidence only.

## 14. Required evidence

Candidate revision; expected and actual catalog; source-freshness report; all test outputs; exclusions with rationale; defect list and disposition; secret and privacy scans; independent review verdict; and final pass/fail result.

## 15. Definition of done

The release-candidate catalog contains every required deliverable, all validations pass without waiver, defects are resolved through their owning stories, evidence is accepted, and P10-S009 is unblocked.

## 16. Pause-safe boundaries

Pause before the test run, between independent test groups, and after durable results. Restart the affected deterministic group after interruption; never merge partial passes into a final verdict.
