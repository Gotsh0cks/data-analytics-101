# Improvement Backlog

This backlog is for future Codex sessions and human review. Keep it focused on polish and learning quality for private, self-paced learners.

## Priority 0: Learner Friction Fixes

- Fix module-number drift in lesson and script headings.
- Make Python lesson scripts resilient to being run from the repo root or lesson folder.
- Pin or bound core dependencies in `requirements.txt`.

## Priority 1: Learning Feedback

- Add expected output blocks to individual lesson pages where learners commonly need a checkpoint, especially Python and visualization lessons.
- Add short "check your understanding" questions to each module.
- Add common-mistake callouts near terminal, path, package, and SQL Server steps.
- Add a small "what good looks like" note to chart-heavy lessons so learners can judge readability, labels, and formatting.

## Priority 2: Capstone Support

- Add a Tableau dashboard checklist.
- Add optional project-extension ideas for learners who finish early.
- Add screenshots or sample exported charts after the example project format stabilizes.

## Priority 3: Maintenance Guardrails

- Add a dataset validation script for expected files, columns, and row counts.
- Add tests for scripts that do not require SQL Server, Tableau, Excel, or internet access.
- Add GitHub Actions only if automatic validation becomes useful.
- Document how to refresh generated Excel, Tableau-ready CSV, and chart assets.

## Recently Completed

- Added a learner-facing `START_HERE.md`.
- Added a `progress_tracker.md` checklist.
- Added `.gitignore` entries for Python caches, local worktrees, and generated exercise outputs.
- Added a setup verification script that checks Python packages and expected data files.
- Added a Module 3 exercise support ladder with hints, expected outputs, and a solution script.
- Added support ladders for Modules 2, 4, 5, and 6 with hints, expected outputs, and solutions.
- Added capstone completion support with a rubric, write-up template, and example project.
- Added a first-session guide, expanded setup rescue guide, module readiness checks, and private learner helper guide.
- Added a lightweight local course file and Markdown link validator.

## Parking Lot

These ideas may be useful later, but they should not distract from core course polish:

- Optional Mac/Linux setup notes.
- Optional SQLite path for learners who cannot install SQL Server.
- Optional Jupyter notebook versions.
- Short videos or screenshots.
- A small static website version of the course.
- Power BI alternative lessons.

