"""Build docs/guide/uxd-ai-toolkit-user-guide.pdf from navigator_data.py.

Usage (from the repository root):
    python scripts/build_guide.py [FONT_DIR]

FONT_DIR is a folder that contains the @fontsource packages source-sans-3,
barlow-semi-condensed and source-code-pro (for example node_modules/@fontsource).
Without it the guide falls back to system fonts.
Needs: playwright (chromium), pypdf, reportlab.
"""
import base64, html, io, json, re, sys
from pathlib import Path

here = Path(__file__).resolve().parent
root = here.parent
sys.path.insert(0, str(here))
import navigator_data as nd

VERSION = json.loads((root / ".claude-plugin" / "plugin.json").read_text())["version"]
DATE = "November 2026"
AUTHOR = "Prof. Dr. Ignacio Alvarez"
S = {s["id"]: s for s in nd.SKILLS}
N = len(nd.SKILLS)
e = html.escape


def font_css(font_dir):
    if not font_dir:
        return ""
    fd = Path(font_dir)
    faces = [("Source Sans 3", "source-sans-3", 400, "normal"), ("Source Sans 3", "source-sans-3", 400, "italic"),
             ("Source Sans 3", "source-sans-3", 600, "normal"), ("Source Sans 3", "source-sans-3", 700, "normal"),
             ("Barlow Semi Condensed", "barlow-semi-condensed", 600, "normal"), ("Barlow Semi Condensed", "barlow-semi-condensed", 700, "normal"),
             ("Source Code Pro", "source-code-pro", 400, "normal"), ("Source Code Pro", "source-code-pro", 600, "normal")]
    out = []
    for fam, pkg, w, st in faces:
        f = fd / pkg / "files" / f"{pkg}-latin-{w}-{st}.woff2"
        if f.is_file():
            b = base64.b64encode(f.read_bytes()).decode()
            out.append(f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};src:url(data:font/woff2;base64,{b}) format('woff2')}}")
    return "\n".join(out)


