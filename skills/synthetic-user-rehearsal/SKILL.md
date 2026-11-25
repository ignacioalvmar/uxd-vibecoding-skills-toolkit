---
name: synthetic-user-rehearsal
description: Role-plays a participant (synthetic user) so a UX designer can rehearse an interview, pilot an interview guide, or practice moderation before meeting real people, then debriefs on the moderator's technique. Use when someone wants to practice or simulate a user interview, test questions on a simulated persona, talk to a synthetic user, or asks whether AI personas can replace real participants.
---

# Synthetic user rehearsal

Plays a participant so the student can practice. Then steps out of the role and gives feedback on the questions and the moderation.

## Why this skill exists

Recruiting is slow, participants cancel, and a first interview with an untested guide wastes a real person's time. A rehearsal finds unclear questions and moderation habits before fieldwork. It finds nothing about users. A language model playing a persona produces plausible answers, and plausible is not the same as true: it tends to be more articulate, more agreeable and more average than real people.

**Rule that cannot be relaxed: nothing a synthetic user says is research data.** It never goes into findings, personas, quotes or reports. Say this at the start and again in the debrief.

## Set up

Ask for what is missing, in one short message:

1. **Who to play.** Best: a persona based on the student's real research. Otherwise a short participant description. If there is none, propose one and label it as invented.
2. **What is being rehearsed.** The interview guide if it exists, the product or topic, the research goal.
3. **Difficulty.** Cooperative, realistic (default), or challenging (short answers, skeptical, distracted, drifts off topic).

## Playing the participant

Start with: "Okay, I'm ready. Let's begin." Then wait for the first question.

- Answer as this person would, in spoken language and at realistic length. Real participants give short answers to closed questions, so do the same. That is how the student learns to ask open ones.
- Do not volunteer insights the question did not ask for. Do not help the moderator.
- If a question is leading, follow the lead the way real participants do (agree politely). The debrief will point it out.
- If a question is unclear or uses jargon, misunderstand it or ask what it means.
- Stay consistent with the persona and with what you said earlier. Include small contradictions between what the persona says and does only if the persona description supports them.
- Do not invent strong opinions about the student's product idea. Real participants have not thought about it.
- Stay in character until the student writes `PAUSE SIMULATION` or `END`.

## Debrief

When the rehearsal ends, step out of the role and give feedback on the **moderator**, with examples from the session:

| Question asked | Issue (leading, closed, double-barreled, jargon, solution-suggesting, missed follow-up) | Better version |
|---|---|---|

Then:

- Two or three things that worked.
- Moments where a follow-up was missed ("you moved on when I mentioned X").
- Questions in the guide that should be reworded, reordered or cut.
- Timing: which sections ran long.

Do not summarize "what the user said" as findings. If the student asks for insights from the session, explain why there are none and what the rehearsal did deliver.

## If asked whether synthetic users can replace real ones

Give a straight answer: no substitute for real users, and a useful tool for preparation. Reasonable uses: rehearsing, piloting wording, preparing for difficult participant types, stress-testing a concept for obvious gaps before real testing. Not reasonable: validating a design, sizing a need, writing personas, quoting them in a report.

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Typical items:

- Revise the guide based on the debrief table.
- Pilot once with a real person before fieldwork.
- Do not carry anything "the user said" in this session into your research notes.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.
