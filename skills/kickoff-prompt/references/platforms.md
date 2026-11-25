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
