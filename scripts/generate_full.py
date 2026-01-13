#!/usr/bin/env python3
"""
Generate content/full.md from headings in content/*.md.

This is optional (not run in CI) but helps keep the "full list" consistent.

Usage:
  python3 scripts/generate_full.py > content/full.md

Or (safer):
  python3 scripts/generate_full.py > /tmp/full.md && diff -u content/full.md /tmp/full.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"


def github_slugify(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^a-z0-9 \-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-")


def iter_content_files() -> list[Path]:
    files = sorted(CONTENT_DIR.glob("*.md"))
    return [p for p in files if p.name != "full.md"]


def parse_topic_and_questions(path: Path) -> tuple[str, list[str]]:
    topic = path.stem
    questions: list[str] = []

    h1_re = re.compile(r"^#\s+(.+?)\s*$")
    h2_re = re.compile(r"^##\s+(.+?)\s*$")

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## [Main title]"):
            continue
        if line.startswith("### [Interview questions]"):
            continue

        m1 = h1_re.match(line)
        if m1 and topic == path.stem:
            topic = m1.group(1).strip()
            continue

        m2 = h2_re.match(line)
        if m2:
            q = m2.group(1).strip()
            if q:
                questions.append(q)

    return topic, questions


def main() -> int:
    content_files = iter_content_files()
    if not content_files:
        print("No content files found.", file=sys.stderr)
        return 2

    topics: list[tuple[str, str, list[str]]] = []
    for p in content_files:
        topic, questions = parse_topic_and_questions(p)
        topics.append((p.name, topic, questions))

    out: list[str] = []
    out.append("## [Main title](../README.md)")
    out.append("")
    for _filename, topic, _questions in topics:
        out.append(f"+ [{topic}](#{github_slugify(topic)})")
    out.append("")

    for filename, topic, questions in topics:
        out.append(f"## {topic}")
        base_counts: dict[str, int] = {}
        for q in questions:
            base = github_slugify(q)
            n = base_counts.get(base, 0)
            base_counts[base] = n + 1
            slug = base if n == 0 else f"{base}-{n}"
            out.append(f"+ [{q}]({filename}#{slug})")
        out.append("")

    sys.stdout.write("\n".join(out).rstrip() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

