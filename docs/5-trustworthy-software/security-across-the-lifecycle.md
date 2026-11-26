---
title: "Security across the lifecycle"
chapter: 5
hero: "5.13 Ubiquitous.png"
hero_alt: "Timeline of security checks across agent work, CLI and IDE, Copilot app, pull requests, repositories and the enterprise, ranging from seconds to hours."
thumb: "thumbs/5-13-ubiquitous.webp"
summary: "Choose the depth and timing of a check to suit the stage of work."
---

??? note "Text version of this slide"

    Security spans the agent loop, CLI and IDE, Copilot app, pull request, repository and enterprise, with checks ranging from seconds to hours.

## The right feedback at the right time

Not every security control needs the same scope or runtime. A quick check while editing can help a developer address a problem immediately. Pull request checks evaluate a proposed change before it merges. Broader repository scans and enterprise campaigns help find and address existing risk across a larger estate.

The stages are complementary. Fast feedback should not be mistaken for a comprehensive audit, and a deep scan run occasionally cannot prevent every unsafe change in between. Design a pipeline where the checks work together and findings have a clear owner.

## Further reading

- [About code scanning](https://docs.github.com/en/code-security/concepts/code-scanning/about-code-scanning) (GitHub Docs). Integrating analysis into development.
- [Fix alerts at scale](https://docs.github.com/en/code-security/tutorials/secure-your-organization/best-practice-fix-alerts-at-scale) (GitHub Docs). Organising remediation across repositories.
