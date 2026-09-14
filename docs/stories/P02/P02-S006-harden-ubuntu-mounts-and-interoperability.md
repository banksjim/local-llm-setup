# P02-S006: Harden Ubuntu mounts and interoperability

| Property | Value |
|---|---|
| Story ID | P02-S006 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 6 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P02-S005 |
| Unlocks | P02-S007 |
| Preferred route | Interface: interactive Codex CLI with Ubuntu and Windows shells; Provider: OpenAI; Model class: architecture and security implementation; Effort: high; Fallback: Claude Code with an Anthropic architecture/security model using the same accepted policy; P02 phase authorization and isolated rollback rehearsal are mandatory. |
| Research freshness | Current Microsoft WSL configuration and networking docs checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to apply the approved no-automount and no-Windows-executable profile while retaining required NAT networking, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Apply the approved no-automount and no-Windows-executable profile while retaining required NAT networking.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P02-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current Microsoft WSL configuration and networking docs checked within 7 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P02-S005. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Implement preview/apply/verify/rollback operations under `operations/ubuntu/p02/` for the accepted `/etc/wsl.conf` security profile in `AI-Workbench`: disable automatic Windows-drive mounting and Windows executable interoperability, preserve required localhost or NAT networking, restart only the target distribution, and test access denials plus required network reachability.

## 7. Out of scope and prohibited changes

Changing global WSL settings or other distributions; mounting `C:` or `H:`; exposing the container socket; blocking required Windows-to-WSL VS Code startup without a documented resolution; changing Windows Firewall; enabling systemd unless selected by current P02 research; and weakening the boundary merely for convenience.

## 8. Privilege and human approval

Required human participation — the existing P02 phase authorization covers the accepted security profile. The owner observes restart and connectivity checks and performs acceptance evidence; a changed mount, interoperability, networking, or security design requires a new phase preview and authorization.

## 9. Risk rationale

The story is Critical because it defines the host/agent security boundary and an error can either expose Windows data and executables or make the environment unusable. It requires the existing P02 authorization, exact backup, isolated config validation, restart recovery, owner validation, and cross-provider security review.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. Windows drives and executables are unavailable, Ubuntu networking works, and rollback restores the prior configuration.

## 11. Automated acceptance tests

Windows drives and executables are unavailable, Ubuntu networking works, and rollback restores the prior configuration. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

The owner confirms that Windows-initiated VS Code access and required networking still work while Windows drives and executables remain unavailable inside `AI-Workbench`.

## 13. Idempotency and rollback

Applying the same normalized configuration twice changes nothing. Before replacement, save the exact prior `wsl.conf` and distribution state. Rollback restores that file, terminates only `AI-Workbench`, and verifies its prior mount, interop, networking, and VS Code-connectivity state.

## 14. Required evidence

Current Microsoft and VS Code requirements; configuration and operation hashes; pre-change file/state backup; P02 authorization; preview; syntax validation; post-restart mount and Windows-executable denial tests; required network and Windows-initiated VS Code checks; repeat result; rollback rehearsal; owner validation; and cross-provider verdict.

## 15. Definition of done

Inside `AI-Workbench`, Windows drives are absent and Windows executables cannot launch; required package/network access and Windows-initiated VS Code connectivity still work; other distributions are unchanged; rerun and rollback pass; and P02-S007 is unblocked.

## 16. Pause-safe boundaries

Pause before replacing `wsl.conf`, after syntax validation, after terminating only `AI-Workbench`, after restart, and after each boundary check. Never leave an unverified configuration as accepted state.
