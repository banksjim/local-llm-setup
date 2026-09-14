# P02-S008: Configure Git and GitHub authentication in Ubuntu

| Property | Value |
|---|---|
| Story ID | P02-S008 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 8 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P02-S007 |
| Unlocks | P02-S009 |
| Preferred route | Interface: interactive Codex CLI plus Ubuntu shell and browser device flow; Provider: OpenAI; Model class: security-aware systems guide; Effort: medium; Fallback: Claude Code with an Anthropic security-aware model using the same native-Linux credential boundary; the owner performs authentication. |
| Research freshness | Current GitHub CLI authentication and credential-storage docs checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to configure one durable Linux credential boundary usable by all Ubuntu repositories without copying Windows roaming tokens, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Configure one durable Linux credential boundary usable by all Ubuntu repositories without copying Windows roaming tokens.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P02-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current GitHub CLI authentication and credential-storage docs checked within 7 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P02-S007. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Create an idempotent managed Git-configuration and verification operation under `operations/ubuntu/p02/`; configure Git identity and the P02-S001-selected native-Linux credential storage for the dedicated Ubuntu user; perform owner-controlled GitHub device or browser authentication; configure GitHub CLI and Git to use that boundary for all Linux repositories; and verify access with a disposable private-or-public-safe test that exposes no token. Authentication entry and credential-store unlock remain manual.

## 7. Out of scope and prohibited changes

Copying or mounting Windows `%APPDATA%`, roaming GitHub tokens, `.git-credentials`, SSH private keys, or credential-manager files; storing a plaintext token in a repository or shell history; per-repository duplicate authentication; changing organization policy; and exposing repository names not needed for evidence.

## 8. Privilege and human approval

Required human participation — the owner completes the device or browser authentication and any credential-store unlock. The accepted P02 phase authorization covers configuration; the LLM never enters, reads, records, or approves credentials.

## 9. Risk rationale

The story is High risk because it creates a durable credential boundary and authenticated remote access. Credential entry is human-only; secret storage, filesystem permissions, history hygiene, least scopes, revocation, redacted evidence, and cross-provider security review are required.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. Clone, fetch, and push to an approved test repository works from CLI and VS Code; secrets do not appear in files or logs.

## 11. Automated acceptance tests

Clone, fetch, and push to an approved test repository works from CLI and VS Code; secrets do not appear in files or logs. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

The owner performs authentication, confirms the expected GitHub account and scopes without exposing them unnecessarily, and verifies that logout or revocation instructions are understandable.

## 13. Idempotency and rollback

A rerun recognizes valid authentication and correct Git configuration without requesting or writing a second credential. Rollback removes only managed Git configuration and invokes the documented logout/revocation path if the owner chooses; it never prints, copies, or commits the credential and preserves unrelated keys/configuration.

## 14. Required evidence

Official authentication and credential-storage sources; selected backend and threat tradeoffs; managed Git configuration diff; owner-performed authentication timestamp; sanitized `gh auth status`; secret location and permission check without content; clone/fetch/push-safe verification; shell-history and repository secret scans; rerun; revocation/rollback procedure; and cross-provider verdict.

## 15. Definition of done

Git and GitHub CLI work for repositories from the dedicated Ubuntu user through one native-Linux credential boundary; no Windows credential path is mounted or referenced; no secret appears in history, output, or Git; rerun creates nothing; and P02-S009 is unblocked.

## 16. Pause-safe boundaries

Pause before the trusted authentication prompt, after authentication status verifies, after managed Git configuration, and after remote tests. Never record, echo, or inspect credential content at a checkpoint.
