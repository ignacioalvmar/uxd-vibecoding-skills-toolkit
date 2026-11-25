# Conventions for skill authors

Rules every skill in this toolkit follows. Students do not need this file; it is for whoever writes or edits skills.

## Format

- One folder per skill under `skills/`, named like the skill (lowercase, hyphens).
- `SKILL.md` with YAML frontmatter containing only `name` and `description`. No platform-specific frontmatter fields.
- The description says what the skill does and when to use it, with the words a student would actually type.
- Longer material (templates, examples, platform notes) goes in `references/` and is linked from SKILL.md.
- Each skill is self-contained. Skills get copied individually, so nothing may depend on a file outside its own folder.
- SKILL.md stays under about 150 lines.

## Portability

- No instructions that assume one vendor's tools, connectors, artifacts or slash commands. Platform specifics live in a reference file.
- Outputs are markdown or plain text.
- Other skills may be mentioned by name ("the `interview-guide` skill does this"), always with a fallback for when they are not installed.
- Anything that writes files needs a fallback for chat-only tools ("if you cannot write files, print it").

## Content rules (from the course)

1. **Ask before inventing.** Missing inputs are requested in one short message. Skills never make up users, quotes, numbers or requirements.
2. **Show the checking.** Bias audits, traceability tables and critique tables are visible outputs.
3. **Explain why.** Each skill has a short "Why this skill exists" section, and instructions give reasons so that students can learn from reading the file.
4. **Your judgment.** Every skill ends its output with a block titled "Your judgment" listing what the human must verify or decide.
5. **Prompt log.** Skills append to `PROMPTS.md` in the project root where possible.
6. **Ethics.** Consent, anonymization and the limits of synthetic data are stated where they apply.
7. **Course vocabulary.** TACO / RISEN for prompt structure; Thinking, Frameworks, Checkpoints, Debugging, Context for vibe coding.

## Style

- Plain English, CEFR B2 or simpler. Students are designers, many are non-native speakers.
- No em dashes.
- Examples come from course cases (THI GreenAI Portal, CampusGO, SproutingBean) where possible.

## Paste-me versions

`paste-me/<skill>.md` is generated from the skill folder by `scripts/build_paste_me.py`. Do not edit those files by hand.
