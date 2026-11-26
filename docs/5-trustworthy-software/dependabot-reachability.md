---
title: "Prioritise with reachability"
chapter: 5
hero: "5.12 Fix.png"
hero_alt: "Slide: Fix what your code can actually reach. A Dependabot alert shows a call path from application code to a vulnerable dependency function."
thumb: "thumbs/5-12-fix.webp"
summary: "Use call-path evidence alongside severity and exposure when triaging dependencies."
---

??? note "Text version of this slide"

    Reachability analysis traces possible calls from application code to a vulnerable dependency function. It is in public preview for JavaScript and TypeScript; a verdict does not close an alert.

## A call path is evidence, not a verdict on safety

Reachability analysis combines curated advisory data with CodeQL call graphs to show whether application code can reach a vulnerable function. When available, the alert can include a call path that helps a developer understand why the dependency matters.

Verdicts include reachable, potentially reachable, unreachable and unavailable. Reachable does not by itself prove a vulnerability is exploitable; unreachable is not a guarantee of safety. Combine the result with severity, exploit prediction, runtime exposure and business impact. GitHub does not automatically close an alert because of its reachability verdict.

The feature is in public preview for supported JavaScript and TypeScript repositories with a supported lockfile. Azure DevOps dependency alerts can provide EPSS context, which estimates exploitation likelihood rather than reachability.

## Further reading

- [About reachability analysis for Dependabot alerts](https://docs.github.com/en/code-security/concepts/supply-chain-security/about-reachability-analysis-for-dependabot-alerts) (GitHub Docs). Verdicts, supported ecosystems and limitations.
- [Prioritize Dependabot alerts with reachability analysis](https://github.blog/changelog/2026-10-28-prioritize-dependabot-alerts-with-reachability-analysis/) (GitHub Changelog). The preview announcement.
- [Azure DevOps sprint 280 update](https://learn.microsoft.com/en-us/azure/devops/release-notes/2026/sprint-280-update) (Microsoft Learn). EPSS and Autofix updates.
