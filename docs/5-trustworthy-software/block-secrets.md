---
title: "Block secrets before they reach history"
chapter: 5
hero: "5.7 Block.png"
hero_alt: "Slide: Block the secret before it reaches history. It covers push protection, AI-detected secrets, public leak monitoring and replacing long-lived secrets with federated identity."
thumb: "thumbs/5-7-block.webp"
summary: "Prevent credential exposure and reduce the need for stored secrets."
---

??? note "Text version of this slide"

    Push protection blocks supported secrets at push time; AI detection extends coverage beyond fixed patterns. Public leak monitoring and federated identity add further protection.

## Prevent exposure, then reduce credential lifetime

Push protection checks a push for supported secrets before the content reaches the repository. Where delegated bypass is configured, an exception can go through an accountable approval process. Secret scanning and public leak monitoring complement that control by finding relevant exposures elsewhere.

GitHub's AI-powered classifier adds context to detect unstructured secrets that fixed patterns may miss. GitHub reported that early preview results more than doubled the number of pushes where a secret was caught; that is an early measurement, not a guarantee of complete detection.

The strongest way to avoid leaking a long-lived deployment secret is not to store it in the first place. Where supported, use OpenID Connect or workload identity federation to obtain short-lived credentials for GitHub Actions or Azure Pipelines. Existing exposed credentials still need revocation or rotation.

## Further reading

- [Push protection beyond predefined secret patterns](https://github.blog/changelog/2026-10-28-push-protection-beyond-predefined-secret-patterns/) (GitHub Changelog). AI-based detection and preview results.
- [About push protection](https://docs.github.com/en/code-security/concepts/secret-security/push-protection) (GitHub Docs). How push protection works.
- [Configuring OpenID Connect in Azure](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-azure) (GitHub Docs). Federated authentication for Actions.
