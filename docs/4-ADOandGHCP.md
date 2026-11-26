## Azure DevOps + GitHub Copilot

Good morning, everyone, and thank you for staying with me.
I'm Michelle Sandford, and for the next forty minutes I want to leave you with one idea.
Agents should work inside your rules, not around them.
Everything you've heard today about GitHub Copilot, I want to bring to the place many of you actually work: Azure DevOps.
Public sector teams have years of work sitting in Azure Repos.
Branch policies, approvals, security groups: all defined, all trusted.
So the question I hear from government isn't "is AI impressive?"
It's "can we use it without loosening anything?"
Here's the short answer.
The GitHub Copilot app now works directly with Azure DevOps repositories and pull requests.
Your code stays where it is.
Your permissions stay as they are.
Your policies still decide what merges.
One caveat up front, and I'll repeat it, because honesty is part of trust.
This integration is in public preview and subject to change.
So please treat today as the start of a pilot conversation, not a production commitment.
Here's how we'll use the time.
Why it matters, what it does, and how you set it up.
Then what a session feels like, and what it looks like when work lands.
Then the part I know you care about most: governance and data.
We'll finish with a pilot you could start in a single sprint.
Before we start, a quick show of hands, just in your head.
How many of your teams already have code sitting in Azure Repos?
Keep that picture in mind, because everything I talk about today is about that code.
Public sector delivery is judged on outcomes and on accountability.
Citizens expect services to improve, and they expect someone to be answerable for how.
So my promise is that nothing I show you removes the accountable human from the loop.
If at any point something sounds too good to be true, ask me, and I'll tell you where the limits are.
Let's get into it.

## Why it matters

Let me start with why this matters to government.
Most agencies I speak with aren't starting from a blank page.
They have large estates in Azure Repos, years of history, and branch policies that took real effort to get right.
The worst answer to "how do we adopt agents?" is "first, move all your code."
This integration takes the opposite approach.
It brings the agent to your repository, not your repository to the agent.
Three ideas on this slide, and each one is a promise.
First, code stays put.
You clone your Azure DevOps repository into the app and start an agent session, just as you would for a GitHub repository.
No migration project, and no new home for your source.
Second, same permissions.
Azure DevOps permissions apply to every action.
Connecting your account does not grant additional access.
If you couldn't do it yesterday, the agent can't do it today.
Third, policies gate merges.
Your permissions, plus the checks and policies configured on the repository, decide who can approve or complete a pull request.
The agent doesn't get a side door.
If this slide were a coffee mug, it would say: new capability, same controls.
That's the line I'd like you to take back to your security team.
Because their first question will be, "does this change our risk model?"
And the honest answer is: it changes how fast work moves, not who is allowed to approve it.
Let me give you the version for a senior executive, in thirty seconds.
Your people already work in Azure DevOps.
Your controls already live in Azure DevOps.
We're adding an assistant to that place, not asking you to build a new one.
If someone asks, "doesn't this mean our code leaves our environment?", I'd answer carefully.
The repository stays in Azure DevOps, and the later slides cover exactly what content can reach the model.
So I won't wave that question away, I'll show you the specifics when we get to data handling.
Think of this slide as the principle, and the rest of the session as the proof.
So let's see what it actually does.

## Slide 33: The capability

