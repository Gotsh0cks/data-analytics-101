# Repo Overview for AI Agents

## What This Repo Is

`data-analytics-101` is a beginner-friendly data analytics course built for private, self-paced learners. It is intended for friends and family, not a public MOOC or enterprise training product.

The course teaches practical analytics skills in this sequence:

1. What data analytics is.
2. Local tool setup.
3. Spreadsheets and Excel.
4. Python with pandas.
5. SQL Server and T-SQL.
6. Visualization with matplotlib, seaborn, and Tableau Public.
7. Real-world datasets.
8. A capstone project.

## Design Intent

The course should reduce intimidation. A learner should always know:

- Where to start.
- What file to open next.
- What command or action to run.
- What successful output looks like.
- How to recover when something goes wrong.

The best improvements are usually small: clearer instructions, expected outputs, path fixes, setup checks, solution keys, rubrics, and better signposting.

## Current Structure

- `README.md`: top-level course entry point and navigation.
- `00-what-is-data-analytics/`: concepts, tools, careers.
- `01-setting-up/`: Python, VS Code, SQL Server, Tableau Public, first script, common errors.
- `02-spreadsheets/`: Excel basics, formulas, sorting, filtering, pivot tables, charts, exercises.
- `03-data-analysis/`: pandas lessons and exercises.
- `04-databases-and-sql/`: SQL Server setup script, T-SQL lessons, Python + SQL.
- `05-visualization/`: matplotlib, seaborn, Tableau, generated chart assets.
- `06-real-world-data/`: public dataset discovery, download scripts, exploration.
- `07-capstone/`: final project guide, example questions, project template.
- `cheatsheets/`: printable quick references.
- `data/`: course datasets, Excel files, external datasets, Tableau-ready files.

## Audience Assumptions

- Learners may not know what GitHub, Markdown, terminal, PATH, packages, or folders mean.
- Learners may paste commands exactly as written.
- Learners may run scripts from the wrong directory unless the lesson is explicit.
- Learners benefit from reassurance, but they also need precise steps.

## Technical Assumptions

- Windows 10 or 11 is the primary operating system.
- Python is installed locally.
- VS Code is the home base.
- SQL lessons assume SQL Server / T-SQL.
- Tableau lessons assume Tableau Public.
- Excel is preferred, but free spreadsheet alternatives may be mentioned where appropriate.

## Stability Risks

- Relative file paths in lesson scripts can fail when run from a different working directory.
- Unpinned dependencies may change behavior over time.
- Module numbers and cross-references can drift as files move.
- Generated assets can become stale if source scripts change.
- External dataset URLs may break.
- SQL Server and Tableau instructions may become outdated as those products change.

## Non-Goals

Avoid these unless the user explicitly asks:

- Turning the repo into a full web app or LMS.
- Replacing Markdown lessons with notebooks.
- Adding heavy build systems.
- Making the course platform-neutral at the cost of beginner clarity.
- Refactoring all modules at once.

