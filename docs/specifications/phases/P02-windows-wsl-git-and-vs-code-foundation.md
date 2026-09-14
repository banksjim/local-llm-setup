# P02: Windows, WSL, Git, and VS Code Foundation

**Depends on:** P01  
**Required outcome:** A protected Ubuntu WSL2 development environment with repeatable toolchains, VS Code integration, and durable credentials.  
**Status:** Planned

## Gate

The phase activates only after its dependencies are accepted and the owner authorizes its first story through the current controller policy. Research and design may occur earlier, but implementation cannot cross this gate.

Before the first P02 mutation, the controller presents one privileged-phase preview covering the H-drive directories, WSL distribution creation or relocation, Ubuntu security profile, toolchain installation, native-Linux GitHub authentication, VS Code integration, and controller migration. One owner approval authorizes only those named, revision-pinned, reversible operations for P02. Later elevation prompts, browser authentication, learning evidence, and acceptance steps still require the owner to act, but they are not repeated approvals of unchanged scope. Any material scope, risk, or target change invalidates the phase authorization.

## Fixed phase boundaries and planned artifacts

- Dedicated WSL distribution name: `AI-Workbench`.
- Approved host root: `H:\ai`; the activation packet may not relocate it without a design-change story.
- Planned WSL storage parent: `H:\ai\wsl\AI-Workbench`; the exact VHDX mechanism is selected from current Microsoft-supported procedures in P02-S001.
- Linux repositories and agent workspaces live beneath the dedicated Linux user's home, not `/mnt/c` or `/mnt/h`.
- Windows drives are not automatically mounted into `AI-Workbench`; Windows executable interoperability is disabled unless P02 research proves a narrower compatible mechanism and the owner accepts a design change.
- Windows VS Code initiates the remote connection; extensions and language servers that operate on code run in `AI-Workbench`.
- Windows and Ubuntu remain separate credential stores. Ubuntu authentication is created natively and is available to processes running as the dedicated Linux user; Windows roaming token files are never copied or mounted.
- Reusable, idempotent host operations live under `operations/windows/p02/`; Ubuntu operations live under `operations/ubuntu/p02/`; verification and rollback tests live under `tests/p02/`. P10 composes these accepted operations rather than reimplementing them.

## Story sequence

| Seq. | Story | Step | Risk |
|---:|---|---|---|
| 1 | [P02-S001: Refresh Windows and WSL foundation guidance](../../stories/P02/P02-S001-refresh-windows-and-wsl-foundation-guidance.md) | Research | Low |
| 2 | [P02-S002: Learn the Windows and WSL trust boundary](../../stories/P02/P02-S002-learn-the-windows-and-wsl-trust-boundary.md) | Learning | Low |
| 3 | [P02-S003: Verify human-installed prerequisites](../../stories/P02/P02-S003-verify-human-installed-prerequisites.md) | Human Validation | Medium |
| 4 | [P02-S004: Create the H drive data layout](../../stories/P02/P02-S004-create-the-h-drive-data-layout.md) | Implementation | High |
| 5 | [P02-S005: Create and locate the dedicated Ubuntu distribution](../../stories/P02/P02-S005-create-and-locate-the-dedicated-ubuntu-distribution.md) | Implementation | Critical |
| 6 | [P02-S006: Harden Ubuntu mounts and interoperability](../../stories/P02/P02-S006-harden-ubuntu-mounts-and-interoperability.md) | Implementation | Critical |
| 7 | [P02-S007: Install Ubuntu baseline and language toolchains](../../stories/P02/P02-S007-install-ubuntu-baseline-and-language-toolchains.md) | Implementation | High |
| 8 | [P02-S008: Configure Git and GitHub authentication in Ubuntu](../../stories/P02/P02-S008-configure-git-and-github-authentication-in-ubuntu.md) | Implementation | High |
| 9 | [P02-S009: Install and configure VS Code WSL development](../../stories/P02/P02-S009-install-and-configure-vs-code-wsl-development.md) | Implementation | High |
| 10 | [P02-S010: Install the approved VS Code extension baseline](../../stories/P02/P02-S010-install-the-approved-vs-code-extension-baseline.md) | Implementation | Medium |
| 11 | [P02-S011: Migrate goagentic canonical runtime to Ubuntu](../../stories/P02/P02-S011-migrate-goagentic-canonical-runtime-to-ubuntu.md) | Implementation | High |
| 12 | [P02-S012: Perform foundation human acceptance](../../stories/P02/P02-S012-perform-foundation-human-acceptance.md) | Human Validation | Critical |

## Completion

The phase is complete only when every non-superseded story is Done, required human evidence is genuine, independent review findings are resolved, rollback evidence exists, and the phase outcome is demonstrated on the reference workstation.
