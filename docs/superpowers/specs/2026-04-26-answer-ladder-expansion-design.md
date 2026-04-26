# Answer Ladder Expansion Design

Date: 2026-04-26
Status: Draft for user review

## Purpose

Expand the guided self-paced support model from Module 3 to the rest of the course where answer ladders make sense.

The goal is to help private learners check their work without removing the productive struggle of practice. The pattern should continue to be:

1. Try the exercise first.
2. Use hints if stuck.
3. Compare to expected outputs.
4. Review full solutions only after trying.

## Audience

The audience remains private, self-paced friends and family. They may not know whether an Excel formula, SQL query, chart, or pandas result is "close enough." The ladder should give them confidence while preserving a beginner-friendly tone.

## Scope Decision

Not every module should get the same kind of answer ladder.

- Module 0 is conceptual reading. It should not get a full answer ladder.
- Module 1 is setup. It already has `check_setup.py` and `GET_HELP.md`; it should not get exercise solutions.
- Module 2 has objective spreadsheet exercises. It should get hints, expected outputs, and written solutions.
- Module 3 already has the reference ladder. It should only be used as the pattern.
- Module 4 has objective SQL exercises. It should get hints, expected outputs, SQL solutions, and a Python + SQL solution example.
- Module 5 mixes objective chart exercises and open-ended Tableau/dashboard exercises. It should get code solutions for the matplotlib exercises and checklist-style solution guidance for Tableau/dashboard exercises.
- Module 6 has objective external-data exercises plus one open-ended dataset exercise. It should get hints, expected outputs, Python solutions for objective exercises, and guidance for the open-ended exercise.
- Module 7 is a capstone. It should get a rubric, write-up template, and example project, not a single "correct" solution.

## Recommended Approach

Use a module-local support-folder pattern. Each practice-heavy module gets folders beside its exercise file:

- `hints/`
- `expected_outputs/`
- `solutions/`

Open-ended project work uses more descriptive names when "solution" would imply a single correct answer:

- `rubric.md`
- `writeup_template.md`
- `example_project/`

This keeps learners in the module they are already working in and matches the Module 3 pattern.

## Alternatives Considered

### Centralized `solutions/` Directory

A single repo-level `solutions/` folder would make support files easy to find, but it would separate help from the lesson context. Beginners are more likely to lose their place.

### Inline Hints And Answers

Keeping everything inside each exercise file would reduce file count, but it makes accidental answer-peeking too easy and makes exercise files long.

### Module-Local Ladder

This is the recommended approach. It keeps support near the exercises, preserves the "try first" flow, and scales cleanly across modules.

## Module 2 Design

Module 2 should add:

- `02-spreadsheets/hints/lesson_06_hints.md`
- `02-spreadsheets/expected_outputs/lesson_06_expected_outputs.md`
- `02-spreadsheets/solutions/lesson_06_solutions.md`

The existing `lesson_06_exercises.md` should be updated to link the support ladder near the top and remove inline hints from the bottom.

Expected outputs should include objective spreadsheet answers:

- Total payroll: `4037000`
- Average salary: `84104.17`
- Employee count: `50`
- Sales department count: `11`
- Engineering salary spend: `1720000`
- First hire: Mark Hernandez
- Highest salary: Monica Cook
- Highest-paid HR employee: Michelle Thomas
- Furniture sales count: `24`
- Sales with revenue greater than `1000`: `20`
- Electronics North revenue: `16269.68`
- Revenue by region, average sale by product, category-by-region counts, top customer states by spend, and average orders by state.

For chart exercises, expected outputs should describe what the chart should show rather than requiring pixel-perfect images.

## Module 4 Design

Module 4 should add:

- `04-databases-and-sql/hints/lesson_07_hints.md`
- `04-databases-and-sql/expected_outputs/lesson_07_expected_outputs.md`
- `04-databases-and-sql/solutions/lesson_07_solutions.sql`
- `04-databases-and-sql/solutions/lesson_07_python_sql_solution.py`

The existing `lesson_07_exercises.md` should link to the ladder and remove the inline `<details>` hints.

