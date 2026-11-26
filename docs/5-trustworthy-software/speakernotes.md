Here are the speaker notes from slides 93–125, in markdown. Every slide in that range has notes. I haven't changed the deck.

# Speaker Notes: Slides 93–125

## Slide 93

Today is about one idea: security that starts at the first commit and keeps pace with AI-speed development.

We'll cover three things. Getting secure: finding and fixing the risk already in your code. Staying secure: keeping new risk out of every push, pull request, package and pipeline, on GitHub and on Azure DevOps. Secure by default: making the safe path the easy one, for developers and for AI agents.

Everything shown is either generally available or clearly marked as preview.

## Slide 94

AI has changed both sides of security. Developers and agents now ship far more code, and attackers use the same tools to find and exploit weaknesses faster.

The answer is not more manual review. It is putting the right automated control at each stage of development, so security keeps pace without slowing anyone down.

## Slide 95

GitHub's own data shows the problem. Dependabot alerts flagged from advisories have grown from about 18 million a quarter in 2023 to 438 million now, while the time from disclosure to a confirmed exploit has fallen from 128 days to under 24 hours.

The Australian Signals Directorate makes the same point: attackers can use AI to discover vulnerabilities and build working exploits within hours, and chain lower-severity issues into serious impact.

A recent example: within about a day of the PHP2Shell disclosure in October 2026, researchers had a working exploit, and nearly two weeks later around 29 million services were still exposed.

Sources:
- GitHub Universe 2026, Agentic security for every developer
- ASD, Defending against AI-enabled cyber attacks (July 2026): https://www.cyber.gov.au/sites/default/files/2026-07/Defending%20against%20AI-enabled%20cyber%20attacks%20-%20Guidance%20for%20government%2C%20critical%20infrastructure%20and%20large%20enterprises.pdf
- Microsoft Security blog, Security for the agentic era (17 Nov 2026): https://www.microsoft.com/en-us/security/blog/2026/11/17/security-for-the-agentic-era-powered-by-microsoft-perception/

## Slide 96

These are the questions Microsoft suggests every executive ask their CIO, CTO and CISO, backed by the Secure Now guidance in Microsoft Security Exposure Management.

Today is mostly an answer to question two, have we scanned our own code, and question four, is a baseline enforced everywhere, with links to the other three.

Sources:
- Microsoft Secure Now: https://aka.ms/securenow
- From guidance to action, security fundamentals that materially reduce risk (17 Sep 2026): https://www.microsoft.com/en-us/security/blog/2026/09/17/from-guidance-to-action-security-fundamentals-that-materially-reduce-risk/

## Slide 97

Microsoft's Fortify your Enterprise approach runs three tracks at once. Fortify closes the gaps you have today. Modernise rebuilds the applications that are too old or too fragile to patch quickly. Defend puts machine-speed detection and response around everything.

GitHub shows up in all three: Code Security in Fortify, GitHub Copilot modernization in Modernise, and the code findings that feed Defend. The rest of this session goes deep on the code.

Sources:
- Microsoft Secure Now: https://aka.ms/securenow
- GitHub Copilot modernization: https://learn.microsoft.com/en-us/azure/developer/github-copilot-app-modernization/overview
- Microsoft Perception (17 Nov 2026): https://www.microsoft.com/en-us/security/blog/2026/11/17/security-for-the-agentic-era-powered-by-microsoft-perception/

## Slide 98

Getting secure. Most organisations already carry years of security debt in their secrets, code and dependencies. Before we talk about prevention, let's find what is already there and fix it quickly.

## Slide 99

GitHub Advanced Security is now two products. GitHub Secret Protection covers secret scanning across 200+ token types from 180+ service providers, push protection with delegated bypass, AI-detected secrets and public leak monitoring. GitHub Code Security covers CodeQL code scanning, AI Scan, Copilot Autofix and agentic autofix, security campaigns, Dependabot, dependency review and third-party SARIF results.

Both are available on GitHub Enterprise Cloud and Server, and for Azure Repos as GitHub Advanced Security for Azure DevOps, licensed per active committer. More than 1.3 million developers actively use it.

