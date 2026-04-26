# Guided Confidence Layer Design

Date: 2026-04-26
Status: Draft for user review

## Purpose

Add a lightweight guided support layer to `data-analytics-101` so private, self-paced learners can get unstuck during setup and check their exercise work without needing a live instructor.

The repo already has the core curriculum. This feature should not rewrite that curriculum. It should make the existing path easier to start, easier to recover from, and easier to validate.

## Audience

The intended learner is a friend or family member working independently on Windows. They may have little or no experience with GitHub, Markdown, VS Code, terminals, Python packages, file paths, or debugging error messages.

The support materials should feel calm, direct, and practical. They should avoid turning the course into a formal platform or a public MOOC.

## Goals

- Give learners a clear starting point.
- Help learners track progress through the course.
- Catch common setup problems before they become discouraging.
- Give learners a simple way to ask for help with useful context.
- Add a repeatable answer-support pattern: hints first, expected outputs second, full solutions last.
- Pilot the answer-support pattern in Module 3, where Python paths, packages, and DataFrame answers are likely to create uncertainty.

## Non-Goals

- Do not convert the repo into a web app, LMS, or notebook-first course.
- Do not rewrite all modules in the first pass.
- Do not make SQL Server, Tableau, or Excel checks block early learners before those tools are needed.
- Do not change sample datasets as part of this feature.
- Do not add heavy automation or CI as part of the first implementation.

## Scope

The first implementation pass includes:

1. Repo-level learner entry and help files.
2. A setup verification script.
3. A progress tracker.
4. A Module 3 answer ladder for the existing pandas exercises.
5. Small consistency fixes only when they directly support the guided experience.

The first implementation pass does not include full answer ladders for SQL, visualization, real-world data, or capstone. Those can reuse the Module 3 pattern later.

## Components

### START_HERE.md

`START_HERE.md` becomes the friend/family-facing front door. It should explain:

- What this course is.
- Who it is for.
- The recommended module order.
- How to read Markdown files.
- How to use the progress tracker.
- How to run the setup checker.
- What to do when stuck.

The top-level `README.md` should link to `START_HERE.md` near the existing getting-started guidance.

### progress_tracker.md

`progress_tracker.md` gives learners a visible checklist for:

- Downloading/extracting the repo.
- Reading Module 0.
- Completing setup milestones.
- Completing each module.
- Completing exercises.
- Completing capstone deliverables.

The tracker should use plain Markdown checkboxes so learners can edit it in VS Code.

### GET_HELP.md

`GET_HELP.md` helps learners send useful support requests. It should include:

- A short reassurance that getting stuck is normal.
- A copy/paste help template.
- What file they were on.
- What command or step they tried.
- What happened.
- What they expected.
- Any error message.
- Whether they already ran `check_setup.py`.

The goal is to reduce vague help requests like "it does not work" and make it easier for the course creator to help quickly.

### check_setup.py

`check_setup.py` verifies the basics needed for early course success:

- Python version is available.
- Required Python packages can be imported: `pandas`, `matplotlib`, `seaborn`, `openpyxl`, `requests`.
- `pyodbc` is checked separately as a later SQL-related dependency.
- Expected core data files exist:
  - `data/sales_data.csv`
  - `data/employees.csv`
  - `data/customers.csv`
- Expected course folders exist.
- The script is being run from the repo root, or it can clearly explain how to run it from the repo root.

The script should use beginner-friendly output:

- `[OK]` for passing checks.
- `[FIX]` for required fixes.
- `[LATER]` for optional checks that are not needed until a later module.

The script should exit with code `0` if core setup checks pass. It should exit with code `1` if required early-course checks fail.

### Module 3 Answer Ladder

Module 3 gets the first complete answer-support pattern for `lesson_05_exercises.md`.

Files:

- `03-data-analysis/hints/lesson_05_hints.md`
- `03-data-analysis/expected_outputs/lesson_05_expected_outputs.md`
- `03-data-analysis/solutions/lesson_05_solutions.py`

The existing exercise file should link to these in order:

1. Try the exercise first.
2. Use hints if stuck.
3. Compare to expected outputs.
4. Open the solution only after trying.

The solution script should be runnable and should print answers for all current Module 3 exercises.

## Learner Flow

1. Learner opens the repo.
2. Learner reads `START_HERE.md`.
3. Learner runs `python check_setup.py` from the repo root.
4. Learner fixes any `[FIX]` items or uses `GET_HELP.md` to ask for help.
5. Learner uses `progress_tracker.md` while moving through modules.
6. In Module 3 exercises, learner tries independently.
7. If stuck, learner opens hints.
8. After solving, learner checks expected outputs.
9. If still confused, learner reads or runs the full solution script.

## Error Handling

`check_setup.py` should avoid scary tracebacks for expected beginner problems. It should catch import and file checks cleanly and print specific next steps.

Examples:

- Missing package: tell the learner to run `python -m pip install -r requirements.txt`.
- Missing data file: tell the learner to confirm they extracted the full ZIP and are in the course folder.
- Wrong working directory: tell the learner to open the `data-analytics-101` folder in VS Code and run the command from there.

The solution script should avoid modifying datasets. It should only read files and print answers.

## File Responsibilities

- `START_HERE.md`: learner entry point and orientation.
- `progress_tracker.md`: learner-owned progress checklist.
- `GET_HELP.md`: support request template and stuck guidance.
- `check_setup.py`: local environment and file verification.
- `03-data-analysis/lesson_05_exercises.md`: existing exercise entry, updated to point to the answer ladder.
- `03-data-analysis/hints/lesson_05_hints.md`: hint-only support.
- `03-data-analysis/expected_outputs/lesson_05_expected_outputs.md`: expected answer shapes and representative outputs.
- `03-data-analysis/solutions/lesson_05_solutions.py`: complete runnable solution.

## Verification

Implementation should be verified with:

- `python check_setup.py`
- `python -m compileall -q .`
- `python 03-data-analysis/solutions/lesson_05_solutions.py`
- Manual review of new Markdown files for beginner clarity.
- Manual check that all new Markdown links point to real files.

The SQL Server, Tableau, and Excel applications do not need to be verified for this first pass because they are not core blockers for the new Guided Confidence Layer.

## Implementation Sequence

The detailed implementation plan should break work into small tasks:

1. Add learner entry/help files.
2. Add setup checker.
3. Add Module 3 answer ladder directories and files.
4. Update existing README and Module 3 exercise links.
5. Run verification and fix any issues.

Each task should be independently reviewable and should avoid broad course rewrites.

## Future Extensions

After the Module 3 pilot is working, the same answer ladder can be added to:

- Module 4 SQL exercises.
- Module 5 visualization exercises.
- Module 6 real-world data exercises.
- Module 7 capstone rubric and example project.

Additional maintenance guardrails can be added later:

- Dataset validation script.
- Markdown link checker.
- Lightweight tests for scripts that do not require external GUI tools.

