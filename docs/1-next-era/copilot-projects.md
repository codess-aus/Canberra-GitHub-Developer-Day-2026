---
title: "More complex work: Copilot Projects"
chapter: 1
hero: "1.4-More complex work, with developers in control.png"
hero_alt: "Slide: More complex work, with developers in control. GitHub Copilot Projects, marked GA, lets you delegate complex tasks to remote agents, organize projects and tackle more than coding in one app. A screenshot shows the GitHub Copilot app with a list of projects and a customise view offering an Azure DevOps canvas, a design skill and a Microsoft Foundry canvas."
thumb: "thumbs/1-4-more-complex-work-with-developers-in-control.webp"
summary: "Give Copilot a goal and let it coordinate work across repositories."
---

??? note "Text version of this slide"

    **More complex work, with developers in control**

    **GitHub Copilot Projects (GA)**

    Delegate complex tasks to remote agents, organize projects, and tackle more than just coding, all in one app.

    **Less time coordinating work. More time focused on what matters.**

    Lifecycle: building, reviewing, and collaborating (Build and Review highlighted).

    Screenshot: the GitHub Copilot app. The left menu lists New, Pull requests, Issues, Automations, Customize and a list of projects. The main view shows Editor's picks: an Azure DevOps canvas, an Impeccable Design skill and a Microsoft Foundry canvas.

!!! warning "Public preview, not GA"

    The slide marks Projects as **GA**, but Copilot Projects is in **public preview**. GitHub Docs says projects in the GitHub Copilot app are in public preview and subject to change, and the Universe changelog entry says the same. Plan pilots with that in mind.

## From sessions to goals

Most agent tools start from a single task. Projects start from a goal.

GitHub Docs describes a project as a way to give Copilot an ongoing goal and let it coordinate the work across repositories, sessions and recurring tasks. A project can span one or more repositories, or focus on work that does not need a repository at all. Depending on the task, Copilot can start sessions, set up recurring automations or create artefacts.

The Docs give two examples of goals: investigating customer feedback to decide what to improve, and tracking urgent work and in-progress tasks across repositories. That second example shows why this suits larger teams. You follow overall progress in the project instead of directing each session separately.

A project is not always the right tool. For a task in one repository, GitHub suggests starting a session directly from that repository. Use a project when you want Copilot to coordinate toward a broader goal, and give each one a focused goal so related tasks and results stay together.

## Parallel work in one place

The Universe blog says projects let you run agent work across multiple repositories in fully managed, parallel sessions, with one place to track progress, make decisions and direct what happens next. The changelog adds that you can bring in the context Copilot needs, such as repositories, design mocks, Slack threads or notes from a design meeting.

That is the point of the slide's second line. The aim is less time coordinating work and more time on what matters.

## What the screenshot shows

The screenshot is a demonstration workspace. The left menu lists projects such as "Go to market", "Nightly scenario pass" and "Copilot App Quality Monitor", which shows that a project is not limited to coding. The main view is the app's customise screen, where **Editor's picks** include:

- An **Azure DevOps** canvas, described as a way to plan and manage Azure DevOps work in a visual, interactive workspace.
- An **Impeccable Design** skill, for designing, critiquing and polishing product interfaces.
- A **Microsoft Foundry** canvas, for building, testing and deploying hosted agents.

If you use Azure DevOps, the first of these connects directly to [Chapter 4](../4-ado-and-github-copilot/index.md). The Azure DevOps Copilot Plugin, listed in [Resources](../6-resources-and-workshops/index.md), adds an interactive Azure DevOps canvas to the app so you can see work items and pull requests without leaving your session.

## "With developers in control"

Delegating more complex work only makes sense if you can see and limit what agents do. GitHub's guidance points to several controls.

- **Permissions you set centrally.** Enterprise managed permissions can block, require approval for, or allow agent shell commands, file reads and edits, and network domains. GitHub's Well-Architected guidance says these are generally available in the Copilot app, the Copilot CLI and Visual Studio Code sessions that use Agent Host, and suggests requiring approval rather than blocking where teams need flexibility, so workflows keep running with a human in the loop.
- **An audit trail.** The Enterprise AI Controls and agent control plane, generally available since February 2026, add an `actor_is_agent` identifier to audit log entries, alongside the user the agent acted on behalf of. An `agent_session.task` event records when sessions start, finish or fail.
- **A shared allowlist.** Administrators can manage an enterprise-wide MCP allowlist through a central registry URL.

## Further reading

- [Working with projects in the GitHub Copilot app](https://docs.github.com/en/copilot/how-tos/github-copilot-app/working-with-projects) (GitHub Docs). How to create a project and what it can do, with the current release stage.
- [GitHub Copilot app](https://docs.github.com/copilot/concepts/agents/github-copilot-app) (GitHub Docs). The wider app, including projects.
- [GitHub Copilot app, Universe releases](https://github.blog/changelog/2026-10-28-github-copilot-app-universe-releases/) (GitHub Changelog). The Universe release notes for the app.
- [Enterprise AI Controls and agent control plane now generally available](https://github.blog/changelog/2026-02-26-enterprise-ai-controls-agent-control-plane-now-generally-available/) (GitHub Changelog). The audit and policy controls described above.
- [Governing agents](https://learn.github.com/well-architected/library/governance/recommendations/governing-agents/) (GitHub Well-Architected). Recommendations for permissions, auditing and MCP controls.
