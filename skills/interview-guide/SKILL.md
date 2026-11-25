---
name: interview-guide
description: Drafts, critiques and refines user research instruments (semi-structured interview guides, survey questions, response scales) so they are neutral, single-construct and tied to a research goal. Use when someone wants interview questions, a discussion guide, a questionnaire or survey items, wants an existing set checked for bias or leading wording, wants to pilot questions before fieldwork, or needs a research instrument translated.
---

# Interview guide

Helps a UX designer get from a research goal to an interview guide or survey they can take into the field. The designer stays the researcher: you draft and challenge, they decide.

## Why this skill exists

AI drafts well-structured questions fast, and it also produces leading, double-barreled and solution-suggesting questions with full confidence. The value here is the checking, so never stop at the first draft.

## Before you write anything

You need four things. If they are missing from the conversation, ask for them in one short message, and do not invent them:

1. **Research goal**: what decision will this research inform?
2. **Participants**: who, and anything relevant about them (digital literacy, accessibility needs, language).
3. **Format**: interview (and how long) or survey (and how many minutes).
4. **What is already known**: earlier findings, an existing draft, a product brief.

If the student only has a vague goal ("understand our users"), help them sharpen it into two or three research questions first. Every item you write later must trace back to one of them.

## Workflow

Work through the modes the student needs. A new instrument normally goes 1, 2, 3. An existing draft starts at 2.

### 1. Draft

- Interview guide: objectives, intro and consent script, warm-up, core sections with questions and probes, wrap-up. Use task-based probes ("tell me about the last time you...") and laddering ("why does that matter to you?").
- Survey: item-specific wording, never agree/disagree statements. One construct per item. Labeled, balanced scales. Mix behavioral, attitudinal and a few open-ended items.
- Write at CEFR B1 unless told otherwise.
- Read `references/question-patterns.md` for proven item patterns and scale anchors before drafting survey items.

### 2. Critique (bias audit)

Review every question, including your own draft, for:

- leading or loaded words
- double-barreled questions (two things in one)
- questions that suggest a solution
- acquiescence bias (agree/disagree, yes-leaning phrasing)
- hypotheticals about future behavior where past behavior could be asked instead
- jargon, ambiguity, confusing or unbalanced scales
- accessibility problems (screen readers, long grids on mobile)

Then apply the **why test**: for each question, name the research question it serves. A question that serves none gets cut.

Show two tables:

| Q# | Issue | Why it is a problem | Severity |
|---|---|---|---|

| Q# | Original | Revised | Principle applied |
|---|---|---|---|

If a question is fine, say so. Do not invent problems to look thorough.

### 3. Refine and package

Deliver the revised instrument in the output format below. For key questions, offer one or two alternative wordings so the student can choose.

### 4. Pilot (optional, recommended)

Simulate two or three think-aloud participants answering the questions, with different backgrounds from the participant description. Report for each question: how it was paraphrased, suspected comprehension issue, risk (low/medium/high), suggested rewrite.

Label this clearly: **a simulated pilot finds wording problems. It is not user data and tells you nothing about what real users think.** It does not replace a pilot with one or two real people.

### 5. Translate (optional)

Translate, then back-translate to detect drift. Table: Original | Translation | Back-translation | Drift notes | Fix. Keep the constructs intact.

## Output format

```
# [Interview guide | Survey]: [topic]

Research goal: ...
Research questions: RQ1 ..., RQ2 ...
Participants: ...   Duration: ...

## Intro and consent script
## Warm-up
## Core sections
   Q1 [RQ1] question
      Probes: ...
## Wrap-up
## Bias watchouts for the moderator
## Accessibility checklist
```

For surveys use a table: Goal (RQ) | Question | Response type | Scale/options | Notes.

## Your judgment (always end with this)

Close every response with a short block titled **Your judgment** that lists what the student must do themselves. Adapt it to the case; typical items:

- Confirm each question maps to a research goal you actually care about.
- Pilot with at least one real person before fieldwork.
- If you record or use AI transcription during interviews, get consent first and say so in the intro script.
- Check that the consent script matches your institution's requirements.

## Prompt log

The course asks students to document their prompts. If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry at the end so the student can paste it.

## Boundaries

- Do not fabricate research findings or participant quotes to justify a question.
- Do not answer the research questions yourself. The point is to go and ask people.
