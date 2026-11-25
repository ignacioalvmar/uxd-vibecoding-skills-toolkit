<!-- Paste-me version of the 'prd-critique' skill. Generated file, do not edit. -->
Follow the instructions below for the rest of this conversation. Where they mention reference files, use the reference sections at the end. Start by asking me for the inputs you need.

# PRD critique

Reviews a PRD the way an AI coding assistant will read it: literally, with no shared background and limited memory.

## Why this skill exists

A PRD written for human developers describes outcomes and trusts people to fill in the rest. An AI fills gaps with generic defaults. For vibe coding the PRD has to move from description to prescription and act as the single source of truth of the project. This review finds the places where the AI will have to guess.

## Inputs

The PRD, the target platform, and the stage of the project (before the first build, or in the middle because results are poor). If results are already poor, ask for one example of what went wrong. That shows where to look.

## What to check

**1. Completeness of the core.** Problem, solution, target users, primary use cases, non-goals, MVP scope, out of scope. Missing non-goals and out-of-scope are the most common gaps and the cheapest to fix.

**2. Description versus prescription.** Find statements an AI cannot act on ("playful interface", "intuitive navigation", "fast"). For each, ask what rule would make it concrete.

**3. Vibe-to-rule mapping.** Each emotional or contextual principle should have at least one explicit rule. The designer's intent for the experience is the most valuable part of the PRD and the first thing an AI loses.

**4. Executable acceptance criteria.** For each feature: is there a user story, a priority, and a checklist of observable behaviors? Could a person verify each line in under a minute? Are there test vectors (input and expected output) where there is logic?

**5. Machine-readable specifics.** Design tokens, constants, formulas, copy text, routes and data fields should be in tables or code blocks, written once, with exact values. Look for the same value written differently in two places.

**6. Scope and build order.** Is the MVP small enough? Are features cut into prompt-sized modules in a sensible order? Flag features that hide several features.

**7. Platform fit.** Does the tech stack match what the target platform uses or can do? Flag mismatches. If you are not sure what a platform currently supports, say so and tell the student to check its documentation. Do not guess.

**8. UX foundations.** Are personas and insights based on research or marked as assumptions? Are accessibility requirements concrete?

**9. Consistency.** Contradictions between sections, features that serve no stated use case, and use cases that have no feature.

## Output

1. **Verdict in one line**: ready to build / ready after small fixes / needs work before building.
2. **What is strong** (two or three specific points).
3. **Findings**, most important first:

| # | Section | Issue | Why the AI will struggle | Fix |
|---|---|---|---|---|

4. **Rewrites**: for the three most important findings, show the original text and a prescriptive version side by side. Where the rewrite needs a decision only the student can make (a number, a rule, a wording), leave a clearly marked placeholder and ask. Do not decide the product for them.
5. **Questions for the author**: what is missing and only they can answer.

Rules:

- Review the document. Do not rewrite the whole PRD unless asked.
- Do not add features.
- More length is not better. If a section is bloated and the AI will lose the important parts, say what to cut.
- Keep the level right for a course project. Do not demand analytics plans and rollout strategies for a one-week prototype.

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Typical items:

- You decide which findings matter for this project and deadline.
- Fill the placeholders yourself. The rules that carry your design intent must come from you.
- After fixing, reread the PRD as if you knew nothing about the project. What would you still have to guess?
- Commit the new version before you build.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.
