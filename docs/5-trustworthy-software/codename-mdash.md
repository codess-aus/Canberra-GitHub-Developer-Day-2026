---
title: "Go deeper with Codename MDASH"
chapter: 5
hero: "5.9 Deeper.png"
hero_alt: "Slide: Codename MDASH in preview. Four stages prepare, scan, validate and deduplicate findings, alongside research benchmark results and integration options."
thumb: "thumbs/5-9-deeper.webp"
summary: "Use a multi-agent scanner for deeper assessment of important code."
---

??? note "Text version of this slide"

    Codename MDASH prepares and ranks code, scans with specialised agents, validates findings and deduplicates results. The slide reports benchmark and Windows research findings, and shows GitHub, Azure DevOps and Defender CLI integration.

## A deeper, asynchronous assessment

Codename MDASH is Microsoft's multi-model agentic code scanner. Microsoft describes a pipeline that ranks code by risk, uses specialised agents to look for different vulnerability classes, validates potential findings and combines duplicates. Findings can be reviewed in Microsoft Defender, with proposed fixes reviewed by developers.

The benchmark and Windows vulnerability figures on the slide are research results under particular conditions, not promises about a customer's codebase. A deep scan complements, rather than replaces, faster checks in the development workflow. Consider its runtime and cost when deciding which critical repositories to assess.

MDASH is in preview. Its prerequisites include eligible Microsoft security services and a Microsoft Foundry resource; consult the current documentation for supported regions, access and inference costs.

## Further reading

- [Codename MDASH overview](https://learn.microsoft.com/en-us/security-exposure-management/ai-code-security-overview) (Microsoft Learn). The scanning stages, integrations and prerequisites.
- [Codename MDASH FAQ](https://learn.microsoft.com/en-us/security-exposure-management/codename-mdash-faq) (Microsoft Learn). Preview limits and practical questions.
- [Defense at AI speed](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/) (Microsoft Security Blog). Research and benchmark context.
