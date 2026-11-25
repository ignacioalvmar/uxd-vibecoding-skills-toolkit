"""Build single-file 'paste-me' prompts from each skill folder.

Usage: python scripts/build_paste_me.py   (run from the repository root)
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
out = root / "paste-me"
out.mkdir(exist_ok=True)

for skill in sorted((root / "skills").iterdir()):
    md = skill / "SKILL.md"
    if not md.is_file():
        continue
    text = md.read_text(encoding="utf-8")
    body = text.split("---", 2)[2].strip() if text.startswith("---") else text.strip()
    parts = [
        f"<!-- Paste-me version of the '{skill.name}' skill. Generated file, do not edit. -->",
        "Follow the instructions below for the rest of this conversation. "
        "Where they mention reference files, use the reference sections at the end. "
        "Start by asking me for the inputs you need.",
        "",
        body,
    ]
    for ref in sorted((skill / "references").glob("*.md")):
        parts += ["", "---", f"## Reference: references/{ref.name}", "", ref.read_text(encoding="utf-8").strip()]
    (out / f"{skill.name}.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    print("built", skill.name)
