Here are the speaker notes for slides 9–19, copied as written. I tidied the blank lines but did not change any wording. The deck now has 49 slides, so this section sits at 9–19, which differs from the earlier numbering. I'd read through slide 9 and slide 12 before presenting. Slide 9 holds the whole talk track in one note, and slides 10, 11 and 12 repeat parts of it.

````markdown
# Speaker Notes: Modern by Design, Secure by Default (Slides 9–19)

## Slide 9: Canberra Developer Days – Modern by Design, Secure by Default

Presenter notes - slide 1 –

legacy code and a lot of PSPF 002, permission structure ISM

**Talk track**

I'm Xavier, a Software Solution Engineer here at Microsoft.

I've been working across regulated industries and the public sector lately, and before we jump into the technology, I'd like to test an observation with you.

CHANGE SLIDE

Two separate modernization conversations seem to be colliding right now.

There's the near-term focus about: managing legacy systems, improving developer productivity, and keeping up with strict compliance mandates like PSPF, where the clock is constantly ticking to identify, modernise and remediate vulnerabilities.

Then there's the paradigm shift: AI is transforming how we build software. If that changes, our approach to planning, quality, security, and ops has to evolve too—otherwise, faster output won't lead to better outcomes.

On 29 September, legacy stopped being a someday problem. PSPF says that Frontier AI has targeted the Commonwealth's technology estate, so keeping old, vulnerable systems running while weaknesses pile up is no longer an acceptable risk.

So I asked myself three questions

The first is: What is changing, and why now?

Well, there are really two clocks running. One is on the calendar: 31 December for Systems of Government Significance, then 31 March 2027 for every non-corporate Commonwealth entity to have its stocktake and a Legacy Technology Risk Management Plan with a reduction target. The other clock isn't written down anywhere, and it's moving faster: the time it takes to go from a vulnerability being found to being exploited

This leads us to the second question: who feels this most?

Accountable Authorities and CISOs, who need risk reduced and evidence to prove it. Service owners, who can't let public-facing services go down, and the PSPF policy backs them by asking for availability to be balanced with security.

The final question is: What's the impact on government agencies?

