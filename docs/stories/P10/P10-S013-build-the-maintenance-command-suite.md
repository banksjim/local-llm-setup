# P10-S013: Build the maintenance command suite

| Property | Value |
|---|---|
| Story ID | P10-S013 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 9 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P10-S012 |
| Unlocks | P10-S014 |
| Preferred route | Controller-selected quality route with independent cross-provider review; qualified local model may implement bounded commands. |
| Research freshness | Current component health, update, backup, restore, and removal interfaces checked within 7 days. |

## 1. User story

As the workstation owner, I want a consistent maintenance command suite, so that routine health, start, stop, update preview, backup, restore, and removal tasks are safe and memorable.

## 2. Bounded objective

Implement separate discoverable maintenance entry points that wrap the accepted operational workflows without duplicating installer logic.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P10-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Refresh official interfaces for the installed versions within 7 days and record any changed health, lifecycle, backup, migration, or removal behavior.

## 5. Preconditions and unlock conditions

P10-S012 is accepted; P10-S003 through P10-S007 define the approved operations; Git, controller state, route, lease, and research checks pass.

## 6. In scope

Status, health, start, stop, log collection, update preview, backup, restore, rollback, uninstall preview, retained-data choices, help, structured output, and shared modules.

## 7. Out of scope and prohibited changes

Automatic unapproved updates, scheduled unattended mutation, new backup destinations, secret output, broad deletion, installer duplication, and GUI development.

## 8. Privilege and human approval

Required for live commands that elevate privileges, restore data, remove components, or cross a separately defined approval boundary; read-only health and preview commands require no additional approval.

## 9. Risk rationale

Most commands are bounded, but restore, rollback, update, and removal can affect multiple services or data. Each command must preserve the risk and approval rules of the underlying accepted workflow.

## 10. Execution contract

Every command supports help and preview where meaningful, delegates to one authoritative implementation, validates exact targets, reports intended and actual changes, stops on ambiguity, and writes sanitized evidence.

## 11. Automated acceptance tests

Command discovery, help, parameter validation, read-only status, structured output, no-op behavior, mocked success/failure, privilege rejection, exact-target enforcement, secret scan, and delegation-without-duplication tests pass for every entry point.

## 12. Human validation

The owner runs help, status, and one safe preview from a fresh shell and confirms the commands are understandable without this chat.

## 13. Idempotency and rollback

Read-only and preview commands never mutate. Repeated mutation commands no-op or reconcile safely, and each delegates to the tested rollback contract of its owning operation.

## 14. Required evidence

Command catalog; ownership mapping; source revisions; current interface sources; test matrix and outputs; privilege and target checks; secret scan; no-op results; review verdict; and owner usability result.

## 15. Definition of done

Every accepted maintenance workflow has one tested, documented entry point with correct safety behavior and no duplicate implementation; P10-S014 is unblocked.

## 16. Pause-safe boundaries

Pause between commands and at the safe boundaries defined by each delegated workflow. Never pause during an atomic restore, migration, or replacement.