Sources:
- GitHub Advanced Security on Azure: https://azure.microsoft.com/en-us/products/github/advanced-security
- GitHub Docs, enabling security features at scale: https://docs.github.com/en/code-security/concepts/security-at-scale/organization-security
- GitHub Advanced Security for Azure DevOps: https://azure.microsoft.com/en-us/products/devops/github-advanced-security

## Slide 100

Security configurations are collections of enablement settings you apply to any repository in an organisation. The GitHub-recommended configuration is maintained by GitHub and suits most repositories. Custom configurations let you tier critical, standard and archived repositories, and enforcement stops repository admins switching features off.

Global settings cover Dependabot auto-triage rules, grouped security updates, code scanning and secret scanning defaults, and the security manager role. Production context from Microsoft Defender for Cloud, JFrog Artifactory or deployment records ranks alerts by what actually runs.

On Azure DevOps you enable at organisation, project or repository level, can auto-enable new repositories, and CodeQL default setup runs on a shared schedule for C#, C/C++, Java, JavaScript/TypeScript, Python, Ruby and Rust.

Sources:
- https://docs.github.com/en/code-security/concepts/security-at-scale/organization-security
- https://docs.github.com/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/configuring-global-security-settings-for-your-organization
- https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features?view=azure-devops

## Slide 101

GitHub's new push protection classifier, built with Microsoft, looks at how a potential secret is used in the surrounding code, so it can block secrets that have no recognisable format. In early public preview results it more than doubled the number of pushes where push protection caught a secret.

Anthropic API keys are now blocked by push protection by default, and public leak monitoring for enterprises is generally available. On Azure DevOps, push protection and repository secret scanning switch on with Secret Protection.

The best fix of all is to remove long-lived secrets: OIDC from GitHub Actions to Azure, and workload identity federation in Azure Pipelines.

Sources:
- https://github.blog/changelog/2026-10-28-push-protection-beyond-predefined-secret-patterns/
- https://github.blog/changelog/2026-10-13-secret-scanning-blocks-anthropic-keys-by-default-adds-salesforce/

## Slide 102

GitHub's direction is a hybrid engine: deterministic CodeQL for speed, precision and repeatability, plus AI reasoning focused on security-sensitive code, with a stability layer so a finding that disappears isn't silently treated as fixed.

AI Scan for pull requests is generally available. It covers languages and formats CodeQL doesn't, such as PHP, Shell, Terraform, Dockerfile, JSP and Blazor, and adds advisory findings beside CodeQL results.

AI Scan for repositories is in public preview: an on-demand scan of the whole default branch, including logic flaws, that skips what CodeQL already reports and lands in the same backlog. You can bulk start it on up to 20 repositories at a time.

Sources:
- https://github.blog/changelog/2026-10-15-ai-scan-for-pull-requests-generally-available/
- https://github.blog/changelog/2026-10-28-ai-scan-for-repositories-in-public-preview/
- https://github.blog/changelog/2026-11-16-bulk-start-ai-scan-for-repositories/

## Slide 103

Codename MDASH is Microsoft Security's multi-model agentic code scanner inside Microsoft Defender, built by the Autonomous Code Security team, whose members were part of the DARPA AI Cyber Challenge winning team.

It runs in four stages. Prepare ranks files by risk using call graphs and complexity. Scan runs more than 100 specialised auditor agents, such as injection, memory-safety and authentication-bypass auditors. Validate uses taint analysis and a debate between models to test each finding. Dedupe collapses the results into a short list of validated findings.

Results under test conditions: 96.55% on the CyberGym benchmark, and 16 new Windows vulnerabilities found, including four critical remote code execution flaws addressed in the May 2026 Patch Tuesday. These are benchmark and research results, not customer outcomes.

How you use it: GitHub and Azure DevOps connectors, or the Defender CLI locally or in CI/CD, with SARIF and HTML output. Findings appear in Defender Exposure Management, and fixes are generated locally with GitHub Copilot for a developer to review. It needs an eligible Defender plan and a dedicated Microsoft Foundry resource; there is no extra MDASH licence during preview, and Foundry inference is billed at your rates. Australia East is a supported region.

