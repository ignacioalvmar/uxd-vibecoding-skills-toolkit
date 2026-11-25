---
name: prd-builder
description: Builds a Product Requirements Document (PRD) for a vibe coding project from a product brief, research and design decisions, through a short guided interview, using the course Vibe-Coding PRD template. Use when someone wants to write, draft, start or complete a PRD, plan an app before building it with an AI coding tool, or turn a concept into requirements, features and acceptance criteria.
---

# PRD builder

Guides a designer from a concept to a PRD that both the team and an AI coding assistant can build from. THINKING is the first of the five vibe coding skills: define what you want before you prompt.

## Why this skill exists

The PRD is the context the AI builds from, and the project's memory when the chat context runs out. A vague PRD produces a generic app and many repair prompts. A good one is specific enough that every feature can be built and checked one at a time. Writing it is design work, so this skill asks and structures. It does not decide the product for the student.

## If PRD-Copilot is available

The course provides a PRD-Copilot plugin for Claude. If a PRD-Copilot skill or plugin is available in this environment, hand the interview over to it and use this skill only for the final check below. If it is not available, as in most other tools, run the workflow here. The result is the same template either way.

## Inputs

Ask what exists already, in one short message: product brief, personas or research findings, wireframes or mock-ups, design tokens or a DESIGN.md, the target platform, team and time frame. The `concept-brief` skill creates a brief if there is none.

## Workflow

Use `references/prd-template.md` as the structure.

### 1. Fill what is known
Draft the sections the provided material supports. Mark everything else `TBD`, with the question that would settle it. Never invent personas, metrics, features or technical choices to make the document look complete.

### 2. Interview for the gaps
Ask about the gaps in small rounds of three to five questions, most important first:

1. Core context: problem, solution, target users, primary use cases, non-goals
2. Scope: what is in the MVP, what is explicitly out, assumptions and risks
3. Features: for each one a user story, a priority (P0/P1/P2) and acceptance criteria
4. UX foundations: vibe principles, accessibility requirements, the high-level journey
5. Design: tokens, components, tone. Point to DESIGN.md if there is one
6. Tech stack: only as far as the platform needs it

Stop interviewing when the P0 features are fully specified. A complete PRD for three features beats a thin one for ten.

### 3. Make it buildable
Three things turn a descriptive PRD into one an AI can follow:

- **Acceptance criteria as checklists.** Observable and testable, one behavior per line: "With 20 prompts per day, large model and 5 images per week, the page shows 155.0 Wh." Not: "The calculator works correctly."
- **Vibe turned into rules.** A principle such as "curious, not guilty" needs at least one concrete rule: "Result texts never use the words 'waste' or 'bad'. Each result card shows one everyday equivalent." Ask the student for the rule. Offer examples only if they are stuck.
- **Exact values in one place.** Constants, formulas, copy text and tokens are written once, as tables or code blocks, and referenced from elsewhere.

### 4. Tech stack in plain words
Students are designers. Recommend a stack only as far as the target platform requires, and explain each choice in one plain sentence. If the platform decides the stack (Lovable does), say so and do not offer alternatives. Mark recommendations as yours, so the student can ask someone who knows.

### 5. Order the build
List the feature modules in build order, one prompt-sized feature each, foundations first. This list becomes the sequence of prompts.

## Final check

Before delivering, check: every P0 feature has a user story and testable acceptance criteria; non-goals and out-of-scope are filled; accessibility requirements are concrete; no personas or user claims without a source or an "assumption" label; exact values appear once; no section invented by you; `TBD` items listed at the top. Offer a deeper review with the `prd-critique` skill.

## Output

The PRD as markdown, to be saved as `PRD.md` in the project root, plus a short list of open `TBD` questions. Next step: the `kickoff-prompt` skill turns it into the first build prompt.

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Typical items:

- Read every acceptance criterion. Could you check it yourself in under a minute?
- Cut scope. What could leave the MVP without hurting the core use case?
- Resolve the `TBD` list before you build, or decide on purpose to leave items open.
- Keep the PRD alive: update it when decisions change, and commit it to your repository.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.