CSS = """
:root{--ink:#1d2430;--muted:#555f6d;--line:#cfd4da;--paper:#f0f1f3;--navy:#102a63;--navy-soft:#e3e9f6;
  --go:#00765a;--go-soft:#dcf2ea;--you:#566f00;--you-soft:#eef4d4;--lime:#96be00;--chip:#e9ebee;
  --display:'Barlow Semi Condensed','Arial Narrow',Arial,sans-serif;
  --body:'Source Sans 3','Segoe UI',Helvetica,Arial,sans-serif;
  --mono:'Source Code Pro',Consolas,'DejaVu Sans Mono',monospace}
*{box-sizing:border-box}
html{font:10.4pt/1.45 var(--body);color:var(--ink)}
body{margin:0}
p{margin:0 0 6pt}
h1{font:700 23pt/1.08 var(--display);color:var(--navy);margin:0 0 4pt;padding-bottom:6pt;border-bottom:3pt solid var(--lime);break-before:page;break-after:avoid}
h1 .n{color:var(--go);margin-right:8pt}
h2{font:700 15pt/1.15 var(--display);color:var(--navy);margin:16pt 0 5pt;break-after:avoid}
h3{font:700 10.6pt/1.3 var(--body);margin:10pt 0 3pt;break-after:avoid}
.lead{font-size:11.4pt;color:var(--muted);margin:8pt 0 10pt}
code,.mono{font-family:var(--mono);font-size:8.8pt}
code{background:var(--chip);padding:.5pt 3pt;border-radius:1.5pt}
ul,ol{margin:0 0 6pt;padding-left:15pt}
li{margin-bottom:2.5pt}
table{border-collapse:collapse;width:100%;font-size:9.4pt;margin:6pt 0 8pt}
th,td{text-align:left;vertical-align:top;padding:4.5pt 6pt;border-bottom:.6pt solid var(--line)}
th{font-weight:700;color:var(--muted);border-bottom:1.2pt solid var(--navy)}
td:first-child{font-weight:600}
tr{break-inside:avoid}
table{break-inside:avoid}
p{orphans:3;widows:3}
.keep{break-inside:avoid}
.steps{list-style:none;padding:0;counter-reset:s;margin:6pt 0}
.steps li{counter-increment:s;display:grid;grid-template-columns:17pt 1fr;gap:7pt;margin-bottom:6pt;break-inside:avoid}
.steps li::before{content:counter(s);width:15pt;height:15pt;background:var(--navy);color:#fff;font:700 9.5pt/15pt var(--display);text-align:center;border-radius:1.5pt}
.prompt{background:var(--paper);border-left:3pt solid var(--go);padding:6pt 9pt;margin:5pt 0 6pt;font-size:9.6pt;white-space:pre-wrap;break-inside:avoid}
.prompt .lbl{display:block;font:700 8pt/1.2 var(--body);color:var(--go);margin-bottom:2pt}
.you{background:var(--you-soft);border-left:3pt solid var(--you);padding:6pt 9pt;margin:6pt 0;break-inside:avoid}
.you b{display:block;font-size:8.6pt;color:var(--you)}
.note{background:var(--go-soft);border-left:3pt solid var(--go);padding:6pt 9pt;margin:6pt 0;break-inside:avoid}
.skill{border:.6pt solid var(--line);border-top:2pt solid var(--navy);padding:8pt 10pt 6pt;margin:9pt 0;break-inside:avoid}
.skill .name{font:700 13.5pt/1.1 var(--display);color:var(--navy)}
.skill .tag{float:right;font:600 8pt var(--body);background:var(--go-soft);color:var(--go);padding:1pt 5pt;border-radius:1.5pt}
.skill .sum{margin:3pt 0 5pt}
.io{display:grid;grid-template-columns:1fr 1fr;gap:3pt 12pt;font-size:9.4pt;margin-bottom:2pt}
.io b{display:block;font-size:8.2pt;color:var(--muted)}
.then{font-size:9pt;color:var(--muted);margin:2pt 0 0}
.tree{font:8.6pt/1.5 var(--mono);background:var(--paper);border:.6pt solid var(--line);padding:6pt 9pt;margin:5pt 0 8pt;white-space:pre;break-inside:avoid}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14pt}
.rail{display:grid;grid-template-columns:repeat(6,1fr);margin:12pt 0 6pt}
.rail div{font:700 11pt/1.15 var(--display)}
.rail .num{display:inline-block;width:19pt;height:19pt;background:var(--navy);color:#fff;text-align:center;font:700 11pt/19pt var(--display);border-radius:1.5pt;margin-bottom:4pt}
.rail .bar{display:flex;align-items:center}
.rail .bar::after{content:"";flex:1;height:1.2pt;background:var(--line);margin:0 4pt 4pt}
.rail div:last-child .bar::after{visibility:hidden}
.rail small{display:block;font:400 8.2pt/1.25 var(--body);color:var(--muted);padding-right:6pt;margin-top:1pt}
.path{margin:5pt 0 9pt;break-inside:avoid}
.path b{display:block;margin-bottom:2pt}
.path span{font:8.8pt var(--mono);background:var(--chip);padding:1pt 4pt;border-radius:1.5pt;display:inline-block;margin:1.5pt 0}
.path i{font-style:normal;color:var(--muted);margin:0 2pt}
/* contents */
.toc{break-before:page}
.toc h1{break-before:auto}
.toc .row{display:flex;align-items:baseline;gap:6pt;margin:3pt 0}
.toc .row.l1{font-weight:700;margin-top:9pt}
.toc .row.l2{padding-left:16pt;color:var(--muted)}
.toc .dots{flex:1;border-bottom:.8pt dotted var(--line);transform:translateY(-2.5pt)}
/* cover */
.cover{height:297mm;display:flex;flex-direction:column}
.cover .band{background:var(--navy);color:#fff;padding:34mm 22mm 16mm;border-bottom:5pt solid var(--lime)}
.cover .kick{font:600 12pt var(--body);color:#cdd6ec}
.cover .title{font:700 50pt/1 var(--display);margin:8pt 0 6pt}
.cover .sub{font:600 19pt/1.2 var(--display);color:#cdd6ec}
.cover .meta{font:600 10pt var(--body);color:#cdd6ec;margin-top:16pt}
.cover .body{padding:14mm 22mm 0;flex:1}
.cover .body p{font-size:12pt;max-width:150mm;margin-bottom:8pt}
.cover .foot{padding:0 22mm 16mm;font-size:9.6pt;color:var(--muted)}
.cover .foot b{color:var(--ink);font-size:11pt}
"""


