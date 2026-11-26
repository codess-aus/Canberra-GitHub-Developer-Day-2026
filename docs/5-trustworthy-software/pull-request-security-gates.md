---
title: "Pull request security gates"
chapter: 5
hero: "5.16 Gates.png"
hero_alt: "Slide showing a pull request with CodeQL, AI Scan, dependency review, secret scanning, AI application scanning and Copilot code review."
thumb: "thumbs/5-16-gates.webp"
summary: "Use complementary checks and explicit merge rules for every change."
---

??? note "Text version of this slide"

    The example pull request combines required CodeQL and dependency checks, advisory AI Scan, push protection, AI application scanning and Copilot code review.

## A gate is a policy, not just a green icon

The slide shows checks with different roles. Push protection acts before a secret reaches the repository; CodeQL and dependency review can surface issues in a change; AI Scan adds findings for eligible pull requests; and Copilot code review can provide another review perspective. Code scanning for AI applications adds checks for risks such as indirect prompt injection and excessive agency and is in public preview.

A check only gates merging when the repository's rules or branch protection require it. Configure required checks, reviewers and exception processes deliberately, and confirm what happens if a scanner is unavailable or a finding needs triage. The same rules should apply to changes from people and agents.

## Further reading

- [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) (GitHub Docs). Required checks and reviews.
- [AI Scan for pull requests](https://docs.github.com/en/code-security/concepts/code-scanning/ai-powered-security-detections) (GitHub Docs). Coverage and eligibility.
- [Code scanning for AI applications in public preview](https://github.blog/changelog/2026-10-28-code-scanning-for-ai-applications-in-public-preview/) (GitHub Changelog). AI application risk detection.
