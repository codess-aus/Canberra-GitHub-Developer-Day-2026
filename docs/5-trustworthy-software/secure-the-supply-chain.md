---
title: "Secure the software supply chain"
chapter: 5
hero: "5.15 Secure what agents install.png"
hero_alt: "Slide listing package firewall, dependency review, Dependabot, artifact attestations, Actions hardening and the pull_request_target policy change."
thumb: "thumbs/5-15-secure-what-agents-install.webp"
summary: "Protect package installation, dependency changes and build provenance."
---

??? note "Text version of this slide"

    The slide covers install-time package policy, dependency review, Dependabot, artifact attestations, Actions hardening and a change to the default pull_request_target policy.

## Protect more than the source code

Dependencies and build workflows can run code before an application is deployed. GitHub's Package Firewall is an install-time policy gate for npm in public preview. Dependency review examines dependency changes in pull requests, while Dependabot helps identify and update vulnerable dependencies. Artifact attestations record signed provenance for a build; consumers still need to verify and enforce their own policy.

Harden workflows with least-privilege tokens and trusted, pinned actions. The slide's `pull_request_target` warning needs a scope qualification: from 2 December 2026, GitHub's default blocking rule applies to **public repositories** without an applicable policy allowing the event. Private and internal repositories are not affected by that default. Review affected workflows and the current policy before the change.

## Further reading

- [GitHub Package Firewall in public preview](https://github.blog/changelog/2026-10-20-github-package-firewall-in-public-preview/) (GitHub Changelog). Install-time policy and preview details.
- [Artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations) (GitHub Docs). Build provenance and verification.
- [pull_request_target blocked by default December 2](https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2/) (GitHub Changelog). Scope, timing and migration guidance.
