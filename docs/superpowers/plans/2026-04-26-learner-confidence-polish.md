# Learner Confidence Polish Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a first-hour learner support layer, module readiness checks, helper guidance, and a lightweight course validator for private beginner use.

**Architecture:** Keep learner support as plain Markdown at the repo root and module-level `README.md` sections. Add one standard-library Python validator at the repo root so maintenance checks remain easy to run without external services or extra dependencies.

**Tech Stack:** Markdown, Python standard library, existing unittest/setup-check infrastructure, PowerShell-compatible commands.

---

## File Structure

- Create: `FIRST_30_MINUTES.md`
- Create: `HELPING_A_LEARNER.md`
- Create: `check_course_files.py`
- Create: `tests/test_check_course_files.py`
- Modify: `START_HERE.md`
- Modify: `GET_HELP.md`
- Modify: `progress_tracker.md`
- Modify: `docs/ai/improvement_backlog.md`
- Modify: `docs/ai/course_quality_checklist.md`
- Modify: module `README.md` files:
  - `00-what-is-data-analytics/README.md`
  - `01-setting-up/README.md`
  - `02-spreadsheets/README.md`
  - `03-data-analysis/README.md`
  - `04-databases-and-sql/README.md`
  - `05-visualization/README.md`
  - `06-real-world-data/README.md`
  - `07-capstone/README.md`

## Task 1: First-Hour Entry Point

**Files:**
- Create: `FIRST_30_MINUTES.md`
- Modify: `START_HERE.md`
- Modify: `progress_tracker.md`

- [ ] Create `FIRST_30_MINUTES.md` with these sections:
  - `# First 30 Minutes`
  - `## What You Need`
  - `## Minute 0 To 5: Open The Course Folder`
  - `## Minute 5 To 10: Open The Tracker`
  - `## Minute 10 To 20: Read The Course Map`
  - `## Minute 20 To 30: Start Module 0`
  - `## If You Already Installed Python`
  - `## A Good First Session`
  - `## Where To Stop`
- [ ] Link `FIRST_30_MINUTES.md` from `START_HERE.md` near the top.
- [ ] Add a checklist item to `progress_tracker.md` under "Getting The Course Ready": `Read FIRST_30_MINUTES.md`.
- [ ] Commit with `docs: add first 30 minutes guide`.

## Task 2: Setup Rescue Layer

**Files:**
- Modify: `GET_HELP.md`

- [ ] Expand `GET_HELP.md` with sections for:
  - `python is not recognized`
  - `No such file or directory`
  - Running commands from the wrong folder
  - Package install errors
  - VS Code terminal confusion
  - SQL Server connection trouble
  - Tableau cannot find a CSV
- [ ] Keep the help request template near the top.
- [ ] Add a short "Try these before asking" checklist that starts with checking the folder and copying the exact command/error.
- [ ] Commit with `docs: expand setup rescue guide`.

## Task 3: Module Readiness And Reflection Checks

**Files:**
- Modify all eight module `README.md` files listed in File Structure.

- [ ] Add `## Before You Move On` to each module README with 5-8 concrete learner checks.
- [ ] Add `## Quick Reflection` to each module README with 3 short prompts.
- [ ] Keep wording beginner-friendly and module-specific.
- [ ] Do not add large lesson rewrites.
- [ ] Commit with `docs: add module readiness checks`.

## Task 4: Helper Guide For The Course Owner

**Files:**
- Create: `HELPING_A_LEARNER.md`
- Modify: `docs/ai/improvement_backlog.md`

- [ ] Create `HELPING_A_LEARNER.md` with:
  - how to ask what file, folder, command, and error they saw
  - how to check setup without taking over
  - when to point to hints, expected outputs, and solutions
  - common confidence dips and how to respond
  - a short troubleshooting order
- [ ] Add this completed item to `docs/ai/improvement_backlog.md`.
- [ ] Commit with `docs: add learner helper guide`.

## Task 5: Lightweight Course Validator

**Files:**
- Create: `check_course_files.py`
- Create: `tests/test_check_course_files.py`
- Modify: `README.md`
- Modify: `docs/ai/improvement_backlog.md`

- [ ] Implement `check_course_files.py` with standard-library functions:
  - `required_paths() -> list[str]`
  - `check_required_paths(root: Path) -> list[CheckResult]`
  - `extract_markdown_links(text: str) -> list[str]`
  - `check_markdown_links(root: Path, files: Iterable[Path]) -> list[CheckResult]`
  - `run_checks(root: Path) -> list[CheckResult]`
  - `main() -> int`
- [ ] Define `CheckResult` as a dataclass with `status`, `path`, and `detail`.
- [ ] Check local Markdown links only. Skip `http`, `https`, `mailto`, anchors-only links, and image links.
- [ ] Add tests for required path failures, Markdown link extraction, skipped external links, and broken local links.
- [ ] Link the validator from the main `README.md`.
- [ ] Add this completed item to `docs/ai/improvement_backlog.md`.
- [ ] Commit with `test: add course file validator`.

## Task 6: Final Verification

**Files:**
- Verify all changed files.

- [ ] Run `python -m unittest tests.test_check_setup tests.test_check_course_files -v`.
- [ ] Run `python check_setup.py`.
- [ ] Run `python check_course_files.py`.
- [ ] Run `python -m compileall -q .`.
- [ ] Run `git diff --check`.
- [ ] Remove generated caches inside the repo.
- [ ] Commit any missed documentation updates with a focused message.

## Self-Review Notes

- This plan intentionally avoids screenshots and videos.
- This plan focuses on friend/family beginner confidence, not commercial polish.
- The validator is deliberately local-only so it remains fast and internet-independent.
- Module readiness checks should help learners stop polishing and keep moving.