def prompt_text(s, runner_kind="agent"):
    t = (s["prompt"].replace("{product}", "<your project>").replace("{users}", "<your users>")
         .replace("{usersp}", "").replace("{builder}", "<your build tool>"))
    return t if runner_kind == "paste" else f"Use the {s['id']} skill.\n\n{t}"


def prompt_box(s, label="Prompt"):
    return f'<div class="prompt"><span class="lbl">{label}</span>{e(prompt_text(s))}</div>'


def skill_block(s):
    tag = '<span class="tag">needs your project</span>' if s["where"] == "project" else ""
    then = ""
    if s["next"]:
        then = '<p class="then">Then: ' + ", ".join(f"<code>{n}</code>" for n in s["next"]) + "</p>"
    return f"""<div class="skill">{tag}<div class="name">{s['id']}</div>
<p class="sum">{e(s['sum'])}</p>
<div class="io"><div><b>You bring</b>{e(s['needs'])}</div><div><b>You get</b>{e(s['gives'])}</div></div>
{prompt_box(s)}{then}</div>"""


def rail():
    cells = "".join(f'<div><span class="bar"><span class="num">{p["n"]}</span></span>{e(p["name"])}<small>{e(p["when"])}</small></div>' for p in nd.PHASES)
    return f'<div class="rail">{cells}</div>'


SECTIONS = []  # (number, title, [subtitles])


def h1(n, title):
    SECTIONS.append([n, title, []])
    return f'<h1><span class="n">{n}</span>{e(title)}</h1>'


def h2(title, toc=True):
    if toc:
        SECTIONS[-1][2].append(title)
    return f"<h2>{e(title)}</h2>"


