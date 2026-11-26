---
title: "Five actions to take"
chapter: 5
hero: "5.23 5 Things.png"
hero_alt: "Slide summarising five actions: fix quickly, scan code, protect secrets and the supply chain, govern agents, and make security the default."
thumb: "thumbs/5-23-5-things.webp"
summary: "Turn the session into a prioritised security improvement plan."
---

??? note "Text version of this slide"

    Five actions: fix quickly, scan your code, protect secrets and the supply chain, govern AI agents, and make security the default.

## Put the pieces together

1. **Prioritise and fix.** Use severity, reachability and production context to focus the backlog; use campaigns and proposed fixes where they help.
2. **Scan owned code.** Combine suitable CodeQL and AI Scan coverage with deeper assessments for important repositories.
3. **Protect secrets and dependencies.** Prevent exposure at push, review dependency changes, harden builds and use short-lived credentials.
4. **Govern agents.** Identify owners, limit permissions, log activity and require appropriate review of consequential actions.
5. **Make the baseline repeatable.** Apply configurations and merge policies to new as well as existing repositories.

These are capabilities to configure and operate, not guarantees that every repository is automatically protected. Start with a manageable set of repositories and measure coverage, time to remediate and exceptions.

## Further reading

- [GitHub security documentation](https://docs.github.com/en/code-security) (GitHub Docs). Configuration and remediation guidance.
- [GitHub Advanced Security for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features?view=azure-devops) (Microsoft Learn). Equivalent controls in Azure Repos.
- [Microsoft Secure Now](https://aka.ms/securenow) (Microsoft). Wider security guidance.
