---
title: "Security at agent speed"
chapter: 1
hero: "1.23 Secure.png"
hero_alt: "Slide: Security that moves at agent speed. It reports 101,078 published CVEs and lists AI Scan for repositories, AI push protection, agentic autofix and Package Firewall with their release stages."
thumb: "thumbs/1-23-secure.webp"
summary: "Find, prevent and help fix security risks as development activity grows."
---

## Secure the work at more than one stage

The slide pairs a rise in published vulnerabilities with security capabilities at different points in development. AI Scan for repositories can examine a default branch across languages, including languages CodeQL does not support. AI push protection aims to catch unstructured secrets before they are pushed. Agentic autofix can help prepare pull requests to address code scanning alerts, while Package Firewall is designed to block risky packages at install time.

These capabilities do different jobs and have different release stages. AI Scan for repositories and Package Firewall are shown in preview; check the current documentation for eligibility and limitations. Repository owners and security teams still decide what to enable and how findings are triaged.

The AI Scan page already covered in this chapter explains how repository scans complement code scanning. This slide widens the view from finding vulnerabilities in existing code to protecting more of the development path.

## Further reading

- [About AI Scan](https://docs.github.com/en/code-security/concepts/code-scanning/ai-scan) (GitHub Docs). Repository, pull request and AI application scanning.
- [AI Scan for a repository's backlog](https://docs.github.com/code-security/concepts/code-scanning/ai-scan-for-repositories) (GitHub Docs). Scope, findings and preview details.
- [Agentic autofix for code scanning alerts is generally available](https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/) (GitHub Changelog). How Copilot can propose fixes.
- [National Vulnerability Database](https://nvd.nist.gov/). The vulnerability data referenced by the slide.
