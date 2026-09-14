# P02: Windows, WSL, Git, and VS Code Foundation

**Depends on:** P01  
**Required outcome:** A protected Ubuntu WSL2 development environment with repeatable toolchains, VS Code integration, and durable credentials.  
**Status:** Planned

## Gate

The phase activates only after its dependencies are accepted and the owner authorizes its first story through the current controller policy. Research and design may occur earlier, but implementation cannot cross this gate.

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

