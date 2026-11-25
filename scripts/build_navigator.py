"""Build docs/navigator/index.html from navigator_data.py and the skill folders.

Usage: python scripts/build_navigator.py   (run from the repository root)
"""
import json, re, sys
from pathlib import Path

here = Path(__file__).resolve().parent
root = here.parent
sys.path.insert(0, str(here))
import navigator_data as nd

on_disk = {p.parent.name: p.read_text(encoding="utf-8") for p in (root / "skills").glob("*/SKILL.md")}
ids = [s["id"] for s in nd.SKILLS]
missing = sorted(set(on_disk) - set(ids)); extra = sorted(set(ids) - set(on_disk))
if missing or extra:
    sys.exit(f"Navigator data and skills/ disagree. Not in data: {missing}. Not on disk: {extra}.")
for s in nd.SKILLS:
    s["desc"] = re.search(r"^description: (.+)$", on_disk[s["id"]], re.M).group(1)
    for n in s["next"]:
        assert n in on_disk, (s["id"], n)
for p in nd.PATHS:
    for n in p["steps"]:
        assert n in on_disk, n

version = json.loads((root / ".claude-plugin" / "plugin.json").read_text())["version"]
data = {"phases": nd.PHASES, "skills": nd.SKILLS, "runners": nd.RUNNERS, "builders": nd.BUILDERS, "paths": nd.PATHS}
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
html = (here / "navigator_template.html").read_text(encoding="utf-8")
html = html.replace("__DATA__", blob).replace("__VERSION__", version).replace("__COUNT__", str(len(nd.SKILLS)))
out = root / "docs" / "navigator"; out.mkdir(parents=True, exist_ok=True)
(out / "index.html").write_text(html, encoding="utf-8")
print("built", out / "index.html", len(html), "bytes,", len(nd.SKILLS), "skills")
