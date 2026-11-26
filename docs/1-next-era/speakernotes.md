Here are the speaker notes from the images just added, in markdown. Every slide in that range has notes. 

# Speaker Notes: Slides 9–48

## Slide 9

Today is about one idea: security that starts at the first commit and keeps pace with AI-speed development.

We'll cover three things. Getting secure: finding and fixing the risk already in your code. Staying secure: keeping new risk out of every push, pull request, package and pipeline, on GitHub and on Azure DevOps. Secure by default: making the safe path the easy one, for developers and for AI agents.

Everything shown is either generally available or clearly marked as preview.

## Slide 10

GitHub now serves more than 225 million developers. In the US and India alone, each added more than 10 million developers this year.

That number is people learning, shipping, reviewing each other's work and making code reusable for the next developer. This isn't a niche experiment in agentic development: an enormous global community is making the transition together.

Source: Octoverse 2026, https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/

## Slide 11

The scale of activity in the 12 months to 30 September 2026, across public and private repositories:
- 17.9 billion pushes, more than 2024 and 2025 combined
- 34.3 billion commits, more than three times two years ago
- 1.3 billion merged pull requests, about 3.5 million a day
- 2.5 billion public open source contributions, more than double last year

GitHub Actions ran a job 1,440 times every second, 124 million a day.

Source: Octoverse 2026, https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/

## Slide 12

The shape of the curve matters more than any single number. Growth bent sharply upward from mid-2026 as agents took on more of the work: by September, commits were running at about six times September 2025 levels.

The last few months alone have seen more merged pull requests, commits and new repositories than years before them. Agent-driven development is letting every developer build what was only a plan a year ago.

Source: Octoverse 2026, https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/

## Slide 13

This is the single clearest signal of the shift. By September 2026, more than 40% of pull requests on GitHub started with an agent's first draft, up from 17% in March. That's 110 million agent-started pull requests in September alone.

And they're good pull requests: about 90% of agent-started pull requests were merged within two weeks, against about 86% for others.

Teams that give agents context see more: new repositories with an agent configuration file, such as AGENTS.md or custom instructions, logged eight times the commits of those without.

Source: Octoverse 2026, https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/

## Slide 14

Closer to home. More than 2.57 million Australian developers build on GitHub, up 30% year on year, which is more than 2,200 new developers every day.

Activity is growing even faster than headcount: Australian developers uploaded code more than 5.26 million times in the June quarter, up 111% on a year earlier. Australian developers and organisations own more than 4.8 million repositories.

Figures are from the GitHub Innovation Graph for the quarter to 30 June 2026, released by GitHub at Universe.

Sources:
- GitHub Universe 2026 Australian press release (as published by KBI.Media): https://kbi.media/press-release/news-from-github-universe-2026-2-57-million-australian-developers-github-rebuilds-for-the-agentic-era/
- GitHub Innovation Graph: https://innovationgraph.github.com/

## Slide 15

Our day-to-day work has changed. In a couple of years we've gone from writing every line ourselves, to pair-programming with AI, to delegating whole pieces of work to agents that plan and implement while we verify.

It can feel like the developer is disappearing. It isn't. It's the craft maturing. We set direction, provide the right context, steer the work and decide whether the result is good enough to ship.

The unit of value a developer brings has never been lines of code. It's completed work: more bugs fixed, more features shipped, more security issues resolved.

Source: Jay Parikh, GitHub Universe 2026 keynote blog, https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/

## Slide 16

Here's the catch. Writing code got dramatically cheaper. Knowing whether that code is correct, secure and ready to ship did not.

Independent telemetry from 22,000 developers across more than 4,000 teams compared each organisation's lowest and highest periods of AI adoption. Median time a pull request spends in review rose about 441%, and pull requests merged with no review at all rose about 31%. These are industry figures, not GitHub-wide numbers, and they show correlation rather than cause, but they describe the pressure most teams feel.

The answer isn't asking the same reviewers to read faster. It's better checks earlier, clearer context, and agents that help with verification, not just generation. That's a big part of what GitHub announced at Universe.

