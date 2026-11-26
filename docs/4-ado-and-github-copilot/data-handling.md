---
title: "Data handling"
chapter: 4
hero: "4.8 Data Handling.png"
hero_alt: "Slide: Know what reaches the model. Four kinds of Azure DevOps content can enter the model's context, and existing guardrails still apply."
thumb: "thumbs/4-8-data-handling.webp"
summary: "Know what content can reach the model, and which guardrails still apply."
---

??? note "Text version of this slide"

    **Data handling: Know what reaches the model**

    Azure DevOps content returned to the agent can enter the selected model's context, including:

    - Private code
    - PR descriptions and diffs
    - Review comments
    - Build log excerpts

    Content that appears in chat or tool results is retained in local session history.

    Guardrails that still apply:

    - Existing model restrictions, training settings and enterprise policies continue to apply.
    - GitHub-provided models follow the Copilot terms and policies for your plan.
    - Other providers' models: review that provider's terms and data handling.

    **Recommendation:** Match model choice to your data classification before piloting on sensitive repos.

## What the model actually sees

The next question is always about data.

What does the model actually see?

Let me be precise, because precision is what a risk assessor needs.

Azure DevOps content that is returned to the agent can enter the selected model's context.

That includes private code.

It includes pull request descriptions and diffs.

It includes review comments.

And it includes build log excerpts.

There's a second point, about what stays on the machine.

Content that appears in chat or tool results is retained in local session history.

So there's a local footprint, and your device standards apply to it.

Now the reassuring part.

Existing model restrictions, training settings and enterprise policies continue to apply.

You aren't bypassing anything you've already decided.

GitHub-provided models follow the Copilot terms and policies for your plan.

Other providers' models are different.

Review that provider's terms and data handling before you rely on them.

Now our recommendation, and I want to be clear it's ours.

Match model choice to your data classification before piloting on sensitive repos.

For Australian government audiences, think about how your information classification, for example under the PSPF, maps to which models you approve.

The question isn't "is AI safe?"

It's "is this model right for this classification of information?"

That's a question your agency already knows how to answer.

It's the same discipline you apply to any system that handles your data.

So for the pilot, pick a non-sensitive repository.

Prove the workflow where the stakes are low.

Then extend to sensitive work only when your classification and model choices line up.

Know what reaches the model, and you control what the model reaches.

If someone asks, "does our code train the model?", I'd point to the slide.

Existing model restrictions, training settings and enterprise policies continue to apply.

For GitHub-provided models, the Copilot terms and policies for your plan govern.

For other providers, review their terms and data handling directly.

Don't assume, check.

If someone asks, "what's the safest place to begin?", the answer is a non-sensitive repository.

There's very little to lose and a great deal to learn.

And if someone asks, "what about the local session history?", treat it as you would any other working data on a managed device.

Know where it sits and who can reach it.

Here's a question to take back to your teams.

Do your developers know which classification of information they are allowed to put in front of which tool?

If the answer is "not yet", this pilot is a good reason to write it down.

That's the heart of responsible adoption.
