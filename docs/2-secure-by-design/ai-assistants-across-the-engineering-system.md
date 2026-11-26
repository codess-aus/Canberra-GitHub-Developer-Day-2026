---
title: "AI assistants across the engineering system"
chapter: 2
hero: "2.6 - Outcomes.png"
hero_alt: "Slide: AI assistants across the engineering system. Results for GitHub Copilot, FirstMate and ES Chat from the 1ES modernisation outcomes."
thumb: "thumbs/2-6-outcomes.webp"
summary: "Results for GitHub Copilot, FirstMate and ES Chat."
---

??? note "Text version of this slide"

    **1ES modernisation outcomes**

    **GitHub Copilot:** AI assistant for code completion and developer chat.

    - **5.5%** increase in PR velocity for the average developer
    - **40%** increase in PR velocity, per hour of active coding time

    **FirstMate:** AI assistant for new hires to accelerate their onboarding journeys.

    - **65%** reduction in Time-To-First-PR during a large-scale pilot

    **ES Chat:** AI assistant for engineering systems providing instant, contextual answers.

    - **46.7** minutes saved per task (on average) compared with traditional search methods

!!! info "About these figures"

    These are internal results from Microsoft's 1 Engineering System, shared in the talk. Treat them as a benchmark for what to measure, not a promise of what you will see.

Now the numbers. 1ES put AI assistants at several points in the engineering system rather than in one tool, and measured each one against the work it was meant to change.

## GitHub Copilot: two ways to read PR velocity

Copilot shows a **5.5%** increase in pull request velocity for the average developer, and a **40%** increase per hour of active coding time. The talk reads the second figure as responsiveness: when developers are actually coding, work moves through to a pull request much faster. The gap between the two is a reminder that writing code is only part of the job, which is why measuring at the system level matters.

## FirstMate: faster starts for new hires

FirstMate is the AI assistant for new hires. In a large-scale pilot it cut Time-To-First-PR by **65%**, so people get from joining the team to shipping their first change in a fraction of the time.

## ES Chat: answers instead of searching

ES Chat gives engineers instant, contextual answers about the engineering system. It saved **46.7 minutes** per task on average compared with traditional search methods.

## Across the whole system, not just the editor

Microsoft's IT organisation reports a similar pattern. AI supported test generation, defect analysis and code review, so issues surfaced sooner and engineers spent more time on quality and architecture than on cleanup. In service engineering it summarised incidents and surfaced relevant knowledge. The reported result is a chain reaction: faster design cycles reduced downstream rework, better testing lowered operational noise, and better operational insight shortened recovery times.

GitHub Universe 2026 pushed the same direction. The GitHub Copilot app is a single agent-first surface for more than code, and Copilot automations run in the cloud on a schedule or in response to an event, handling work such as issue triage and code review.

## Measure your own baseline

To compare your team against these figures, measure before you change anything. GitHub's Copilot usage metrics are available through a dashboard and APIs at enterprise and organisation scope, with aggregated, repository-level and user-level reports. They include acceptance rate, lines of code changed with AI and the share of lines added by agents, and adoption cohorts that group users by how they work, from code completions through to agent-first workflows.

## Further reading

- [Copilot usage metrics](https://docs.github.com/copilot/concepts/billing-and-usage/copilot-usage-metrics/copilot-metrics) (GitHub Docs)
- [Data available in Copilot usage metrics](https://docs.github.com/copilot/reference/copilot-usage-metrics/copilot-usage-metrics) (GitHub Docs)
- [Powering the new age of AI-led engineering in IT at Microsoft](https://www.microsoft.com/insidetrack/blog/powering-the-new-age-of-ai-led-engineering-in-it-at-microsoft/) (Microsoft Inside Track)
- [GitHub Universe 2026: Evolving every layer of the stack](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) (GitHub Blog)
