---
title: "Stronger results: Copilot Fusion"
chapter: 1
hero: "1.6-Stronger results, less model selection.png"
hero_alt: "Slide: Stronger results, less model selection. Copilot Fusion, marked GA, brings together the strengths of multiple AI models without developers managing the orchestration. You can bring your own local models to the model picker, and select local models can be orchestrated through Copilot Fusion. A screenshot shows a model menu with Copilot Fusion switched on and effort levels Standard, High and Max."
thumb: "thumbs/1-6-stronger-results-less-model-selection.webp"
summary: "Let Copilot route and combine models, with local models in the mix."
---

??? note "Text version of this slide"

    **Stronger results, less model selection**

    **Copilot Fusion (GA)**

    Copilot brings together the strengths of multiple AI models to tackle complex development tasks, without requiring developers to manage the orchestration.

    **Bring your own local models to /model.** Select local models can now be orchestrated through Copilot Fusion.

    Lifecycle: building and developing (Build highlighted).

    Screenshot: the model menu in the GitHub Copilot app. Copilot Fusion is switched on, with an effort level of Standard, High or Max. A note reads: "Copilot Fusion selects a single model or orchestrates multiple models to complete your task."

## A system, not a model

When you pick Copilot Fusion in the model picker, you are not choosing a model. GitHub Docs describes it as an intelligent runtime router and orchestrator that chooses models and execution patterns for your task, then returns a single response. For example, it can choose one model to draft a solution and a separate model to review it.

GitHub's Docs and changelog list the patterns it can use, including:

- **Single:** one model solves the task directly.
- **Cascade:** an efficient model drafts a response, and a quality check decides whether to accept it or escalate to a stronger model.
- **Critique:** one model drafts while several others critique it in parallel.

GitHub says Fusion combines the multi-model orchestration of Project HydraFusion with the fine-tuned selection of Copilot auto model selection. You no longer switch models during a task or decide which model suits each step.

## Choosing an effort level

The one decision left to you is how much effort to spend. The three levels in the screenshot trade quality against cost and speed.

| Level | What it prioritises | Suits |
| --- | --- | --- |
| Fusion Standard | Versatile models for everyday coding. Balances cost, quality and latency. | Everyday work. Selects one model for each task. |
| Fusion High | Capable models for challenging tasks and deeper reasoning, with moderate token savings. | Substantial, well-scoped tasks, such as fixing a complex bug or changing several files. |
| Fusion Max | The most capable models for the most demanding tasks and complex reasoning. | The hardest problems. |

High and Max can use more than one model for a task, so a task may use more AI credits than it would at Standard. That links back to the usage-based billing on [Simpler access to AI](simpler-access-to-ai.md).

## Why less model selection

Octoverse 2026 shows why this problem exists. Among Copilot users who select a model themselves, 61% used more than one model in September 2026, up from 50% four months earlier. Developers on paid plans used 29 distinct models in May and 47 in September, and no single model carried more than 25% of requests in a month. Developers are already juggling models. Fusion takes that decision away.

On results, the Universe blog reports that in the Artificial Analysis Coding Agent Index, Fusion Max scored within two points of Opus 5.5 Max at half the cost and 40% less time per task. That is GitHub's own reporting of a third-party index, so test it on your own tasks before you rely on it.

## Control for administrators

Hiding model choice from developers does not remove it from the organisation. According to the changelog, enterprise administrators can see which models Fusion picks from, set the effective policy for each model, and disable a model for Fusion without disabling it for everyone. They can also set Fusion, at any effort level, as the default model for Copilot users through Enterprise managed settings.

## Bring your own local models

The second line of the slide covers local models. GitHub Docs explains that in an interactive Copilot CLI session you enter `/model` and look under **Local and self-hosted**. The CLI can discover models served by Ollama on your machine, and you can also add a provider with your own credentials, often called bring your own key.

For a bundled option, the Docs describe MAI Code 1.1 Flash, a coding-optimised model you can run locally. Running a local model means you can use Copilot offline and avoid consuming GitHub AI Credits. Once installed, it also becomes available to Fusion Standard, which uses it where appropriate and leaves cloud models for tasks that need more resources or performance.

Two cautions from the Docs apply:

- **Requirements differ by page.** One Docs page says local models are only downloadable on a Windows PC that meets GPU and memory requirements, while the Fusion page says support covers Windows, macOS and Linux. The Fusion page also names Qwen3.8 Flash Next. Confirm the current list and requirements for your devices.
- **Do not run one local model in several places at once.** Each surface (Copilot CLI, the Copilot app, Visual Studio Code) loads its own copy into memory, which is likely to exhaust RAM.

## Further reading

- [About GitHub Copilot Fusion](https://docs.github.com/en/copilot/concepts/models/copilot-fusion) (GitHub Docs). Execution patterns, effort levels and credit use.
- [Route and orchestrate models with GitHub Copilot Fusion](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/) (GitHub Changelog). The general availability announcement, including admin controls.
- [Adding LLM models to GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-llm-models) (GitHub Docs). Local models, Ollama and bring your own key.
- [Octoverse: Commits, pushes, reach new highs in 2026 as developers build with agents](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/) (GitHub Blog). The model usage figures.