def body_html():
    SECTIONS.clear()
    o = []
    agents = [r for r in nd.RUNNERS if r["kind"] == "agent"]

    # 1 Quick start
    o.append(h1(1, "Quick start"))
    o.append(f"""<p class="lead">The toolkit is a set of {N} skills. Each skill does one job in the UX process, for example writing an interview guide, building a persona from your data, or writing the first prompt for your AI builder. You talk to your AI tool in plain language. The skill makes sure the work follows the method from the course.</p>""")
    o.append(h2("Six steps to your first result"))
    o.append("""<ol class="steps">
<li><div><b>Pick your tools.</b> Decide where you talk to AI (a coding agent such as Cursor, or a chat tool) and what you build with (for example Lovable). Chapter 2 explains the difference.</div></li>
<li><div><b>Install the skills.</b> Copy the skill folders into your tool's skills folder. It takes about two minutes. Chapter 3 has the steps for each tool. In chat tools there is nothing to install.</div></li>
<li><div><b>Say where you are.</b> Find your phase in chapter 5 and copy the prompt of the skill you need. If you are unsure, ask <code>ux-process-guide</code>.</div></li>
<li><div><b>Answer the skill's questions.</b> A skill asks for what it needs. It will not invent users, quotes or requirements, so have your material ready.</div></li>
<li><div><b>Do your part.</b> Every skill ends its answer with a block called Your judgment. Those checks are the design work.</div></li>
<li><div><b>Save as you go.</b> Keep outputs as files in your project, log your prompts in <code>PROMPTS.md</code> and commit after each working step.</div></li>
</ol>""")
    o.append(prompt_box(S["ux-process-guide"], "First prompt if you are unsure"))
    o.append('<div class="two"><div>')
    o.append(h2("What ends up in your project"))
    o.append("""<div class="tree">your-project/
  .agents/skills/     the toolkit skills
  PRD.md              what you are building
  DESIGN.md           how it looks and feels
  AGENTS.md           how the agent should work
  PROMPTS.md          your prompt log
  research/           notes, themes, personas</div>
<p>A skill is a folder with a file called <code>SKILL.md</code>: plain-text instructions that an AI agent loads when your request matches. Open one and read it. You can change it or write your own.</p>""")
    o.append("</div><div>")
    o.append(h2("Ground rules"))
    o.append("""<ul>
<li>AI is the pattern-finder. You are the meaning-maker.</li>
<li>Skills never invent users, quotes, data or requirements. They ask, or they mark an assumption.</li>
<li>Your own ideas and sketches come first. AI adds breadth and speed afterwards.</li>
<li>Anonymize research data before you paste it. Get consent before you record or use AI in a session.</li>
<li>Synthetic users are for rehearsal. They are never evidence.</li>
<li>One step at a time, with a saved checkpoint after each. "Done!" from an AI is a claim.</li>
</ul>""")
    o.append("</div></div>")

    # 2 Choose your tools
    o.append(h1(2, "Choose your tools"))
    o.append("""<p class="lead">Two questions decide how you use the toolkit. The interactive Navigator asks them once and adapts every prompt. In this guide you look up your combination in the tables.</p>""")
    o.append(h2("Where do you talk to AI?"))
    o.append("<p>This is the tool that runs the skills.</p>")
    rows = "".join(f"<tr><td>{e(r['name'])}</td><td>{'Coding agent. Loads skill folders and works in your project folder.' if r['kind']=='agent' else 'Chat app. Loads the toolkit as a plugin.' if r['kind']=='app' else 'Chat only. No skill folders. You paste a skill into the chat when you need it.'}</td><td>{e(r['invoke'])}</td></tr>" for r in nd.RUNNERS)
    o.append(f"<table><tr><th>Tool</th><th>What it is</th><th>How you call a skill</th></tr>{rows}</table>")
    o.append(h2("What do you build with?"))
    o.append("<p>This is the tool that writes the code. It only matters in the Build and Test phases.</p>")
    rows = "".join(f"<tr><td>{e(b['name'])}</td><td>{'Yes' if b['skills'] else 'No'}</td><td>{e(b['hint'])}</td></tr>" for b in nd.BUILDERS)
    o.append(f"<table><tr><th>Builder</th><th>Loads skills</th><th>How to give it a prompt</th></tr>{rows}</table>")
    o.append(h2("When the two tools are different"))
    o.append("""<p>Lovable, Replit and DeepSite build apps but do not load skills. The pattern is always the same:</p>
<ol class="steps">
<li><div>Run the skill where skills work: in a coding agent, in the Claude app, or in a chat tool with the paste-me file.</div></li>
<li><div>The skill writes a prompt for your builder, for example a kick-off prompt or a fix prompt.</div></li>
<li><div>Copy that prompt into your builder and follow the builder's own way of working from the table above.</div></li>
</ol>
<div class="note">Example: you plan in Cursor and build in Lovable. Run <code>kickoff-prompt</code> in Cursor, copy the result into Lovable, plan in Chat mode first, then switch to Builder mode.</div>
<p>Some skills are marked <b>needs your project</b>. They work best where the AI can read your files: <code>project-context-files</code>, <code>feature-prompt</code>, <code>checkpoint-coach</code>, <code>debug-protocol</code> and <code>acceptance-check</code>. In a chat tool, paste the relevant files, the full error text or screenshots.</p>""")

    # 3 Install
    o.append(h1(3, "Install the skills"))
    o.append("""<p class="lead">Download <code>uxd-ai-toolkit.zip</code> from the course page on Moodle and unzip it. The steps below assume it is in your Downloads folder.</p>""")
    o.append(h2("Coding agents: Claude Code, Cursor, Codex, Antigravity"))
    rows = "".join(f"<tr><td>{e(r['name'])}</td><td><code>{r['project']}</code></td><td><code>{r['home']}</code></td></tr>" for r in agents)
    o.append(f"""<p>Copy every folder inside <code>uxd-ai-toolkit/skills/</code> into the skills folder of your tool. Create the folder if it is not there.</p>
<table><tr><th>Tool</th><th>This project only (inside your project folder)</th><th>All your projects (inside your home folder)</th></tr>{rows}</table>
<p><code>.agents/skills/</code> in a project works for Cursor, Codex and Antigravity at once. Cursor also reads <code>.cursor/skills/</code> and <code>.claude/skills/</code>.</p>
<h3>Three ways to copy</h3>
<p><b>A. Ask the agent.</b> Open your project in the tool and send this. Replace the folder with the one from the table.</p>
<div class="prompt">Copy every folder from ~/Downloads/uxd-ai-toolkit/skills/ into .agents/skills/ in this project. Create the folder if it does not exist. Do not change the files. Then list the skills you can see.</div>
<p><b>B. In the terminal,</b> from inside your project folder.</p>
<div class="tree">macOS / Linux
mkdir -p .agents/skills &amp;&amp; cp -R ~/Downloads/uxd-ai-toolkit/skills/* .agents/skills/

Windows PowerShell
New-Item -ItemType Directory -Force ".agents\\skills" | Out-Null
Copy-Item -Recurse -Force "$HOME\\Downloads\\uxd-ai-toolkit\\skills\\*" ".agents\\skills"</div>
<p><b>C. By hand</b> in Finder or Explorer. Folders that start with a dot are hidden. Show them with Cmd + Shift + . on macOS, or with View, Show, Hidden items on Windows.</p>
<h3>Check and test</h3>
<div class="tree">.agents/skills/
  interview-guide/
    SKILL.md
    references/
  persona-builder/
  kickoff-prompt/
  ... ({N} folders)</div>
<p>Restart the tool or start a new chat. Then check that the skills are there:</p>""")
    rows = "".join(f"<tr><td>{e(r['name'])}</td><td>{e(r['verify'])}</td></tr>" for r in agents)
    o.append(f"<table><tr><th>Tool</th><th>How to check</th></tr>{rows}</table>")
    o.append('<div class="prompt"><span class="lbl">Test prompt</span>Use the ux-process-guide skill. I am starting a new project. What should I do first?</div>')
    o.append(h2("Claude app"))
    o.append("""<ol class="steps">
<li><div>Download the plugin file <code>uxd-ai-toolkit.plugin</code> from the course page on Moodle.</div></li>
<li><div>Open it in the Claude desktop app and accept it. The skills are then available in every chat.</div></li>
<li><div>Test it. Ask: "Which UXD toolkit skills do you have?"</div></li>
<li><div>When you work on a project, connect its folder to the chat so Claude can read your PRD and code.</div></li>
</ol>
<p>If you have no plugin file, or you use Claude on the web only, use the paste-me files described next.</p>""")
    o.append(h2("Chat tools: ChatGPT, Gemini and others"))
    o.append("""<p>There is nothing to install. The toolkit has a <code>paste-me</code> folder with one file per skill.</p>
<ol class="steps">
<li><div>When you need a skill, open its file, for example <code>paste-me/interview-guide.md</code>.</div></li>
<li><div>Copy everything, paste it into a <b>new</b> chat and send it.</div></li>
<li><div>Then send your prompt. Leave out the first line ("Use the ... skill.").</div></li>
<li><div>Use one skill per chat. Start a new chat for the next skill and bring the result of the last one with you.</div></li>
</ol>""")
    o.append(h2("If a skill does not show up"))
    o.append("""<ul>
<li>Check the path. <code>SKILL.md</code> must sit directly inside the skill's folder, for example <code>.agents/skills/interview-guide/SKILL.md</code>. A common mistake is an extra level such as <code>skills/skills/</code>.</li>
<li>Keep the folder names as they are. The folder name must match the skill name.</li>
<li>Restart the tool or start a new chat. Skills are read when a session starts.</li>
<li>Name the skill in your prompt: "Use the interview-guide skill". Agents choose skills by their description and sometimes miss one.</li>
<li>Still nothing? Use the file in <code>paste-me/</code> for now. It gives the same result.</li>
</ul>
<p style="color:var(--muted);font-size:9pt">Folder locations were checked against each tool's documentation in November 2026. These tools change often. If something does not match, look at the tool's current skills documentation.</p>""")

    # 4 Process at a glance
    o.append(h1(4, "The process at a glance"))
    o.append("""<p class="lead">Six phases. You can enter anywhere and go back at any time. With AI, design moves in short loops between exploring, building and testing.</p>""")
    o.append(rail())
    rows = ""
    for p in nd.PHASES:
        sk = [s["id"] for s in nd.SKILLS if s["phase"] == p["id"] or s.get("also") == p["id"]]
        rows += f"<tr><td>{p['n']} {e(p['name'])}</td><td>{e(p['when'])}</td><td>{', '.join(f'<code>{x}</code>' for x in sk)}</td><td>{e(p['you'])}</td></tr>"
    o.append(f"<table><tr><th>Phase</th><th>Use when</th><th>Skills</th><th>Your part</th></tr>{rows}</table>")
    o.append("<p>At any time: <code>ux-process-guide</code> finds where you are and points to the next skill.</p>")
    o.append(h2("How to read a skill in this guide"))
    o.append("""<table>
<tr><td>You bring</td><td>What to have ready before you start. Skills ask for missing input and do not make it up.</td></tr>
<tr><td>You get</td><td>The result of the skill. Save it as a file in your project.</td></tr>
<tr><td>Prompt</td><td>A starting prompt. Replace everything in &lt;angle brackets&gt; with your own content.</td></tr>
<tr><td>Then</td><td>The skills that usually follow.</td></tr>
<tr><td>Your judgment</td><td>Every skill ends its answer with this block. It lists what you must verify or decide yourself.</td></tr>
</table>""")
    o.append(h2("Typical paths"))
    for p in nd.PATHS:
        o.append('<div class="path"><b>' + e(p["name"]) + "</b>" + "<i>&gt;</i>".join(f"<span>{x}</span>" for x in p["steps"]) + "</div>")

    # 5 Phase by phase
    o.append(h1(5, "Phase by phase"))
    o.append('<p class="lead">Each phase with its skills, what to bring, what you get, and a prompt to start from.</p>')
    for p in nd.PHASES:
        o.append(h2(f"Phase {p['n']}: {p['name']}"))
        o.append(f"<p>{e(p['what'])}</p><div class=\"you\"><b>Your part</b>{e(p['you'])}</div>")
        for s in nd.SKILLS:
            if s["phase"] == p["id"]:
                o.append(skill_block(s))
        also = [s["id"] for s in nd.SKILLS if s.get("also") == p["id"]]
        if also:
            o.append("<p>Also useful in this phase: " + ", ".join(f"<code>{a}</code>" for a in also) + " (see Prototype).</p>")
    o.append(h2("Any time: ux-process-guide"))
    o.append(skill_block(S["ux-process-guide"]))

    # 6 Running a skill
    o.append(h1(6, "Running a skill, step by step"))
    o.append('<p class="lead">The same five steps apply to every skill. Only the first two depend on your tool.</p>')
    o.append(h2("In a coding agent"))
    o.append("""<ol class="steps">
<li><div>Open your project folder in the tool. The skills must be in its skills folder (chapter 3).</div></li>
<li><div>Paste the prompt into the agent chat. You can also call the skill directly with the shortcut from the table below.</div></li>
<li><div>Answer its questions. It asks before it invents anything.</div></li>
<li><div>If the skill writes a prompt for your builder, review it. Then send it, or copy it into your builder (chapter 2).</div></li>
<li><div>Do the checks under Your judgment. Add the prompt to <code>PROMPTS.md</code>. In the Build phase, save a checkpoint.</div></li>
</ol>""")
    rows = "".join(f"<tr><td>{e(r['name'])}</td><td><code>{e(r['slash'].replace('{id}', 'interview-guide'))}</code></td><td>{e(r['invoke'])}</td></tr>" for r in agents)
    o.append(f"<table><tr><th>Tool</th><th>Shortcut</th><th>How you call a skill</th></tr>{rows}</table>")
    o.append(h2("In the Claude app or a chat tool"))
    o.append("<p><b>Claude app:</b> open a new chat, with the toolkit plugin installed. For skills that need your project, connect the project folder first. Paste the prompt and continue from step 3 above.</p><p><b>Chat tool:</b> open <code>paste-me/&lt;skill&gt;.md</code>, copy all of it into a new chat and send it. Then send your prompt without the first line and continue from step 3 above.</p>")
    o.append(h2("Worked example: kick-off for the THI GreenAI Portal"))
    o.append("""<div class="keep"><p>Setup: you talk to AI in Cursor and build with Lovable. Your PRD is saved as <code>PRD.md</code>.</p>
<div class="prompt"><span class="lbl">You send in Cursor</span>Use the kickoff-prompt skill.

Write a kick-off prompt for Lovable from my PRD for the THI GreenAI Portal. Goal of the first build: Scaffold the whole page. PRD: @PRD.md</div>
<p>The skill reads the PRD, asks about anything that is missing (for example what is out of scope), and returns a kick-off prompt with sections in order, exact values, design tokens, accessibility rules and a check such as: "with 20 prompts per day, large model and 5 images per week the page must show 155.0 Wh and 58.9 g CO2".</p>
<p>You copy that prompt into Lovable, plan in Chat mode, then build. Afterwards you run the check yourself, save a checkpoint, and continue with <code>feature-prompt</code> for the next feature.</p></div>""")

    # 7 Reference
    o.append(h1(7, "Skill reference"))
    o.append(f'<p class="lead">All {N} skills in one table.</p>')
    rows = ""
    for s in nd.SKILLS:
        ph = "Any time" if s["phase"] == "any" else next(p["name"] for p in nd.PHASES if p["id"] == s["phase"])
        rows += f"<tr><td><code>{s['id']}</code></td><td>{ph}</td><td>{e(s['want'])}</td><td>{'Yes' if s['where']=='project' else ''}</td></tr>"
    o.append(f"<table><tr><th>Skill</th><th>Phase</th><th>Use it when you want to</th><th>Needs your project</th></tr>{rows}</table>")
    o.append(h2("Frequently asked questions"))
    o.append("""<h3>Do I have to remember the skill names?</h3>
<p>No. Describe what you need and the agent picks the skill. Naming the skill is more reliable, so the prompts in this guide do it.</p>
<h3>The skill asks me many questions. Can I skip them?</h3>
<p>You can say what you do not know. The skill then marks those points as assumptions or as TBD. It will not fill the gaps with invented content.</p>
<h3>Can I use the skills in German?</h3>
<p>Yes. Write in the language you prefer. The skills are written in English and answer in your language.</p>
<h3>Can I change a skill?</h3>
<p>Yes, and you should try. A skill is a text file. Copy the folder, give it a new name, edit <code>SKILL.md</code> and see what changes.</p>
<h3>Is the result of a skill correct?</h3>
<p>Not automatically. Skills reduce typical AI mistakes, and they show their checks so that you can verify them. The block Your judgment tells you what to check.</p>
<h3>Which data may I paste?</h3>
<p>Only anonymized research data. No names, emails or other identifying details, and never passwords or API keys.</p>
<h3>Do I have to say that I used AI?</h3>
<p>Follow the course rules. Your prompt log in <code>PROMPTS.md</code> is the record of what you asked and what you changed.</p>""")
    return "\n".join(o)


