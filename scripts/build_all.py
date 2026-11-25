"""Rebuild everything that is generated: paste-me files, navigator and user guide.

Usage (from the repository root):
    python scripts/build_all.py [FONT_DIR]

FONT_DIR is passed on to build_guide.py (see that file). Run this after you
change a skill, navigator_data.py or the version in .claude-plugin/plugin.json.
"""
import subprocess, sys
from pathlib import Path

here = Path(__file__).resolve().parent
for script, args in [("build_paste_me.py", []), ("build_navigator.py", []), ("build_guide.py", sys.argv[1:2])]:
    print(">>", script)
    subprocess.run([sys.executable, str(here / script), *args], check=True, cwd=here.parent)
