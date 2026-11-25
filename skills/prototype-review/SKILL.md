---
name: prototype-review
description: Reviews a wireframe, mock-up or working prototype for usability and accessibility problems against the intended user flow, using Nielsen's heuristics and WCAG checks, and returns a short prioritized fix list with ready-to-use fix prompts. Use when someone shares a screen, screenshot, prototype link or front-end code and asks for feedback, a UX review, a heuristic evaluation, an accessibility check, or what to improve next.
---

# Prototype review

A structured second pair of eyes on a prototype between iterations. It reports problems, ranks them and suggests fixes. It does not replace testing with users.

## Why this skill exists

When you prototype with AI you iterate quickly and stop seeing your own screen. A review against the flow and a fixed set of heuristics catches the obvious problems cheaply. It cannot tell you whether real users understand the product. Only testing can.

## Inputs

Ask for what is missing in one short message:

1. **The prototype**: screenshots, a description, a file, or code.
2. **The intended flow and user**: what should a user be able to do, and who are they? Without this you can only judge the surface.
3. **Stage**: wireframe, mock-up or working prototype. This sets the level of the review. Do not criticize missing colors in a wireframe.
4. **Focus**, if any: usability, accessibility, visual consistency, copy.

Say clearly what you can and cannot see. From a screenshot you cannot check keyboard behavior, focus order, screen reader output or responsiveness. List those as "not checked" and tell the student how to check them by hand.

## Review

Walk through the flow step by step as the user, then check against:

**Usability (Nielsen's 10 heuristics):** visibility of system status; match with the real world; user control and freedom; consistency and standards; error prevention; recognition over recall; flexibility and efficiency; aesthetic and minimalist design; help users recover from errors; help and documentation.

**Accessibility (WCAG 2.1 AA basics):** text contrast; color not the only signal; labels on inputs; visible focus; keyboard operability; logical heading and reading order; touch target size; alternative text; motion that can be reduced; error messages that say what to do.

**Flow:** can the task be completed, is the primary action obvious on each screen, are there dead ends, what happens on empty, loading and error states.

## Output

1. **What works** (two or three points, specific). The team should know what to keep.
2. **Findings**, most severe first:

| # | Where | Problem | Principle | Severity | Suggested fix |
|---|---|---|---|---|---|

Severity: **blocker** (user cannot finish the task), **major** (causes errors or serious confusion), **minor** (friction), **polish**.

3. **Fix these first**: three findings at most.
4. **Not checked**: what needs manual testing.
5. **Fix prompts** (on request): for each of the top findings, one small prompt for the student's tool that changes one thing and says what must stay untouched.

Rules:

- Tie every finding to a place on the screen and to a principle. No vague taste comments ("feels cluttered") without saying what causes it.
- Do not redesign. Do not propose new features.
- If you see no serious problems, say so. Do not pad the list.
- Offer an alternative view of a component only when a finding calls for it.

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Typical items:

- Decide which findings to act on. A heuristic violation is not always a real problem for your users.
- Do the manual checks: keyboard only, 200 percent zoom, a screen reader for the main flow, a real phone.
- Test with at least one real person. Five minutes of watching beats any review.
- Save a version before applying fixes, and apply them one at a time.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.
