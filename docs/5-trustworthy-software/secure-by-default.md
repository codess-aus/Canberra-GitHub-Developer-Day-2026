---
title: "A secure-by-default baseline"
chapter: 5
hero: "5.19 Secure by default.png"
hero_alt: "Slide outlining a secure-by-default baseline for identity, repositories, Advanced Security, Actions and Copilot, with Australian data residency."
thumb: "thumbs/5-19-secure-by-default.webp"
summary: "Make security controls part of the platform rather than an optional extra."
---

??? note "Text version of this slide"

    The baseline covers managed identities, repository rules, security configurations, hardened Actions, Copilot controls and Australian data residency.

## Make the safe path repeatable

A baseline is a set of controls that apply consistently as teams create repositories and workflows. The slide groups them into five areas: managed identity and least privilege; repository rules and required reviews; scanning and push protection; hardened Actions and federated access; and policies and audit for Copilot agents.

The details need to match the organisation's threat model, existing identity architecture and operational needs. Enforce the controls that are required, define an accountable exception process, and check new repositories for coverage. Data residency and agent features have their own scope and eligibility, so verify what data and services are covered before making a compliance claim.

## Further reading

- [About securing your organization at scale](https://docs.github.com/en/code-security/concepts/security-at-scale/organization-security) (GitHub Docs). Security configurations.
- [Enterprise AI Controls and agent control plane](https://github.blog/changelog/2026-02-26-enterprise-ai-controls-agent-control-plane-now-generally-available/) (GitHub Changelog). Policy and audit capabilities.
- [GitHub Enterprise Cloud with data residency](https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/about-github-enterprise-cloud-with-data-residency) (GitHub Docs). Residency scope and requirements.
