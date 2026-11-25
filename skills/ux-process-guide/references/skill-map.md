# Skill map

## By phase

| Phase | You want to | Skill | Needs | Gives you |
|---|---|---|---|---|
| Research | Write interview or survey questions | `interview-guide` | Research goal, participants | Bias-checked guide or survey |
| Research | Practice before fieldwork | `synthetic-user-rehearsal` | Guide, participant description | Rehearsal and feedback on your moderation |
| Research | Run and document interviews | `interview-moderator` | Guide; later transcript or notes | Live probes, structured notes with quotes |
| Define | Find themes in interviews and comments | `qual-analysis` | Anonymized qualitative data | Codes, themes, pain points with evidence |
| Define | Analyze survey or test numbers | `quant-analysis` | CSV or software output, research questions | Descriptives, analysis plan, checked stats |
| Define | Describe your users | `persona-builder` | Research findings | Personas with traceability table |
| Ideate | Get more and wilder ideas | `divergent-ideation` | Design challenge, your own ideas | Expanded idea set |
| Ideate | Group and shortlist ideas | `idea-clustering` | List or photo of ideas | Clusters, draft scores, shortlist |
| Ideate | Decide whether an idea is worth building | `idea-filter` | Idea, evidence so far | Build, rework or drop, with cheapest test |
| Ideate | Write up the concept | `concept-brief` | Workshop material, chosen direction | Summary, product brief, pitch outline |
| Ideate | Visualize problem or concept | `concept-visuals` | Concept or scenario | Image prompts |
| Prototype | Get first wireframes | `text-to-wireframe` | Brief, one user flow, sketch | Lo-fi wireframes or prompt |
| Prototype | Apply brand and polish | `wireframe-to-hifi` | Wireframe, brand identity | Design specification, hi-fi prompt |
| Prototype | Get feedback between iterations | `prototype-review` | Screens, intended flow | Prioritized fix list |
| Build | Plan the product for an AI builder | `prd-builder` | Brief, research, design | PRD.md |
| Build | Check the PRD | `prd-critique` | PRD | Findings and rewrites |
| Build | Give the agent standing context | `project-context-files` | PRD, design specification, repo | AGENTS.md, DESIGN.md |
| Build | Start the build | `kickoff-prompt` | PRD, platform | First prompt |
| Build | Add the next feature | `feature-prompt` | PRD feature, current state | One focused prompt |
| Build | Save, branch, undo | `checkpoint-coach` | Project folder or builder | Git steps in plain language |
| Build | Fix what broke | `debug-protocol` | Error, expected vs. actual | Diagnosis, targeted fix prompt |
| Test | Verify against requirements | `acceptance-check` | PRD criteria, the build | Pass, fail or not checked, per criterion |
| Test | Review usability and accessibility | `prototype-review` | Running prototype, flow | Prioritized fix list |

## Typical chains

**Research to concept**
`interview-guide` -> `synthetic-user-rehearsal` -> `interview-moderator` -> `qual-analysis` -> `persona-builder` -> `divergent-ideation` -> `idea-clustering` -> `idea-filter` -> `concept-brief`

**Concept to prototype**
`concept-brief` -> `text-to-wireframe` -> `prototype-review` -> `wireframe-to-hifi` -> `prototype-review`

**Concept to working product**
`concept-brief` -> `prd-builder` -> `prd-critique` -> `project-context-files` -> `kickoff-prompt` -> loop: `feature-prompt` -> `acceptance-check` -> `checkpoint-coach` (and `debug-protocol` when needed)

**Hackathon shortcut (one day)**
Own ideas -> `divergent-ideation` -> `idea-clustering` -> `concept-brief` -> short `prd-builder` (three features) -> `kickoff-prompt` -> `feature-prompt` loop with checkpoints -> `acceptance-check` before the demo

## Dependencies worth respecting

| Before you... | You should have... | Why |
|---|---|---|
| build personas | real research data | otherwise they are stereotypes |
| ask AI for ideas | your own ideas | otherwise everyone gets the same average concepts |
| generate wireframes | one defined user flow | flow matters more than visuals |
| style a screen | an approved wireframe | polish hides structural problems |
| write a kick-off prompt | a PRD | the AI will invent the product |
| send the next feature prompt | a saved checkpoint | things will break |
| call it done | an acceptance check | "Done!" from the AI is a claim |

## The five vibe coding skills and where the toolkit covers them

| Core skill | Toolkit skills |
|---|---|
| Thinking | `prd-builder`, `prd-critique`, `idea-filter` |
| Frameworks | `kickoff-prompt` (platform notes), `project-context-files` |
| Checkpoints | `checkpoint-coach`, `acceptance-check` |
| Debugging | `debug-protocol` |
| Context | `project-context-files`, `feature-prompt` |
