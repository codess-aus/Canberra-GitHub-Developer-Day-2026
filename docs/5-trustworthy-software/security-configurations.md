---
title: "Security configurations at scale"
chapter: 5
hero: "5.6 Turn it on.png"
hero_alt: "Slide: Turn it on everywhere, then enforce. Apply a baseline, tier and enforce configurations, set organisation defaults, and rank alerts using runtime context."
thumb: "thumbs/5-6-turn-it-on.webp"
summary: "Apply consistent security coverage without configuring every repository by hand."
---

??? note "Text version of this slide"

    Apply a baseline, use enforced configurations for different repository tiers, set organisation defaults, and use runtime context to prioritise alerts. Azure DevOps can enable protections at organisation, project or repository level.

## From opt-in to a managed baseline

Security configurations group feature settings so an organisation can apply them across repositories. The GitHub-recommended configuration is maintained by GitHub; custom configurations let an organisation select settings for different repository groups. Enforcement helps prevent individual repositories from silently drifting away from the intended baseline.

Start with an inventory and decide which repositories are critical, standard or archived. Check licensing and ownership, apply suitable settings, and review coverage as repositories are added. Organisation-level defaults for scanning and Dependabot complement the configuration; runtime context can then help prioritise the findings.

## Further reading

- [About securing your organization at scale](https://docs.github.com/en/code-security/concepts/security-at-scale/organization-security) (GitHub Docs). Security configurations and coverage.
- [Configuring global security settings for your organization](https://docs.github.com/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/configuring-global-security-settings-for-your-organization) (GitHub Docs). Organisation-wide settings.
- [Configure GitHub Advanced Security for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features?view=azure-devops) (Microsoft Learn). Scope and enablement in Azure Repos.
