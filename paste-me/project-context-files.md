<!-- Paste-me version of the 'project-context-files' skill. Generated file, do not edit. -->
Follow the instructions below for the rest of this conversation. Where they mention reference files, use the reference sections at the end. Start by asking me for the inputs you need.

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

---
## Reference: references/agents-md-template.md

# AGENTS.md template

Fill only with facts from the project. Delete sections that would be empty.

````markdown
# AGENTS.md

## Project overview
[One paragraph: what this project is, who it is for, the stack.]
Source of truth for requirements: `PRD.md`. For visual design: `DESIGN.md`.

## Dev environment and setup
- Requirements: [runtime and version]
- Install: `[command]`
- Environment variables: see `.env.example`. Never commit `.env`.

## Build, run and test
| Command | What it does |
|---|---|
| `[dev command]` | Local dev server |
| `[build command]` | Production build |
| `[test command]` | Run tests |
| `[lint command]` | Lint and format check |

## Code style and conventions
- [Language, formatter, naming patterns]
- Styling: use design tokens from `DESIGN.md`. No raw hex colors in components.
- Accessibility: semantic HTML, labels on inputs, visible focus, WCAG 2.1 AA.

## Project structure
```
[folder map with one line per folder]
```

## Commits and pull requests
- Work on a feature branch (`feature/<name>`). Never commit to `main`.
- Commit after each completed task with a descriptive message.
- One feature per branch and pull request.
- Add the prompts used to `PROMPTS.md`.

## Security and safety
- Never commit secrets or API keys.
- Do not delete data or files outside the task.
- Do not add dependencies without asking.
- Store no personal data beyond what `PRD.md` allows.

## Do not
- [Mistakes the agent has made in this project, one per line]

## Prompt hints
- "Read PRD.md section [x] and plan feature [y]. Do not write code yet."
- "Change only [file]. Do not change anything else."
- "Run the tests and tell me how I can verify the result myself."
````

## Notes

- A nested `AGENTS.md` in a subfolder can add or override rules for that part of the project.
- Keep it to one or two pages. Long files get skimmed, by people and by models.

---
## Reference: references/design-md-template.md

# DESIGN.md template

Values come from the student's design. Mark anything proposed by the AI as "proposed".

````markdown
# DESIGN.md

## 1. Visual theme and atmosphere
Mood: [for example: calm and institutional, curious, positive]
Density: [sparse with generous whitespace / information-rich]
Philosophy: [one sentence]

## 2. Color palette and roles
| Token | Hex | Role |
|---|---|---|
| `--color-primary` | `#......` | Header, primary buttons |
| `--color-accent` | `#......` | Highlights, links |
| `--color-success` | `#......` | Success states |
| `--color-error` | `#......` | Errors, destructive actions |
| `--bg-canvas` | `#......` | Page background |
| `--bg-surface` | `#......` | Cards, panels |
| `--text-primary` | `#......` | Body copy, headings |
| `--text-muted` | `#......` | Captions, metadata |
| `--border-subtle` | `#......` | Dividers, card borders |

Checked contrast pairs: [text on background = ratio, pass or fail AA]

## 3. Typography rules
Font families: headings [..], body [..], fallbacks [..]
| Element | Size | Weight | Line height |
|---|---|---|---|
| H1 | | | |
| H2 | | | |
| H3 | | | |
| Body | | | |
| Caption | | | |

## 4. Component stylings
Buttons: primary, secondary. States: default, hover, focus, disabled.
Inputs: default, focus, error, with label and help text.
Cards: [radius, border, padding]
Navigation: [behavior, active state]

## 5. Layout principles
Spacing scale: [4, 8, 16, 24, 32, 48]
Grid and max content width: [..]
Whitespace: [..]

## 6. Depth and elevation
[Shadow system or "flat, borders only"]

## 7. Do's and don'ts
Do:
- Use tokens for every color, size and space.
- Keep focus visible on every interactive element.
- Keep touch targets at least 44 px.
Don't:
- No raw hex values in components.
- No new colors, fonts or shadows without asking.
- [Generic habits to avoid, for example: no purple or blue gradients]

## 8. Responsive behavior
Breakpoints: [375, 768, 1440]
Collapsing strategy: [how columns and navigation change]
Motion: respect `prefers-reduced-motion`.

## 9. Agent prompt guide
Quick reference: primary [hex], accent [hex], text [hex], background [hex]
Ready-to-use prompts:
- "Build [component] using only tokens from DESIGN.md."
- "Audit this page against DESIGN.md and list every deviation. Do not fix yet."
````

## Ways to get a first draft

- From a design specification (the `wireframe-to-hifi` skill produces one).
- From existing code: ask the agent to extract the tokens that are in use, then correct them.
- From a design tool that exports a DESIGN.md, or from a public example adapted to the brand. Always replace borrowed values with your own.