Source: Faros AI, AI Engineering Report 2026, "The Acceleration Whiplash", https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways

## Slide 17

The classic delivery lifecycle is drawn as a tidy circle: plan, build, deploy, observe. Real work is never that tidy, and as we move faster the cracks get wider.

Work can start from an issue, a dependency update or a customer signal. It can also start from a new vulnerability, a failed check or a production alert. Agents can help at every stage, building and verifying, while the platform carries context forward and learns from what happened.

Developers stay accountable for intent and outcomes. What's needed is a system that connects the stages, not a series of disconnected AI interactions.

Source: Jay Parikh, GitHub Universe 2026 keynote blog, https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/

## Slide 18

Three questions to judge any agentic development platform:
- Velocity: can it get from idea to completed software quickly and cost-effectively?
- Intelligence: does it combine context across the platform and get better as you use it?
- Quality: is completed work secure by default, with bugs caught before they ship?

This isn't a pick-two choice. Speed without quality just moves the bottleneck downstream, and intelligence without context creates noise. GitHub's direction is to deliver all three across the whole delivery system.

Source: Jay Parikh, GitHub Universe 2026 keynote blog, https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/

## Slide 19

No engineering organisation works in a single tool. Designs live in Figma, operational signals in Datadog, infrastructure in Cloudflare, and so on.

GitHub stays open and extensible, so teams keep the tools they depend on and connect them to the platform. The quality of an agent's work depends on the context it can reach and the boundaries it's given. The goal is a connected delivery system, not another isolated assistant.

Source: Jay Parikh, GitHub Universe 2026 keynote blog, https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/

## Slide 20

This is what GitHub shipped and announced across the platform at Universe, more than 100 announcements in total. Over the next part of the session we'll go through the highlights: the Copilot app and Projects, Copilot Fusion, memory and dreaming, automations, session continuity, Agent Merge, AI security scanning, stacked pull requests and a new Git architecture built on Azure.

Source: GitHub changelog, Universe 2026 label: https://github.blog/changelog/label/universe26/

## Slide 21

Let's start with GitHub Copilot, and what we're seeing as developers move from writing every line to directing agents.

## Slide 22

What we're seeing with GitHub Copilot is a move from suggestions to delegation.
- More than 140,000 organisations use GitHub Copilot, nearly triple a year earlier (May 2026).
- Copilot cloud agent, the agent that works on an issue and opens a pull request, grew 230% year on year, against 85% for agent chat.
- Copilot code review passed 60 million reviews and accounts for more than one in five code reviews on GitHub (March 2026).
- About 90% of agent-started pull requests are merged within two weeks.

Sources:
- Gartner Magic Quadrant post (140,000 organisations): https://github.blog/ai-and-ml/github-copilot/github-recognized-as-a-leader-in-the-gartner-magic-quadrant-for-enterprise-ai-coding-agents-for-the-third-year-in-a-row/
- Octoverse 2026: https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/
- 60 million Copilot code reviews: https://github.blog/ai-and-ml/github-copilot/60-million-copilot-code-reviews-and-counting/

## Slide 23

The GitHub Copilot app is designed from the ground up for agentic software delivery. It's generally available on every Copilot plan.

It's where developers, and the people around them, run many streams of agent work at once and get them all the way to merge: parallel sessions in their own worktrees, Copilot watching CI and review comments until the pull request is ready, canvases for specs and reports, and connectors to the tools your team already uses. For enterprises it brings app policies, managed settings, sandboxes, OpenTelemetry and the audit log.

Sources:
- GitHub Copilot app generally available: https://github.blog/changelog/2026-06-17-github-copilot-app-generally-available/
- Copilot app Universe releases: https://github.blog/changelog/2026-10-28-github-copilot-app-universe-releases/

## Slide 24

Copilot Projects, in public preview in the Copilot app, let you delegate outcomes rather than individual sessions.

Describe the goal and add context such as repositories, design mocks, Slack threads or meeting notes. A project can span several repositories, or none. Copilot runs as many agents as the work needs in fully managed, parallel sessions, and brings the results back, such as pull requests. The overview groups work by status (needs input, open, working, done), so you spend less time managing execution and more time deciding what's worth building.

