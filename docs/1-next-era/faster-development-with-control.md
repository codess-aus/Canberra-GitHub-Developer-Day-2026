---
title: "Faster development, with control"
chapter: 1
hero: "1.8-Faster development.png"
hero_alt: "Slide: Faster development, with control over what moves forward. Benefits for developers, teams and organizations along a Plan, Build, Review, Ship line with security throughout development, ending with the question: where is your team feeling the most pressure across the development lifecycle?"
thumb: "thumbs/1-8-faster-development.webp"
summary: "What developers, teams and organisations gain, and a question for your team."
---

??? note "Text version of this slide"

    **Faster development, with control over what moves forward**

    - **For developers:** Less friction accessing AI and more support for complex development tasks.
    - **For teams:** Better visibility and more efficient collaboration as development activity grows.
    - **For organizations:** Broader AI adoption with security, reliability, and governance to support scale.

    Lifecycle: Plan, Build, Review, Ship. Security throughout development.

    **Where is your team feeling the most pressure across the development lifecycle?**

## Closing the loop

The opening slide described a chain: development accelerates, activity grows, complexity increases. This slide answers each link, and the title carries the whole argument. Faster development matters, but only alongside control over what moves forward.

Each audience gets its own benefit, and each traces back to something covered earlier in the chapter.

| Audience | Benefit on the slide | Where it came from |
| --- | --- | --- |
| Developers | Less friction accessing AI and more support for complex tasks | [Simpler access to AI](simpler-access-to-ai.md), [Copilot Fusion](copilot-fusion.md) and [Copilot Projects](copilot-projects.md) |
| Teams | Better visibility and more efficient collaboration as activity grows | [Copilot Projects](copilot-projects.md) and [Copilot Automations](copilot-automations.md) |
| Organisations | Broader adoption with security, reliability and governance to support scale | Enterprise policy and billing controls, the agent control plane and [AI Scan](ai-scan-for-repositories.md) |

## Where is your team feeling the pressure?

The slide ends on a question rather than a call to action, and it is worth taking seriously. Use the lifecycle as a quick diagnostic.

| Stage | A question to ask your team | Where to look |
| --- | --- | --- |
| Plan | Are goals, context and work items scattered across tools? | None of the product slides highlights Plan on its own. The Copilot app can help write specs, and the Azure Boards integration in [Resources](../6-resources-and-workshops/index.md) sends work items to Copilot. |
| Build | Is complex work slowed by coordination, repetitive tasks or model choice? | [Projects](copilot-projects.md), [Automations](copilot-automations.md) and [Fusion](copilot-fusion.md) |
| Review | Is review the bottleneck as more code and more agent-started pull requests arrive? | [Projects](copilot-projects.md) and [Automations](copilot-automations.md) |
| Ship | Are you confident about what is in the code you release? | [AI Scan](ai-scan-for-repositories.md) |

If you run this as an exercise, ask each person to name one stage and one specific symptom. Patterns in the answers show you which part of this chapter to start with.

## The controls that run through everything

The title promises control "over what moves forward". Across the chapter, the same few controls keep appearing.

- **Deliberate switches.** Copilot access is assigned, AI Scan is off by default at the enterprise level, and shared automations are a choice made per automation.
- **A human decision at the point of change.** Proposed improvements to automations come to you for review, and you can require approval for agent actions.
- **Visible identity and audit.** Shared automations act as Copilot, and audit log entries record when an agent acted and for whom.
- **Policy over models and tools.** Administrators can set which models Fusion may use and manage an MCP allowlist.
- **Budgets for usage.** AI credits are metered, so cost centres, budgets and alerts become part of governance.

## What next

- If you plan to use GitHub Copilot with Azure DevOps repositories, [Chapter 4](../4-ado-and-github-copilot/index.md) covers setup, controls and a suggested pilot.
- If modernising legacy systems is the pressure, [Chapter 2](../2-secure-by-design/index.md) follows a real engineering system through that journey.
- For courses, documentation and videos to continue with, see [Resources and Workshops](../6-resources-and-workshops/index.md).

## Further reading

- [GitHub Universe 2026: Evolving every layer of the stack](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) (GitHub Blog). The announcements behind this chapter.
- [GitHub Universe recap](https://github.com/events/universe/recap) (GitHub). A product tour you can try in the Copilot app.
- [Universe 2026 releases](https://github.blog/changelog/label/universe26/) (GitHub Changelog). Every Universe changelog entry.