def toc_html(pages):
    rows = []
    for n, title, subs in SECTIONS:
        pg = pages.get(title, "")
        rows.append(f'<div class="row l1"><span>{n} {e(title)}</span><span class="dots"></span><span>{pg}</span></div>')
        for s in subs:
            rows.append(f'<div class="row l2"><span>{e(s)}</span><span class="dots"></span><span>{pages.get(s, "")}</span></div>')
    return '<section class="toc"><h1>Contents</h1>' + "".join(rows) + "</section>"


def cover_html(fonts):
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><style>{fonts}{CSS}@page{{size:A4;margin:0}}</style></head><body>
<div class="cover"><div class="band">
<div class="kick">Vibecoding for UX Designers, Technische Hochschule Ingolstadt</div>
<div class="title">UXD AI Toolkit</div><div class="sub">User guide</div>
<div class="meta">Version {VERSION}, {N} skills, {DATE}</div></div>
<div class="body"><p>How to install and use the toolkit skills across the whole UX design process, from the first interview question to a tested prototype, in the AI tool you prefer.</p>
<p style="color:var(--muted);font-size:10.6pt">Written for students of the UX Design master. Covers Claude Code, Cursor, Codex, Antigravity, the Claude app and chat tools, and building with Lovable, Replit and DeepSite. The interactive UXD AI Toolkit Navigator offers the same content with a prompt builder.</p>
<div style="margin-top:14mm">{rail()}</div></div>
<div class="foot"><b>{AUTHOR}</b><br>Human-Centered Intelligent Systems Lab, Technische Hochschule Ingolstadt<br>Tool facts were checked in {DATE}. AI tools change often, so check the tool's own documentation when something does not match.</div>
</div></body></html>"""


def doc_html(fonts, pages):
    body = body_html()
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>UXD AI Toolkit User Guide</title>
<style>{fonts}{CSS}@page{{size:A4;margin:17mm 19mm 20mm}}</style></head><body>{toc_html(pages)}{body}</body></html>"""


