---
name: project-context-files
description: Creates or updates the context files that AI coding agents read in a project. AGENTS.md covers how to build (commands, conventions, structure, rules). DESIGN.md covers how it should look and feel (theme, color tokens, typography, components, layout, do's and don'ts). Built from the PRD, the design specification and the existing code. Use when someone starts a project in Cursor, Codex, Claude Code or Antigravity, wants the AI to stop ignoring their design system or conventions, asks for an AGENTS.md, DESIGN.md or CLAUDE.md, or keeps repeating the same instructions in every prompt.
---

# Project context files

Writes the two files that give an AI coding agent standing knowledge of a project, so the student does not have to repeat it in every prompt. CONTEXT is one of the five vibe coding skills.

## Why this skill exists

An agent starts every session knowing nothing about the project. Without context files it guesses the commands, invents colors and restyles components. Two short files fix most of this:

| File | Read by | Defines |
|---|---|---|
| `AGENTS.md` | Coding agents | How to build: commands, conventions, structure, rules |
| `DESIGN.md` | Agents doing interface work | How it looks and feels: tokens, type, components |
| `README.md` | Humans | What the project is and how to run it |

For designers, DESIGN.md is the lever that matters most. It is the design system in a form the AI will follow.

## Inputs

Ask for what is missing in one short message:

1. **Which file(s)**: AGENTS.md, DESIGN.md or both.
2. **Sources**: PRD, design specification or tokens, Figma or screenshots, brand guidelines, the existing repository.
3. **Tool(s) in use.** Most coding agents read `AGENTS.md`. Claude Code reads `CLAUDE.md`, and a common pattern is a short `CLAUDE.md` that points to `AGENTS.md`. Conventions change, so tell the student to check their tool's documentation, and do not promise what a tool reads.

**If you have access to the project files, read them first.** Take commands from `package.json` or the equivalent, the structure from the folders, tokens from the existing styles. Write down what is there. Never invent a command, a path or a version number. A wrong command in AGENTS.md is worse than a missing one, because the agent will trust it.

## AGENTS.md

Use the eight sections in `references/agents-md-template.md`: project overview; setup; build, run and test commands; code style and conventions; project structure; commit and pull request rules; security and safety; prompt hints.

Rules:

- Short and specific. One to two pages. Every line should change what the agent does.
- Commands exactly as they must be typed, in a table.
- Include the course rules unless the student says otherwise: work on a feature branch, commit after each task, do not change files outside the task, never commit secrets, follow PRD.md and DESIGN.md, add prompts to PROMPTS.md.
- A "Do not" list for the mistakes the agent has already made in this project.
- Leave a section out if there is nothing true to put in it. Do not fill it with generic advice.

## DESIGN.md

Use the nine sections in `references/design-md-template.md`: visual theme and atmosphere; color palette and roles; typography; component stylings; layout principles; depth and elevation; do's and don'ts; responsive behavior; agent prompt guide.

Rules:

- Color and type as **tables with token name, exact value and role**. The agent needs the role ("primary buttons, links") to use a color correctly.
- Components with their states: default, hover, focus, disabled, error.
- Do's and don'ts are the most effective section. Name the generic habits to avoid ("no gradients", "no raw hex values in components, use tokens") and the accessibility rules to keep (contrast, visible focus, touch targets, reduced motion).
- Take values from the student's design. If a value is missing (no spacing scale, no error color), list it as a question. Offer a proposal only when asked, and mark it as proposed.
- Check text and background pairs for contrast, and flag any that fail WCAG AA.

## Output

Each file in its own code block (or written to the project root if you can write files), followed by:

- a list of what you could not fill and why
- two or three test prompts to verify that the agent follows the files, for example "Explain this project's architecture in 5 bullets and name anything that contradicts PRD.md or DESIGN.md" and "Add a secondary button to the hero. Use only tokens from DESIGN.md."

If a file already exists, read it and propose changes as a short list. Do not overwrite it without asking.

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Typical items:

- Every command in AGENTS.md: run it once yourself.
- DESIGN.md is your design system. Correct anything that is not what you intended.
- Keep both files up to date. When the agent repeats a mistake, add a rule. When a rule no longer applies, delete it.
- Commit both files. They are part of the project.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.
