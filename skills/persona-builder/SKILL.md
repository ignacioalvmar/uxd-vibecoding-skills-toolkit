---
name: persona-builder
description: Synthesizes real user research (interview notes, quotes, survey results, observations) into evidence-based user personas with a traceability table, a bias and stereotype audit, and task scenarios. Use when someone wants to create, draft, check or improve a user persona, proto-persona or user segment description, or asks to turn research findings into personas. Also use when asked to "just make a persona" without data, to steer the request toward evidence.
---

# Persona builder

Helps a UX designer synthesize and articulate their research as personas. It does not invent a user.

## Why this skill exists

Asked for "a persona for my app", a language model produces a plausible, generic stereotype. That is worse than no persona, because teams then design for a person who does not exist. A persona is only useful when every claim in it can be pointed back to something a real participant said or did.

## Before you start

Ask for what is missing, in one short message:

1. **Research data**: interview notes, quotes, survey results, observations. Participant IDs (P1, P2...) help.
2. **Product and research goal**: what is being designed and what the research set out to learn.
3. **Who will use the persona** and for which decisions.

**Anonymization check.** Look at the data before using it. If it contains real names, emails, employers or other identifying details, tell the student and ask them to anonymize it (or offer to replace identifiers with P1, P2... in your working copy). Do not carry identifying details into the persona.

**If there is no data.** Say plainly that a persona without research is a guess. Offer two honest options: (a) help plan the research (the `interview-guide` skill does this), or (b) write a **proto-persona** that is labeled as assumptions on every page, with each assumption phrased as a hypothesis to test. Never present a proto-persona as a persona.

## Workflow

Run all six steps. Show the intermediate results; the student should see how the persona was built.

### 1. Structure the findings

From the data only, summarize: primary goals, pain points and frustrations, motivations, observed behaviors. Keep participant IDs next to each point.

### 2. Cluster by behavior

Propose behavioral segments: groups of participants who share goals and behaviors. Do not segment by demographics (age, gender, nationality) unless the data shows that the attribute drives behavior. Say how many participants support each segment. With very few participants, say that the segments are tentative.

Ask the student which segment(s) to turn into personas.

### 3. Draft the persona

One page, in this structure (details in `references/persona-template.md`):

- Name and one-line descriptor based on behavior ("the anxious first-time gardener"), plus a suggestion for a neutral image
- A quote taken or closely adapted from the data, with participant ID
- Short bio based only on the data
- Goals, frustrations, motivations, behaviors
- Context of use

Leave out anything the data does not support. A gap is information: list it under "What we do not know yet".

### 4. Bias audit

Reread the draft and flag anything that leans on demographic or social stereotypes, or that you added because it "sounds right". Typical offenders: age, gender, job, income, hobbies, tech skill, family status. For each flag, give a replacement grounded in observed behavior, or delete it.

### 5. Evidence mapping

Produce a traceability table for every claim in the persona:

| Persona claim | Evidence (quote or observation) | Participant | Strength |
|---|---|---|---|

Strength: **strong** (several participants), **weak** (one participant), **none** (no evidence). Remove or mark every "none" row. This table is the main quality check, so do not skip or shorten it.

### 6. Scenario check

Write one or two short task scenarios that show the persona in a real moment of struggle, plus acceptance criteria the design should meet for this persona. Scenarios build empathy; keep them consistent with the evidence.

## Your judgment (always end with this)

Close with a short block titled **Your judgment** listing what the student must do. Adapt to the case; typical items:

- Read the traceability table and challenge every weak row.
- Check the persona against your own memory of the interviews. Does it feel like the people you met?
- Decide whether the sample is large enough to trust the segments.
- Share it with the team and note where they disagree.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.

## Boundaries

- Never invent quotes, numbers or participants.
- Do not add demographic detail for color.
- Synthetic users can be useful for rehearsal. They are not evidence and never appear in the traceability table.
