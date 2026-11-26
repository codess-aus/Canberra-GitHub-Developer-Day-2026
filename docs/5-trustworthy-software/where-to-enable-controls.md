---
title: "Where to enable controls"
chapter: 5
hero: "5.23 switch.png"
hero_alt: "Slide listing where to enable GitHub security configurations, AI Scan, agentic autofix, cloud agent checks, Azure DevOps Advanced Security, Azure DevOps Autofix and Codename MDASH."
thumb: "thumbs/5-23-switch.webp"
summary: "Find the documentation and settings for the controls discussed in this chapter."
---

??? note "Text version of this slide"

    The slide points to organisation security configurations, AI Scan settings, enterprise agentic autofix policy, cloud agent checks, Azure DevOps security settings and MDASH onboarding.

## Before switching features on

Start with the documentation for the specific product and platform. Check licensing, enterprise and organisation policies, repository permissions, supported languages, data handling and the expected cost of scans or agent usage. A feature being allowed at enterprise level does not necessarily mean it is enabled in a repository.

For organisation-owned repositories, GitHub's AI Scan announcement describes organisation-level enablement after the enterprise policy is allowed. The slide's repository-settings route applies to repositories owned by personal accounts; check the current Docs for the applicable controls.

Copilot cloud agent's documented security validation is enabled by default for its own work; it does not replace repository-wide scanning. Azure DevOps Autofix is a separate preview workflow that requires configured scanning and a supported alert.

## Further reading

- [Security configurations](https://docs.github.com/en/code-security/concepts/security-at-scale/organization-security) (GitHub Docs). Organisation-wide setup.
- [AI Scan for repositories](https://docs.github.com/en/code-security/concepts/code-scanning/ai-scan-for-repositories) (GitHub Docs). Repository scan prerequisites and policy.
- [Agentic autofix](https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/) (GitHub Changelog). Remediation workflow.
- [Copilot cloud agent security](https://docs.github.com/en/copilot/concepts/agents/coding-agent/risks-and-mitigations) (GitHub Docs). Built-in validation.
- [Advanced Security for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features?view=azure-devops) (Microsoft Learn). Azure Repos setup.
- [Copilot Autofix for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-autofix?view=azure-devops) (Microsoft Learn). Preview setup.
- [Codename MDASH onboarding](https://learn.microsoft.com/en-us/security-exposure-management/ai-code-security-onboarding) (Microsoft Learn). Defender and Foundry prerequisites.