def render(page, html_text):
    page.set_content(html_text, wait_until="load")
    page.evaluate("document.fonts.ready")
    return page.pdf(format="A4", print_background=True, prefer_css_page_size=True)


def find_pages(pdf_bytes, offset):
    from pypdf import PdfReader
    r = PdfReader(io.BytesIO(pdf_bytes))
    norm = lambda t: re.sub(r"\s+", "", t).lower()
    texts = [norm(pg.extract_text() or "") for pg in r.pages]
    toc_pages = 1
    while toc_pages < len(texts) and norm("1Quick start") not in texts[toc_pages][:40]:
        toc_pages += 1
    pages, start = {}, toc_pages
    for n, title, subs in SECTIONS:
        for key, label in [(f"{n}{title}", title)] + [(s, s) for s in subs]:
            for i in range(start, len(texts)):
                if norm(key) in texts[i]:
                    pages[label] = i + 1 + offset
                    start = i
                    break
    return pages, len(texts)


def main():
    from playwright.sync_api import sync_playwright
    from pypdf import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.colors import HexColor

    fonts = font_css(sys.argv[1] if len(sys.argv) > 1 else None)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        cover = render(pg, cover_html(fonts))
        first = render(pg, doc_html(fonts, {}))
        pages, n1 = find_pages(first, offset=1)
        body = render(pg, doc_html(fonts, pages))
        pages2, n2 = find_pages(body, offset=1)
        if pages2 != pages:
            body = render(pg, doc_html(fonts, pages2))
        b.close()

    w = PdfWriter()
    for src in (cover, body):
        for page in PdfReader(io.BytesIO(src)).pages:
            w.add_page(page)
    total = len(w.pages)
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    W, _ = A4
    for i in range(total):
        if i > 0:
            c.setStrokeColor(HexColor("#cfd4da")); c.setLineWidth(0.5)
            c.line(54, 40, W - 54, 40)
            c.setFillColor(HexColor("#555f6d")); c.setFont("Helvetica", 8)
            c.drawString(54, 28, f"UXD AI Toolkit v{VERSION}, User guide, {AUTHOR}, THI")
            c.drawRightString(W - 54, 28, str(i + 1))
        c.showPage()
    c.save()
    over = PdfReader(io.BytesIO(buf.getvalue()))
    for i, page in enumerate(w.pages):
        page.merge_page(over.pages[i])
    w.add_metadata({"/Title": "UXD AI Toolkit User Guide", "/Author": AUTHOR, "/Subject": "Vibecoding for UX Designers, THI"})
    out = root / "docs" / "guide"; out.mkdir(parents=True, exist_ok=True)
    f = out / "uxd-ai-toolkit-user-guide.pdf"
    with open(f, "wb") as fh:
        w.write(fh)
    labels = [x for _, title, subs in SECTIONS for x in [title] + subs]
    missing = [x for x in labels if x not in pages2]
    print("built", f, total, "pages; toc entries without page:", missing)


if __name__ == "__main__":
    main()
