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
