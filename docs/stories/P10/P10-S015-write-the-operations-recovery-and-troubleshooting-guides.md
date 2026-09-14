# P10-S015: Write the operations, recovery, and troubleshooting guides

| Property | Value |
|---|---|
| Story ID | P10-S015 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 11 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P10-S014 |
| Unlocks | P10-S008 |
| Preferred route | Controller-selected quality route with cross-provider review of destructive and recovery instructions. |
| Research freshness | Current operational documentation and accepted local test evidence checked within 7 days. |

## 1. User story

As the workstation owner, I want tested tuning, troubleshooting, update, backup, restore, rollback, and uninstall guides, so that I can operate and recover the system safely when normal workflows fail.

## 2. Bounded objective

Write operational runbooks tied to the accepted maintenance commands and proven test evidence, with symptoms, diagnostics, stop conditions, escalation, expected results, and exact recovery boundaries.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P10-S002; this story consolidates previously taught operational workflows.

## 4. Current research requirements

Refresh official operational guidance for pinned components and use only accepted local measurements for workstation-specific claims. Record source dates, versions, commands, known limitations, and conflicts.

## 5. Preconditions and unlock conditions

P10-S014 and all P10 operational implementation stories are accepted; failure and recovery evidence exists; exact commands and targets are stable; Git, controller, route, and lease checks pass.

## 6. In scope

Performance tuning, health interpretation, common failures, diagnostic decision trees, safe log collection, update and migration, backup and restore, rollback, uninstall and retained data, emergency stop, and escalation guidance.

## 7. Out of scope and prohibited changes

Untested fixes, generic internet advice, destructive shortcuts, credential display, unsupported hardware tuning, automatic update scheduling, and workstation mutation while authoring documentation.

## 8. Privilege and human approval

Not applicable for documentation edits. Every documented privileged, destructive, restore, publication, or security-boundary action must visibly retain its own approval requirement.

## 9. Risk rationale

These instructions may be followed during failures and include high-impact recovery operations. They require exact-target safeguards, tested outcomes, prominent stop conditions, and cross-provider review.

## 10. Execution contract

Map each procedure to accepted commands and evidence; distinguish diagnosis from repair; begin with least-invasive checks; label privilege and data impact; provide expected outputs and abort criteria; and never invent a recovery step that was not tested or explicitly marked for human escalation.

## 11. Automated acceptance tests

Runbook inventory, command-to-implementation mapping, safe command validation, broken-link scan, symptom coverage, stop-condition presence, privilege/destructive warning checks, source freshness, secret scan, and evidence-link validation pass.

## 12. Human validation

The owner follows one benign troubleshooting scenario and locates the correct update, restore, and uninstall safeguards without using this chat.

## 13. Idempotency and rollback

Regeneration from unchanged evidence yields no semantic change. Git reversion restores the prior guides; documentation execution examples must themselves preserve the underlying operation's idempotency and rollback rules.

## 14. Required evidence

Runbook and symptom inventory; command/evidence mapping; source dates and versions; link, warning, command, freshness, and secret checks; review findings; changed-file list; and owner usability notes.

## 15. Definition of done

Every accepted operational workflow has a tested, discoverable runbook with safe diagnostics, explicit approvals, stop conditions, and recovery guidance; P10-S008 is unblocked.

## 16. Pause-safe boundaries

Pause between runbooks and after link/command validation and durable commits. Never leave a renamed guide or command with unresolved references.