Sources:
- Codename MDASH overview: https://learn.microsoft.com/en-us/security-exposure-management/ai-code-security-overview
- Getting started: https://learn.microsoft.com/en-us/security-exposure-management/ai-code-security-onboarding
- FAQ: https://learn.microsoft.com/en-us/security-exposure-management/codename-mdash-faq
- Microsoft Build 2026, securing code, agents and models: https://www.microsoft.com/en-us/security/blog/2026/06/02/microsoft-build-2026-securing-code-agents-and-models-across-the-development-lifecycle/
- Defense at AI speed (12 May 2026): https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/

## Slide 104

GitHub Advanced Security is the developer security platform and remediation workflow. AI Scan extends CodeQL with AI for broader language coverage and new detections. Codename MDASH is a deep, multi-agent research engine that augments it.

Run CodeQL and AI Scan in every pull request. Run MDASH as a periodic deep assessment of your crown-jewel repositories. Because MDASH scans are long-running and non-deterministic, treat them as asynchronous review rather than a build-blocking gate.

Sources:
- Codename MDASH FAQ: https://learn.microsoft.com/en-us/security-exposure-management/codename-mdash-faq
- AI Scan for pull requests: https://github.blog/changelog/2026-10-15-ai-scan-for-pull-requests-generally-available/

## Slide 105

Finding is half the job; the backlog is the other half. Agentic autofix is generally available: assign a code scanning alert to Copilot and it explores the relevant files, proposes a fix, reruns CodeQL to prove the alert closes, and opens a draft pull request explaining the change and how it was validated. You can select up to 25 alerts for one pull request, from a repository or a security campaign.

Security campaigns let a security team burn down up to 1,000 alerts at a time, using templates such as cross-site scripting, with campaign managers, due dates and an issue in each repository.

On Azure DevOps, agentic Copilot Autofix for code scanning and dependency alerts is in public preview.

Sources:
- https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/
- https://docs.github.com/en/code-security/tutorials/secure-your-organization/best-practice-fix-alerts-at-scale
- https://devblogs.microsoft.com/devops/agentic-autofix-for-advanced-security-for-azure-devops-public-preview/

## Slide 106

Reachability analysis for Dependabot is in public preview. Curated advisory data names the vulnerable functions, and CodeQL builds a call graph across your repository and its dependencies to look for a path.

Each alert gets one of four verdicts: reachable, potentially reachable, unreachable or unavailable. Verdicts never close or dismiss alerts. Reachable doesn't automatically mean exploitable and unreachable isn't a guarantee, so combine the verdict with severity, EPSS and production context.

It supports JavaScript and TypeScript with npm, Yarn or pnpm lockfiles on GitHub Enterprise Cloud, rescans daily while alerts are open, and is free during preview. On Azure DevOps, dependency alerts now show EPSS percentiles.

Screenshot: GitHub Universe 2026.

Sources:
- https://github.blog/changelog/2026-10-28-prioritize-dependabot-alerts-with-reachability-analysis/
- https://docs.github.com/en/code-security/concepts/supply-chain-security/about-reachability-analysis-for-dependabot-alerts
- https://learn.microsoft.com/en-us/azure/devops/release-notes/2026/ghazdo/sprint-280-update

## Slide 107

Demo: from scan to merged fix.

1. Run AI Scan for repositories on a sample repository and show the AI findings beside the CodeQL alerts.
2. Assign findings to Copilot with agentic autofix, then open the draft pull request and its CodeQL validation.
3. Group the remaining alerts into a security campaign using the cross-site scripting template.
4. Show reachability verdicts and call paths on Dependabot alerts.

Docs:
- https://github.blog/changelog/2026-10-28-ai-scan-for-repositories-in-public-preview/
- https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/

## Slide 108

Staying secure. Clean-up without prevention just refills the backlog. Next: stopping new risk at every push, pull request, package and pipeline, on GitHub and on Azure DevOps, and connecting code to what runs in production.

## Slide 109

Not every control needs to run at the same speed. Some act in seconds in the developer's flow, like agents checking their own code and on-demand reviews in the CLI and IDE. Some take minutes, like pull request checks. Some go deep over hours, like full repository and enterprise-wide scans and bulk remediation.

The aim is the right control at the right stage, from prevention through to the fix.

Source: GitHub Universe 2026, Agentic security for every developer.

