---
title: "GitHub Copilot @ Microsoft highlights"
chapter: 2
hero: "2.8 Microsoft Adoption.png"
hero_alt: "Slide: GitHub Copilot @ Microsoft highlights. Internal adoption figures including 47.8k employees with access and an 81% active rate."
thumb: "thumbs/2-8-microsoft-adoption.webp"
summary: "Internal adoption figures from Microsoft."
---

??? note "Text version of this slide"

    **Internal adoption**

    1ES scaled Copilot adoption through an easy opt-in experience backed by GitHub Enterprise Managed Users. Adoption is viral within many teams.

    **Copilot brings our engineers**

    - Increased productivity and efficiency: get more done with less task-switching
    - Developer happiness from using industry-leading AI tools
    - A chance to contribute to the success of the Copilot product by dogfooding and sharing feedback

    **By the numbers**

    - **47.8k:** Microsoft employees with access to GitHub Copilot
    - **81%:** Active percentage of engineers who have used the Copilot extension
    - **62k / 218k:** Employees with GitHub accounts (individual / EMU) to enjoy Copilot anywhere
    - **29 to 40%:** Suggestion acceptance rate range observed

Here is more data on internal Copilot adoption at Microsoft. It was taken up quickly and positively, and the vast majority of engineers, **81%**, are using the Copilot extension.

## How the rollout scaled

1ES scaled adoption through an easy opt-in experience backed by GitHub Enterprise Managed Users (EMU). With EMU you manage the lifecycle and authentication of users from your own identity provider: people authenticate there, and you control usernames, organisation membership and repository access from it. Entra ID is supported using OpenID Connect or SAML, with SCIM provisioning creating the accounts. Managed user accounts cannot create public content or collaborate outside the enterprise, which is what lets a large organisation open up Copilot without losing governance.

The numbers show the reach: **47.8k** Microsoft employees have access to GitHub Copilot, and **62k** individual and **218k** EMU accounts mean Copilot is available wherever people work. Adoption is described as viral within many teams.

Microsoft's IT organisation describes the early approach in similar terms: start by making AI visible in the tools engineers already use, and let small wins on low-risk tasks build confidence and organic adoption.

## Reading the acceptance rate

Roughly a third up to **40%** of suggestions were accepted. The talk draws two lessons from that. Firstly, humans are still building the guardrails and quality assurance is still in place. Secondly, the team is being realistic about outcomes and how to improve them.

It helps to know what the metric means in GitHub's own reporting. Code completion acceptance rate is the percentage of suggestions accepted by users, so it measures acceptance in the editor rather than what reaches production. Pair it with lines of code changed with AI, the share of lines added by agents, pull request throughput and review time to get a rounded picture.

## What engineers said

Specific feedback is that Copilot enables less task-switching, and encourages more collaboration through dogfooding and sharing experience. The slide adds developer happiness from using industry-leading AI tools, and the chance to contribute to Copilot's success by sharing feedback.

## Scaling it in your own organisation

At GitHub Universe 2026, GitHub announced that Enterprise customers can use all Copilot features without buying a separate subscription, paying for the AI credits they use. That includes the GitHub Copilot app, code review and automations, and it lowers the barrier to the kind of opt-in rollout described here.

So what does this look like in your world? The next page turns the lessons into three things to take away: [Takeaways](takeaways.md).

## Further reading

- [About Enterprise Managed Users](https://docs.github.com/admin/authentication/managing-your-enterprise-users-with-your-identity-provider/about-enterprise-managed-users) (GitHub Docs)
- [Data available in Copilot usage metrics](https://docs.github.com/copilot/reference/copilot-usage-metrics/copilot-usage-metrics) (GitHub Docs)
- [GitHub Universe 2026: Evolving every layer of the stack](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) (GitHub Blog)
- [Powering the new age of AI-led engineering in IT at Microsoft](https://www.microsoft.com/insidetrack/blog/powering-the-new-age-of-ai-led-engineering-in-it-at-microsoft/) (Microsoft Inside Track)
