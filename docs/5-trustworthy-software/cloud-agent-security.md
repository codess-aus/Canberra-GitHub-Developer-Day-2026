---
title: "Security checks for Copilot cloud agent"
chapter: 5
hero: "5.20 secure agents.png"
hero_alt: "Slide showing agents running code, dependency and secret checks on their changes and attempting fixes before committing."
thumb: "thumbs/5-20-secure-agents.webp"
summary: "Understand built-in validation and why agent output still needs review."
---

??? note "Text version of this slide"

    The slide shows security checks during agent work and attempts to fix discovered issues before committing.

## Built-in validation is a layer, not a guarantee

GitHub Docs says Copilot cloud agent checks generated code by default using CodeQL, checks newly introduced dependencies for malware and high or critical vulnerabilities, runs secret scanning and obtains a Copilot code review. It attempts to address issues before completing its pull request. This validation does not require a separate GitHub Secret Protection, Code Security or Advanced Security licence.

The session log records the analysis and actions. The agent remains subject to repository protections and required checks, and its changes still need review. GitHub documents an important branch exception: when the agent is invoked on an existing pull request it can write to that pull request's branch; otherwise it creates a `copilot/` branch.

The slide's general statements about agents and security should not be read as a guarantee that every provider or surface runs identical checks, or that generated code is vulnerability-free.

## Further reading

- [Risks and mitigations for GitHub Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/risks-and-mitigations) (GitHub Docs). Security validation, branch access and auditability.
- [About code scanning](https://docs.github.com/en/code-security/concepts/code-scanning/about-code-scanning) (GitHub Docs). Repository-level scanning that complements agent checks.