Also in public preview in the app: computer use on macOS and Windows, with approval first, and image generation for mock-ups.

Sources:
- Copilot app Universe releases: https://github.blog/changelog/2026-10-28-github-copilot-app-universe-releases/
- Working with projects: https://docs.github.com/en/copilot/how-tos/github-copilot-app/working-with-projects

## Slide 25

Here's what this looks like at real scale, from GitHub's own engineering team.

The Copilot agent runtime, the harness behind the Copilot CLI, the Copilot app and the Copilot SDK, was completely rewritten from TypeScript into Rust using the Copilot app and Copilot CLI. By 21 August the runtime was 100% production Rust: 832,378 lines, landed across 128 pull requests over roughly fourteen and a half weeks, shipped incrementally while the main branch kept moving.

A project that would have taken a whole team a year or two was completed primarily by a single developer. His role was to frame problems, set boundaries, enforce quality gates and decide direction. Human judgement stayed heavily involved; the developer's involvement moved up a level.

Source: Stephen Toub, "Migrating the GitHub Copilot runtime to Rust, using Copilot", https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/

## Slide 26

Model choice is one of Copilot's strengths, but it can be hard to know which model to use for which task, and the best result sometimes needs more than one.

Copilot Fusion, now generally available, evaluates what a task needs across reasoning, code generation, debugging and tool use, then chooses whether to use one model or combine several, down to individual steps. The goal is frontier-level quality at lower cost. It draws on models from Anthropic, OpenAI, Google, Microsoft and more, within your organisation's model policies.

Source: Route and orchestrate models with GitHub Copilot Fusion, https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/

## Slide 27

The results are strong. In the Artificial Analysis Coding Agent Index, Copilot Fusion Max scored 60, within two points of Claude Code with Opus 5.5 Max. It did that at about half the average cost per task, using about half as many tokens and taking about 40% less time per task.

In a November update, Fusion Max reached a 71.2% resolution rate on Terminal-Bench 4.1, and Fusion arrived on the web, mobile and Visual Studio.

Sources:
- Copilot Fusion GA: https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/
- Copilot Fusion updates, 17 November 2026: https://github.blog/changelog/2026-11-17-github-copilot-fusion-updates-more-availability-benchmarks-and-models/
- Artificial Analysis: https://artificialanalysis.ai/

## Slide 28

How it works. Developers pick an effort level, Standard, High or Max, in the model picker. Fusion then decides how to execute:
- Single: one selected model solves the task directly.
- Cascade: an efficient model produces a candidate, then a gate accepts it or escalates to a stronger model.
- Critique: one model drafts, an independent read-only critic reviews, and the drafting model revises once.

Admins stay in control: Fusion only uses models enabled in your model policies, and can be made the default.

Source: Route and orchestrate models with GitHub Copilot Fusion, https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/

## Slide 29

Developers don't use one model any more, and they shouldn't be locked into one agent.
- 61% of Copilot users who choose a model themselves used more than one in September. Paid plans used 47 distinct models, and no model carried more than 25% of requests.
- Agent HQ delivered on its promise: Claude and Codex agents are available inside paid Copilot subscriptions, alongside Copilot.
- Copilot connectors, in public preview on all plans, give one-click access to 26 GitHub-verified services, including Slack, Figma, Notion, Sentry, Linear, Atlassian Rovo, Cloudflare, Vercel and Work IQ.
- The GitHub Copilot SDK is becoming the Microsoft Copilot SDK, the programmable interface to the same agent harness.

Sources:
- Octoverse 2026: https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/
- Claude and Codex for Copilot Business and Pro: https://github.blog/changelog/2026-02-26-claude-and-codex-now-available-for-copilot-business-pro-users/
- Copilot connectors: https://github.blog/changelog/2026-10-28-connect-your-tools-to-copilot-without-all-the-setup/
- Universe 2026 changelog: https://github.blog/changelog/label/universe26/

## Slide 30

