<!-- Paste-me version of the 'wireframe-to-hifi' skill. Generated file, do not edit. -->
Follow the instructions below for the rest of this conversation. Where they mention reference files, use the reference sections at the end. Start by asking me for the inputs you need.

# Wireframe to high fidelity

Takes an approved wireframe and adds visual design: color, type, spacing, components, states. The layout and flow stay as they are.

## Why this skill exists

Left alone, an AI tool styles everything in the same generic look: a blue or purple gradient, rounded cards, the default font. It also likes to "improve" the layout while styling. This skill gives the tool an explicit design direction in the form of tokens and locks the structure. Brand alignment and accessibility are decided here and not left to the tool's defaults.

## Inputs

Ask for what is missing in one short message:

1. **The wireframe**: file, screenshot, or the screen descriptions. If there is none, start with the `text-to-wireframe` skill. Styling without an agreed structure wastes time.
2. **Brand identity**: colors with hex codes, fonts, logo, an existing design system or DESIGN.md. If the student has nothing, ask for three adjectives and one or two reference products, then propose a small token set for approval.
3. **Target tool and platform.**
4. **Accessibility target.** The default is WCAG 2.1 AA.

## Step 1: Design specification

Write the specification before any prompt. Keep it short and precise:

```
# Design specification: [product]

## Color tokens
| Token | Hex | Role |
(primary, on-primary, accent, surface, background, text, text-muted, border, error, success)

## Typography
| Element | Font | Size | Weight | Line height |

## Spacing and layout
Spacing scale, grid, corner radius, max content width, breakpoints

## Components
Button (primary, secondary, disabled, focus), input (default, focus, error),
card, navigation: one line each with tokens used and states

## Screens
Per screen: what changes from the wireframe (nothing structural)

## Accessibility notes
```

Rules:

- **Tokens, not raw values.** Name every color and reuse the name. This is the language designers and developers share, and it is what an AI coding tool follows most reliably later.
- **Check contrast.** For each text and background pair, state the contrast ratio and whether it passes AA (4.5:1 for body text, 3:1 for large text and interface components). If you can run code, compute it. If you cannot, say it is an estimate and tell the student to verify with a contrast checker. If a brand color fails, say so and propose the nearest passing use (for example, use it for large headings only).
- **States are part of the design**: hover, focus, disabled, error, empty, loading.
- Focus must be visible. Color is never the only signal. Touch targets are at least 44 px.
- Say what to avoid. This steers the tool away from its default look ("no gradients, no drop shadows on cards").

## Step 2: Prompt for the tool

```
Task: Transform this low-fidelity wireframe into a high-fidelity [mock-up /
interactive prototype]. Keep the existing layout and navigation flow exactly.
Apply the visual design below. Do not add, remove or move components.
Actor: You are an expert UX/UI designer.
Context: [one paragraph on the product and its users; list of screens in the wireframe]
Design: [tokens from the specification: colors with hex and role, typography, spacing, radius]
Avoid: [list]
Accessibility: WCAG 2.1 AA contrast, visible keyboard focus, labels on all inputs,
states for hover, focus, disabled and error.
Output: [what the tool should return]
```

If the project has a DESIGN.md, reference it and do not repeat the tokens. The `project-context-files` skill creates one from this specification.

## Step 3: Refine one thing at a time

After the first result, iterate with small, targeted prompts. One change each, naming what must stay untouched: swap the logo, replace the placeholder avatar, fix one component's states, add one missing screen. Save a version before each prompt.

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Typical items:

- Compare the result with the wireframe. Did the tool change the structure?
- Check contrast with a real checker and try the screen with the keyboard only.
- Does it look like your brand, or like every other AI-generated interface?
- Fit and finish is your job: alignment, spacing rhythm, the small details that make it feel cared for.
- Save a version before every iteration.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.