## Slide 110

Security now meets developers wherever they work: on-demand security reviews in the Copilot CLI, side-by-side findings in VS Code, and interactive scanning, triage and fixing in the GitHub Copilot app through the security extension.

GitHub reports 39,000 developers scanned 130,000 work trees with on-demand reviews.

Source: GitHub Universe 2026, Agentic security for every developer.

## Slide 111

Malware increasingly runs at install time, and agents and CI runners install dependencies with no one watching.

The package firewall is in public preview for npm: an install-time policy gate between your developers, pipelines and upstream registries, with cooldown periods, malware and vulnerability checks, attestation checks and exception requests. It is free during preview.

Dependency review and licence policies block risky packages in the pull request. Artifact attestations provide signed build provenance (SLSA Build Level 2, and Level 3 with reusable workflows). Actions workflow lockfiles are generally available.

From 2 December 2026, GitHub blocks pull_request_target by default, so check the workflows that depend on it.

Sources:
- https://github.blog/changelog/2026-10-20-github-package-firewall-in-public-preview/
- https://docs.github.com/en/actions/concepts/security/artifact-attestations
- https://github.blog/changelog/label/universe26/

## Slide 112

Every pull request, whether a developer or an agent opened it, runs the checks that matter.

CodeQL runs as a required status check through rulesets. AI Scan for pull requests is generally available and adds advisory findings for languages CodeQL doesn't cover. Dependency review blocks vulnerable or non-compliant packages. Push protection has already stopped secrets at push time. Code scanning for AI applications, in public preview, flags indirect prompt injection, sensitive information disclosure and excessive agency in agent code paths. Copilot code review now offers a Max effort level and can approve when ready.

Sources:
- https://github.blog/changelog/2026-10-15-ai-scan-for-pull-requests-generally-available/
- https://github.blog/changelog/2026-10-28-code-scanning-for-ai-applications-in-public-preview/

## Slide 113

Azure DevOps customers get the same engines, native in Azure Repos. Secret Protection for Azure DevOps covers push protection, repository secret scanning and the security overview. Code Security for Azure DevOps covers dependency scanning, CodeQL code scanning and third-party SARIF results.

You enable it at organisation, project or repository level. CodeQL default setup supports C#, C/C++, Java, JavaScript/TypeScript, Python, Ruby and Rust, with advanced setup for Go and Swift. Status checks for new or all critical and high alerts work as branch policies. Billing is per active committer, charged daily to your Azure subscription.

New in Azure DevOps: agentic Copilot Autofix for code scanning and dependency alerts is in public preview, billed as AI credits to the linked subscription; Copilot code review is generally available; and the GitHub Copilot app works with Azure Repos in preview. You can move repositories to GitHub when ready and keep Boards and Pipelines.

Screenshot: Azure DevOps repository settings.

Sources:
- https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features?view=azure-devops
- https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-billing?view=azure-devops
- https://devblogs.microsoft.com/devops/agentic-autofix-for-advanced-security-for-azure-devops-public-preview/
- https://devblogs.microsoft.com/devops/azure-devops-and-github-start-your-agentic-journey-where-you-are/

## Slide 114

Walk the flow left to right. Push protection evaluates every push once it is enabled, and repository scanning catches what is already in history. A build validation policy runs the Advanced Security CodeQL and dependency scanning tasks on the pull request branch; annotations appear once the default branch has been scanned. Status checks for new or all critical and high alerts are set as branch policies. Release pipelines use workload identity federation instead of stored secrets.

Alongside the flow, Copilot Autofix runs as a pipeline job under a dedicated GitHub Copilot identity and opens a pull request; the security overview shows alerts across the organisation; and Defender for Cloud gives DevOps posture across both platforms, with an Azure DevOps connector for Codename MDASH deep scans.

Sources:
- https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features?view=azure-devops
- https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-autofix?view=azure-devops

## Slide 115

The integration between GitHub Advanced Security and Microsoft Defender for Cloud is generally available. It automatically maps repositories to the cloud workloads they deploy and back again, so GitHub alerts are prioritised by runtime risk from Defender CSPM attack path analysis: internet exposure, sensitive data, critical resources and lateral movement. Security and engineering share one view, and fixes use Copilot.

