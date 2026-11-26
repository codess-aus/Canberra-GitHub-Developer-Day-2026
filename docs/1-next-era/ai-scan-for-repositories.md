---
title: "Get ahead of vulnerabilities: AI Scan"
chapter: 1
hero: "1.7-Get ahead of vulnerabilities already sitting in your code.png"
hero_alt: "Slide: Get ahead of vulnerabilities already sitting in your code. AI Scan for repositories, in public preview, runs an on-demand AI-powered scan to uncover vulnerabilities in existing code, including languages traditional scanning misses. A screenshot shows the code scanning page with an AI Scan menu offering a standard scan and a deep scan, and a Start scan button."
thumb: "thumbs/1-7-get-ahead-of-vulnerabilities-already-sitting-in-your-code.webp"
summary: "On-demand AI scanning for existing code, in any language."
---

??? note "Text version of this slide"

    **Get ahead of vulnerabilities already sitting in your code**

    **AI Scan for repositories (Public Preview)**

    Run an on-demand, AI-powered scan to uncover vulnerabilities in existing code, including languages traditional scanning miss.

    **Expand scanning coverage. Uncover hidden vulnerabilities.**

    Lifecycle: Review + Ship, with security throughout development.

    Screenshot: the Code scanning page. An AI Scan menu with Standard scan and Deep scan tabs reads: "Full-repo AI-powered security scan on main. Available for any programming language." A Start scan button is below. Behind it is a list of open alerts, including deserialization of user-controlled data, server side template injection and uncontrolled command line.

!!! note "Public preview"

    AI Scan for repositories is in public preview and subject to change, as the slide says. Check the Docs for the current behaviour before you rely on it.

## Looking back, not only forward

Most security tooling is described in terms of catching problems in new code. This slide is about the code that already exists. Legacy estates carry vulnerabilities that were never found, and a scan on every pull request does not help with code nobody is changing.

According to GitHub Docs, AI Scan for repositories uses a proprietary harness that draws on multiple models to find vulnerabilities on a repository's default branch. It supports all languages. That extends coverage beyond the languages CodeQL supports, and it can also find additional vulnerabilities in languages CodeQL already analyses. You run it on demand, independently of CodeQL.

## It lands in the backlog you already have

The most practical detail is where results go. Findings appear in the repository's code scanning alert list under **Security and quality**, next to CodeQL alerts, and you can filter by the AI Scan tool. That means existing workflows apply: assign the alert, apply agentic autofix, include it in a security campaign, or link it to an issue.

The screenshot shows this. The scan menu floats over a normal alert list, with open alerts such as deserialization of user-controlled data and uncontrolled command line.

## How a scan runs, and what that implies

The Docs describe the process in a way that is worth reading carefully.

1. A user with write access triggers a scan of the default branch.
2. The AI agent searches the repository to identify files and functions to examine. It selects code for further analysis rather than reading every file in full.
3. The agent runs within a time budget. When the budget is used up, it stops and reports what it found.

So treat a scan as a way to expand coverage, not as proof that a repository is clean. In public preview, merging a fix does not trigger another scan automatically, so you start a new scan to confirm alerts are resolved.

The screenshot's menu offers **Standard scan** and **Deep scan** tabs. Check the AI Scan Docs for how they differ before you choose.

## Related Universe security releases

AI Scan for repositories was one of several security announcements.

- **AI Scan for pull requests** finds general security vulnerabilities in selected languages and frameworks that CodeQL does not cover, such as PHP and Terraform configuration (HCL). It scans eligible pull requests when they are created and after each new commit, and labels findings "AI".
- **Scan for AI applications** finds risks specific to AI applications and agents, such as indirect prompt injection.
- **Push protection with AI** catches unstructured secrets, like passwords, and blocks them at push, whether a person or an agent wrote the code. Both push protection and AI secret detection must be enabled.
- **A Security canvas in the Copilot app** shows what you and your agents just wrote beside your code scanning alerts, so you can ask Copilot to explain and fix findings and then review each change.

## Who controls it

Switching AI Scan on is a deliberate step at two levels.

- **Enterprise:** owners can allow or prevent organisations from enabling it. The policy is **Not allowed** by default, and allowing it does not enable it automatically.
- **Organisation:** owners and security managers can enable it for eligible repositories. After that, you can start one-off scans of up to 20 repositories.

## Why it matters for an agency

Government estates often include older applications in languages and frameworks that mainstream scanners cover poorly. AI Scan gives you a way to ask what is sitting in those codebases before you plan a change to them. It pairs naturally with the modernisation themes in [Chapter 2](../2-secure-by-design/index.md), and the GitHub Advanced Security learning paths in [Resources](../6-resources-and-workshops/index.md) cover the CodeQL, secret scanning and Dependabot foundations that AI Scan builds on.

## Further reading

- [AI Scan for a repository's backlog](https://docs.github.com/en/code-security/concepts/code-scanning/ai-scan-for-repositories) (GitHub Docs). How scans run, results, policies and limits.
- [About AI Scan](https://docs.github.com/code-security/concepts/code-scanning/ai-scan) (GitHub Docs). AI Scan for repositories, pull requests and AI applications.
- [GitHub Universe recap](https://github.com/events/universe/recap) (GitHub). The Security canvas, AI Scan and AI push protection in the product tour.
- [Universe 2026 releases](https://github.blog/changelog/label/universe26/) (GitHub Changelog). The full list of security changelog entries.
