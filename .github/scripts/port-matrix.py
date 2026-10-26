#!/usr/bin/env python3
"""Read the tracked port list and emit a GitHub Actions matrix."""
import json
import os
import sys
from pathlib import Path

config = json.loads(Path(".github/port-updates.json").read_text())
selected = sys.argv[1] if len(sys.argv) > 1 else "all"
ports = config["ports"]

if selected != "all":
    ports = [port for port in ports if port["name"] == selected]
    if not ports:
        raise SystemExit(f"Unknown port: {selected}")

value = json.dumps({"include": ports}, separators=(",", ":"))
with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
    output.write(f"matrix={value}\n")
