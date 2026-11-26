---
title: "Which scanner, when?"
chapter: 5
hero: "5.10 Scan.png"
hero_alt: "Table comparing CodeQL, AI Scan and Codename MDASH by analysis approach, when they run and where results appear."
thumb: "thumbs/5-10-scan.webp"
summary: "Match scan depth and timing to the question being asked."
---

??? note "Text version of this slide"

    CodeQL provides semantic analysis in developer workflows. AI Scan adds AI-based analysis for eligible pull requests and on-demand repository scans. MDASH provides deeper multi-agent analysis with findings in Defender and SARIF.

## Build a layered scanning strategy

Use CodeQL and eligible pull request scanning to give developers timely feedback on changes. Use on-demand AI Scan for repositories to assess the existing default branch and add findings to the code scanning backlog. Use deeper MDASH assessments where the importance of a repository justifies a longer-running analysis.

The diagram presents a target workflow, not an automatic configuration. CodeQL only blocks a merge when the relevant checks and rules are configured; AI Scan for pull requests has language, target-branch and other eligibility requirements. Repository scans are manually triggered and in public preview.

## Further reading

- [About code scanning](https://docs.github.com/en/code-security/concepts/code-scanning/about-code-scanning) (GitHub Docs). CodeQL and other analysis tools.
- [About AI Scan](https://docs.github.com/en/code-security/concepts/code-scanning/ai-scan) (GitHub Docs). Pull request and repository scan coverage.
- [Codename MDASH FAQ](https://learn.microsoft.com/en-us/security-exposure-management/codename-mdash-faq) (Microsoft Learn). Deep scanning and preview limitations.
