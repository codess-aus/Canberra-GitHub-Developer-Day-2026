---
title: "Rewriting the Copilot runtime"
chapter: 1
hero: "1.14 Rewrite.png"
hero_alt: "Slide: A rewrite this size was not affordable before agents. The Copilot agent runtime was ported to 832,378 lines of production Rust across 128 pull requests in about 14.5 weeks, with one developer directing the agents."
thumb: "thumbs/1-14-rewrite.webp"
summary: "A large engineering rewrite delivered incrementally with agent assistance."
---

## A large change, delivered in reviewable slices

GitHub's Copilot agent runtime rewrite is an example of agents contributing to complex engineering work, not just small code completions. The runtime moved from TypeScript to Rust through 128 pull requests, with each change replacing a component incrementally while the rest of the team continued shipping.

GitHub's engineering account reports 832,378 lines of production Rust by 21 August 2026. The work took roughly fourteen and a half weeks, with a developer directing the agents and making decisions about boundaries, quality and direction. The scale is notable, but so is the method: a series of smaller changes that could be built, exercised and reviewed as they landed.

This is not evidence that a codebase rewrite can be safely handed over without engineering oversight. It illustrates how a developer's contribution can shift toward shaping the work, maintaining quality gates and deciding whether each result is ready to merge.

## Further reading

- [Migrating the GitHub Copilot runtime to Rust, using Copilot](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/) (GitHub Blog). The engineering team's detailed account of the rewrite.
