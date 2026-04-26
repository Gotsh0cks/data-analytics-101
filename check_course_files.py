"""Validate key course files and local Markdown links.

Run from the main course folder:

    python check_course_files.py

This script uses only the Python standard library. It does not check internet
links, SQL Server, Tableau, Excel, or package installation.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys
from typing import Iterable


SKIP_DIRS = {".git", ".pytest_cache", ".mypy_cache", ".ruff_cache", "__pycache__"}
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


@dataclass(frozen=True)
class CheckResult:
    status: str
    path: str
    detail: str


def required_paths() -> list[str]:
    return [
        "README.md",
        "START_HERE.md",
        "FIRST_30_MINUTES.md",
        "GET_HELP.md",
        "HELPING_A_LEARNER.md",
        "progress_tracker.md",
        "check_setup.py",
        "check_course_files.py",
        "00-what-is-data-analytics/README.md",
        "01-setting-up/README.md",
        "02-spreadsheets/README.md",
        "03-data-analysis/README.md",
        "04-databases-and-sql/README.md",
        "05-visualization/README.md",
        "06-real-world-data/README.md",
        "07-capstone/README.md",
        "02-spreadsheets/hints/lesson_06_hints.md",
        "03-data-analysis/hints/lesson_05_hints.md",
        "04-databases-and-sql/hints/lesson_07_hints.md",
        "05-visualization/hints/lesson_10_hints.md",
        "06-real-world-data/hints/05_hints.md",
        "07-capstone/rubric.md",
        "07-capstone/writeup_template.md",
    ]


def check_required_paths(root: Path) -> list[CheckResult]:
    results = []
    for relative_path in required_paths():
        path = root / relative_path
        if path.exists():
            results.append(CheckResult("OK", relative_path, "Found"))
        else:
            results.append(CheckResult("FIX", relative_path, "Missing required file"))
    return results


def extract_markdown_links(text: str) -> list[str]:
    return [match.group(1).strip() for match in MARKDOWN_LINK_RE.finditer(text)]


def should_skip_link(target: str) -> bool:
    normalized = target.strip()
    return (
        not normalized
        or normalized.startswith("#")
        or normalized.lower().startswith(EXTERNAL_PREFIXES)
    )


def clean_link_target(target: str) -> str:
    cleaned = target.strip().strip("<>")
    if " " in cleaned and not Path(cleaned).exists():
        cleaned = cleaned.split(" ", 1)[0]
    return cleaned.split("#", 1)[0]


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.md"):
        relative_parts = path.relative_to(root).parts
        if any(part in SKIP_DIRS or part.startswith(".worktrees") for part in relative_parts):
            continue
        if len(relative_parts) >= 2 and relative_parts[0] == "docs" and relative_parts[1] == "superpowers":
            continue
        yield path


def check_markdown_links(root: Path, files: Iterable[Path]) -> list[CheckResult]:
    results = []
    for markdown_file in files:
        text = markdown_file.read_text(encoding="utf-8")
        for raw_target in extract_markdown_links(text):
            if should_skip_link(raw_target):
                continue

            target = clean_link_target(raw_target)
            if not target:
                continue

            candidate = (markdown_file.parent / target).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                results.append(
                    CheckResult(
                        "FIX",
                        str(markdown_file.relative_to(root)),
                        f"Link points outside course folder: {raw_target}",
                    )
                )
                continue

            if candidate.exists():
                results.append(
                    CheckResult(
                        "OK",
                        str(markdown_file.relative_to(root)),
                        f"Link found: {raw_target}",
                    )
                )
            else:
                results.append(
                    CheckResult(
                        "FIX",
                        str(markdown_file.relative_to(root)),
                        f"Broken local link: {raw_target}",
                    )
                )
    return results


def run_checks(root: Path) -> list[CheckResult]:
    root = root.resolve()
    results = check_required_paths(root)
    results.extend(check_markdown_links(root, iter_markdown_files(root)))
    return results


def format_result(result: CheckResult) -> str:
    return f"[{result.status}] {result.path}: {result.detail}"


def main() -> int:
    root = Path.cwd()
    results = run_checks(root)

    print("=" * 60)
    print("Data Analytics 101 Course File Check")
    print("=" * 60)
    print()

    failures = [result for result in results if result.status == "FIX"]
    for result in results:
        if result.status == "FIX":
            print(format_result(result))

    if failures:
        print()
        print(f"{len(failures)} issue(s) need attention.")
        return 1

    print("Course files and local Markdown links look ready.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
