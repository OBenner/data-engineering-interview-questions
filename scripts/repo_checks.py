#!/usr/bin/env python3
"""
Lightweight repo checks for this markdown-based project.

What it checks:
- No placeholder TODO links in README (e.g. href="TODO")
- No obvious encoding artifacts (U+FFFD replacement char, "пїЅ")
- Internal links in content/full.md that point to other content/*.md headings exist
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
import os
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
README = ROOT / "README.md"
FULL = CONTENT_DIR / "full.md"


FORBIDDEN_TEXT_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("replacement character (U+FFFD)", re.compile("\uFFFD")),
    ("mojibake marker (пїЅ)", re.compile(r"пїЅ")),
]


@dataclass(frozen=True)
class Problem:
    file: Path
    line_no: int
    message: str
    line: str


def _read_text(path: Path) -> str:
    # Explicit UTF-8 helps surface bad encodings early.
    return path.read_text(encoding="utf-8")


def _iter_lines(path: Path) -> Iterable[tuple[int, str]]:
    for idx, line in enumerate(_read_text(path).splitlines(), start=1):
        yield idx, line


def _github_slugify(text: str) -> str:
    """
    Approximate GitHub heading id generation:
    - lower-case
    - remove punctuation
    - spaces -> hyphens
    - collapse multiple hyphens

    Note: GitHub's exact algorithm has edge cases; this is intentionally simple
    and good enough for catching broken anchors in this repo.
    """
    s = text.strip().lower()
    # Keep alphanumerics, spaces, and hyphens; drop the rest.
    s = re.sub(r"[^a-z0-9 \-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-")


def _collect_heading_slugs(md_path: Path) -> set[str]:
    """
    Collect all GitHub-like slugs for headings within a markdown file.
    Includes duplicate handling: 'title', 'title-1', 'title-2', ...
    """
    slugs: set[str] = set()
    counts: dict[str, int] = {}
    heading_re = re.compile(r"^(#{1,6})\s+(.+?)\s*$")

    for _line_no, line in _iter_lines(md_path):
        m = heading_re.match(line)
        if not m:
            continue
        heading_text = m.group(2)
        base = _github_slugify(heading_text)
        if not base:
            continue
        n = counts.get(base, 0)
        counts[base] = n + 1
        slug = base if n == 0 else f"{base}-{n}"
        slugs.add(slug)
    return slugs


def check_readme_placeholders(problems: list[Problem]) -> None:
    readme_text = _read_text(README)
    if 'href="TODO"' in readme_text:
        for line_no, line in _iter_lines(README):
            if 'href="TODO"' in line:
                problems.append(
                    Problem(
                        file=README,
                        line_no=line_no,
                        message='README contains placeholder link href="TODO"',
                        line=line,
                    )
                )

    # Verify all linked content files exist (simple sanity check).
    for line_no, line in _iter_lines(README):
        for m in re.finditer(r'href="(\./content/[^"]+\.md)"', line):
            rel = m.group(1)
            target = (ROOT / rel).resolve()
            if not target.exists():
                problems.append(
                    Problem(
                        file=README,
                        line_no=line_no,
                        message=f"README links to missing file: {rel}",
                        line=line,
                    )
                )


def check_forbidden_text(problems: list[Problem]) -> None:
    paths = [README, FULL, *sorted(CONTENT_DIR.glob("*.md"))]
    for path in paths:
        try:
            text = _read_text(path)
        except UnicodeDecodeError as e:
            problems.append(
                Problem(
                    file=path,
                    line_no=1,
                    message=f"File is not valid UTF-8: {e}",
                    line="",
                )
            )
            continue

        for label, pattern in FORBIDDEN_TEXT_PATTERNS:
            for line_no, line in enumerate(text.splitlines(), start=1):
                if pattern.search(line):
                    problems.append(
                        Problem(
                            file=path,
                            line_no=line_no,
                            message=f"Found {label}",
                            line=line,
                        )
                    )


def check_full_internal_links(problems: list[Problem], *, strict_anchors: bool) -> None:
    if not FULL.exists():
        return

    # Cache heading slugs for all content files.
    slug_cache: dict[Path, set[str]] = {}

    link_re = re.compile(r"\(([^)]+\.md#[^)]+)\)")
    for line_no, line in _iter_lines(FULL):
        for raw_target in link_re.findall(line):
            if "://" in raw_target:
                continue
            file_part, frag = raw_target.split("#", 1)
            target_path = (CONTENT_DIR / file_part).resolve()
            if not target_path.exists():
                problems.append(
                    Problem(
                        file=FULL,
                        line_no=line_no,
                        message=f"Broken link target file not found: {file_part}",
                        line=line,
                    )
                )
                continue

            if strict_anchors:
                if target_path not in slug_cache:
                    slug_cache[target_path] = _collect_heading_slugs(target_path)

                frag = unquote(frag)
                frag_slug = _github_slugify(frag.replace("-", " "))
                if frag_slug and frag_slug not in slug_cache[target_path]:
                    problems.append(
                        Problem(
                            file=FULL,
                            line_no=line_no,
                            message=f"Broken anchor: {file_part}#{frag} (normalized: #{frag_slug})",
                            line=line,
                        )
                    )


def main() -> int:
    problems: list[Problem] = []

    if not CONTENT_DIR.exists():
        print(f"Expected directory not found: {CONTENT_DIR}", file=sys.stderr)
        return 2

    check_readme_placeholders(problems)
    check_forbidden_text(problems)
    strict_anchors = os.environ.get("STRICT_ANCHORS", "").strip() == "1"
    check_full_internal_links(problems, strict_anchors=strict_anchors)

    if problems:
        print("Repo checks failed:\n", file=sys.stderr)
        for p in problems[:200]:
            rel = p.file.relative_to(ROOT)
            print(f"- {rel}:{p.line_no}: {p.message}", file=sys.stderr)
            if p.line:
                print(f"    {p.line}", file=sys.stderr)
        if len(problems) > 200:
            print(f"\n... and {len(problems) - 200} more", file=sys.stderr)
        return 1

    print("Repo checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

