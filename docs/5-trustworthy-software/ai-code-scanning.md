---
title: "AI and code scanning"
chapter: 5
hero: "5.8 any language.png"
hero_alt: "Slide comparing hybrid pull request scanning with full repository AI scanning. Screenshots show a security finding and a choice of standard and deep scans."
thumb: "thumbs/5-8-any-language.webp"
summary: "Combine CodeQL with AI-based scanning for broader coverage."
---

??? note "Text version of this slide"

    The slide contrasts fast pull request scanning with on-demand repository scans, combining CodeQL and AI-based analysis.

## Different scans answer different questions

CodeQL uses semantic code analysis to find known classes of vulnerability. AI Scan extends code scanning with AI-based detection. For pull requests it currently covers selected languages and frameworks that CodeQL does not cover; repository scans analyse the default branch on demand across languages, including languages supported by CodeQL.

The repository feature is in public preview and its findings appear alongside CodeQL alerts. GitHub Docs explains that a scan selects code for analysis within a time budget; it does not read every file in full. A completed scan is useful evidence, not proof that the repository contains no vulnerabilities.

The controls must be enabled and configured, and the pull request feature has eligibility constraints. See [AI Scan for repositories](../1-next-era/ai-scan-for-repositories.md) for a closer look at scope and costs.

## Further reading

- [About AI Scan](https://docs.github.com/en/code-security/concepts/code-scanning/ai-scan) (GitHub Docs). Differences between the scanning modes.
- [AI Scan for a repository's backlog](https://docs.github.com/en/code-security/concepts/code-scanning/ai-scan-for-repositories) (GitHub Docs). Preview, scope and limitations.
- [AI Scan for pull requests](https://docs.github.com/en/code-security/concepts/code-scanning/ai-powered-security-detections) (GitHub Docs). Supported pull requests and languages.