Here's the whole lifecycle on one slide, left to right.
Five steps, and every one of them happens against your Azure DevOps organisation.
Step one, clone.
You add an Azure DevOps repo by organisation name and clone it into the app.
Step two, branch and code.
An agent session creates a branch, makes code changes and commits them.
That's the ordinary work, the part nobody enjoys doing at four in the afternoon.
Step three, open a pull request.
The agent opens the pull request in your Azure DevOps repository.
Not in a side system, not in a copy.
In the place your reviewers already look.
Step four, review.
You track status in the sidebar, then choose View PR to check the changes, the checks and the comments.
Step five, Agent Merge.
This one is optional.
It lets an agent fix feedback, CI failures and conflicts, and then complete the pull request.
I'll spend more time on that shortly, because it's the step that deserves your attention.
One thing to hold on to: the agent acts as the signed-in user.
It isn't a mysterious new identity wandering around your estate.
It's a person, with their permissions, getting help.
And a reminder at the bottom of the slide.
This is public preview, it's subject to change, it's disabled by default, and it's enabled per user in the app.
Nobody gets this by accident.
If someone asks, "will this just appear on our developers' machines?", the answer is no.
Someone has to switch it on, deliberately.
Speed is the benefit; deliberate choice is the control.
If someone asks, "does the agent get its own login?", the answer is on this slide.
The agent acts as the signed-in user.
If someone asks, "can it change things we haven't allowed?", the answer is the same.
Azure DevOps permissions apply to every action, so it can only do what that person could do.
And if someone asks, "what's the one step I should be most careful about?", it's Agent Merge.
It's optional for a reason, and I'd treat it as something you earn.
Here's a question for the room.
Which of these five steps takes your team the most time today?
For many teams it's the review and rework loop, and that's exactly where the sidebar and Agent Merge are aimed.
That brings us to what you need before you start.

## Slide 34: Availability

Before anyone gets excited, let's check the ground rules.
Four prerequisites, and then one planning note that matters a lot.
Plans first.
You need Copilot Business, Copilot Enterprise or Copilot Individual. I would hope in Government, you are all working with the Enterprise Version because that's the holistic control plane of security, governance, privacy and compliance that people would expect from you.
If you're already licensed, you may be closer than you think.
Second, the app.
The GitHub Copilot app needs to be installed and signed in.
Third, identity.
You need a Microsoft account with access to the Azure DevOps organisation, project and repository.
Notice what that means.
The access question is answered by the access you already manage.
Fourth, policy.
For Copilot Business and Enterprise, admins must keep the GitHub Copilot app policy enabled.
So there are two gates: your administrators have to allow it, and your users have to opt in.
Now the planning note, because I'd rather you hear it from me than discover it in a pilot.
Cloud sessions aren't available for Azure DevOps repositories.
Agent sessions run in the app, on the developer's machine.
Local sessions only.
For some agencies that's actually a feature.
Work happens on a device you already manage, rather than somewhere new.
But it does mean you should confirm agency-managed devices can run the GitHub Copilot app before a pilot.
To be clear, that device check is our planning recommendation.
It isn't a documented requirement.
Think of it as a cheap question that saves an expensive surprise.
Prerequisites are boring.
Boring prerequisites are what make exciting pilots possible.
If someone asks, "which plan should we choose?", the slide gives the three options.
Copilot Business, Copilot Enterprise or Copilot Individual all qualify.
For an agency, the practical difference is administration.
Business and Enterprise let your admins keep the app policy enabled or not, which is control you'll want.
If someone asks, "can we run this in the cloud so developers don't need anything installed?", the answer today is no.
Cloud sessions aren't available for Azure DevOps repositories.
I'd rather give you that answer now than have it surprise your project manager in week two.
A good pilot lead checks four things: licence, app, identity, policy.
Then adds one more: is the device ready?
Now, how do you switch it on?

## Slide 35: Set up

Here's my favourite slide for anyone responsible for change control.
The integration is off by default and enabled deliberately.
Opt-in by design.
There are eight steps, in two short groups of four.
The first group enables the integration.
Open the app settings.
Click Experimental.
Enable the Azure DevOps integration.
Then click Accounts, and add the Microsoft account you use for Azure DevOps.
That's it for enabling.
The second group adds a repository.
In the sidebar, click the plus next to Sessions.
Choose Add Azure DevOps repo.
Type your organisation name, pick the repository, and clone.
I want to make a point about the order.
The integration must be switched on before an account or repository is connected.
So the sequence itself is a checkpoint.
Nothing is connected until someone has made a conscious decision.
For public sector, that default is a gift.
Your change board doesn't have to chase a feature that quietly appeared.
It can approve a feature that someone deliberately enabled.
There's an old saying that trust is built in drops and lost in buckets.
Opt-in is how you keep the bucket empty.
And a practical note.
Whoever is running your pilot should do these eight steps together with a small group first.
It takes minutes, and it makes the later governance conversation concrete rather than theoretical.
If someone asks, "who can switch this on?", the answer is each user, in the app.
And for Business and Enterprise, only where your admins have kept the app policy enabled.
So there are two layers of consent.
If someone asks, "what if a developer enables it and we didn't plan for it?", that's why your pilot approach matters.
Communicate early, enable for a small team, and make the opt-in a visible decision.
Here's a question for the room.
In your agency, how long does it take to get a new capability through change control?
Opt-in by design means the capability can be ready, while the decision stays with you.
Small steps, deliberately taken, are how public sector teams actually move.
Now let's see a session.

