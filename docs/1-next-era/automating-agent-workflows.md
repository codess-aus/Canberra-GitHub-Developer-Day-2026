---
title: "Automating agent workflows"
chapter: 1
hero: "1.20 Autopilot.png"
hero_alt: "Slide: Put recurring work on autopilot. It compares Copilot Automations, configured to run on schedules, events or API calls, with GitHub Agentic Workflows, written in Markdown and compiled to GitHub Actions."
thumb: "thumbs/1-20-autopilot.webp"
summary: "Choose between a configured Copilot automation and automation-as-code."
---

## Two approaches to recurring work

The slide compares two ways to delegate repeatable tasks. [Copilot Automations](copilot-automations.md) let a team configure a prompt, trigger and tools for work such as issue triage, code review or a recurring summary. Automations run with a Copilot cloud agent and can propose prompt improvements based on outcomes for a person to approve.

GitHub Agentic Workflows take an automation-as-code approach. Teams describe workflows in Markdown, which is compiled to GitHub Actions. The project is designed to run in a sandbox and be read-only by default, with changes applied through controlled outputs. This makes the workflow definition reviewable and versioned alongside repository code.

The slide includes an Accenture example reporting time savings, a high share of AI-authored commits and fewer production errors. Those are results from one organisation's experience, not a forecast for every team. Start with a bounded workflow, review what it can access and write, and measure whether the automation improves the actual process.

## Further reading

- [GitHub Agentic Workflows are now generally available](https://github.blog/changelog/2026-10-28-github-agentic-workflows-generally-available/) (GitHub Changelog). The automation-as-code project and its release details.
- [GitHub Universe 2026: Evolving every layer of the stack](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) (GitHub Blog). Copilot Automations and outcome-based improvements.
- [Copilot Automations](copilot-automations.md) (this chapter). The related Copilot feature and its controls.
