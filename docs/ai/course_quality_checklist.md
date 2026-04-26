# Course Quality Checklist

Use this checklist when polishing lessons, scripts, exercises, or capstone material.

## Beginner Clarity

- The learner knows what file to open first.
- The lesson states what they will learn or do.
- Required prior knowledge is named plainly.
- New terms are explained in context.
- Commands are copy-pasteable.
- The lesson avoids unexplained abbreviations and expert shorthand.
- The next step is clear.

## Self-Paced Feedback

- The learner can tell whether they succeeded.
- Script output examples are included where useful.
- Exercises include hints.
- Exercises have solutions when the goal is practice rather than assessment.
- Common beginner mistakes are called out near the relevant step.
- Error recovery guidance is specific enough to act on.

## File and Path Reliability

- File paths match the actual repo structure.
- Python scripts use robust paths where practical.
- Lessons say which folder to run commands from.
- Generated outputs are saved to predictable locations.
- Instructions do not rely on hidden local state.

## Curriculum Consistency

- Module numbers are correct.
- Lesson titles match README tables.
- Cross-links point to existing files.
- Terminology is consistent across Excel, pandas, SQL, and Tableau.
- Datasets used in examples match available files.
- Expected outputs match current datasets.

## Code Quality for Lesson Scripts

- Scripts compile.
- Imports are limited to documented requirements.
- Error messages are beginner-friendly when likely failures are expected.
- Examples are readable before they are clever.
- Comments explain why, not every tiny operation.
- Scripts avoid destructive writes unless clearly documented.

## Data Quality

- Dataset row counts and columns are stable or documented.
- Changes to `data/` are reflected in lessons and exercises.
- External downloads include source notes and fallback guidance.
- Privacy-sensitive or personally identifying real data is not added.

## Capstone Quality

- The learner has a clear definition of done.
- The rubric rewards understandable work, not perfection.
- Templates are easy to modify.
- Example questions are realistic and beginner-sized.
- Portfolio guidance includes write-up and presentation expectations.

## Verification Before Finishing

- Run `git status --short` to confirm intended files changed.
- For Markdown changes, scan headings and links.
- For Python changes, run `python -m compileall -q .`.
- Run representative scripts if they do not require unavailable tools.
- Note any checks that were skipped and why.

