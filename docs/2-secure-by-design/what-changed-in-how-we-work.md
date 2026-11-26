---
title: "What changed in how we work"
chapter: 2
hero: "2.91 What Changed.png"
hero_alt: "Slide: What changed in how we work. Three cards: decisions over chores, build for the team, and observability earns trust."
thumb: "thumbs/2-91-what-changed.webp"
summary: "Decisions over chores, build for the team, observability earns trust."
---

??? note "Text version of this slide"

    1. **Decisions over chores.** Humans own judgment and risk. Agents handle repeatable execution and feed learning back.
    2. **Build for the team.** Shared instructions, tools, standards, and memory create leverage across the whole team.
    3. **Observability earns trust.** Validation and test prove readiness. Measured outcomes allow autonomy to expand.

    **The operating model is the outcome. Observable loops are how you build it.**

Xavier closes with a personal example. For his team at Microsoft, this is what changed in how they work.

## 1. Decisions over chores

The team now does the meatier tasks. Agents handle the operational work, so people can focus on product direction, meaningful trade-offs and risk. Humans own judgment and risk; agents handle repeatable execution and feed learning back.

GitHub's design supports that split. The cloud agent cannot approve or merge its own pull requests, and Copilot automations let you coordinate agents for tasks such as issue triage and code review while you stay in the decision seat. At Universe 2026 GitHub added that automations can learn from their outcomes and propose improvements for you to review and approve. An Engineering@Microsoft post describes the same shift as developers becoming "agent orchestrators" rather than just code authors.

## 2. Build for the team

The team builds shared instructions, tools and standards, so what one person learns becomes organisational leverage instead of staying inside an individual's session.

On GitHub that maps to concrete files and features:

- **Shared instructions** in `.github/copilot-instructions.md` and `AGENTS.md`.
- **Shared skills** in `SKILL.md` folders, distributed with `gh skill`, which records the source repository, ref and tree SHA so installed skills can be checked for upstream changes.
- **Shared tools.** At Universe 2026 GitHub announced that you can authenticate once to services such as Vercel, Cloudflare and Sentry, and GitHub configures and manages the MCP server connection across the Copilot app, CLI, VS Code, web and code review.

## 3. Observability earns trust

Metrics, validation and visibility make it possible to judge whether a workflow is reliable enough to receive more autonomy. Validation and tests prove readiness, and measured outcomes allow autonomy to expand.

- **Agent sessions** appear under AI controls for your enterprise, where you can filter and review them.
- **Audit log streaming** can send Copilot agent session events to a SIEM or to Microsoft Agent 365, so agent activity can be reviewed alongside your other agents.
- **OpenTelemetry** monitoring can send data from Copilot clients to an OTel-compatible backend, to analyse agent sessions and usage.
- **Usage metrics** show adoption, acceptance and the share of code written by agents.

The GitHub Blog's safe-step guide applies the same idea to modernisation itself: the more automated checks cover a system, and the more clearly the remaining gaps are named, the bigger the step you can safely take.

## The shift

The true impact goes beyond faster coding tools. **The operating model is the outcome, and observable loops are how you build it.** It represents a fundamental shift in how we work.

## Further reading

- [Monitoring agentic activity in your enterprise](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/monitor-agentic-activity) (GitHub Docs)
- [Copilot usage metrics](https://docs.github.com/copilot/concepts/billing-and-usage/copilot-usage-metrics/copilot-metrics) (GitHub Docs)
- [Custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions) (GitHub Docs)
- [Risks and mitigations for GitHub Copilot cloud agent](https://docs.github.com/copilot/concepts/agents/cloud-agent/risks-and-mitigations) (GitHub Docs)
- [The interaction changes everything: treating AI agents as collaborators, not automation](https://devblogs.microsoft.com/engineering-at-microsoft/the-interaction-changes-everything-treating-ai-agents-as-collaborators-not-automation/) (Engineering@Microsoft)
- [GitHub Universe recap](https://github.com/events/universe/recap) (GitHub)
