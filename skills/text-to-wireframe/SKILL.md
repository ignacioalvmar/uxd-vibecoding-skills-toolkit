---
name: text-to-wireframe
description: Turns a product brief, user flow, hand sketch or screenshot into low-fidelity wireframes, either as a wireframe prompt for a design tool (Figma Make, Stitch, Miro and similar) or as a simple grayscale HTML wireframe. Covers structure, navigation, content hierarchy and labeled components, with no visual styling. Use when someone wants wireframes, a first layout, a screen flow, a lo-fi prototype, or wants to go from a blank canvas or a sketch to a first draft.
---

# Text to wireframe

Gets a team from a concept to low-fidelity wireframes: structure, navigation and content hierarchy. No colors, no brand, no polish.

## Why this skill exists

AI can produce a screen in seconds, and that makes it tempting to jump straight to pretty visuals. A polished screen with the wrong flow is a waste, and people critique colors when they should be looking at structure. Flow matters more than visuals, so this skill settles the flow first and keeps the output gray on purpose.

## Inputs

Ask for what is missing in one short message:

1. **The concept**: product brief or a short description (what it is, for whom, the main use case).
2. **The main user flow to prototype.** One flow. If the student lists everything the product could do, ask which task matters most.
3. **Platform**: mobile-first or web-first, and the tool the wireframe is for.
4. **Any existing sketch or screenshot.** Encourage the student to sketch by hand first, even roughly, and share a photo. Their sketch then drives the layout and the AI's default does not.

If there is no brief yet, the `concept-brief` skill creates one. Without a defined flow, do not generate screens.

## Step 1: Agree on the flow

Write the flow as numbered steps from the user's point of view, then the list of screens it needs:

```
Flow: [user goal]
1. User lands on ... and sees ...
2. User does ... -> goes to ...
Screens: 1. [Name] - [one-line purpose]   2. ...
```

Three to five screens are enough for a first round. Confirm with the student before going on.

## Step 2: Describe each screen

For each screen, top to bottom:

- purpose of the screen in one line
- regions in order (header, main content, navigation)
- components with labels and real example content (no lorem ipsum, because real content shows whether the layout works)
- the primary action, and where each action leads
- states that matter: empty, loading, error

## Step 3: Produce the wireframe

Choose with the student:

**A. Prompt for a design tool.** Use this structure (course template):

```
Actor: You are an expert UX designer.
Task: Create a low-fidelity wireframe that visualizes the [name] [app/webpage]
structure and navigation flow between the following [n] core screens:
1. [Screen] - [content in one line]
2. ...
Highlight usability, clarity and accessibility. [Use the attached sketch as guidance.]
Context: [one paragraph: what the product is, for whom, main use case]
Output format: [mobile-first/web-first]. Low fidelity: grayscale, boxes and labels,
no brand colors, no images, system font. Label every component. Show how screens connect.
```

**B. HTML wireframe**, if you can create files or the student wants code: one self-contained HTML file, grayscale only, system font, boxes with visible labels, working links between screens, semantic HTML elements. Nothing decorative.

**C. Text wireframe** (ASCII boxes) for a quick discussion in chat.

## Step 4: Review before styling

Check the wireframe against the flow and report briefly: can the user finish the task, is the primary action obvious on each screen, is the navigation consistent, does the reading order make sense for a screen reader, are touch targets large enough on mobile, what happens on error. Suggest at most three changes. Offer one alternative layout for the most important screen, so the student compares options before settling on the first draft.

## What not to do

- No color, brand, icons or imagery. That is the next step (`wireframe-to-hifi` skill).
- Do not invent features that are not in the brief. Ask.
- Do not cover every screen of the product. One flow, done well.

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Typical items:

- Walk through the flow as your persona. Where would they hesitate?
- Compare with your hand sketch. Did the AI change your structure, and is that better or just different?
- Show it to one person outside the team and ask them to complete the task.
- Save this version (commit or duplicate the file) before you iterate.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.
