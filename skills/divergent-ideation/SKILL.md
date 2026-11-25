---
name: divergent-ideation
description: Generates a wide and varied set of ideas for a UX design challenge during the divergent phase of brainstorming, building on the ideas a team already has (text, a list, or a photo of a sticky-note board). Use when someone is brainstorming, stuck or out of ideas, wants more or wilder concepts, wants to expand How Might We questions, or asks for ideas from different points of view.
---

# Divergent ideation

A brainstorming partner for the moment of creative exhaustion. It adds breadth to the team's own ideas. It does not judge them and it does not pick a winner.

## Why this skill exists

AI is strong at breadth and weak at originality: asked for ideas with no steering, a model returns the same safe, average concepts everyone else gets. Used after the humans have had their own ideas, and pushed toward unusual angles, it becomes useful. Use AI for divergence, not for evaluation.

## Human ideas first

Ask what the team has come up with so far. If the answer is "nothing yet", suggest ten minutes of individual ideation first (each person, five to seven sticky notes) and offer to wait. Starting from the AI's ideas anchors the whole team on the same average concepts. If the student insists, continue, and say that the ideas should be treated as provocations.

## Inputs (RISEN)

Collect what is missing in one short message. The course uses RISEN for ideation prompts:

- **Role**: the default is a mixed group of designers, engineers and entrepreneurs in a fast brainstorm.
- **Input**: the design challenge, target users, goal, and the existing ideas (pasted list, or a photo or screenshot of the board).
- **Steps**: which techniques to use (see below).
- **Expectation**: how many ideas and in what form.
- **Narrowing**: constraints to respect, constraints to ignore on purpose, example ideas that show the wanted style.

If the student shares a board photo, first list the ideas you can read and ask about any note you cannot read. Do not guess the text.

## Generate

Default: 20 to 30 ideas as sticky notes (a few words each), grouped into four to six loose themes.

Rules for this phase:

- **Quantity and variety over quality.** No feasibility filter.
- **Weird first.** At least a third of the ideas should be wild, futuristic or uncomfortable. Mark them with a ~ so the team can tell them apart.
- **Build on the team's ideas** by name ("extends 'pledge wall'") and do not repeat them.
- **No two ideas that are the same idea reworded.**
- Fast, playful, messy tone. No explanations per idea.

To get variety, use several lenses and say which you used:

- Other points of view: a first-year student, a skeptical professor, a facilities manager, a child, a person using a screen reader, someone who hates the product
- Inversion: how would we make this problem worse?
- Analogy: how would a game studio, a hospital, a street market or a public library solve this?
- Constraint removal: no budget limit, no screen, no login, ten times the users
- Extremes: the laziest user, the expert user, the first-time user
- SCAMPER on an existing idea: substitute, combine, adapt, modify, put to other use, eliminate, reverse

Offer one follow-up round: "Want another round from a lens we have not used, or ten variations on one idea?"

## What not to do

- Do not score, rank or recommend ideas. Clustering and scoring belong to convergence (`idea-clustering` skill).
- Do not write feature descriptions or a concept. That is the `concept-brief` skill.
- Do not claim an idea is new. You cannot know that.

## Your judgment (always end with this)

Close with a short block titled **Your judgment**. Typical items:

- Cross out everything that bores you. Keep what makes the team argue or laugh.
- Add your own ideas triggered by these. Those are usually the best ones.
- Check that the set still answers the design challenge and the users you defined.
- Put the survivors on the board next to your own notes before clustering.

## Prompt log

If you can write files in this environment, append an entry to `PROMPTS.md` in the project root (create it if missing): date, skill name, what was asked, what was produced, what the student changed. If you cannot write files, print the entry so the student can paste it.
