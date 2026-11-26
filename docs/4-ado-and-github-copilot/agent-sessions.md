---
title: "Agent sessions"
chapter: 4
hero: "4.5 Agent Sessions.png"
hero_alt: "Slide: Describe the task, review the PR. Four steps: start a session, the agent does the work, you stay in the loop, track it to done."
thumb: "thumbs/4-5-agent-sessions.webp"
summary: "Describe the task, let the agent work, and review the pull request."
---

??? note "Text version of this slide"

    **Agent sessions: Describe the task, review the PR**

    1. **Start a session.** Select your connected Azure DevOps repo under "Start session in" and describe the code changes.
    2. **The agent does the work.** It can create a branch, make code changes, commit them and open a pull request.
    3. **You stay in the loop.** Review the agent's changes and respond to any requests for approval.
    4. **Track it to done.** Follow the PR's status in the sidebar, then click View PR to review its checks.

## Talk notes

Now let's look at the experience, because this is where developers will form their opinion.

It's deliberately simple.

Four moves.

One, start a session.

Select your connected Azure DevOps repo under "Start session in", and describe the code changes you want.

Plain language, the way you'd brief a colleague.

Two, the agent does the work.

It can create a branch, make code changes, commit them and open a pull request.

Three, and this is the one I want you to underline: you stay in the loop.

You review the agent's changes, and you respond to any requests for approval.

The human isn't removed. The human is promoted to reviewer.

Four, track it to done.

Follow the pull request's status in the sidebar, then click View PR to review its checks.

It's the same experience as working with a GitHub repository.

So if your people have seen it elsewhere, there's nothing new to learn.

Now an honest note, because your security colleagues will find it anyway.

The agent's tools follow the session's tool permissions.

Depending on those settings, creating a pull request, or replying to and resolving review threads, can run without another approval prompt.

That isn't a flaw, it's a dial.

And dials need a sensible setting.

For public sector pilots, I recommend conservative tool permissions.

Start tight, then loosen based on evidence.

A good rule: trust is earned in sprints, not granted in settings.

If someone asks, "how do I know what the agent did?", the answer is the pull request.

Every change arrives as something a person can read, question and reject.

If someone asks, "will developers get a different experience from what they see on GitHub?", the answer is no.

It's the same experience.

That matters for adoption, because familiar beats clever.

If someone asks, "what does a good first task look like?", I'd suggest something small, well-bounded and low risk.

Think of tasks where a reviewer can tell at a glance whether the change is right.

Save the architecture-changing work for later.

If someone asks, "who is accountable for what the agent produces?", the answer is the person who reviews and approves it.

That's why every request for approval comes back to you.

Our sound bite here is simple.

The agent drafts, the human decides.

Which leads naturally to how the work finally lands.