## Slide 36: Agent sessions

Now let's look at the experience, because this is where developers will form their opinion.
It's deliberately simple.
Four moves.
One, start a session.
Select your connected Azure DevOps repo under "Start session in", and describe the code changes you want.
Plain language, the way you'd brief a colleague.
Two, the agent does the work.
It can create a branch, make code changes, commit them and open a pull request.
Three, and this is the one I want you to underline: you stay in the loop.
You review the agent's changes, and you respond to any requests for approval.
The human isn't removed. The human is promoted to reviewer.
Four, track it to done.
Follow the pull request's status in the sidebar, then click View PR to review its checks.
It's the same experience as working with a GitHub repository.
So if your people have seen it elsewhere, there's nothing new to learn.
Now an honest note, because your security colleagues will find it anyway.
The agent's tools follow the session's tool permissions.
Depending on those settings, creating a pull request, or replying to and resolving review threads, can run without another approval prompt.
That isn't a flaw, it's a dial.
And dials need a sensible setting.
For public sector pilots, I recommend conservative tool permissions.
Start tight, then loosen based on evidence.
A good rule: trust is earned in sprints, not granted in settings.
If someone asks, "how do I know what the agent did?", the answer is the pull request.
Every change arrives as something a person can read, question and reject.
If someone asks, "will developers get a different experience from what they see on GitHub?", the answer is no.
It's the same experience.
That matters for adoption, because familiar beats clever.
If someone asks, "what does a good first task look like?", I'd suggest something small, well-bounded and low risk.
Think of tasks where a reviewer can tell at a glance whether the change is right.
Save the architecture-changing work for later.
If someone asks, "who is accountable for what the agent produces?", the answer is the person who reviews and approves it.
That's why every request for approval comes back to you.
Our sound bite here is simple.
The agent drafts, the human decides.
Which leads naturally to how the work finally lands.

## Slide 37: Review & complete

This slide is about the last mile: getting from "the agent finished" to "it's in the codebase".
The headline is that Agent Merge lands it within policy.
Let me start with the left side, where you stay the approver.
Three actions.
Fix: click Fix on a review comment, and an agent addresses it.
Approve: click Approve when you are ready to approve the pull request.
Complete: review the confirmation, and confirm the merge.
Notice who is clicking.
You are.
The agent can do the typing, but the decision stays with a person.
Now the right side, Agent Merge, which is opt-in per pull request.
When enabled, the agent addresses review feedback, fixes CI failures, resolves conflicts, and completes the pull request when Azure DevOps checks and policies pass.
That's real time saved.
Anyone who has waited on a merge conflict knows the pain.
But read the bottom of the card carefully.
Once enabled for a pull request, the agent can complete it without a separate confirmation.
So this is a power feature, and it should be treated like one.
My advice for pilots is to keep it off to start.
Earn the right to turn it on.
And here's the reassurance underneath.
Your Azure DevOps permissions, and the repository's checks and policies, decide whether a pull request can be approved or completed.
Branch policies and required reviewers remain the real gate.
If the checks don't pass, nothing completes.
The agent can't talk its way past a build policy.
So the sound bite for this slide is: automation proposes, policy disposes.
Speed with a safety net.
If someone asks, "what stops a bad change from merging?", the answer is your branch policies and required reviewers.
They were designed for human mistakes, and they work just as well on agent-assisted work.
If someone asks, "should we turn Agent Merge on?", my honest answer is: not on day one.
Let your reviewers get comfortable first.
Look at the quality of the agent's pull requests over a sprint.
Then decide, per pull request, where the automation earns its place.
And here's a question for the room.
What fraction of your review time goes on chasing CI failures and conflicts rather than judging the actual change?
That's the time Agent Merge is trying to give back.
Handing the tedious bits to an agent frees your experts for the judgement bits.
Now let me turn to the questions you'll be asked.

