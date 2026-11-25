# DESIGN.md template

Values come from the student's design. Mark anything proposed by the AI as "proposed".

````markdown
# DESIGN.md

## 1. Visual theme and atmosphere
Mood: [for example: calm and institutional, curious, positive]
Density: [sparse with generous whitespace / information-rich]
Philosophy: [one sentence]

## 2. Color palette and roles
| Token | Hex | Role |
|---|---|---|
| `--color-primary` | `#......` | Header, primary buttons |
| `--color-accent` | `#......` | Highlights, links |
| `--color-success` | `#......` | Success states |
| `--color-error` | `#......` | Errors, destructive actions |
| `--bg-canvas` | `#......` | Page background |
| `--bg-surface` | `#......` | Cards, panels |
| `--text-primary` | `#......` | Body copy, headings |
| `--text-muted` | `#......` | Captions, metadata |
| `--border-subtle` | `#......` | Dividers, card borders |

Checked contrast pairs: [text on background = ratio, pass or fail AA]

## 3. Typography rules
Font families: headings [..], body [..], fallbacks [..]
| Element | Size | Weight | Line height |
|---|---|---|---|
| H1 | | | |
| H2 | | | |
| H3 | | | |
| Body | | | |
| Caption | | | |

## 4. Component stylings
Buttons: primary, secondary. States: default, hover, focus, disabled.
Inputs: default, focus, error, with label and help text.
Cards: [radius, border, padding]
Navigation: [behavior, active state]

## 5. Layout principles
Spacing scale: [4, 8, 16, 24, 32, 48]
Grid and max content width: [..]
Whitespace: [..]

## 6. Depth and elevation
[Shadow system or "flat, borders only"]

## 7. Do's and don'ts
Do:
- Use tokens for every color, size and space.
- Keep focus visible on every interactive element.
- Keep touch targets at least 44 px.
Don't:
- No raw hex values in components.
- No new colors, fonts or shadows without asking.
- [Generic habits to avoid, for example: no purple or blue gradients]

## 8. Responsive behavior
Breakpoints: [375, 768, 1440]
Collapsing strategy: [how columns and navigation change]
Motion: respect `prefers-reduced-motion`.

## 9. Agent prompt guide
Quick reference: primary [hex], accent [hex], text [hex], background [hex]
Ready-to-use prompts:
- "Build [component] using only tokens from DESIGN.md."
- "Audit this page against DESIGN.md and list every deviation. Do not fix yet."
````

## Ways to get a first draft

- From a design specification (the `wireframe-to-hifi` skill produces one).
- From existing code: ask the agent to extract the tokens that are in use, then correct them.
- From a design tool that exports a DESIGN.md, or from a public example adapted to the brand. Always replace borrowed values with your own.
