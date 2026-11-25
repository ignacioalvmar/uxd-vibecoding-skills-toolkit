---
name: feature-prompt
description: Writes one focused prompt to add or change a single feature in an existing vibe coding project, with the relevant context, acceptance criteria, what may change and what must stay untouched, and a way to verify the result. Splits oversized requests into a sequence of small prompts. Use during a build when someone wants to add the next feature, change existing behavior or styling, or has a long wish list for their AI coding tool.
---

# Feature prompt

Writes the next build prompt: one feature, enough context, clear limits, a check at the end. This is the "attack one feature at a time" step of the vibe coding flow.

## Why this skill exists

Once the first version runs, it is tempting to ask for five things at once. The AI then changes many files, something breaks, and nobody knows which change caused it. Small prompts with explicit limits keep every step easy to verify and easy to undo. They also save credits.

## Inputs

Ask for what is missing in one short message:

1. **What to add or change**, in the student's words.
2. **The PRD**, or at least the feature's user story and acceptance criteria. If the feature is not in the PRD, suggest adding it there first. The PRD is the source of truth.
3. **Platform** and the current state: what already works, and any screenshot of the relevant part.
4. **Is the last working state saved?** If the student has not committed or made a checkpoint, say so before anything else. The `checkpoint-coach` skill helps.

## Step 1: Size the request

One prompt covers one feature: something the student can verify in a few minutes. If the request contains several features, or a feature with front end, data and logic all at once, split it and show the sequence:

```
1. [Smallest useful slice] -> check: ...
2. [Next slice] -> check: ...
```

Write only the first prompt in full. The next ones depend on what the first one produces.

## Step 2: Write the prompt

```
[Plan first, where the tool supports it: "Investigate and plan. Do not write code yet."]

Feature: [name], PRD section [x].
Goal: [what the user can do afterwards, one sentence]

Context: [only what is relevant: where it goes in the app, what it connects to,
which existing components or data it uses]

Requirements:
- [observable behavior]
- [observable behavior]
- [states: empty, loading, error]
- [accessibility: labels, keyboard, focus, announcements]

Exact values: [numbers, copy, tokens. Use the tokens from DESIGN.md. No new colors.]

Change only: [files, sections or components]
Do not change: [everything else: other sections, global styles, navigation, existing logic]

When done: tell me which files you changed and how I can test it.
Check: [one concrete test from the acceptance criteria]
```

Rules:

- Take requirements from the PRD. If the student's wish and the PRD disagree, ask which one is right.
- **"Do not change" is mandatory.** For changes to existing code, be very explicit about what to change and what to leave alone.
- Refer to project files by name (`PRD.md`, `DESIGN.md`) where the tool can read them, and do not paste their content.
- Name a framework or library only if the project already uses it or the student asks. Otherwise let the tool follow the existing code.
- Keep it short. Cut everything the AI does not need for this one feature.

Adapt to the platform: use the tool's planning or chat mode first where there is one (Lovable Chat mode, Plan mode in Cursor and Claude Code, an implementation plan in Antigravity, "propose a plan first" in Replit). Use visual editing for small style changes where the tool offers it. If you are unsure how a tool works today, say so.

## Step 3: After the build

Give a three-line routine: run the check, look at what changed (the file list or diff), save a checkpoint with a message that names the feature. If something broke, stop and use the `debug-protocol` skill. Do not send "fix it".

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Typical items:

- Is this the smallest step that gives you something to look at?
- Test it yourself with realistic data. Do not rely on the AI saying "done".
- Look at the list of changed files. Did it touch something you told it to leave alone?
- If the context is getting long and the tool starts forgetting things, start a fresh session and point it to the PRD.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.
