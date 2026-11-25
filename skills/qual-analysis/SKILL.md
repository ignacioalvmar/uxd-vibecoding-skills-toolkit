---
name: qual-analysis
description: Analyzes qualitative user research data (interview transcripts or notes, open-ended survey answers, usability observations, app reviews, support tickets) into codes, themes, pain points and design implications, with verbatim quotes and participant IDs as evidence. Use when someone wants thematic analysis, coding, affinity clustering of research data, pain point extraction, sentiment classification of user feedback, or a synthesis of interviews.
---

# Qualitative analysis

Helps a UX designer find patterns in qualitative data and tie each one to evidence. AI is the pattern-finder. The student is the meaning-maker.

## Why this skill exists

A language model can read forty pages of transcripts in seconds and return tidy themes. The risks are that the themes are generic, that minority voices disappear, that quotes get "improved", and that the result sounds more certain than a sample of six people allows. Every step below exists to keep the analysis honest and checkable.

## Before you start

Ask for what is missing, in one short message:

1. **The data**, with participant IDs if possible.
2. **Research goal**: what the study set out to learn.
3. **What the output is for**: team synthesis, report, persona input, design decisions.

**Privacy check.** If the data contains names, emails, employers or other identifying details, ask the student to anonymize it, or replace identifiers with P1, P2... in your working copy. For public data such as app reviews this is less critical, but usernames still stay out of the output.

**Size check.** Say how much data you received (number of participants or comments). If a transcript looks cut off or the data is too long to read fully, say so. Never analyze a part and present it as the whole.

## Workflow

### 1. Familiarize

Summarize in a few lines what the data covers and where it is thin. This shows the student that you read it and what its limits are.

### 2. Code (bottom-up)

Create codes from the data. Do not start from a preset list unless the student provides a codebook.

| Code | Definition | Example quote (ID) | Participants |
|---|---|---|---|

### 3. Themes

Group codes into three to six themes. For each:

- a short, specific name ("Decision fatigue at 6 pm", not "Usability issues")
- a one or two sentence description
- two or three **verbatim** quotes with IDs
- how many participants support it, and who does not fit

Then add a section **What does not fit**: contradictions, outliers and single voices that matter. A theme analysis without this section is usually too smooth.

### 4. Pain points

List pain points with trigger, consequence, current workaround, frequency (how many participants) and evidence IDs. Do not rank by "severity" unless the data supports it; say what the ranking is based on.

### 5. Design implications (on request)

| Theme | What it means | Evidence (IDs) | Design implication | Risk |
|---|---|---|---|---|

Implications describe what a solution must achieve, without naming features. "Users need to see what is already in the fridge before planning" is an implication. "Add a fridge scanner" is a solution and belongs to ideation.

### Sentiment classification (only when asked)

For large volumes of short feedback: classify each comment as positive, negative, neutral or mixed, give counts, and list the comments under each heading. Point out sarcasm or ambiguous items you were unsure about. Sentiment counts describe this sample, not all users.

## Rules for evidence

- Quotes are copied exactly. Never clean up, merge or shorten inside quotation marks. Use [...] only for a visible cut.
- Every claim carries participant IDs.
- Use counts ("4 of 6"), not vague words ("most users"). With small samples, do not use percentages.
- Do not explain causes the participants did not give.

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Typical items:

- Spot-check quotes against the source. Search for at least three of them in your original data.
- Rename the themes in your own words. Do they still hold?
- Look for what is missing: what did you hear in the interviews that is not here?
- Decide which themes are strong enough to act on with this sample size.
- A second human coder on part of the data is still the best check.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.
