---
name: kickoff-prompt
description: Writes the first prompt for a vibe coding project (the kick-off prompt) from a PRD or product brief, tailored to the target platform (Lovable, Replit, DeepSite, Cursor, Antigravity, Codex, Claude Code). Use when someone is about to start building an app or prototype with an AI coding tool, asks for a starter, initial or kick-off prompt, wants to turn a PRD or concept into a first build prompt, or wants an existing kick-off prompt reviewed.
---

# Kick-off prompt

Turns a PRD or product brief into the first prompt of a vibe coding project. The first prompt sets the architecture, the scope and the design direction, and a weak one costs credits and hours of repair.

## Why this skill exists

Two failure modes are common. Too little: "build me a study app", which lets the AI invent the product. Too much: the whole PRD pasted as one request for twenty features, which produces a fragile tangle. A good kick-off prompt gives full context, a small first task, explicit limits and a way to check the result.

## Before you write

Collect what is missing in one short message:

1. **PRD or product brief.** If there is none, stop and say that planning comes first (THINKING is the first vibe coding skill). Offer to build the PRD with the `prd-builder` skill if available, or collect the minimum here: problem, target users, three core features, what is out of scope.
2. **Target platform.** Then read `references/platforms.md` for that platform's conventions.
3. **Goal of the first build**, one of:
   - **Scaffold**: the whole small app in one go. Fine for single-page or very small projects.
   - **Foundations**: project structure, navigation and the main page only, then feature by feature. Better for anything larger.
   If the student is unsure: more than three features, a backend or user accounts means Foundations.
4. **Design direction**: brand colors, typography, a DESIGN.md, reference screenshots. If none exists, ask for two or three adjectives and one reference, so the AI does not fall back on its generic default look.

## Build the prompt

Use the structure in `references/kickoff-template.md`. Rules that matter:

- **Take content from the PRD, do not invent it.** If the PRD is silent on something important (for example what is out of scope), ask the student. Do not fill the gap yourself.
- **Out of scope is mandatory.** Naming what not to build is the cheapest way to stop the AI from wasting effort.
- **Name the stack only when the platform lets you choose.** Follow `references/platforms.md`. Students are designers: explain any stack choice in one plain sentence.
- **Exact values stay exact.** Numbers, formulas, copy text and color codes from the PRD go in verbatim, with "use exactly these, do not invent others".
- **Accessibility is part of the first prompt**, not a later fix: contrast, labels, keyboard focus, reduced motion, target screen widths.
- **End with a check.** One concrete, observable acceptance test taken from the PRD ("with inputs X the page must show Y"), plus what the student should see on screen.
- **Plan before code** where the platform supports it: ask for a plan and approval first, and invite clarifying questions.
- **Self-contained when needed.** Some tools cannot read attached files. For those, everything the AI needs must be in the prompt text.
- Keep it as short as it can be while keeping all critical context. Cut adjectives, keep facts.

## Output

1. The kick-off prompt in one code block, ready to copy.
2. **How to use it**: three or four lines for this platform (which mode, what to attach, what to do before sending, for example create the repo and first checkpoint).
3. **What comes next**: the first two or three follow-up feature prompts as one-line titles only, to show the one-feature-at-a-time path. Do not write them out unless asked.

If the student gives an existing kick-off prompt to review, check it against the rules above, list the gaps, and return an improved version.

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Adapt to the case; typical items:

- Read the prompt against your PRD. Is anything there that you did not decide?
- Is the first task small enough to verify in five minutes?
- After the first build: run the acceptance check yourself, then commit or save a checkpoint before the next prompt.
- If the result is far off, fix the prompt and restart. Do not patch a bad foundation with ten follow-ups.

## Prompt log

If you can write files in this environment, append the final kick-off prompt to `PROMPTS.md` in the project root (create it if missing) with date, platform and skill name. If you cannot write files, remind the student to save it there.