(Well, it's) Code that's hard to update, hard to explain, thinly tested and slow to patch. So each system you keep needs a documented mitigation. That mitigation competes with modernisation for the same scarce people.

If my thinking is right, the PSPF policy isn't really a stocktake problem; it's a modernisation-capacity problem. The stocktake tells you what you have; it doesn't give you the capacity to change it safely at the speed the threat now moves.

Let's pause for a moment, here. I'm making two assumptions. First, that a good portion of your current work is custom applications, not just infrastructure. Second, that your tightest constraint is people and time, not budget or intent.

So, quick show of hands - who thinks this accurately describes their situation? (WAIT) Okay, would anyone who didn't raise their hand like to share why?

(NON-RESPONSE) Okay, maybe not now. Another quick show of hands...

(RESPONSE) Thanks for sharing! Another quick show of hands…

Who already knows which system they'd tackle first? (Point at someone - ask what is it?)

Do you have the capacity to do it safely?

(Use the answers to confirm, correct, challenge or expand the hypothesis.)

Thanks for your participation.

So this is how I landed on today's topic: Modern by Design, Secure By Default

I'm going to use a case study from Microsoft's 1 Engineering System: a real product rewrite using agent-driven workflows. The central idea is to build the system that modernises the app. Along the way, I'll map it back to PSPF and to the ISM.

---

## Slide 10: Context – Two conversations colliding

Two separate modernization conversations seem to be colliding right now.

There's the near-term focus about: managing legacy systems, improving developer productivity, and keeping up with strict compliance mandates like PSPF, where the clock is constantly ticking to identify, modernise and remediate vulnerabilities.

Then there's the paradigm shift: AI is transforming how we build software. If that changes, our approach to planning, quality, security, and ops has to evolve too—otherwise, faster output won't lead to better outcomes.

On 29 September, legacy stopped being a someday problem. PSPF says that Frontier AI has targeted the Commonwealth's technology estate, so keeping old, vulnerable systems running while weaknesses pile up is no longer an acceptable risk.

---

## Slide 11: Framing – Three questions

So I asked myself three questions

The first is: What is changing, and why now?

Well, there are really two clocks running. One is on the calendar: 31 December for Systems of Government Significance, then 31 March 2027 for every non-corporate Commonwealth entity to have its stocktake and a Legacy Technology Risk Management Plan with a reduction target. The other clock isn't written down anywhere, and it's moving faster: the time it takes to go from a vulnerability being found to being exploited

This leads us to the second question: who feels this most?

Accountable Authorities and CISOs, who need risk reduced and evidence to prove it. Service owners, who can't let public-facing services go down, and the PSPF policy backs them by asking for availability to be balanced with security.

The final question is: What's the impact on government agencies?

(Well, it's) Code that's hard to update, hard to explain, thinly tested and slow to patch. So each system you keep needs a documented mitigation. That mitigation competes with modernisation for the same scarce people.

If my thinking is right, the PSPF policy isn't really a stocktake problem; it's a modernisation-capacity problem. The stocktake tells you what you have; it doesn't give you the capacity to change it safely at the speed the threat moves right now.

---

## Slide 12: Let's pause – Two assumptions

Let's pause for a moment, here. I'm making two assumptions.

First - you're spending an awful lot of time on custom applications, not just infrastructure.
Second, you've got all the budget and intent that you need - you're just struggling with people and time.

Show of hands - Thumbs up if that's 100% true for you.
Thumbs to the side if it's not the whole picture.

First, that a good portion of your current work is custom applications, not just infrastructure. Second, that your tightest constraint is people and time, not budget or intent.

So, quick show of hands - who thinks this accurately describes their situation? (WAIT) Okay, would anyone who didn't raise their hand like to share why?

(NON-RESPONSE) Okay, maybe not now. Another quick show of hands...

(RESPONSE) Thanks for sharing! Another quick show of hands…

Who already knows which system they'd tackle first to get out of this mess? (Point at someone - ask what is it?)
Can you do it safely?

(Use the answers to confirm, correct, challenge or expand the hypothesis.)

Thanks for your participation.

So this is how I landed on today's topic: Modern by Design, Secure By Default

I'm going to use a case study from Microsoft's 1 Engineering System: a real product rewrite using agent-driven workflows. The central idea is to build the system that modernises the app. Along the way, I'll map it back to PSPF and to the ISM.

---

## Slide 13: Today's story – From a trusted engineering loop to a connected product system

Presenter notes - slide 2 –

**Talk track**

Here's our agenda today, in four parts.

1. Why modernise the system, and how trust comes from goals and evidence
2. How Microsoft builds its 1 Engineering system to modernise the development practice.
3. We'll do a demo using a GitHub CoPilot modernisation extension.
4. I'll finish with what's changed about how we work.

We'll = wheel

---

## Slide 14: Section 01

Presenter notes - slide 3

By now, we've all experimented with AI agents in some capacity. (ChatGPT example) And chances are, we've also hit the same walls: integration friction, scaling limits, low production rates, and security roadblocks. It seems like our current approach won't hold up in our work environments, and we also fear messing it up.

So, our starting question wasn't just whether agents could write a feature. It was whether we could build a repeatable system that would reliably deliver production-quality software with AI. In order to trust a system, we have to see clear goals, guardrails, and evidence, and we also (awlso) have to see these put into practice in the real world

So, to put it to the test, we used the Microsoft 1 Engineering System as our proving ground.

---

## Slide 15: 1ES Modernisation Outcomes – AI assistants across the engineering system

Looking at 1 ES modernisation outcomes – let's crunch some numbers.

Using GitHub Copilot, there's a 5.5.% increase in PR Velocity on average, and a 40% increase in PR Velocity per hour of coding time - in other words, the responsiveness.

FirstMate - the AI assistant helping new hires gives us a 65% reduction in the time-it-takes to get them started.

ES Chat saves a huge 46.7 minutes on average per task, compared to traditional search methods.

DELETE LAST TWO

---

## Slide 16: Internal Adoption – GitHub Copilot @ Microsoft Highlights

Here's some more data on internal Copilot adoption at Microsoft. As you can see, it was quickly and positively taken up, with the vast majority of engineers – 81% – using the Copilot extension.

Looking at the suggestion acceptance rate - roughly a third up to 40% of AI generated code makes it to production. That tells us two things - firstly, humans are still building the guardrails and there's a quality assurance, but also that we're being realistic about outcomes and how to improve them.

Specific feedback we've received is that Copilot enables less task-switching and encourages more collaboration through dogfooding and sharing experience.

Let me show you what this all looks like in your world.

---

## Slide 17: Section 04

Presenter notes

**Talk track**

I have three things I'd like you to take away today. They are: assessment, transformation - and, what do governments desperately need? Security.

1. **Assessment** - GitHub Copilot analyses the current state of your project and comes up with modernisation plans. It identifies anything outdated, any dependencies, any migration problems and gives you actionable strategies to remove them.

2. **Transformation** - the system captures and reuses patterns, helps you build custom skills, and applies similar fixes across multiple codebases, resolving any resource and skill issues you may have.

3. **Security** - This is where GitHub Copilot is really essential. It patches vulnerabilities, auto-applies fixes, with security engineers reviewing changes every step of the way to ensure you're meeting PSPF requirements.

---

## Slide 18: What changed in how we work

Presenter notes - slide 21

**Talk track**

I'd like to finish with a personal example. For my team at Microsoft, this is what changed in how we work

To start, we now do the meatier tasks. Agents handle the operational work so the team can focus on product direction, meaningful tradeoffs, and risk.

Next, we build for the team. We use shared instructions, tools and standards. Accumulated learning creates organizational leverage, rather than simply leaving the benefit of all we've learnt inside an individual's session.

Finally, observability earns trust. Metrics, validation, and visibility make it possible to judge whether a workflow is reliable enough to receive more autonomy.

The true impact goes beyond faster coding tools, it represents a fundamental shift in how we work

---

## Slide 19: Thank You! – Questions and discussion

Presenter notes - slide 23 - Xavier / discussion participants

**Closing talk track**

Thanks very much for coming to my talk. I appreciate your time. This is the end of the session, but there is time for some further discussion if any of you would like to hang on. I'm happy to take any questions, but I also have a prompt for you. What would GitHub Copilot modernisation unlock for your team?

—-

Thanks very much for coming to my talk. I appreciate your time. This is the end of the session, but I'm happy to take any questions. One question I have for you is: what would GitHub Copilot modernisation unlock for your team? Please hang on, or else find me for a chat later on.

—-

Thank the audience. The main lesson is to combine structured knowledge, autonomous execution, validation, learning, and deliberate human decision points into a connected system.
````

I made a few light formatting changes in the markdown only, and I didn't touch the notes in the deck:

- I added bold for "Talk track" and the numbered items.
- I turned the agenda on slide 13 into a numbered list.
- I straightened the curly quotes and apostrophes.
- I added a space in "(ChatGPT example) And" on slide 14.

I left the stage cues and the "DELETE LAST TWO" reminder on slide 15 in place. Remove them before you share the notes with anyone else.
