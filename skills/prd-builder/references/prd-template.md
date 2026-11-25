# Vibe-Coding PRD template (UXD Master)

Course template. Sections 1 to 5 are needed before the first build prompt. Sections 6 to 11 can stay short for course projects; fill them as the project grows.

```
# [Project Name]: Vibe-Coding PRD

Project vibe (1-sentence pitch):
Date:            Author(s):            Version: v0.1
Links: [Figma / Figma Make] [Repo] [Docs]
Companion files: DESIGN.md, AGENTS.md
Open questions (TBD):

## 1) Core context ("master prompt")
Problem (1-2 sentences):
Solution (1-2 sentences):
Target users:
Primary use cases:
North-star success metric:
Non-goals:

## 2) UX foundations (vibe, research, accessibility)
Personas: [with source: research / assumption]
Top insights / pain points:
Emotional and contextual "vibe" principles: [each with at least one concrete rule]
Accessibility and inclusion requirements:
High-level journey:

## 3) Scope and priorities
MVP (V1) goals:
Out of scope for V1:
Assumptions and risks:

## 4) Tech stack and architecture
| Layer | Choice | Why (one plain sentence) |
|---|---|---|
| Frontend | | |
| Backend | | |
| Database | | |
| Key APIs | | |
| Deployment | | |
| Security / privacy | | |

## 5) Feature modules (prompt by prompt)
### F1: [Feature name]
Priority: P0 / P1 / P2
User story: As a [user type], I want to [action], so that [benefit].
Acceptance criteria (to-prompt checklist):
- [ ] [observable behavior]
- [ ] [observable behavior]
- [ ] [accessibility behavior]
Exact values: [constants, formulas, copy]
Test vectors: [input -> expected output]

## 6) AI design and prompting strategy
System prompt (if the product itself uses AI):
Prompt bank (TACO examples):
Hallucination mitigation and safety:
Vibe-coding history: see PROMPTS.md

## 7) IA, flows and UI
Information architecture:
Key flows:
Design tokens and components: see DESIGN.md
Localization and tone guidelines:

## 8) Iteration plan and workflow
Build rhythm: one feature per prompt, checkpoint after each
Versioning and reviews: branches, pull requests, tags
Risk / spike tickets:

## 9) Quality: testing, accessibility, performance
Testing:
Accessibility: WCAG checklist
Performance budgets:

## 10) Metrics and analytics
Events:
KPIs:

## 11) Launch and ops
Environments:
Rollout plan:
Support and maintenance:
```

## Writing acceptance criteria

| Weak | Buildable |
|---|---|
| Login works | UI route `/login` exists. Primary button "Sign in" is visible and has an accessible label. On success the user is redirected to `/home`. On wrong password the message "Email or password is not correct" appears under the form. |
| The calculator is accurate | With 20 prompts/day, large model and 5 images/week the page shows 155.0 Wh and 58.9 g CO2. Results update live without a submit button. |
| Accessible | All inputs have labels. Focus is visible on every interactive element. Results are announced with `aria-live="polite"`. Layout works at 375 px and 1440 px. |

## Turning vibe into rules

| Principle | Rule the AI can follow |
|---|---|
| Curious, not guilty | Result texts never use blame words. Every number is paired with one everyday equivalent. |
| Transparent when uncertain | Any estimate shows its margin or the note "illustrative estimate" directly below it, in the muted text color. |
| Playful, but institutional | One celebration message at the top level, no confetti, motion respects `prefers-reduced-motion`. |
