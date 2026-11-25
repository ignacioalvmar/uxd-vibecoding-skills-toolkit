# UXD AI Skills Toolkit

Skills that help UX designers work with AI across the design process. Course companion for "Vibecoding for UX Designers" (UXD Master, Technische Hochschule Ingolstadt, Prof. Dr. Ignacio Alvarez).

**Status: v0.2, complete first set.** 23 skills. Structure checked; not yet tested with students.

Start with `ux-process-guide` if you do not know which skill you need.

| Phase            | Skill                      | What it does                                                                    |
| ---------------- | -------------------------- | ------------------------------------------------------------------------------- |
| Any              | `ux-process-guide`         | Finds where you are in the process and points to the next skill                 |
| Research         | `interview-guide`          | Drafts, bias-checks and pilots interview guides and survey questions            |
| Research         | `synthetic-user-rehearsal` | Plays a participant so you can rehearse, then gives feedback on your moderation |
| Research         | `interview-moderator`      | Readiness check, silent co-pilot during a session, structured notes afterwards  |
| Define           | `qual-analysis`            | Codes, themes and pain points from qualitative data, with verbatim evidence     |
| Define           | `quant-analysis`           | Descriptives, analysis plan, a check of your statistics, plain-language results |
| Define           | `persona-builder`          | Turns real research data into personas with a traceability table and bias audit |
| Ideate           | `divergent-ideation`       | Expands your own ideas in many directions, weird ones first                     |
| Ideate           | `idea-clustering`          | Groups ideas into themes and supports a shortlist                               |
| Ideate           | `idea-filter`              | Four product strategy questions: build, rework or drop                          |
| Ideate           | `concept-brief`            | Workshop summary, one-page product brief, pitch outline                         |
| Ideate           | `concept-visuals`          | Image prompts for problem scenes, storyboards and moodboards                    |
| Prototype        | `text-to-wireframe`        | From brief and flow to low-fidelity wireframes                                  |
| Prototype        | `wireframe-to-hifi`        | Design specification with tokens and a high-fidelity prompt                     |
| Prototype / Test | `prototype-review`         | Usability and accessibility review with a prioritized fix list                  |
| Build            | `prd-builder`              | Guided PRD from your brief, using the course template                           |
| Build            | `prd-critique`             | Checks whether a PRD is ready for an AI builder                                 |
| Build            | `project-context-files`    | Writes AGENTS.md and DESIGN.md for your project                                 |
| Build            | `kickoff-prompt`           | Writes the first prompt of a vibe coding project, for your platform             |
| Build            | `feature-prompt`           | One focused prompt for the next feature                                         |
| Build            | `checkpoint-coach`         | Git in plain language: save, branch, undo                                       |
| Build            | `debug-protocol`           | Stop, understand, then one targeted fix                                         |
| Test             | `acceptance-check`         | Checks the build against the PRD's acceptance criteria                          |

## What is a skill?

A folder with a `SKILL.md` file: instructions that an AI agent loads when your request matches the skill's description. Skills follow the open Agent Skills format, so the same folder works in several tools. Open any `SKILL.md` and read it. It is plain text, and reading it is part of the learning.

## Install

Copy the folders inside `skills/` to the place your tool looks for skills.

| Tool        | In one project                                             | For all your projects      |
| ----------- | ---------------------------------------------------------- | -------------------------- |
| Claude Code | `<project>/.claude/skills/`                                | `~/.claude/skills/`        |
| Cursor      | `<project>/.agents/skills/` or `<project>/.cursor/skills/` | `~/.cursor/skills/`        |
| Codex       | `<project>/.agents/skills/`                                | `~/.agents/skills/`        |
| Antigravity | `<project>/.agents/skills/`                                | `~/.gemini/config/skills/` |

Tip: `<project>/.agents/skills/` works for Cursor, Codex and Antigravity at once. Cursor also reads `.claude/skills/`.

Result, for example: `<project>/.agents/skills/interview-guide/SKILL.md`

Restart the tool or open a new chat after copying. These locations were checked against each tool's documentation in November 2026. The tools change often, so if a skill does not show up, check the tool's current skills documentation.

**Claude (desktop and web app):** this repository is also a plugin (see `.claude-plugin/plugin.json`). Alternatively add each skill folder as a skill in your Claude settings.

**Tools without skills (Lovable chat, Replit, ChatGPT, Gemini, any chat):** open the file in `paste-me/`, copy all of it into a new chat, and continue from there.

## Use

Just describe what you need; the agent picks the skill. Or name it.

```
I'm planning interviews with THI students about how they use AI tools.
Goal: find out what they know about the energy use of AI. 30-minute interviews.
Help me write the interview guide.
```

```
Use the persona-builder skill. Here are my anonymized notes from 6 interviews: [paste]
Product: THI GreenAI Portal. The personas are for our design team.
```

```
Write a kick-off prompt for Lovable from the attached PRD.md. Foundations first.
```

```
I have a product brief and rough sketches for a campus mobility app. Demo is in two weeks. What should I do next?
```

## What every skill does

- Asks for missing inputs. It will not invent users, quotes or requirements.
- Shows its checks (bias audit, traceability table).
- Ends with **Your judgment**: what you must verify or decide yourself.
- Logs prompts to `PROMPTS.md` in your project, as the course requires.

AI is a pattern-finder. You are the meaning-maker.

## Repository layout

```
skills/            one folder per skill (SKILL.md + references/)
paste-me/          single-file versions for chat-only tools (generated)
docs/conventions.md  rules for writing skills
scripts/           build script for paste-me files
```

## Navigator

`docs/navigator/index.html` is an interactive guide for students: pick your tools, find the skill for your phase, build the prompt, and follow the install steps for your tool. It is one self-contained file and can be opened locally or hosted anywhere. To change it, edit `scripts/navigator_data.py` (content) or `scripts/navigator_template.html` (layout), then run `python scripts/build_navigator.py`.

## User guide

`docs/guide/uxd-ai-toolkit-user-guide.pdf` is the printable guide: quick start, choosing tools, install steps per tool, every skill phase by phase with a prompt, and a reference table. It is generated from the same data as the navigator: `python scripts/build_guide.py <fontsource folder>` (needs playwright, pypdf and reportlab).

## Maintaining this repository

| You want to                                            | Edit                                                                     | Then run                                   |
| ------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------ |
| Change what a skill does                               | `skills/<name>/SKILL.md` or its `references/`                            | `python scripts/build_all.py`              |
| Add a skill                                            | New folder under `skills/`, plus an entry in `scripts/navigator_data.py` | `python scripts/build_all.py`              |
| Change prompts, phases or tool notes shown to students | `scripts/navigator_data.py`                                              | `python scripts/build_all.py`              |
| Change the look of the navigator                       | `scripts/navigator_template.html`                                        | `python scripts/build_navigator.py`        |
| Change the guide's chapters or layout                  | `scripts/build_guide.py`                                                 | `python scripts/build_guide.py <fonts>`    |
| Release a new version                                  | `version` in `.claude-plugin/plugin.json`, and `CHANGELOG.md`            | `python scripts/build_all.py`, commit, tag |

Rules for writing skills are in `docs/conventions.md`. The build stops with an error if `navigator_data.py` and the `skills/` folder list different skills. `paste-me/`, `docs/navigator/index.html` and the PDF guide are generated files: do not edit them by hand.

The guide build needs `playwright` (with Chromium), `pypdf` and `reportlab`, and the fonts from `npm install @fontsource/source-sans-3 @fontsource/barlow-semi-condensed @fontsource/source-code-pro` (pass `node_modules/@fontsource` as the font folder).