Expected outputs should match the SQL Server setup data in `00_setup_database.sql`, not the larger CSV files. This matters because the SQL module uses its own inserted sample data.

The SQL solution file should include all eight SQL exercise solutions. The Python + SQL solution should mirror Exercise 9 and use the same connection assumptions as `lesson_06_python_and_sql.py`.

## Module 5 Design

Module 5 should add:

- `05-visualization/hints/lesson_10_hints.md`
- `05-visualization/expected_outputs/lesson_10_expected_outputs.md`
- `05-visualization/solutions/lesson_10_matplotlib_solutions.py`
- `05-visualization/solutions/lesson_10_tableau_solution_guide.md`

The existing `lesson_10_exercises.md` should link to the ladder and remove inline hints.

The matplotlib solution script should create the first five exercise charts and save them to an exercise-specific output folder such as `05-visualization/exercise_outputs/`. That folder should be ignored by git.

Expected outputs should verify:

- Chart file names.
- Core values used in each chart.
- Required chart features such as titles, labels, markers, and saved PNG files.

The Tableau guide should be checklist-style because dashboard construction is partly visual and cannot be fully verified by a script.

## Module 6 Design

Module 6 should add:

- `06-real-world-data/hints/05_hints.md`
- `06-real-world-data/expected_outputs/05_expected_outputs.md`
- `06-real-world-data/solutions/05_solutions.py`

The existing `05_exercises.md` should be corrected from `# Module 4 Exercises` to `# Module 6 Exercises`, link to the ladder, and remove inline hints.

Expected outputs should cover objective exercises:

- Titanic dataset shape: `891` rows and `12` columns.
- Titanic survival percentage: about `38.38%`.
- Titanic average age: about `29.70`.
- Titanic columns with missing values: `3`.
- Tips average tip: about `3.00`.
- Highest average tip day: `Sun`.
- Dinner average tip is higher than lunch.
- Iris average petal length by species.
- Widest average sepal width species: `setosa`.

Exercise 4 is open-ended, so the solution should provide a worked example and a checklist, not a single expected answer.

## Module 7 Design

Module 7 should not get a "solution ladder" because the capstone has many valid outcomes.

Instead, add:

- `07-capstone/rubric.md`
- `07-capstone/writeup_template.md`
- `07-capstone/example_project/README.md`
- `07-capstone/example_project/titanic_example.py`

The Module 7 README and project guide should link these files.

The example project should use an included dataset and produce a clear, small completed analysis. The rubric should define "good enough to finish" so learners do not over-polish forever.

## File Naming Rules

Use the existing lesson number in support files:

- `lesson_06_*` for Module 2 exercises.
- `lesson_07_*` for Module 4 exercises.
- `lesson_10_*` for Module 5 exercises.
- `05_*` for Module 6 exercises, matching the current file name.

This preserves local naming patterns and avoids a broad file rename.

## Error Handling And Learner Flow

Each exercise file should put the support ladder before the exercises:

1. Hints if stuck.
2. Expected outputs to check your answer.
3. Full solution after trying.

Solution scripts should:

- Use paths relative to the script file.
- Avoid modifying source datasets.
- Print clear section headings.
- Save generated exercise outputs to ignored folders when needed.

## Testing And Verification

Implementation should verify:

- Python solution scripts compile.
- Python solution scripts run from the repo root.
- Expected output values match current datasets or SQL setup data.
- New Markdown links point to existing files.
- Generated exercise output folders are ignored by `.gitignore`.
- `python -m compileall -q .` passes.
- Existing `check_setup.py` tests still pass.

Manual review is still needed for Excel, SQL Server, Tableau, and capstone guidance because those workflows cannot be fully verified in a simple unit test.

## Non-Goals

- Do not create a web app, LMS, or notebook version.
- Do not make learners submit answers to an autograder.
- Do not require SQL Server or Tableau to run basic repository verification.
- Do not force pixel-perfect visualization outputs.
- Do not replace the productive practice of trying exercises first.

## Future Extensions

After the ladders are added, future work can add:

- A Markdown link checker.
- Dataset validation.
- Expected-output blocks inside lesson files, not just exercise files.
- Optional check-understanding questions for Modules 0 and 1.

