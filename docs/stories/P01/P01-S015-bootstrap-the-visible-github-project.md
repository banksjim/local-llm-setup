# P01-S015: Bootstrap the visible GitHub Project

| Property | Value |
|---|---|
| Story ID | P01-S015 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 1 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Approval |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | Not applicable — this is the first program story. |
| Unlocks | P01-S001 |
| Preferred route | Interface: authenticated GitHub CLI from the Windows repository shell guided by Codex; Provider: OpenAI; Model class: standard integration; Effort: medium; Fallback: Claude Code with an Anthropic general-purpose model and the same GitHub CLI; owner approval is required immediately before external creation. |
| Research freshness | Current official GitHub Projects and GitHub CLI documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want a personal GitHub Project containing the complete approved backlog before implementation proceeds, so that I can see the program, its sequence, and its current holds from the beginning.

## 2. Bounded objective

Create one personal GitHub Project owned by `banksjim`, configure the canonical fields and views, add every approved story as a draft Project item linked to its repository document, and record the Project URL. Keep draft items lightweight; create or convert a repository issue only when a story becomes Ready unless current GitHub capabilities require a documented alternative.

## 3. Learning objective

Show the owner how to open the Project, read Phase, Story ID, Status, Step, Hold reason, Risk, Owner action, and Evidence link, and recognize which single item is actionable.

## 4. Current research requirements

Check current official GitHub Projects, draft-item, field, view, visibility, and GitHub CLI or GraphQL documentation within 7 days. Confirm live authentication and required scopes without displaying credentials. Record access dates, direct links, relevant limitations, and any necessary deviation from the draft-item approach.

## 5. Preconditions and unlock conditions

The written specification set passes local structural validation; the repository remote is confirmed; GitHub CLI authentication and Project scopes pass a sanitized read-only check; and the owner approves the complete revision-bound P01 phase preview, including these external mutations. This story unlocks P01-S001 only after the Project URL and reconciliation inventory are recorded.

## 6. In scope

One personal Project; selected private visibility unless the owner explicitly chooses public; canonical fields and useful table/board views; one draft item per approved story; phase, sequence, workflow, risk, owner-action, and document-link metadata; a sanitized local bootstrap record; and a versioned dependency-free PowerShell bootstrap operation under `goagentic/bootstrap/` with preview, apply, verify, and story-owned rollback modes using authenticated GitHub CLI calls.

## 7. Out of scope and prohibited changes

Controller automation, workstation installation, bulk repository issues for stories that are not Ready, organization-owned Projects, public visibility without explicit approval, secrets in Project content, and changing story requirements to fit GitHub limitations.

## 8. Privilege and human approval

Required phase authorization — the P01 preview names the exact Project owner, title, visibility, fields, views, item count, and controller mutation set. The owner authorizes that bounded phase once before creation; authentication or scope renewal is a separate human action, while any material preview change requires reauthorization.

## 9. Risk rationale

The story is High risk because it creates and updates many externally hosted records through authenticated GitHub access. It is reversible, but a partial import or duplicate rerun could create widespread clutter; therefore preview, stable item keys, reconciliation, rollback evidence, and independent review are mandatory.

## 10. Execution contract

Use the P01 bootstrap protocol defined by `SYS-CTL`, because the controller does not yet exist. Export or record the pre-change Project inventory, preview all mutations, use Story ID as the stable deduplication key, create or reconcile rather than blindly append, stop on authentication or schema drift, and write the resulting URL and item mapping to durable sanitized evidence.

## 11. Automated acceptance tests

Verify exactly one target Project, all canonical fields, the required views, exactly one Project item per approved non-superseded story ID, working document links, correct Phase and Sequence values, no duplicate story IDs, no secrets, and an idempotent dry rerun that proposes no duplicate creation.

## 12. Human validation

The owner opens the recorded Project URL, confirms the complete backlog is visible and understandable, locates the one next story, and confirms no workstation implementation has started.

## 13. Idempotency and rollback

A rerun reconciles by Project identity and Story ID and creates no duplicates. Before mutation, capture enough inventory to remove only story-owned fields, views, and items or delete the newly created Project after explicit owner approval; never delete a pre-existing Project.

## 14. Required evidence

Official sources and access dates; sanitized authentication result; approved mutation preview; Project owner, title, visibility, number, and URL; field/view inventory; expected and actual item counts; Story ID mapping; duplicate and secret scans; idempotent rerun result; rollback plan; and owner validation.

## 15. Definition of done

The owner can open the personal GitHub Project URL and see one correctly classified item for every approved story; validations and owner review pass; evidence is durable; and P01-S001 is the only story unblocked.

## 16. Pause-safe boundaries

Pause before external creation, after the Project shell exists, after fields and views exist, after each resumable import batch, after reconciliation, and after evidence is committed. On interruption, inventory remote state before continuing; never restart with an unkeyed bulk append.