## Slide 38: Controls & assurance

Now to the slide I suspect many of you came for.
These are the governance questions agencies will ask, and I'd rather we take them head on.
The middle column is what GitHub Docs say.
The right column is our recommended interpretation for agencies.
Let me take them one at a time.
Who can access what?
Azure DevOps permissions apply to every action, and connecting grants no extra access.
So your existing security groups and branch policies stay the control plane.
You don't need a second rulebook.
Can we limit it to certain repos?
Here's the first gap.
There is no setting that restricts it to selected repositories.
Azure DevOps permissions govern access.
So scope your pilot through project and repo permissions.
Is there an audit trail?
Here's the second gap.
There's no separate audit log in the app.
Actions appear in Azure DevOps under the signed-in user.
So use Azure DevOps auditing and pull request history.
Do agents act without approval?
Tools follow session permissions, and some pull request actions may run without a prompt.
So set conservative tool permissions, and keep Agent Merge off at first.
How do we revoke access?
Signing out removes local tokens, but it does not revoke access with Microsoft.
So revoke through Microsoft Entra, and add it to your offboarding process.
I've put two gaps on this slide in a box, and I did that on purpose.
No per-repo restriction, and no separate audit log.
I'd rather tell you now than have you discover it later.
Honesty is the shortest route to a yes from a security team.
Every gap has a mitigation, and every mitigation lives in tools you already run.
The principle I'd leave you with: don't ask agents to be more trustworthy than your people.
If a security officer pushes back on the gaps, I'd answer in three sentences.
Yes, there's no per-repo restriction setting in the app.
Yes, there's no separate audit log in the app.
And no, that doesn't leave you blind, because Azure DevOps permissions scope access, and actions appear in Azure DevOps under each signed-in user.
If someone asks, "can we get an agent-specific audit report?", I'd say what the docs say today.
Actions appear in Azure DevOps under the signed-in user, so use Azure DevOps auditing and pull request history.
If it changes while the product is in preview, we'd want to tell you.
And on offboarding, please don't miss the Entra point.
Signing out clears local tokens, but revoking access happens in Microsoft Entra.
The best audit is the one that tells a clear story: who did what, when, and who approved it.
Hold them to the same controls.

## Slide 39: Data handling

The next question is always about data.
What does the model actually see?
Let me be precise, because precision is what a risk assessor needs.
Azure DevOps content that is returned to the agent can enter the selected model's context.
That includes private code.
It includes pull request descriptions and diffs.
It includes review comments.
And it includes build log excerpts.
There's a second point, about what stays on the machine.
Content that appears in chat or tool results is retained in local session history.
So there's a local footprint, and your device standards apply to it.
Now the reassuring part.
Existing model restrictions, training settings and enterprise policies continue to apply.
You aren't bypassing anything you've already decided.
GitHub-provided models follow the Copilot terms and policies for your plan.
Other providers' models are different.
Review that provider's terms and data handling before you rely on them.
Now our recommendation, and I want to be clear it's ours.
Match model choice to your data classification before piloting on sensitive repos.
For Australian government audiences, think about how your information classification, for example under the PSPF, maps to which models you approve.
The question isn't "is AI safe?"
It's "is this model right for this classification of information?"
That's a question your agency already knows how to answer.
It's the same discipline you apply to any system that handles your data.
So for the pilot, pick a non-sensitive repository.
Prove the workflow where the stakes are low.
Then extend to sensitive work only when your classification and model choices line up.
Know what reaches the model, and you control what the model reaches.
If someone asks, "does our code train the model?", I'd point to the slide.
Existing model restrictions, training settings and enterprise policies continue to apply.
For GitHub-provided models, the Copilot terms and policies for your plan govern.
For other providers, review their terms and data handling directly.
Don't assume, check.
If someone asks, "what's the safest place to begin?", the answer is a non-sensitive repository.
There's very little to lose and a great deal to learn.
And if someone asks, "what about the local session history?", treat it as you would any other working data on a managed device.
Know where it sits and who can reach it.
Here's a question to take back to your teams.
Do your developers know which classification of information they are allowed to put in front of which tool?
If the answer is "not yet", this pilot is a good reason to write it down.
That's the heart of responsible adoption.

