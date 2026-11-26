---
title: "AI is accelerating software development"
chapter: 1
hero: "1-AI is accelerating software development.png"
hero_alt: "Slide: AI is accelerating software development. Three steps in a row: development accelerates, engineering activity grows, and complexity increases, with more work to review, secure and govern."
thumb: "thumbs/1-ai-is-accelerating-software-development.webp"
summary: "Development accelerates, activity grows, and complexity increases."
---

??? note "Text version of this slide"

    **AI is accelerating software development**

    1. **Development accelerates:** Teams move faster and take on more complex work.
    2. **Engineering activity grows:** More code, agents, and workflows to coordinate.
    3. **Complexity increases:** More work to review, secure, and govern.

## A chain, not a list

The slide reads left to right because each step causes the next. When teams move faster, more code and more automated agents are involved. When more code and agents are involved, there is more to coordinate, and the sum of that work is harder to review, secure and govern.

The rest of the keynote is a response to the third box. Speed is only useful if the review, security and governance steps can keep pace with it.

## What the data says

GitHub's Octoverse 2026 report, published on the GitHub Blog at Universe, puts numbers on each step.

| Step on the slide | What Octoverse 2026 reports |
| --- | --- |
| Development accelerates | Developers pushed code to GitHub 17.9 billion times in the past 12 months, more than in 2024 and 2025 combined. Commits across all repository types reached 34.3 billion, more than three times the level of two years ago. |
| Engineering activity grows | Merged pull requests more than tripled over the same period to 1.3 billion, an average of 3.5 million a day. By September 2026, more than 40% of pull requests on GitHub started with an agent's first draft, up from 17% in March. |
| Complexity increases | Agent-started pull requests change multiple files more often, about 87% compared with 79% for pull requests without detected agent involvement. Among Copilot's monthly active users, 55% now use agentic features, up from 35% a year ago. |

Octoverse does not measure review effort directly. Multi-file changes are a proxy for how much a reviewer has to take in at once, so treat that row as a signal rather than a measurement.

Agent work is also landing. By September, about 90% of agent pull requests merged within two weeks, against about 86% for pull requests without detected agent involvement. That is the reason review matters so much: this work is being accepted, so the checks that sit in front of the merge button carry real weight.

## What this means for an agency

The same pressure applies inside government. Agencies are not short of ideas for what AI could help build, but the hours available for review, security assurance and audit have not grown with the volume of change. The useful question is not only how to get AI into the hands of developers, but how to keep the checks around it proportionate and visible.

Keep that question in mind. It returns on the last slide as [Faster development, with control](faster-development-with-control.md).

## Further reading

- [Octoverse: Commits, pushes, reach new highs in 2026 as developers build with agents](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/) (GitHub Blog). The source for every figure on this page.
- [GitHub Universe 2026: Evolving every layer of the stack](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) (GitHub Blog). How GitHub responded to these trends at Universe.
