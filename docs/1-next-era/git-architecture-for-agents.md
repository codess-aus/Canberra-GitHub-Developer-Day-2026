---
title: "Git architecture for agents"
chapter: 1
hero: "1.24 simplify.png"
hero_alt: "Diagram of Git architecture principles: simplify the primitives, decouple storage from compute and minimise coordination. Durable repository data sits in Azure Blob Storage, while serving caches scale with demand."
thumb: "thumbs/1-24-simplify.webp"
summary: "Redesign Git's serving architecture to handle more concurrent work."
---

## Change the architecture as demand changes

The diagram sets out three principles for serving repositories as more developers and agents work concurrently: simplify the primitives, separate durable storage from compute, and minimise coordination. Repository data can live durably in Azure Blob Storage while the serving layer uses caches that can be added as demand grows. Branch-level coordination can reduce contention between unrelated work.

This is an infrastructure response to a different workload. Agents can create branches, read history and push updates in parallel, so a repository service needs to handle more simultaneous activity without making every operation wait on every other one.

GitHub reported a load test with 5,000 concurrent agent sessions writing to one repository and 180 times the throughput of the existing architecture for that workload. A follow-up engineering post describes the test sustaining 7,200 pushes per second. These figures describe a specific workload, not a promise that an individual developer's push becomes 180 times faster. The broader aim is more predictable performance when a repository has many concurrent contributors.

## Further reading

- [GitHub Universe 2026: Evolving every layer of the stack](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) (GitHub Blog). The architecture principles and performance context.
- [Inside GitHub's new Git storage architecture](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/) (GitHub Blog). Details of the load test and storage design.
- [The bridge to agent-scale Git infrastructure](https://github.blog/engineering/architecture-optimization/the-bridge-to-agent-scale-git-infrastructure/) (GitHub Blog). How the architecture is evolving toward higher throughput.
- [GitHub Universe recap](https://github.com/events/universe/recap) (GitHub). The keynote's Git architecture announcement.
