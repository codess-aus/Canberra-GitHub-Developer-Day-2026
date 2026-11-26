---
title: "Security gates in Azure DevOps"
chapter: 5
hero: "5.18 Gates in ADO.png"
hero_alt: "Flow from developer to push, pull request, status checks and release in Azure DevOps, with push protection, CodeQL, dependency scanning and workload identity federation."
thumb: "thumbs/5-18-gates-in-ado.webp"
summary: "Connect Azure Repos controls from push through release."
---

??? note "Text version of this slide"

    The flow includes push protection, pull request build validation, branch-policy status checks, and federated identity at release. Autofix, security overview and Defender for Cloud support the flow.

## Follow a change from push to release

When enabled, push protection checks a push for supported secrets. Pull request build validation can run CodeQL and dependency scanning, and branch policies can require status checks before completion. Release pipelines can use workload identity federation rather than storing long-lived credentials.

The surrounding views matter too. Security overview helps teams see alerts across repositories; Copilot Autofix can propose a fix for a supported alert; and Defender for Cloud can add a broader posture view. These capabilities need deliberate setup and appropriate permissions, rather than turning on automatically for every repository.

## Further reading

- [Configure GitHub Advanced Security for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features?view=azure-devops) (Microsoft Learn). Scanning and enablement.
- [Copilot Autofix for code security alerts](https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-autofix?view=azure-devops) (Microsoft Learn). Requesting and validating fixes.
- [Configure workload identity federation](https://learn.microsoft.com/en-us/azure/devops/pipelines/release/configure-workload-identity?view=azure-devops) (Microsoft Learn). Federated Azure service connections.
