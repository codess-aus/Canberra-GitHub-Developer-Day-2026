---
title: "The capability"
chapter: 4
hero: "4.2 ADO Integrations.png"
hero_alt: "Slide: What the integration does. Five steps: clone, branch and code, open PR, review, and Agent Merge. A note says the integration is in public preview."
thumb: "thumbs/4-2-ado-integrations.webp"
summary: "Clone, branch and code, open a pull request, review, and optionally Agent Merge."
---

??? note "Text version of this slide"

    **The capability: What the integration does**

    1. **Clone.** Add an Azure DevOps repo by organisation name and clone it into the app.
    2. **Branch and code.** An agent session creates a branch, makes code changes and commits them.
    3. **Open PR.** The agent opens a pull request in your Azure DevOps repository.
    4. **Review.** Track status in the sidebar, then View PR to check changes, checks and comments.
    5. **Agent Merge.** Optionally let an agent fix feedback, CI failures and conflicts, then complete.

    Public preview: the Azure DevOps integration is subject to change. It is disabled by default and enabled per user in the app.

## Talk notes

Here's the whole lifecycle on one slide, left to right.

Five steps, and every one of them happens against your Azure DevOps organisation.

Step one, clone.

You add an Azure DevOps repo by organisation name and clone it into the app.

Step two, branch and code.

An agent session creates a branch, makes code changes and commits them.

That's the ordinary work, the part nobody enjoys doing at four in the afternoon.

Step three, open a pull request.

The agent opens the pull request in your Azure DevOps repository.

Not in a side system, not in a copy.

In the place your reviewers already look.

Step four, review.

You track status in the sidebar, then choose View PR to check the changes, the checks and the comments.

Step five, Agent Merge.

This one is optional.

It lets an agent fix feedback, CI failures and conflicts, and then complete the pull request.

I'll spend more time on that shortly, because it's the step that deserves your attention.

One thing to hold on to: the agent acts as the signed-in user.

It isn't a mysterious new identity wandering around your estate.

It's a person, with their permissions, getting help.

And a reminder at the bottom of the slide.

This is public preview, it's subject to change, it's disabled by default, and it's enabled per user in the app.

Nobody gets this by accident.

If someone asks, "will this just appear on our developers' machines?", the answer is no.

Someone has to switch it on, deliberately.

Speed is the benefit; deliberate choice is the control.

If someone asks, "does the agent get its own login?", the answer is on this slide.

The agent acts as the signed-in user.

If someone asks, "can it change things we haven't allowed?", the answer is the same.

Azure DevOps permissions apply to every action, so it can only do what that person could do.

And if someone asks, "what's the one step I should be most careful about?", it's Agent Merge.

It's optional for a reason, and I'd treat it as something you earn.

Here's a question for the room.

Which of these five steps takes your team the most time today?

For many teams it's the review and rework loop, and that's exactly where the sidebar and Agent Merge are aimed.

That brings us to what you need before you start.
