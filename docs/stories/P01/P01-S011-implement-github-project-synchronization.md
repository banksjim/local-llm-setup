# P01-S011: Implement GitHub Project synchronization

| Property | Value |
|---|---|
| Story ID | P01-S011 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 12 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P01-S010 |
| Unlocks | P01-S012 |
| Preferred route | Interface: Codex CLI plus authenticated GitHub CLI; Provider: OpenAI; Model class: architecture-capable integration; Effort: medium; Fallback: Claude Code plus GitHub CLI with an Anthropic architecture-capable model at medium effort; live mutation must remain inside the P01 phase authorization and receive cross-provider review. |
| Research freshness | Current GitHub Projects GraphQL and gh documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to replace bootstrap Project maintenance with tested controller synchronization while preserving local authority and manual conflict detection, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Automate reconciliation of the Project created by P01-S015, including story fields, lifecycle transitions, activation-time issue creation or conversion, and evidence links, while preserving local authority and surfacing manual conflicts.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P01-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current GitHub Projects GraphQL and gh documentation checked within 7 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S010. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

Implement a GitHub Project reconciliation module in `goagentic/src/GitHubProject.psm1`, a versioned local field mapping, mock fixtures, preview/apply/verify/rollback commands, activation-time draft-to-issue behavior, and approved live tests against the Project created by P01-S015.

## 7. Out of scope and prohibited changes

Making GitHub the authority over Git, deleting unknown fields, items, or views, force-overwriting manual edits, creating issues for non-Ready stories, exposing secrets, changing Project visibility, or mutating any Project other than the recorded P01-S015 target.

## 8. Privilege and human approval

No new approval for the unchanged target — the exact Project and reconciliation operations are covered by the P01 phase authorization. Authentication renewal or a changed Project, visibility, field set, or deletion requires a new preview and owner action.

## 9. Risk rationale

The story is High risk because it performs authenticated bulk external mutations and a duplicate or destructive reconciliation could clutter or damage the owner's Project. Stable keys, dry-run previews, bounded retries, preserved unknown state, integration tests, and owner-approved live mutation are required.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the currently accepted P01 mutation guard—the bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the guard; and route to review or human validation. Mock and approved live tests cover create, update, outage, retry, and conflicting remote edits.

## 11. Automated acceptance tests

Mock and approved live tests cover create, update, outage, retry, and conflicting remote edits. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

The owner inspects the approved live Project after reconciliation and confirms that manual content, visibility, and non-target items are unchanged; this is verification within the existing P01 authorization, not a new approval.

## 13. Idempotency and rollback

Reconciliation keys on Project ID and Story ID; an unchanged rerun proposes zero mutation. Before apply, export the targeted field and item values. Rollback restores only values changed by the recorded operation or removes items it created; it never deletes the Project or unknown content without a separate owner decision.

## 14. Required evidence

Story revision; current GitHub documentation and API or CLI versions; target Project identity; field mapping; sanitized mutation preview; mock and live create, update, conflict, and outage results; expected-versus-actual counts; duplicate scan; unchanged rerun; rollback inventory and rehearsal; and cross-provider verdict.

## 15. Definition of done

Mock and owner-approved live reconciliation agree; each story has one mapped item; only Ready stories become issues; manual conflicts are surfaced rather than overwritten; outage retry creates no duplicates; unchanged rerun is empty; and P01-S012 is unblocked.

## 16. Pause-safe boundaries

Pause before any live API mutation, after the remote inventory, after each resumable keyed batch, after conflict reconciliation, and after verification. Never retry an unkeyed request after interruption.
