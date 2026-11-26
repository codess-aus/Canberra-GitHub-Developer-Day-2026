---
title: "Copilot memory and Dreaming"
chapter: 1
hero: "1.19 Remembers.png"
hero_alt: "Slide: Copilot remembers how your team works. It distinguishes generally available Memory from Dreaming in public preview, and shows code search across accessible repositories."
thumb: "thumbs/1-19-remembers.webp"
summary: "Reuse relevant context, keep repository guidance current and search across repositories."
---

## Carry useful context forward

Copilot Memory stores useful repository facts and personal preferences so they can be reused in later interactions. The slide reports that, in preview CLI sessions using memory, 93% showed better adherence to developer preferences and 42% showed more efficient workflows. These figures describe the sessions GitHub evaluated; they are not a guarantee that memory improves every task.

Dreaming is a separate capability that works in the background to review eligible sessions and feedback, identify useful context, and propose updates to repository instructions or skills. Those proposed changes arrive as pull requests for people to review, rather than silently rewriting the repository's guidance. Dreaming is in public preview and is subject to policy and eligibility requirements.

The slide also points to code search beyond a local checkout. Searching text, symbols, regular expressions or semantic concepts across accessible repositories can help an agent gather context without requiring every repository to be cloned locally. Access permissions still determine what can be searched.

## Further reading

- [About GitHub Copilot Memory](https://docs.github.com/en/copilot/concepts/prompting-and-context/copilot-memory) (GitHub Docs). How personal and repository memories work.
- [About GitHub Copilot Dreaming](https://docs.github.com/en/copilot/concepts/prompting-and-context/copilot-dreaming) (GitHub Docs). How memory curation and proposed guidance changes work.
- [GitHub intelligence puts your code context and history to work](https://github.blog/changelog/2026-10-28-github-intelligence-puts-your-code-context-and-history-to-work/) (GitHub Changelog). Memory, Dreaming and cross-repository search.