GitHub intelligence is the context and learning layer, drawn from the graph of GitHub data, so agents remember how you work and keep improving.
- Copilot Memory is generally available on paid plans. Memories can be created from the app, CLI, VS Code, cloud agent, code review, Slack, Teams and Mobile. In preview CLI sessions that used memory, 93% showed better adherence to developer preferences and 42% showed more efficient workflows.
- Dreaming, in public preview and opt-in by admin policy, curates memories in the background and proposes repository instruction and skill changes as pull requests for you to review.
- Code search now reaches beyond your local checkout: text, symbol, regex and semantic search across the repositories you can access. Use /research to ask questions such as "where could retries overlap across these services?"

Source: GitHub intelligence puts your code context and history to work, https://github.blog/changelog/2026-10-28-github-intelligence-puts-your-code-context-and-history-to-work/

## Slide 31

Two ways to put agents to work automatically.

Copilot Automations, generally available, are the quick way: set a prompt, trigger and tools, and a Copilot cloud agent runs the task, such as issue triage, code review or a weekly changelog draft. New at Universe: a REST API trigger for services like Jira, Sentry and PagerDuty, 24 new GitHub triggers, chaining, 20 new GitHub tools plus custom MCP tools, and AI credit limits. Automations now learn from outcomes, for example from label corrections or accepted review comments, and propose prompt changes that you approve.

GitHub Agentic Workflows, an open-source project from GitHub Next, are now generally available: automation as code, written in Markdown and compiled to standard Actions YAML, running sandboxed and read-only by default, with writes applied through controlled safe outputs.

Accenture's results with Agentic Workflows: one lead saved an estimated 29 hours a week; AI now authors 91% of the team's commits; and production errors fell from about 11,000 a day to under 1,000.

Sources:
- Agentic Workflows GA: https://github.blog/changelog/2026-10-28-github-agentic-workflows-generally-available/
- Universe 2026 keynote blog: https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/

## Slide 32

Your work shouldn't restart when you switch devices or tools. The connected Copilot cloud experience, now generally available on paid plans, lets you start and follow the same cloud agent session across the web, GitHub Mobile, the Copilot app, the CLI, VS Code, Slack and Microsoft Teams. Start it from your phone at stand-up, steer it from VS Code at your desk and check in from github.com. The agent keeps working in the cloud.

Cloud sandboxes are generally available: they start fast, snapshot and resume, and have no one-hour limit, drawing on your included Actions entitlement. Local sandboxes are generally available too, now including JetBrains, so you can limit what an agent can touch on a developer machine.

Copilot also keeps expanding where developers already work: Fusion, local sandboxes and next edit suggestions in JetBrains, and Copilot in Xcode's built-in coding assistant in public preview.

Sources:
- Connected Copilot cloud experience: https://github.blog/changelog/2026-10-28-work-from-anywhere-with-a-new-connected-copilot-cloud-experience/
- Copilot in JetBrains, Universe releases: https://github.blog/changelog/2026-10-28-github-copilot-in-jetbrains-universe-releases/
- Copilot in Xcode: https://github.blog/changelog/2026-11-04-github-copilot-is-now-available-in-xcodes-coding-assistant/

## Slide 33

More code means more pull requests and more demand for review. Moving faster only helps if we keep the quality of what ships. This is where GitHub put a lot of investment this year.

## Slide 34

GitHub is putting agents to work on verification, not just generation.
- Copilot code review Max, in public preview, runs several independent review agents across models from different providers for changes that need a deeper look. It posted the highest F1 score on ReviewBench for high-severity issues. Lite and Balanced keep everyday reviews fast.
- Copilot approvals are generally available and can count toward required approvals.
- Agent Merge watches your pull request in the cloud and fixes blockers such as failing Actions workflows and merge conflicts, and can combine with auto-merge.
- Stacked pull requests are generally available: break big changes into focused, linked pull requests and merge the stack in one click. Repositories using stacks saw 9% more merged code.
- GitHub Code Quality is generally available; teams resolve 67.3% of its findings before merging.

