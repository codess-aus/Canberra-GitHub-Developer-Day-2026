---
title: "Why it matters"
chapter: 4
hero: "4.1 - Bring Agents to Your Repos.png"
hero_alt: "Slide: Bring agents to your repos. Three cards: code stays put, same permissions, and policies gate merges."
thumb: "thumbs/4-1-bring-agents-to-your-repos.webp"
summary: "Code stays put, permissions stay the same, and policies still gate merges."
---

??? note "Text version of this slide"

    **Why it matters: Bring agents to your repos**

    Work with Azure DevOps repositories and pull requests without leaving the GitHub Copilot app.

    1. **Code stays put.** Clone Azure DevOps repositories into the app and start agent sessions just as you would for a GitHub repository.
    2. **Same permissions.** Azure DevOps permissions apply to every action. Connecting your account does not grant additional access.
    3. **Policies gate merges.** Your permissions and the repository's configured checks and policies decide who can approve or complete a PR.

    The agent works inside the guardrails your agency already runs in Azure DevOps.

## Talk notes

Let me start with why this matters to government.

Most agencies I speak with aren't starting from a blank page.

They have large estates in Azure Repos, years of history, and branch policies that took real effort to get right.

The worst answer to "how do we adopt agents?" is "first, move all your code."

This integration takes the opposite approach.

It brings the agent to your repository, not your repository to the agent.

Three ideas on this slide, and each one is a promise.

First, code stays put.

You clone your Azure DevOps repository into the app and start an agent session, just as you would for a GitHub repository.

No migration project, and no new home for your source.

Second, same permissions.

Azure DevOps permissions apply to every action.

Connecting your account does not grant additional access.

If you couldn't do it yesterday, the agent can't do it today.

Third, policies gate merges.

Your permissions, plus the checks and policies configured on the repository, decide who can approve or complete a pull request.

The agent doesn't get a side door.

If this slide were a coffee mug, it would say: new capability, same controls.

That's the line I'd like you to take back to your security team.

Because their first question will be, "does this change our risk model?"

And the honest answer is: it changes how fast work moves, not who is allowed to approve it.

Let me give you the version for a senior executive, in thirty seconds.

Your people already work in Azure DevOps.

Your controls already live in Azure DevOps.

We're adding an assistant to that place, not asking you to build a new one.

If someone asks, "doesn't this mean our code leaves our environment?", I'd answer carefully.

The repository stays in Azure DevOps, and the later slides cover exactly what content can reach the model.

So I won't wave that question away, I'll show you the specifics when we get to data handling.

Think of this slide as the principle, and the rest of the session as the proof.

So let's see what it actually does.
