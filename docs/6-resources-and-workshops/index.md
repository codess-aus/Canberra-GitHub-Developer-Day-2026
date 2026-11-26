---
title: Resources and Workshops
chapter: 6
hero: generated/chapter-6-hero.webp
hero_alt: "Chapter 06: Resources and Workshops. Glowing orange, pink, yellow and purple lines flow down the right side."
thumb: thumbs/chapter-6-hero.webp
summary: Resources and workshops to continue learning after the day.
---

Resources and workshops to continue learning after the day.

## Learning paths

### Agentic AI systems

- [Developing in Agentic AI Systems Part 1 of 2](https://learn.microsoft.com/en-us/training/paths/gh-developing-agentic-systems-1) (Microsoft Learn). A self-paced path on designing, deploying and managing agentic AI systems within the software development lifecycle, with modules on the agent lifecycle (plan, act, evaluate), pull request governance, MCP and tool permissions, and observability.
- [Developing in Agentic AI Systems Part 2 of 2](https://learn.microsoft.com/en-us/training/paths/github-agentic-systems-part-two/github-agentic-systems-part-two) (Microsoft Learn). Continues with reliable multi-agent systems using observable workflows, agent memory and state, evaluation signals and quality gates, and governance with least-privilege access and human-in-the-loop approvals.

### GitHub Copilot

- [GitHub Copilot Fundamentals Part 1 of 2](https://learn.microsoft.com/en-gb/training/paths/copilot/) (Microsoft Learn). Core Copilot concepts, responsible use, prompting, and how to start implementing Copilot in your organisation.
- [GitHub Copilot Fundamentals Part 2 of 2](https://learn.microsoft.com/en-gb/training/paths/gh-copilot-2/) (Microsoft Learn). Plan comparisons, agent mode, delegating tasks to Copilot in the cloud, the GitHub MCP Server, and Copilot code review.

### GitHub Advanced Security

- [GitHub Advanced Security Part 1 of 2](https://learn.microsoft.com/en-gb/training/paths/github-advanced-security/) (Microsoft Learn). Introduces GitHub Advanced Security, Dependabot security updates, secret scanning and code scanning.
- [GitHub Advanced Security Part 2 of 2](https://learn.microsoft.com/en-gb/training/paths/github-advanced-security-2) (Microsoft Learn). Goes deeper on CodeQL, rolling out GitHub Advanced Security across an organisation, and managing sensitive data and security policies.

## Azure DevOps and GitHub together

These pages cover the integration points between the two platforms. Two details are worth knowing before you choose a route. The Azure Boards integration sends work items to Copilot in GitHub repositories only, and Azure Repos are not supported there. The GitHub Copilot app integration is the route that works directly with Azure Repos, and it is in public preview.

### Documentation

- [GitHub integration overview](https://learn.microsoft.com/en-us/azure/devops/cross-service/github-integration?view=azure-devops) (Microsoft Learn). How Azure Boards and Azure Pipelines connect to GitHub, including linking commits and pull requests to work items.
- [Use GitHub Copilot with Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/github/work-item-integration-github-copilot?view=azure-devops) (Microsoft Learn). Start Copilot from a work item to create a branch and a draft pull request, with progress tracked on the work item. A started operation cannot be cancelled, so manage or discard the pull request in GitHub if you do not want the result.
- [Integrating Copilot cloud agent with Azure Boards](https://docs.github.com/en/copilot/how-tos/copilot-integrations/integrate-cloud-agent-with-azure-boards) (GitHub Docs). The GitHub side of the same integration: installing the Azure Boards app and sending a work item to the cloud agent.
- [Managing Azure DevOps work with the GitHub Copilot app](https://docs.github.com/en/copilot/how-tos/github-copilot-app/manage-azure-devops-work) (GitHub Docs). Enable the Azure DevOps integration, start agent sessions on Azure Repos, and land pull requests with Agent Merge. The page notes that the integration has no separate audit log, so actions appear in Azure DevOps under the signed-in user's name.
- [Get started with Copilot code review for pull requests](https://learn.microsoft.com/en-us/azure/devops/repos/git/copilot-code-reviews?view=azure-devops) (Microsoft Learn). Turn on Copilot code review for Azure Repos and request reviews automatically with a branch policy. Copilot always leaves a Comment review, so it never approves a pull request or blocks a merge.

### Tools

- [Azure DevOps Copilot Plugin](https://github.com/microsoft/azure-devops-copilot-plugin/) (GitHub). Brings Azure DevOps work items and pull requests into the GitHub Copilot app, including an interactive Azure DevOps canvas.

### Blogs and news

- [Azure DevOps and GitHub: Journeying into the AI Era](https://devblogs.microsoft.com/devops/azure-devops-and-github-journeying-into-the-ai-era/) (Azure DevOps Blog, June 2026). Why AI is the forcing function for moving repositories to GitHub, a hybrid model that keeps Azure Boards and Pipelines, and Microsoft's own migration of 1,575 repositories.
- [GitHub Copilot app Adds Azure DevOps in Public Preview](https://www.technobezz.com/news/github-copilot-app-azure-devops-public-preview) (Technobezz, November 2026). A third-party news summary of the public preview. Check GitHub Docs for the current limits before relying on it.
- [Getting the most out of Azure DevOps and GitHub](https://devblogs.microsoft.com/devops/getting-the-most-out-of-azure-devops-and-github/) (Azure DevOps Blog, November 2024). Practical guidance on using both products, including Microsoft Entra alignment with Enterprise Managed Users and migrating with GitHub Enterprise Importer.
- [Accelerating DevOps with GitHub and Azure](https://azure.microsoft.com/en-us/blog/accelerating-devops-with-github-and-azure/) (Microsoft Azure Blog, May 2019). Background on how the two platforms first came together. It predates the AI features, so treat it as history.

## Security

- [Securing source code with GitHub Advanced Security](https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-source-code-github-advanced-security) (Microsoft Learn). A Secure Future Initiative pattern from the protect engineering systems pillar. It recommends starting with GitHub Advanced Security for Azure DevOps on critical repositories, then phasing in code scanning, dependency scanning and secret protection.

## Videos

- [Recommended video 1](https://youtu.be/kxEsD9osBuU) (YouTube).
- [Recommended video 2](https://youtu.be/TYeC2xd7d1g) (YouTube).

More resources and workshops are coming soon.