## Slide 40: Recommended approach

So what would I actually do if I were in your seat?
Here's a pilot path for agencies, in three steps.
And as the footnote says, it's a suggested approach based on GitHub Docs guidance, to be adapted to each agency's policies.
It's our recommendation, not something the docs prescribe.
Step one, prepare.
Confirm your Copilot plan, and that the GitHub Copilot app policy is enabled.
Choose approved models for your data.
Agree tool-permission defaults.
That's an afternoon of decisions, and it saves weeks of debate.
Step two, pilot.
Pick one non-sensitive Azure DevOps repo.
Review every agent pull request.
Keep Agent Merge off to start.
Notice the pattern.
Small scope, full visibility, conservative settings.
Step three, scale.
Lean on branch policies and reviewers.
Monitor activity in Azure DevOps.
Add Entra revocation to offboarding.
By now you'll have evidence from your own people, on your own code, rather than a vendor's promise.
That's the sound bite for this slide: start small, prove it, then scale.
Evidence beats enthusiasm every time.
And I'd add a point about how this reads to an executive or a minister's office.
A bounded pilot with named controls is easy to approve and easy to defend.
It says you've moved deliberately, not recklessly.
In public sector, that's the difference between an innovation story and a headline.
A pilot is how you turn a cautious "maybe" into a confident "yes".
It's also how you turn "maybe not" into a well-documented "not yet".
Either outcome is a good result, because it's based on evidence.
If someone asks, "how long should the pilot run?", the next slide says one sprint, and I mean it.
Long enough to see real work, short enough to stay accountable.
If someone asks, "who should be on the pilot team?", pick a small group of people who like to give honest feedback.
Include someone who will review every pull request carefully.
Include someone from security, so governance is part of the pilot rather than an afterthought.
And if someone asks, "how will we know it worked?", decide before you start.
Agree what a good outcome looks like, and what would make you stop.
A pilot with a stop condition is a pilot your leadership can trust.
Write down what you learn, including the awkward findings.
Next time, someone else in government will ask you for exactly that evidence.
Which brings me to the ask.

## Slide 41: Next step

So here's my ask, and it's a small one.
One repo.
One sprint.
Enable the integration for a small team.
Pilot it on a non-sensitive repo.
And review governance together with your security colleagues, side by side, not at the end.
Let me tie the session together.
Your code stays where it is.
Your permissions stay as they are.
Your policies still decide what merges.
New capability, same controls.
It's off by default, so nothing happens until you choose.
It's opt-in per pull request for the powerful bits, so you stay in charge of the pace.
And where there are gaps, there are known mitigations in tools you already run.
That's a story government can say yes to.
Not because it's the most exciting thing you'll see this year.
Because it's the one that respects how you already govern.
If you take one thing away today, take this.
The question isn't whether agents come to the public sector.
It's whether they arrive inside your guardrails.
You can answer that question this month, with one repo and one sprint.
A thought on the word pilot.
Pilot doesn't mean experiment without rules.
In this case it means a controlled, bounded, reviewable step.
Small team, non-sensitive repo, Agent Merge off, every pull request reviewed.
That's something you can explain to an auditor, and to your own leadership, in a single breath.
The leaders I admire in public service don't wait for certainty, and they don't skip governance.
They find the smallest safe step and take it.
This is that step.
If you leave with only one action, make it a conversation.
Sit down with your security team this week and look at the five governance questions together.
Then choose the repo.
The learn-more address is at the bottom of the slide, and the button is the invitation: plan your agency pilot.
I'd love to hear where you'd start.
Which repo is the safe first candidate, and who is the small team?
Let's use the time we have left for your questions.
Thank you.
