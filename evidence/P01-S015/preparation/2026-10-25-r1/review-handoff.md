# Fresh cross-provider implementation review handoff

Status: prepared request; **not an independent review result**. Do not run this against nonexistent implementation or mark the gate passed from the author's self-checks.

After P01-S015's bounded operation exists and synthetic tests/rehearsal have passed, use a fresh Claude Code session with **claude-sonnet-5-5 / Medium**. Confirm authentication/model availability without displaying credentials. Do not install, refresh authentication, purchase usage or substitute a prohibited model silently.

Provide the reviewer the pinned authority documents, this activation packet and phase preview, the actual implementation diff, exact test outputs, synthetic failure/rollback evidence, and observed preflight facts. Withhold author conclusions. The reviewer inspects and reports findings; it does not rewrite the work or operate GitHub.

Required review focus:

- Private owner/Project identity, exact canonical fields/options and both view configurations.
- 137-story key reconciliation across pagination, uncertain responses, partial field assignment and reruns.
- Exactly one current-story public issue conversion with a sanitized payload; no conversion of future stories.
- Explicit approval/hash binding, single-writer manual lock, clean-worktree boundary and checkpoints before external writes.
- Correct Windows PowerShell 5.1 argument/JSON handling, no credentials in output/files, no newly installed dependency.
- No unowned deletion or overwrite, no blanket stale-lock removal, preserved approval/event/review history, whole-Project deletion refused.
- Exact fixture coverage, nonzero assertions, live checks still pending rather than claimed, and owner evidence never fabricated.

Record findings in `evidence/P01-S015/execution/review.md` with reviewer provider/model/session, implementation commit, severity, concrete location, exploit/failure path, required correction and disposition. An author re-read is internal review only. Resolve material findings, rerun affected tests and obtain a new verdict where required before any external write.
