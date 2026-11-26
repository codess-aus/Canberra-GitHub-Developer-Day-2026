---
title: "Advanced Security for Azure DevOps"
chapter: 5
hero: "5.17 GHAS and ADO.png"
hero_alt: "Slide: GitHub Advanced Security, native in Azure Repos, with push protection, CodeQL, dependency scanning, pull request checks and Copilot capabilities."
thumb: "thumbs/5-17-ghas-and-ado.webp"
summary: "Use security scanning and review in Azure Repos without moving the repository."
---

??? note "Text version of this slide"

    Azure Repos supports secret protection, CodeQL and dependency scanning, third-party results and pull request status checks. Copilot Autofix and the Copilot app integration are shown as previews.

## Security where the repository lives

GitHub Advanced Security for Azure DevOps brings secret, code and dependency protections into Azure Repos. Teams can configure coverage at organisation, project or repository level, then use branch policies and status checks to enforce their chosen merge requirements. Billing and setup are managed through the linked Azure subscription.

Copilot Autofix for supported code and dependency alerts is in preview. A developer requests a fix from an alert and reviews the resulting pull request. Enabling Autofix does not configure scanning or automatically generate fixes.

For Copilot app integration and governance considerations, see [Chapter 4](../4-ado-and-github-copilot/index.md). Check each product's documentation for supported languages, prerequisites and current availability.

## Further reading

- [Configure GitHub Advanced Security for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features?view=azure-devops) (Microsoft Learn). Enablement and configuration.
- [Copilot Autofix for code security alerts](https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-autofix?view=azure-devops) (Microsoft Learn). Preview prerequisites and review workflow.
- [GitHub Advanced Security for Azure DevOps billing](https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-billing?view=azure-devops) (Microsoft Learn). Active committer billing.