Codename MDASH findings publish to Microsoft Security Exposure Management, where Microsoft Perception agents can use the exposure context.

Planning note: the Defender portal GitHub connector used by MDASH and an Azure portal connector can't both be connected to the same GitHub organisation, so plan connectors together.

Sources:
- https://learn.microsoft.com/en-us/azure/defender-for-cloud/github-advanced-security-overview
- https://learn.microsoft.com/en-us/azure/defender-for-cloud/github-advanced-security-deploy
- https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/start-secure-stay-secure-how-microsoft-is-closing-the-gap-from-code-to-runtime/4524580
- https://learn.microsoft.com/en-us/security-exposure-management/create-github-connector

## Slide 116

Demo: Azure DevOps, end to end.

1. Push a commit containing a test secret to Azure Repos; push protection blocks it.
2. Open a pull request; the critical and high alerts status check fails on a CodeQL alert.
3. Select Generate fix; Copilot Autofix opens a labelled pull request.
4. Show the alert, its EPSS percentile and the fix in the Advanced Security tab.

Docs:
- https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features?view=azure-devops
- https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-autofix?view=azure-devops

## Slide 117

Secure by default. The goal is a platform where the secure choice is the default for every developer and every agent, so security doesn't depend on someone remembering to opt in.

## Slide 118

Five areas, and each one is a setting rather than a project.

- Identity: Enterprise Managed Users with Microsoft Entra ID, where OIDC lets Conditional Access policies apply to GitHub; prefer GitHub Apps and fine-grained tokens over classic personal access tokens.
- Repositories: enterprise and organisation rulesets, required reviews and checks, and push rules for sensitive file paths.
- Advanced Security: security configurations enforced on new repositories, CodeQL default setup, and push protection with delegated bypass.
- Actions: an allowed-actions policy that requires SHA pinning, a read-only GITHUB_TOKEN by default, and OIDC federation to Azure.
- Copilot: Enterprise AI Controls and the agent control plane are generally available, with agent session activity and audit fields; the enterprise MCP allowlist is in public preview; push rules can protect custom agent definitions.

GitHub Enterprise Cloud with data residency is available in Australia, and new security features such as AI Scan for repositories, agentic autofix and the package firewall support it.

Sources:
- https://github.blog/changelog/2026-02-26-enterprise-ai-controls-agent-control-plane-now-generally-available/
- https://docs.github.com/en/code-security/concepts/security-at-scale/organization-security
- https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/about-github-enterprise-cloud-with-data-residency

## Slide 119

Copilot cloud agent checks its own work before you see it. By default it runs CodeQL on the code it writes, checks newly added dependencies against the GitHub Advisory Database for malware and high or critical vulnerabilities, runs secret scanning, and gets a second opinion from Copilot code review. This validation doesn't need a Secret Protection, Code Security or GitHub Advanced Security licence.

It is also contained by design: it pushes only to its own copilot/ branch, works behind a firewall, and is subject to your rulesets and required checks. It opens draft pull requests only, can't approve or merge its own work, the person who asked for the change can't approve it, and workflows wait for approval. Commits are co-authored with the requester and every session is logged.

Source: https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

## Slide 120

Microsoft Security describes agents as your newest insiders, with four continuous responsibilities. Know which agents exist, who owns them and what they are doing. Contain what each can access before it acts. Protect the data, tools and systems in the agent's path. Adapt protection as behaviour and risk change.

On GitHub that maps to the agent control plane with agent session activity and audit fields, enterprise custom agents protected by push rules, and the MCP allowlist, which is in public preview. Code scanning for AI applications, also in preview, finds prompt injection and excessive agency in agent code. Microsoft Execution Containers, generally available, give policy-driven containment for agent workloads on Windows, macOS and Linux.

Sources:
- Agents are your newest insiders (19 Oct 2026): https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/
- https://github.blog/changelog/2026-02-26-enterprise-ai-controls-agent-control-plane-now-generally-available/

## Slide 121

PHP2Shell was disclosed on 21 October 2026 and added to the CISA Known Exploited Vulnerabilities catalogue on 26 October. Azure App Service began rolling out patched built-in PHP images the same day the fixes shipped. Apps pinned to a full image tag and custom containers still need to be rebuilt on a patched base image.

