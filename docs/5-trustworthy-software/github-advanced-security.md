---
title: "GitHub Advanced Security"
chapter: 5
hero: "5.5 GHAS.png"
hero_alt: "Slide: GitHub Advanced Security, including secret protection, code security, supply chain security and Copilot Autofix; the slide reports 1.3 million active developers."
thumb: "thumbs/5-5-ghas.webp"
summary: "Bring secret, code and dependency risks into developer workflows."
---

??? note "Text version of this slide"

    The slide groups secret protection, code security, supply chain controls and Copilot Autofix, and reports more than 1.3 million active developers.

## Find different kinds of risk

GitHub Secret Protection focuses on exposed credentials, including secret scanning and push protection. GitHub Code Security brings code scanning and remediation capabilities into the repository. Dependency features identify vulnerable packages, while dependency review and package policies help prevent unsafe additions.

These controls solve different problems: scanning existing code does not prevent a new secret being pushed, and dependency alerts do not replace code analysis. Configure them as layers and give alert owners a clear path to investigate and fix findings.

Advanced Security is also available for Azure DevOps, with platform-specific setup and billing. Check each feature's eligibility, licensing and release status before assuming GitHub and Azure Repos behave identically.

## Further reading

- [About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) (GitHub Docs). Product capabilities and eligibility.
- [GitHub Advanced Security for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features?view=azure-devops) (Microsoft Learn). Azure Repos setup.
