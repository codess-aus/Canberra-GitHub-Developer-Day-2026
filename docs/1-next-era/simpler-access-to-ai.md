---
title: "Simpler access to AI"
chapter: 1
hero: "1.3-Simpler access to AI across your development organization.png"
hero_alt: "Slide: Simpler access to AI across your development organization. GitHub Enterprise, marked GA, includes access to Copilot for customers who choose this offering. A billing and licensing screenshot shows a banner saying Copilot access is included with GitHub Enterprise Cloud licences."
thumb: "thumbs/1-3-simpler-access-to-ai-across-your-development-organization.webp"
summary: "GitHub Enterprise now includes access to Copilot, billed by usage."
---

??? note "Text version of this slide"

    **Simpler access to AI across your development organization**

    **GitHub Enterprise (GA)**

    For customers who choose this offering, GitHub Enterprise includes access to Copilot, helping reduce barriers to AI adoption across the organization.

    **Bring AI into the workflows your team already use.**

    Lifecycle: across development workflows (Plan, Build, Review, Ship).

    Screenshot: the Billing and licensing page in a GitHub enterprise. A banner reads: "Access to Copilot is now included with your GitHub Enterprise Cloud licenses. Members with Enterprise Cloud can be assigned Copilot access at no additional cost. For other members, Copilot Standalone is available for $10 per month. AI usage is metered and billed separately; no AI credits are included."

## What changed

This slide is about licensing, and it matters because licensing is often the first barrier to a pilot.

The Universe blog states it plainly. From 28 October 2026, GitHub Enterprise customers can use all Copilot features without buying a separate subscription. That includes the GitHub Copilot app, code review, automations and more. You pay for the AI credits you use.

The slide's wording is careful: "for customers who choose this offering". GitHub Docs calls the new model **Copilot access** and describes it as available to eligible enterprises. The Azure DevOps team's post notes that existing customers will be onboarded to the new model in phases, so do not assume your enterprise has switched over automatically.

## How Copilot access compares

GitHub Docs sets the new model next to the existing plans.

| | Copilot Business | Copilot Enterprise | Copilot access |
| --- | --- | --- | --- |
| Seat charge | $19 USD per user per month | $39 USD per user per month | $0 for users with a GitHub Enterprise Cloud licence. $10 USD per user per month as Copilot Standalone for users without one. |
| Included usage | 1,900 per user per month, pooled | 3,900 per user per month, pooled | None. Metered usage is billed from the first use. |

The screenshot on the slide shows the same idea in the product. The billing page lists Copilot access as included with Enterprise Cloud licences, and says AI usage is metered and billed separately with no AI credits included.

## What to know before you plan a budget

GitHub Docs lists several rules that affect how you roll this out.

- **Access is not automatic.** Enterprise owners must assign Copilot seats to individual members, enterprise teams or organisations. That applies to people who already hold a GitHub Enterprise Cloud licence.
- **It applies to the whole enterprise.** You cannot combine Copilot access with Copilot Business or Copilot Enterprise seats in the same enterprise, including in individual organisations.
- **You can mix the two access routes.** An enterprise can have some developers on their Enterprise Cloud licence and others on Copilot Standalone at the same time.
- **Usage needs watching.** The billing menu in the screenshot includes **Cost centers** and **Budgets and alerts**. With usage billed separately, these are the tools that keep spend predictable.

For a pilot, three questions are worth settling early. Who will be assigned seats? Who owns the AI credit budget? How will you watch usage as the pilot grows?

## Why it matters if you use Azure DevOps

The Azure DevOps team's post after Universe connects this to [Chapter 4](../4-ado-and-github-copilot/index.md). GitHub Enterprise Cloud licences already include Azure DevOps Basic usage rights. The post says GitHub Enterprise Cloud now also includes Copilot access at no additional seat charge, including use of the GitHub Copilot app with Azure DevOps. AI usage is billed separately through AI credits, and without Enterprise Cloud you can buy a standalone Copilot licence instead.

## Further reading

- [What's changing with GitHub Enterprise and Copilot billing](https://docs.github.com/copilot/get-started/whats-changing-with-github-enterprise-and-copilot) (GitHub Docs). The authoritative source for plans, seat charges and the rules above.
- [GitHub Universe 2026: Evolving every layer of the stack](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) (GitHub Blog). The announcement.
- [Azure DevOps and GitHub: Start Your Agentic Journey Where You Are](https://devblogs.microsoft.com/devops/azure-devops-and-github-start-your-agentic-journey-where-you-are/) (Azure DevOps Blog). How the licensing change applies to Azure DevOps teams.