Compare that with self-managed virtual machines and containers, where you own the patch cycle.

GitHub Copilot modernization is an agent that assesses, plans and upgrades .NET and Java applications, fixes build errors and checks dependencies for known CVEs as it goes. Azure Migrate with CAST helps you choose what to modernise first.

Sources:
- https://azure.github.io/AppService/2026/10/21/php-critical-security-release-app-service-linux.html
- https://www.microsoft.com/en-us/msrc/blog/2026/10/patch-now-php2shell-brotli-emudhra-guidance-for-customers
- https://learn.microsoft.com/en-us/azure/developer/github-copilot-app-modernization/overview

## Slide 122

Microsoft Perception reached general availability on 17 November 2026 with eight playbooks and six agents. Red team: the Recon agent. Blue team: Triage, Attack Investigation, Threat Intelligence and Detection Authoring. Green team: Posture Prioritization.

New in public preview: the Web App Pen Test agent, which validates exploitable vulnerabilities and can use code scanning findings, and the Risk Reduction agent, which builds remediation plans and applies vulnerability shielding where immediate patching isn't possible.

Agents authenticate with Microsoft Entra Agent IDs, and people stay in control through approval steps such as Recon scope authorisation and saving new detections.

Sources:
- https://www.microsoft.com/en-us/security/blog/2026/11/17/security-for-the-agentic-era-powered-by-microsoft-perception/
- https://techcommunity.microsoft.com/blog/perception-blog/whats-new-with-microsoft-perception-at-ignite-2026/4571834

## Slide 123

If you remember one slide, make it this one.

1. Fix at machine speed. Attackers can build exploits within hours of disclosure. Reachability analysis and EPSS focus effort, and agentic autofix and security campaigns turn alerts into pull requests. Copilot Autofix is coming to Azure DevOps too.
2. Scan your own code with AI. CodeQL plus AI Scan for pull requests and repositories, and Codename MDASH for deep, validated findings on your most critical code.
3. Lock down secrets and the supply chain. AI-powered push protection, the package firewall, artifact attestations and workflow lockfiles. Check pull_request_target workflows before 2 December 2026.
4. Govern AI agents as insiders. Copilot cloud agent validates its own work with no extra licence; AI Controls, code scanning for AI apps and Microsoft Perception do the rest.
5. Make secure the default. Enforce security configurations, rulesets and Enterprise Managed Users, and on Azure DevOps turn on Secret Protection and Code Security with status checks.

Sources: as cited on the earlier slides.

## Slide 124

Where each capability is enabled.

- GitHub security configurations: https://docs.github.com/en/code-security/concepts/security-at-scale/organization-security
- AI Scan for repositories: https://github.blog/changelog/2026-10-28-ai-scan-for-repositories-in-public-preview/
- Agentic autofix: https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/
- Copilot cloud agent security validation: https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations
- GitHub Advanced Security for Azure DevOps: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features?view=azure-devops
- Copilot Autofix for Azure DevOps: https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-autofix?view=azure-devops
- Codename MDASH getting started: https://learn.microsoft.com/en-us/security-exposure-management/ai-code-security-onboarding
- Set up Microsoft Foundry for MDASH: https://learn.microsoft.com/en-us/security-exposure-management/mdash-foundry-integration

Further reading:
- GitHub security documentation: https://docs.github.com/en/code-security
- GitHub Universe 2026 changelog: https://github.blog/changelog/label/universe26/
- Defender for Cloud with GitHub Advanced Security: https://learn.microsoft.com/en-us/azure/defender-for-cloud/github-advanced-security-overview
- Microsoft Secure Now: https://aka.ms/securenow

## Slide 125

To recap: start secure by finding and fixing what is already in your code; stay secure by gating every push, pull request, package and pipeline; and be secure by default with baselines, agent guardrails, modern platforms and machine-speed defence.

The next step is simple: agree a 30-day plan and the first 20 repositories for AI Scan and CodeQL.

---

I also saved this as `speaker-notes-slides-93-125.md` in the working output folder. As before, I tidied the source lists into bullets and added blank lines before lists so they render properly.
