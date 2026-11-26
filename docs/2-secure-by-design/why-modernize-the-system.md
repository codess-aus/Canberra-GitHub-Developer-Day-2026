---
title: "Why modernize the system"
chapter: 2
hero: "2.7 Why.png"
hero_alt: "Section 01 slide: Why Modernize the System. Building trust through goals and evidence."
thumb: "thumbs/2-7-why.webp"
summary: "Section 01: building trust through goals and evidence."
---

??? note "Text version of this slide"

    **Section 01**

    **Why Modernize the System**

    Building trust through goals and evidence.

## The walls everyone hits

By now most of us have experimented with AI agents in some capacity. Chances are we have also hit the same walls: integration friction, scaling limits, low production rates and security roadblocks. It can feel as though the current approach will not hold up in a real work environment, and there is a fear of messing it up.

## The real question

The starting question for 1ES was not whether agents could write a feature. It was whether they could build a repeatable system that reliably delivers production-quality software with AI. To trust a system you need to see clear goals, guardrails and evidence, and you need to see them put into practice in the real world.

## Goals: tell the agent what good looks like

GitHub Docs describe repository custom instructions as project-specific context: the purpose of the repository, the frameworks and tools in use, and the coding and testing conventions contributors should follow. They live in the repository itself:

- `.github/copilot-instructions.md` for repository-wide guidance.
- One or more `AGENTS.md` files anywhere in the repository, where the nearest file in the directory tree takes precedence.
- `.github/instructions/NAME.instructions.md` files for more targeted guidance.

Because Copilot code review reads instructions from the head branch of a pull request, you can test a change to your instructions in the same pull request, before merging it.

## Guardrails: limits that hold even when the agent is wrong

The documented behaviour of the Copilot cloud agent is a good model of guardrails by default:

- It can only push to a single branch, a new `copilot/` branch unless it was invoked on an existing pull request, and it is still subject to branch protections and required checks.
- Its pull requests are drafts that a human must review and merge. It cannot mark them ready for review, approve them or merge them, and the person who asked for the work cannot approve it either.
- GitHub Actions workflows do not run on its pull requests until a user with write access approves them.
- By default it checks its own code for security issues, such as hardcoded secrets and insecure dependencies, and gets a second opinion from Copilot code review before it finishes.

## Evidence: proof you can show an auditor

Goals and guardrails only build trust if you can show they were followed. On GitHub that evidence includes:

- **Pull requests and checks**, which record what changed and what validated it.
- **The enterprise audit log**, where `actor:Copilot` filters agent activity. It retains events for 180 days, and GitHub recommends streaming it to a SIEM for long-term history and alerts. It does not include client session data such as the prompts a user sends locally, so plan a custom solution if you need that.
- **Copilot usage metrics**, through a dashboard and APIs at enterprise and organisation scope, covering adoption, usage and code generation.

This lines up with the ISM, whose risk management framework runs from defining the system through selecting, implementing, assessing and authorising controls to monitoring the system. When controls change, the ISM expects another assessment and an updated authorisation package, so the authorising officer can make an informed decision about whether the risk is still acceptable.

## The proving ground

To put the idea to the test, the team used the Microsoft 1 Engineering System as its proving ground. Microsoft's IT organisation describes how this kind of adoption began: by making AI visible and accessible in the tools engineers already used. The early goal was not immediate productivity gains but familiarity, so engineers tried AI on low-risk tasks such as summarising documentation, generating test cases or exploring unfamiliar codebases. The next pages show what 1ES measured.

## Further reading

- [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) (GitHub Docs)
- [Risks and mitigations for GitHub Copilot cloud agent](https://docs.github.com/copilot/concepts/agents/cloud-agent/risks-and-mitigations) (GitHub Docs)
- [Reviewing audit logs for GitHub Copilot](https://docs.github.com/copilot/managing-github-copilot-in-your-organization/reviewing-audit-logs-for-copilot-business) (GitHub Docs)
- [Information security manual, September 2026](https://www.cyber.gov.au/ism/2026-09) (Australian Signals Directorate)
- [Powering the new age of AI-led engineering in IT at Microsoft](https://www.microsoft.com/insidetrack/blog/powering-the-new-age-of-ai-led-engineering-in-it-at-microsoft/) (Microsoft Inside Track)
