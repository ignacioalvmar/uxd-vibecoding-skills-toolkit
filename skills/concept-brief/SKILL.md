---
name: concept-brief
description: Condenses the output of a brainstorming or ideation workshop (sticky notes, clusters, shortlist, discussion notes) into a workshop insights summary and a one-page product brief with problem, users, solution and key features, plus an outline for a short pitch or lightning talk. Use when someone wants to summarize a workshop, write up brainstorming results, create a product or concept brief, define a concept after ideation, or prepare a concept pitch.
---

# Concept brief

Turns workshop material into two things a team can use the next day: a summary of what was learned and a product brief for the chosen concept. Also outlines a five-minute pitch.

## Why this skill exists

Workshop results usually die on the wall of sticky notes. AI is good at condensing messy notes into a readable document. The danger is that it fills gaps with invention: a brief full of confident features and user claims that nobody in the room said. Everything in the output must come from the workshop material or be marked as an open question.

## Inputs

Ask for what is missing in one short message:

1. **Workshop material**: ideas, clusters, votes, shortlist, notes. Pasted text, or photos of the board.
2. **Context**: design challenge, participants (roles, not names), date, activities done.
3. **The chosen direction**, if the team has one. If not, produce only the workshop summary and suggest converging first (`idea-clustering` skill).
4. **What is needed**: summary, product brief, pitch outline, or all three.

## Output 1: Workshop insights summary

```
# Workshop summary: [design challenge]

## Overview
Date, participants (roles), challenge, goals

## Process recap
What the team did, in two or three lines

## Key themes and insights
For each theme: title, one sentence on what was learned and why it matters,
three or four representative sticky notes in their original wording

## Emerging opportunities
3 to 5 opportunity areas or design directions

## Open questions and assumptions
What the team does not know yet

## Next steps
Concrete actions with an owner role (prototyping, user testing, further research)
```

## Output 2: Product brief (one page)

```
# [Concept name]: product brief

One-sentence pitch:

## Problem
Who has it, in which situation, and why it matters. Based on: [research / assumption]

## Target users
Primary and secondary. Based on: [research / assumption]

## Solution
What it is and how it helps, in three or four sentences

## Key features (3 to 5)
Feature - what the user can do - which problem it solves

## What makes it different
## Out of scope for now
## Assumptions to test
## Success: how we would know it works
```

Rules for the brief:

- Mark the basis of every claim about users or the problem: **research** (with source) or **assumption**. Workshop ideas are assumptions until tested.
- Three to five features. If the material contains fifteen, ask the team which ones carry the concept. Do not choose silently.
- No technical stack and no acceptance criteria. Those belong in the PRD (`prd-builder` skill), which takes this brief as input.
- Suggest a name only if the team has none, and offer three options.

## Output 3: Lightning talk outline (5 minutes)

1. Hook: the problem in one concrete moment (30 s)
2. Who it is for (30 s)
3. The concept in one sentence, then the solution (90 s)
4. Three key features, shown, not listed (90 s)
5. What we do not know yet and what we test next (30 s)
6. Closing line (15 s)

Give speaker bullet points, not a script. Suggest one visual per section; the `concept-visuals` skill writes the image prompts.

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Typical items:

- Read the brief aloud to the team. Does everyone recognize the concept you agreed on?
- Check every line marked "assumption". Which one would sink the concept if it were false? Test that first.
- Run the brief through the four filter questions (`idea-filter` skill) before prototyping.
- Rewrite the one-sentence pitch in your own words.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.
