---
title: "Controls & assurance"
chapter: 4
hero: "4.7 Governance Questions.png"
hero_alt: "Slide: Governance questions agencies will ask. A table of five questions, what GitHub Docs say and what it means for agencies, plus two gaps to plan for."
thumb: "thumbs/4-7-governance-questions.webp"
summary: "The five governance questions agencies will ask, and two gaps to plan for."
---

??? note "Text version of this slide"

    **Controls & assurance: Governance questions agencies will ask**

    | Question | What GitHub Docs say | What it means for agencies |
    | --- | --- | --- |
    | Who can access what? | Azure DevOps permissions apply to every action; connecting grants no extra access. | Existing ADO security groups and branch policies stay the control plane. |
    | Can we limit it to certain repos? | No setting restricts it to selected repos; ADO permissions govern access. | Scope pilots through ADO project and repo permissions. |
    | Is there an audit trail? | No separate audit log in the app; actions appear in ADO under the signed-in user. | Use Azure DevOps auditing and PR history. |
    | Do agents act without approval? | Tools follow session permissions; some PR actions may run without a prompt. | Set conservative tool permissions; keep Agent Merge off at first. |
    | How do we revoke access? | Signing out removes local tokens but does not revoke access with Microsoft. | Revoke via Microsoft Entra; add it to offboarding. |

    Two gaps to plan for:

    - **No per-repo restriction:** Scope access with Azure DevOps permissions.
    - **No separate audit log:** Actions show in Azure DevOps under each user.

    Source: GitHub Docs, "Managing Azure DevOps work with the GitHub Copilot app" (public preview), docs.github.com

## The governance questions, one at a time

Now to the slide I suspect many of you came for.

These are the governance questions agencies will ask, and I'd rather we take them head on.

The middle column is what GitHub Docs say.

The right column is our recommended interpretation for agencies.

Let me take them one at a time.

Who can access what?

Azure DevOps permissions apply to every action, and connecting grants no extra access.

So your existing security groups and branch policies stay the control plane.

You don't need a second rulebook.

Can we limit it to certain repos?

Here's the first gap.

There is no setting that restricts it to selected repositories.

Azure DevOps permissions govern access.

So scope your pilot through project and repo permissions.

Is there an audit trail?

Here's the second gap.

There's no separate audit log in the app.

Actions appear in Azure DevOps under the signed-in user.

So use Azure DevOps auditing and pull request history.

Do agents act without approval?

Tools follow session permissions, and some pull request actions may run without a prompt.

So set conservative tool permissions, and keep Agent Merge off at first.

How do we revoke access?

Signing out removes local tokens, but it does not revoke access with Microsoft.

So revoke through Microsoft Entra, and add it to your offboarding process.

I've put two gaps on this slide in a box, and I did that on purpose.

No per-repo restriction, and no separate audit log.

I'd rather tell you now than have you discover it later.

Honesty is the shortest route to a yes from a security team.

Every gap has a mitigation, and every mitigation lives in tools you already run.

The principle I'd leave you with: don't ask agents to be more trustworthy than your people.

If a security officer pushes back on the gaps, I'd answer in three sentences.

Yes, there's no per-repo restriction setting in the app.

Yes, there's no separate audit log in the app.

And no, that doesn't leave you blind, because Azure DevOps permissions scope access, and actions appear in Azure DevOps under each signed-in user.

If someone asks, "can we get an agent-specific audit report?", I'd say what the docs say today.

Actions appear in Azure DevOps under the signed-in user, so use Azure DevOps auditing and pull request history.

If it changes while the product is in preview, we'd want to tell you.

And on offboarding, please don't miss the Entra point.

Signing out clears local tokens, but revoking access happens in Microsoft Entra.

The best audit is the one that tells a clear story: who did what, when, and who approved it.

Hold them to the same controls.