Sources:
- Copilot code review Max and approvals: https://github.blog/changelog/2026-10-28-copilot-code-review-merge-with-confidence-with-max-and-approvals/
- Agent Merge: https://github.blog/changelog/2026-10-28-agent-merge-watches-and-fixes-pull-requests-in-the-cloud/
- Stacked pull requests GA: https://github.blog/changelog/2026-10-06-stacked-pull-requests-generally-available/
- GitHub Code Quality GA: https://github.blog/changelog/2026-07-20-github-code-quality-is-now-generally-available/

## Slide 35

As agentic coding speeds up, securing software becomes critical to scaling it. The number of published CVEs more than doubled in a year, to 101,078 in the 12 months to October 2026, according to the US National Vulnerability Database.

GitHub's answer is AI at every stage, from prevention to the fix:
- AI Scan for repositories (public preview): an on-demand, one-click scan of a whole repository, including languages CodeQL doesn't support. Findings land beside CodeQL alerts. AI Scan for pull requests is generally available.
- Push protection now uses AI to catch unstructured secrets such as passwords; early results more than doubled the pushes with secrets caught.
- Agentic autofix (generally available since 15 October): assign up to 25 code scanning alerts to Copilot and get a validated, review-ready pull request.
- Package firewall (public preview): an install-time policy gate that blocks malicious and risky npm packages before agents, runners or IDEs install them.

Also announced: reachability analysis for Dependabot, code scanning for AI applications, and a GitHub Security extension for the Copilot app. Advanced Security usage grew more than 90% year on year.

Sources:
- Universe 2026 changelog: https://github.blog/changelog/label/universe26/
- Agentic autofix GA: https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/
- AI Scan for repositories: https://github.blog/changelog/2026-10-28-ai-scan-for-repositories-in-public-preview/
- National Vulnerability Database: https://nvd.nist.gov/

## Slide 36

One more big announcement for enterprises. GitHub Enterprise customers can now use all Copilot features without buying a separate subscription: the Copilot app, code review, automations and more. You pay for the AI credits you use.

This is available now through GitHub and Microsoft account teams, with self-serve coming in stages. Existing Copilot Business and Copilot Enterprise customers can keep their plans or move when they're ready.

Source: GitHub Enterprise now includes access to GitHub Copilot, https://github.blog/changelog/2026-10-28-github-enterprise-now-includes-access-to-github-copilot/

## Slide 37

How the new model works: included access is not the same as unlimited usage.
1. Every GitHub Enterprise licensed user gets Copilot access, with the same features and models as Copilot Enterprise, and no separate subscription.
2. You set budgets for AI credits at enterprise, organisation or cost-centre level, with alerts and usage attribution.
3. Usage such as Copilot Chat, code review and the cloud agent is metered as AI credits from the first request; there are no per-seat monthly credits.
4. Code completions and next edit suggestions keep working with no budget, and an exhausted budget never removes access.

For users without a GitHub Enterprise licence, Copilot Standalone is US$10 per user per month, again with usage billed as AI credits. Talk to your GitHub or Microsoft account team about pricing and timing for your agreement.

Sources:
- GitHub Enterprise now includes access to GitHub Copilot: https://github.blog/changelog/2026-10-28-github-enterprise-now-includes-access-to-github-copilot/
- Copilot plans: https://github.com/features/copilot/plans

## Slide 38

All of this changes the demands on the platform underneath. Put simply, more agents means more traffic.

Every agent creates branches, reads history and pushes changes, often at the same time. At this scale you start to hit bottlenecks: fetches take longer and pushes stall. Most repositories are comfortably within today's limits, but the busiest are reaching them, and as agents scale more will follow.

Source: Jay Parikh, GitHub Universe 2026 keynote blog, https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/

## Slide 39

So far this year GitHub has added four million CPU cores, 160 petabytes of high-speed storage and 50 terabits per second of network capacity. GitHub is also migrating to a multi-region deployment in Azure, expected to complete early next year, while continuing to serve record traffic.

Source: Jay Parikh, GitHub Universe 2026 keynote blog, https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/

## Slide 40

Capacity matters, but it isn't the whole story. Throwing hardware at the problem doesn't change the ceiling; the architecture has to evolve as well. The agentic era calls for a different ceiling on Git throughput and reliability.

