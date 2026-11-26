---
title: "Review & complete"
chapter: 4
hero: "4.6 Agent Merge.png"
hero_alt: "Slide: Agent Merge lands it within policy. You stay the approver with Fix, Approve and Complete, and Agent Merge is opt-in per pull request."
thumb: "thumbs/4-6-agent-merge.webp"
summary: "You stay the approver, and Agent Merge is opt-in per pull request."
---

??? note "Text version of this slide"

    **Review & complete: Agent Merge lands it within policy**

    You stay the approver:

    - **Fix:** Click Fix on a review comment to have an agent address it.
    - **Approve:** Click Approve when you are ready to approve the PR.
    - **Complete:** Review the confirmation and confirm the merge.

    Agent Merge, opt-in per PR:

    - Addresses review feedback
    - Fixes CI failures
    - Resolves conflicts
    - Completes the PR when Azure DevOps checks and policies pass

    Once enabled for a PR, the agent can complete it without a separate confirmation.

    Your Azure DevOps permissions and the repository's checks and policies decide whether a PR can be approved or completed.

## Talk notes

This slide is about the last mile: getting from "the agent finished" to "it's in the codebase".

The headline is that Agent Merge lands it within policy.

Let me start with the left side, where you stay the approver.

Three actions.

Fix: click Fix on a review comment, and an agent addresses it.

Approve: click Approve when you are ready to approve the pull request.

Complete: review the confirmation, and confirm the merge.

Notice who is clicking.

You are.

The agent can do the typing, but the decision stays with a person.

Now the right side, Agent Merge, which is opt-in per pull request.

When enabled, the agent addresses review feedback, fixes CI failures, resolves conflicts, and completes the pull request when Azure DevOps checks and policies pass.

That's real time saved.

Anyone who has waited on a merge conflict knows the pain.

But read the bottom of the card carefully.

Once enabled for a pull request, the agent can complete it without a separate confirmation.

So this is a power feature, and it should be treated like one.

My advice for pilots is to keep it off to start.

Earn the right to turn it on.

And here's the reassurance underneath.

Your Azure DevOps permissions, and the repository's checks and policies, decide whether a pull request can be approved or completed.

Branch policies and required reviewers remain the real gate.

If the checks don't pass, nothing completes.

The agent can't talk its way past a build policy.

So the sound bite for this slide is: automation proposes, policy disposes.

Speed with a safety net.

If someone asks, "what stops a bad change from merging?", the answer is your branch policies and required reviewers.

They were designed for human mistakes, and they work just as well on agent-assisted work.

If someone asks, "should we turn Agent Merge on?", my honest answer is: not on day one.

Let your reviewers get comfortable first.

Look at the quality of the agent's pull requests over a sprint.

Then decide, per pull request, where the automation earns its place.

And here's a question for the room.

What fraction of your review time goes on chasing CI failures and conflicts rather than judging the actual change?

That's the time Agent Merge is trying to give back.

Handing the tedious bits to an agent frees your experts for the judgement bits.

Now let me turn to the questions you'll be asked.
