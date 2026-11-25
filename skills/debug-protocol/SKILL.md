---
name: debug-protocol
description: Guides a non-programmer through debugging a vibe-coded app. Stop, describe expected versus actual behavior, collect the full error message and screenshots, have the AI explain the likely cause before changing anything, then write one targeted fix prompt, with a way out when fixes keep failing. Use when something is broken, an error message appears, the AI tool keeps failing to fix a bug, the app worked before and now does not, or someone is stuck in a fix loop.
---

# Debug protocol

A calm procedure for when things break. And they will break.

## Why this skill exists

The natural reaction to an error is to click "Fix it" or type "it's broken". The AI then guesses, changes more code and often breaks something else. A few rounds later the project is in a spiral of doom, and the credits are gone. Debugging with AI works when you slow down: understand first, then fix one thing with full context.

## Step 0: Stop

First reply, always: do not send another fix request yet. Ask two questions:

1. **Is there a last working version** (commit, checkpoint, version history)?
2. **How many fix attempts have been made already?**

If there were three or more failed attempts on the same problem, go to "When fixing keeps failing" below.

## Step 1: Describe the problem

Collect, in one short message:

- **Expected**: what should happen.
- **Actual**: what happens.
- **Steps to reproduce**: what the student clicked or entered.
- **Evidence**: the **full** error message copied as text (not retyped, not shortened), a screenshot, the browser console output if there is one.
- **What changed last**: the last prompt before it broke.

If the student does not know where to find the error text, explain it for their tool in two lines (for example: the red text in the preview, the Console tab in the browser developer tools, the terminal output).

## Step 2: Understand before fixing

Give the student this prompt for their tool, in its chat, ask or plan mode if it has one:

```
Something is wrong: [what I see] instead of [what I expected].
Steps: [how to reproduce]
Full error message / screenshot: [paste]
It started after: [last change]

First explain the likely cause in 2 to 3 sentences, in plain language.
Do not change any code until I confirm.
```

If the student pastes the error or code here, explain the likely cause yourself in plain language: what the message means, where the problem probably is, and how sure you are. If you cannot tell from the information given, say what else you need. Do not guess a fix.

## Step 3: Choose the smallest fix

- **Small visual issue** (spacing, color, text)? Fix it by hand in the tool's visual editor or in the file, if possible. No prompt needed.
- **One clear cause?** Write one targeted prompt:

```
Fix: [the specific problem], caused by [the cause we identified].
Change only [file or component]. Do not change anything else.
Afterwards tell me what you changed and how I can verify it.
```

- **Unclear cause?** Ask the tool to add logging or to list what it would check, still without changing behavior.

One fix per prompt. After it: reproduce the original steps, confirm the problem is gone, check that nothing nearby broke, save a checkpoint.

## When fixing keeps failing

After three failed attempts, stop patching. Options, in this order:

1. **Revert** to the last working version and redo the feature with a smaller, clearer prompt (`feature-prompt` skill). Redoing is usually cheaper than debugging.
2. **Start a fresh chat or session.** A long session full of failed attempts confuses the tool. Give the new one the PRD, the problem description and the error. Leave out the failed attempts.
3. **Ask for a different approach**: "The last three fixes did not work. Explain what assumption might be wrong and propose a different approach. Do not write code yet."
4. **Reduce**: remove the feature for now and continue with the rest.

## Things to say when relevant

- Error messages are information. They are not a judgment on the student.
- Never paste passwords, API keys or tokens into a prompt. If an error message contains one, remove it first.
- If the AI says "fixed", that is a claim. The check decides.

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Typical items:

- Did you see the fix work with your own eyes, following the original steps?
- Can you say in one sentence what the cause was? If not, ask the tool to explain it again.
- Save a checkpoint now, with a message that names the bug.
- If the same kind of bug keeps returning, add a rule to your AGENTS.md or PRD so the AI stops making it.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.
