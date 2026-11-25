# Kick-off prompt template

Adapt the sections to the project. Remove lines that do not apply; do not leave placeholders in the final prompt.

```
Build a [type of application] called "[name]" for [target users].

Problem: [the user need, one or two sentences]
Solution: [how the app addresses it, one or two sentences]
Tone / vibe: [three or four words from the PRD]

Core features (build first):
1. [Feature] - [what it does, observable behavior]
2. [Feature] - [...]
3. [Feature] - [...]

Out of scope (do not build): [list]

Tech stack: [only if the platform lets you choose; see platforms.md]

Design: [design language, colors with hex codes, typography, layout rules, things to avoid]. Responsive, mobile-first. [Follow the attached DESIGN.md.]

Accessibility: WCAG 2.1 AA contrast, labels on all inputs, visible keyboard focus, respect prefers-reduced-motion. Must work at [375] px and [1440] px.

Exact values (use exactly these, do not invent others): [constants, formulas, fixed copy]

Initial task: [Scaffold: build the complete page with the sections above, in this order: ...]
              [Foundations: set up the project structure and navigation and implement only [main page] with [sections]. Do not implement other features yet.]

Follow the attached PRD. [Propose a plan first and wait for my approval.] Ask clarifying questions before coding if anything is unclear.

Check before you finish: [one concrete acceptance test from the PRD].
```

## Scaffold or Foundations

| | Scaffold | Foundations |
|---|---|---|
| Use for | Single page, up to about three features, no backend | Several pages, backend, accounts, or more than three features |
| Initial task | Whole page, sections listed in order | Structure, navigation, main page only |
| Risk | Hard to debug if it goes wrong | Slower start, far more stable |

## Worked example (Scaffold, self-contained)

From the course walkthrough, the THI GreenAI Portal. Note the exact constants, the explicit design tokens, and the numeric check at the end.

```
Build a single-page, responsive website called "THI GreenAI Portal" for students of Technische Hochschule Ingolstadt (THI).

Goal: show students the energy and CO2 footprint of their everyday AI use and give them tips to use AI more sustainably. Tone: curious and positive, never guilt-tripping.

Sections, in this order:
1. Sticky header with the wordmark "THI GreenAI" and anchor links: Calculator, Tips, Challenge.
2. Hero: headline "Use AI smart. Use AI green.", one sentence of sub-copy, and a primary button "Calculate my AI footprint" that scrolls to the calculator.
3. AI Footprint Calculator with live results (no submit button):
   - Inputs: text prompts per day (slider 0-200, default 20); model type (segmented control: small, large, reasoning; default large); images generated per week (slider 0-50, default 5).
   - Use exactly these constants, do not invent other numbers:
     WH_PER_TEXT_PROMPT = { small: 0.3, large: 1.0, reasoning: 5.0 }, WH_PER_IMAGE = 3.0, GRID_G_CO2_PER_KWH = 380, WH_PER_PHONE_CHARGE = 15, LED_BULB_WATTS = 10
   - weeklyWh = promptsPerDay * 7 * WH_PER_TEXT_PROMPT[model] + imagesPerWeek * WH_PER_IMAGE
   - Show four result cards (1 decimal): energy per week (Wh), CO2 per week (g), smartphone charges, hours of a 10 W LED bulb.
4. Green Prompting Tips: six cards (1 column on mobile, 3 on desktop), one sentence each.
5. Footer with a note that all values are illustrative.

Design: THI design language. Primary Navy #102A63, accent Green #009664, success Lime #96BE00, surfaces #E5E5E5, body text #333333 on white. Serif headings, sans-serif body. Rounded cards, generous whitespace, no purple or blue gradients.

Accessibility: WCAG 2.1 AA contrast, labels on all inputs, visible keyboard focus, results announced with aria-live="polite", respect prefers-reduced-motion. Must look good at 375 px and 1440 px.

Check before you finish: with 20 prompts/day, large model and 5 images/week the page must show 155.0 Wh and 58.9 g CO2.
```
