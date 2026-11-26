---
title: "Two assumptions"
chapter: 2
hero: "2.3 - Assumptions.png"
hero_alt: "Slide: Two assumptions. Custom applications, not just infrastructure; and people and time are the tightest constraint."
thumb: "thumbs/2-3-assumptions.webp"
summary: "Custom applications, and the tightest constraint: people and time."
---

??? note "Text version of this slide"

    **Let's pause**

    **1. Custom applications, not just infrastructure**

    A large share of your modernisation effort lives inside custom codebases, not just infrastructure upgrades.

    **2. People and time are the tightest constraint**

    You have the intent and budget to act. What's scarce is engineering capacity to change legacy systems safely.

    **Quick check-in:** Which legacy system would you tackle first, and can you modernise it safely?

Before going further, the talk pauses to test two assumptions with the room. Treat them as a self-check too.

## Assumption 1: custom applications, not just infrastructure

A good portion of your current work is custom applications, not only infrastructure upgrades. That matters because the modernisation tooling in this chapter works at the code level. Microsoft Learn describes GitHub Copilot modernization as an agentic, end-to-end solution for upgrading Java, .NET and C++ applications and migrating them to Azure, which is custom code territory.

## Assumption 2: people and time are the constraint, not budget or intent

You have the budget and the intent. What you are short of is engineering capacity to change legacy systems safely, and "safely" is the key word.

The GitHub Blog's guide to choosing the next safe step in application modernisation grades how much of a regression safety net a codebase has:

- At **L0** there is no usable regression net, so the old code and whatever documentation exists is the specification.
- At **L1** the guidance is small reversible changes, old and new paths running in parallel, smoke checks and domain review.

Its worked example establishes a green baseline on the existing stack, puts that baseline into GitHub Actions before changing the production runtime, and only then moves from Java 8 to Java 21 and Spring Boot 3.3. Safe modernisation is sequenced by evidence, which is the theme of the next few pages.

## Check in with the room

Xavier asks for thumbs up if both assumptions are 100% true for you, and thumbs to the side if they are not the whole picture. Then two questions:

- Which system would you tackle first to get out of this mess?
- Can you do it safely?

The answers are used to confirm, correct, challenge or expand the hypothesis. Try them with your own team before reading on.

## Where this leads

That is how the talk lands on its theme: build the system that modernises the app. The case study is from Microsoft's 1 Engineering System, a real product rewrite using agent-driven workflows, and it is mapped back to the PSPF and the ISM as it goes.

## Further reading

- [GitHub Copilot modernization overview](https://learn.microsoft.com/en-us/azure/developer/github-copilot-app-modernization/overview) (Microsoft Learn)
- [How to choose the next safe step in application modernization](https://github.blog/ai-and-ml/github-copilot/how-to-choose-the-next-safe-step-in-application-modernization/) (GitHub Blog)
