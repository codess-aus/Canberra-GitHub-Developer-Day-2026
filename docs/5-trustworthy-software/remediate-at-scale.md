---
title: "Remediate alerts at scale"
chapter: 5
hero: "5.11 Bulk.png"
hero_alt: "Slide: Bulk-fix issues across repositories and tools, showing security campaign progress, selected alerts and a comparison of fix rates."
thumb: "thumbs/5-11-bulk.webp"
summary: "Turn an alert backlog into coordinated, reviewable fixes."
---

??? note "Text version of this slide"

    Security campaigns group alerts for coordinated remediation. The slide compares reported fix rates before and with agentic remediation.

## Finding is only the first step

An alert backlog becomes useful when it has owners, priorities and an agreed remediation path. GitHub security campaigns bring related alerts together across repositories, while agentic autofix can explore code and propose changes in a pull request. The person reviewing the pull request remains responsible for whether the change is appropriate.

GitHub supports selecting up to 25 code scanning alerts for a single agentic autofix pull request. Campaigns help coordinate larger sets of alerts, but a generated fix is not a substitute for review, testing or confirming that scanning closes the relevant finding.

The slide's rate comparison describes a reported outcome, not a guarantee that every organisation will see the same improvement.

## Further reading

- [Agentic autofix for code scanning alerts is generally available](https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/) (GitHub Changelog). How fixes are generated.
- [Fix alerts at scale](https://docs.github.com/en/code-security/tutorials/secure-your-organization/best-practice-fix-alerts-at-scale) (GitHub Docs). Campaigns and coordinated remediation.
