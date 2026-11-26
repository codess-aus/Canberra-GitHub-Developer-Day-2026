---
title: "Takeaways"
chapter: 2
hero: "2.9 Takeaways.png"
hero_alt: "Section 04 slide: Takeaways. Portable concepts and a practical starting point."
thumb: "thumbs/2-9-takeaways.webp"
summary: "Section 04: portable concepts and a practical starting point."
---

??? note "Text version of this slide"

    **Section 04**

    **Takeaways**

    Portable concepts and a practical starting point.

Three things to take away: assessment, transformation and, because this is government, security. They are portable concepts with a practical starting point.

## 1. Assessment

GitHub Copilot analyses the current state of your project and comes up with modernisation plans. It identifies anything outdated, any dependencies and any migration problems, and gives you actionable strategies to remove them.

Microsoft Learn describes this as the first of three stages, assessment, planning and execution, with the results written as Markdown files in your repository under `.github/upgrades`. At Ignite 2026, Azure Catalyst joined Azure Migrate and GitHub Copilot modernization, adding dependency mapping into code and a CLI for running assessments in parallel.

The same principle applies at small scale. In the GitHub Blog's COBOL to Node.js walkthrough, Copilot first produces a test plan that is validated with business stakeholders, and only then is it turned into unit and integration tests.

## 2. Transformation

The system captures and reuses patterns, helps you build custom skills, and applies similar fixes across multiple codebases.

- **Reusable patterns.** Microsoft Learn describes reusable migration patterns through custom skills, with code transformations built on OpenRewrite.
- **Custom skills.** At Build 2026, custom skills for the modernization agent became generally available. A skill is a `skill.md` file that encodes your proprietary patterns, libraries, Azure best practices and migration approaches once, to be reused on every run. Skills build on the open agent skills standard, so you are not locked into a proprietary format.
- **Skills in GitHub.** GitHub Docs describe agent skills as folders of instructions, scripts and resources that Copilot loads when relevant, defined by a `SKILL.md` file. The `gh skill` command in GitHub CLI discovers, installs, updates and publishes them. Use custom instructions for guidance that applies to almost every task, and skills for detail Copilot should only load when it is relevant.
- **Across many codebases.** The modernization agent creates issues, pull requests and shareable assessment reports for each application, and coordinates with the Copilot coding agent to complete tasks asynchronously across repositories, with monitoring and an audit trail in GitHub Agent HQ. At Universe 2026, Copilot projects extended this to managed parallel sessions across multiple repositories.

## 3. Security

This is where GitHub Copilot is essential for government. It patches vulnerabilities and proposes fixes, with security engineers reviewing every change to ensure you are meeting PSPF requirements.

- **After the upgrade.** Microsoft Learn notes that CVE scanning runs after upgrades.
- **Autofix for code scanning.** Copilot Autofix uses large language models to turn a code scanning alert into suggested code changes with an explanation. With agentic autofix you assign an alert to Copilot, which explores the codebase, generates a fix, validates it by re-running CodeQL and iterates until it opens a pull request.
- **Review stays human.** Autofix works on a best-effort basis. It cannot confirm that a fix resolves alerts from custom queries, and GitHub expects most suggestions to be committable with no or minor edits while a small percentage will misread the code. Hence the reviewer.
- **One place to review.** At Universe 2026 GitHub introduced a Security canvas for reviewing what you and your agents just wrote alongside the repository's code scanning alerts, and Copilot code review Max, which posted the highest F1 score on ReviewBench for high-severity issues.

## How the three map to the direction

This mapping is a suggested reading, not official guidance:

| Takeaway | What it gives you | PSPF Direction 002-2026 requirement it supports |
| --- | --- | --- |
| Assessment | Outdated components, dependencies and migration problems, with a plan | The Legacy Technology Stocktake |
| Transformation | Reusable patterns and skills applied across codebases | The reduction target and the procedures to rationalise the estate |
| Security | Fixes for vulnerabilities, reviewed by people, with a trail | Mitigations and evidence for systems that remain |

## Further reading

- [GitHub Copilot modernization overview](https://learn.microsoft.com/en-us/azure/developer/github-copilot-app-modernization/overview) (Microsoft Learn)
- [Closing the AI-readiness gap with agentic modernization](https://techcommunity.microsoft.com/blog/appsonazureblog/closing-the-ai-readiness-gap-with-agentic-modernization/4524011) (Microsoft Build 2026)
- [Adding agent skills for GitHub Copilot](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/create-skills) (GitHub Docs)
- [About autofix for code scanning](https://docs.github.com/code-security/concepts/code-scanning/copilot-autofix-for-code-scanning) (GitHub Docs)
- [Responsible use of Copilot Autofix for code scanning](https://docs.github.com/en/code-security/responsible-use/responsible-use-autofix-code-scanning) (GitHub Docs)
- [Modernizing legacy code with GitHub Copilot: tips and examples](https://github.blog/ai-and-ml/github-copilot/modernizing-legacy-code-with-github-copilot-tips-and-examples/) (GitHub Blog)
- [GitHub Universe recap](https://github.com/events/universe/recap) (GitHub)
