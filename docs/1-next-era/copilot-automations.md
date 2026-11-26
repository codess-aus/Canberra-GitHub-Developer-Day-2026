---
title: "Automate repetitive work: Copilot Automations"
chapter: 1
hero: "1.5-Automate repetitive work, with developers in control.png"
hero_alt: "Slide: Automate repetitive work, with developers in control. Copilot Automations, marked GA, automates repetitive tasks like issue triage and code review, using feedback from results to improve outcomes over time. A screenshot shows the Automations page in a repository, with two automation groups and a list of automations."
thumb: "thumbs/1-5-automate-repetitive-work-with-developers-in-control.webp"
summary: "Agent workflows that run on a schedule or event, and learn from outcomes."
---

??? note "Text version of this slide"

    **Automate repetitive work, with developers in control**

    **Copilot Automations (GA)**

    Automate repetitive development tasks like issue triage and code review, using feedback from results to help improve outcomes over time.

    **Less time on toil. More time building what matters.**

    Lifecycle: building, reviewing, and automating (Build and Review highlighted).

    Screenshot: the Automations page in a repository. Two groups are shown, "Mona Mayhem issue triage" and "PR video demos". Below them is a list of automations, including "Generate plan for assigned issue" (Personal) and "Reproduce bugs" (Shared).

## Define the task once

An automation is a saved agent task that runs without anyone starting it. GitHub Docs says you define your prompt once, choose your triggers and decide which tools Copilot may use. Copilot then runs the automation whenever the trigger fires, and it can take action in the repository where it is configured, such as opening a pull request or labelling an issue.

The documented triggers are:

- **On a schedule:** hourly, daily or weekly.
- **When an issue is created.**
- **When a pull request is opened.**
- **When a pull request is synchronised,** which means new commits are pushed to it.

You can also start any saved automation manually from its card, and run it programmatically through the API. If you turn on **Run in the cloud**, the automation keeps running even when your computer is off.

## Personal or shared

This choice matters most for governance, because it decides whose identity and budget the work uses.

| | Personal | Shared |
| --- | --- | --- |
| Who can see it | Only you | Everyone with access to the repository |
| AI credits are charged to | You | The organisation or user that owns the repository |
| Actions on GitHub use | Your identity | Copilot's identity |

For work that changes shared resources, a shared automation keeps its activity separate from any one person's, because the actions it takes on GitHub use Copilot's identity.

## Learning from outcomes

The slide's second sentence, "using feedback from results to help improve outcomes over time", refers to an announcement made at Universe. According to the GitHub Changelog, automations can now learn from their outcomes and propose improvements to themselves.

The changelog gives three examples:

- An issue triage automation can learn from whether people change the labels it applied.
- A code review automation can learn from whether developers accept its comments.
- A performance automation can learn from whether maintainers merge the pull requests it opens.

The pattern is a pair of automations in a group. One does the work, for instance reviewing each pull request that is opened. The other runs weekly, analyses how people responded and proposes refinements. Automations in a group with the same ownership share persistent storage for artefacts such as results, decisions and feedback, which is how the evaluator can see what happened.

The control sits where the slide's title says it does. Each proposed change to a prompt, tool or trigger comes to you for review, and you accept or reject it before it is applied.

## What the screenshot shows

The two groups in the screenshot are good examples of how to scope an automation.

- **Mona Mayhem issue triage** is described as bounded issue triage that uses the repository's existing labels, with duplicate checks and a durable decision trail.
- **PR video demos** captures concise videos of user-visible pull request changes and posts them to the pull request conversation.

"Bounded" and "decision trail" are the phrases to borrow. An automation that can only choose from labels that already exist, and that records why it chose them, is much easier to trust and to audit than an open-ended one.

## Starting small

A sensible first automation for a team is a low-risk, reversible task such as labelling new issues from your existing set of labels. Start it as a shared automation so its activity is visible, and review the improvements it proposes before accepting any.

On availability, the June 2026 changelog said automations are open to Copilot Pro, Pro+, Max, Business and Enterprise users, and that Business and Enterprise users need the Copilot cloud agent policy enabled by an administrator. It also said each automation is scoped to a single repository.

## Further reading

- [About Copilot automations](https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-automations) (GitHub Docs). Triggers, tools and automation groups.
- [Using automations in the GitHub Copilot app](https://docs.github.com/en/copilot/how-tos/github-copilot-app/using-automations) (GitHub Docs). Creating personal and shared automations, and running them in the cloud.
- [Copilot Automations now learn from outcomes and self-improve](https://github.blog/changelog/2026-10-28-copilot-automations-now-learn-from-outcomes-and-self-improve/) (GitHub Changelog). The Universe announcement.
- [Schedule and automate tasks with Copilot cloud agent](https://github.blog/changelog/2026-06-02-schedule-and-automate-tasks-with-copilot-cloud-agent/) (GitHub Changelog). The original release, with availability and policy notes.