## Slide 41

The redesign follows three principles: simplify the primitives, decouple storage from compute, and minimise coordination.
- Durable repository data lives in Azure Blob Storage as the source of truth.
- The servers that answer Git requests cache data for speed without being tied to storage, so serving capacity can grow with demand.
- Coordination is kept small: locking happens per branch rather than per repository, so pushes only wait for others on the same branch.

The result for users: fewer stalls, more predictable responsiveness for busy repositories, and a foundation for the next generation of agent workflows. No action is needed from customers; Git workflows stay the same. The first phase is in private preview with some of the busiest repositories on GitHub.

Source: Jay Parikh, GitHub Universe 2026 keynote blog, https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/

## Slide 42

What does it enable? In GitHub's load test, 5,000 concurrent agent sessions pointed at a single repository sustained 7,200 writes per second, 180 times the throughput of the existing architecture for that workload. GitHub's engineering blog reports up to 35 times write throughput in broader benchmarks.

This isn't about making one developer's push 180 times faster. It's about room for thousands of developers and agents to work concurrently as demand grows.

Source: Jay Parikh, GitHub Universe 2026 keynote blog, https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/

## Slide 43

This is 24 hours of traffic from the busiest open-source repository on GitHub, compressed into one minute, on the old architecture and the new one.

The traffic hits its limit before the new architecture does. Locking happens at the branch level, code lives durably in Azure Blob Storage, and the serving layer is ephemeral, so capacity can be added as demand grows. The old architecture topped out at dozens of pushes a second; the new one is designed for thousands.

## Slide 44

Jay Parikh closed the Universe keynote with this thought. Our jobs are changing, but developers are more important than ever. The opportunity isn't just to produce more code. It's to solve problems we couldn't solve before.

Source: Jay Parikh, "GitHub Universe 2026: Evolving every layer of the stack", https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/

## Slide 45

Where is this heading? Four patterns are already emerging.
- Spec-driven development: GitHub's open-source Spec Kit moves teams from vague prompts to a specification, a technical plan and tasks that agents implement. It works with Copilot, Claude Code, Gemini CLI and more.
- Continuous AI: just as CI/CD automated build and release, natural-language rules and agentic reasoning now run continuously inside the repository, through GitHub Agentic Workflows.
- Systems that learn: memory, dreaming and automations that learn from their outcomes mean the platform improves as you use it.
- Humans and agents together: developers set direction, make decisions and stay accountable for what ships; agents implement and verify. GitHub Next is exploring multiplayer agents and collaborative planning.

Sources:
- Spec Kit: https://github.github.com/spec-kit/
- Spec-driven development with AI: https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
- Continuous AI: https://githubnext.com/projects/continuous-ai/
- GitHub Next: https://githubnext.com/

## Slide 46

The more capable agents become, the more important human judgement becomes. An agent can produce an implementation, but it can't take responsibility for why a product should exist, whether its behaviour is acceptable, or what risks a team is willing to take.

Our role is to set the intent and the guardrails, challenge assumptions, review the evidence and decide what deserves to ship. That includes security and quality, and also accessibility, usefulness and the needs of the people who depend on our software.

## Slide 47

As developers, we now have more collaborators and more ways to turn an idea into working software. That's an opportunity, and also a responsibility to ask better questions. Who is this for? What problem does it solve? How will we know it actually works?

Those questions matter whether the implementation comes from one developer, a team or a fleet of agents.

## Slide 48

We are in the middle of the biggest shift in how software gets built in a generation. Its impact won't be measured by how much code agents generate or how fast a benchmark runs. It will be measured by the problems we solve, the quality of what we ship and the people whose lives we improve.

GitHub's role is to provide the tools, intelligence and foundations. Ours, as developers, is to bring imagination, judgement and collaboration. How will you push the boundaries of what you know, learn by doing, and learn from the people around you?

---

I also saved this as `speaker-notes-slides-9-48.md` in the working output folder. I tidied the source lists into bullets and added blank lines before lists so they render properly.
