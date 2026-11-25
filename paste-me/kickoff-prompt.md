<!-- Paste-me version of the 'kickoff-prompt' skill. Generated file, do not edit. -->
Follow the instructions below for the rest of this conversation. Where they mention reference files, use the reference sections at the end. Start by asking me for the inputs you need.

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

---
## Reference: references/kickoff-template.md

# Kick-off prompt template

Adapt the sections to the project. Remove lines that do not apply; do not leave placeholders in the final prompt.

```
Build a [type of application] called "[name]" for [target users].

Problem: [the user need, one or two sentences]
Solution: [how the app addresses it, one or two sentences]
Tone / vibe: [three or four words from the PRD]

Core features (build first):
1. [Feature] - [what it does, observable behavior]
2. [Feature] - [...]
3. [Feature] - [...]

Out of scope (do not build): [list]

Tech stack: [only if the platform lets you choose; see platforms.md]

Design: [design language, colors with hex codes, typography, layout rules, things to avoid]. Responsive, mobile-first. [Follow the attached DESIGN.md.]

Accessibility: WCAG 2.1 AA contrast, labels on all inputs, visible keyboard focus, respect prefers-reduced-motion. Must work at [375] px and [1440] px.

Exact values (use exactly these, do not invent others): [constants, formulas, fixed copy]

Initial task: [Scaffold: build the complete page with the sections above, in this order: ...]
              [Foundations: set up the project structure and navigation and implement only [main page] with [sections]. Do not implement other features yet.]

Follow the attached PRD. [Propose a plan first and wait for my approval.] Ask clarifying questions before coding if anything is unclear.

Check before you finish: [one concrete acceptance test from the PRD].
```

## Scaffold or Foundations

| | Scaffold | Foundations |
|---|---|---|
| Use for | Single page, up to about three features, no backend | Several pages, backend, accounts, or more than three features |
| Initial task | Whole page, sections listed in order | Structure, navigation, main page only |
| Risk | Hard to debug if it goes wrong | Slower start, far more stable |

## Worked example (Scaffold, self-contained)

From the course walkthrough, the THI GreenAI Portal. Note the exact constants, the explicit design tokens, and the numeric check at the end.

```
Build a single-page, responsive website called "THI GreenAI Portal" for students of Technische Hochschule Ingolstadt (THI).

Goal: show students the energy and CO2 footprint of their everyday AI use and give them tips to use AI more sustainably. Tone: curious and positive, never guilt-tripping.

Sections, in this order:
1. Sticky header with the wordmark "THI GreenAI" and anchor links: Calculator, Tips, Challenge.
2. Hero: headline "Use AI smart. Use AI green.", one sentence of sub-copy, and a primary button "Calculate my AI footprint" that scrolls to the calculator.
3. AI Footprint Calculator with live results (no submit button):
   - Inputs: text prompts per day (slider 0-200, default 20); model type (segmented control: small, large, reasoning; default large); images generated per week (slider 0-50, default 5).
   - Use exactly these constants, do not invent other numbers:
     WH_PER_TEXT_PROMPT = { small: 0.3, large: 1.0, reasoning: 5.0 }, WH_PER_IMAGE = 3.0, GRID_G_CO2_PER_KWH = 380, WH_PER_PHONE_CHARGE = 15, LED_BULB_WATTS = 10
   - weeklyWh = promptsPerDay * 7 * WH_PER_TEXT_PROMPT[model] + imagesPerWeek * WH_PER_IMAGE
   - Show four result cards (1 decimal): energy per week (Wh), CO2 per week (g), smartphone charges, hours of a 10 W LED bulb.
4. Green Prompting Tips: six cards (1 column on mobile, 3 on desktop), one sentence each.
5. Footer with a note that all values are illustrative.

Design: THI design language. Primary Navy #102A63, accent Green #009664, success Lime #96BE00, surfaces #E5E5E5, body text #333333 on white. Serif headings, sans-serif body. Rounded cards, generous whitespace, no purple or blue gradients.

Accessibility: WCAG 2.1 AA contrast, labels on all inputs, visible keyboard focus, results announced with aria-live="polite", respect prefers-reduced-motion. Must look good at 375 px and 1440 px.

Check before you finish: with 20 prompts/day, large model and 5 images/week the page must show 155.0 Wh and 58.9 g CO2.
```

---
## Reference: references/platforms.md

# Platform notes for kick-off prompts

These tools change quickly. Treat the notes as the state of the course material (winter semester 2026/27) and tell the student to check the tool's own documentation when something does not match what they see.

## Lovable

- Browser app builder, strongest for web front ends. Its default stack is React (Vite) + TypeScript, Tailwind CSS and shadcn/ui, with Supabase for database and authentication. Do not ask for a different front-end stack.
- Attach the PRD to the kick-off prompt.
- Prefer **Foundations** for anything beyond a small page: set up structure and the main page, "do not implement other features yet".
- Plan in Chat mode first ("Investigate but do not write code yet"), build in Builder mode, use the Visual Editor for small styling changes. Chat mode and visual edits save credits.
- Free plans have few prompts per day, so each prompt must count. Say this in "How to use it".

## Replit

- Full-stack: front end, back end and database, with an agent that plans, builds and tests.
- Add a stack line when the project needs a backend, for example: "Stack: React (Vite) + TypeScript + Tailwind for the frontend, Node.js + Express backend, Replit Postgres database."
- Always end with "Propose a plan first and wait for my approval."
- Ask the agent to explain how to test the result. Checkpoints allow rollback.

## DeepSite

- Generates a single web page and cannot read attached files. The prompt must be fully self-contained.
- Add: "Deliver everything as one single index.html file with inline CSS and vanilla JavaScript. No frameworks, no external libraries, no build step."
- Scaffold only.

## Cursor

- A code editor with an agent that works in a project folder. Put `PRD.md` (and `DESIGN.md`, `AGENTS.md` if they exist) in the folder and reference them with `@PRD.md`.
- Start in Plan mode: the agent proposes a plan and asks clarifying questions before writing code.
- The kick-off prompt can be shorter, because the files carry the context: point to the files, state the initial task, the limits and the check.
- Initialize git before the first build.

## Antigravity

- Agent-first editor. Ask for an implementation plan artifact first and wait for approval.
- Describe the app, the stack and the definition of done, PRD-style, or point to `PRD.md`.
- It can verify in a browser: ask it to open the page, walk through the main flow and provide screenshots as proof.

## Codex

- Works in a repository (desktop app, CLI, IDE extension or cloud). Run `/init` first so it creates `AGENTS.md` with the project conventions.
- Point to `PRD.md` and `DESIGN.md`, state the initial task and the check, and ask how you can verify the result yourself.
- Ask for no new dependencies unless needed.

## Claude Code

- Works in a repository. Start in plan mode and approve the plan before it edits.
- Point to `PRD.md` and `DESIGN.md`. Project conventions live in `CLAUDE.md`.
- Ask it to run the site and check the result against the PRD, then to add the prompts to `PROMPTS.md` and commit.

## Any other tool

Use the full self-contained template, ask for a plan first, and keep the first task small.
