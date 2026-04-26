# Answer Ladder Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend the hints -> expected outputs -> solutions support ladder to the practice-heavy modules where it fits, and add capstone completion support instead of a single answer key.

**Architecture:** Use module-local `hints/`, `expected_outputs/`, and `solutions/` folders beside existing exercise files. Preserve Module 3 as the reference pattern, adapt the pattern for Excel, SQL, visualization, real-world data, and use rubric/example/template support for the capstone.

**Tech Stack:** Markdown, Python standard library, pandas, matplotlib, seaborn, T-SQL, existing CSV/XLSX datasets, PowerShell-compatible verification commands.

---

## File Structure

- Modify: `.gitignore` - already includes Python caches and planned local output folders.
- Create: `02-spreadsheets/hints/lesson_06_hints.md`
- Create: `02-spreadsheets/expected_outputs/lesson_06_expected_outputs.md`
- Create: `02-spreadsheets/solutions/lesson_06_solutions.md`
- Modify: `02-spreadsheets/lesson_06_exercises.md`
- Create: `04-databases-and-sql/hints/lesson_07_hints.md`
- Create: `04-databases-and-sql/expected_outputs/lesson_07_expected_outputs.md`
- Create: `04-databases-and-sql/solutions/lesson_07_solutions.sql`
- Create: `04-databases-and-sql/solutions/lesson_07_python_sql_solution.py`
- Modify: `04-databases-and-sql/lesson_07_exercises.md`
- Create: `05-visualization/hints/lesson_10_hints.md`
- Create: `05-visualization/expected_outputs/lesson_10_expected_outputs.md`
- Create: `05-visualization/solutions/lesson_10_matplotlib_solutions.py`
- Create: `05-visualization/solutions/lesson_10_tableau_solution_guide.md`
- Modify: `05-visualization/lesson_10_exercises.md`
- Create: `06-real-world-data/hints/05_hints.md`
- Create: `06-real-world-data/expected_outputs/05_expected_outputs.md`
- Create: `06-real-world-data/solutions/05_solutions.py`
- Modify: `06-real-world-data/05_exercises.md`
- Create: `07-capstone/rubric.md`
- Create: `07-capstone/writeup_template.md`
- Create: `07-capstone/example_project/README.md`
- Create: `07-capstone/example_project/titanic_example.py`
- Modify: `07-capstone/README.md`
- Modify: `07-capstone/01_project_guide.md`
- Modify: `progress_tracker.md`
- Modify: `docs/ai/improvement_backlog.md`

## Task 1: Module 2 Spreadsheet Answer Ladder

**Files:**
- Create: `02-spreadsheets/hints/lesson_06_hints.md`
- Create: `02-spreadsheets/expected_outputs/lesson_06_expected_outputs.md`
- Create: `02-spreadsheets/solutions/lesson_06_solutions.md`
- Modify: `02-spreadsheets/lesson_06_exercises.md`

- [ ] **Step 1: Check worktree**

Run: `git status --short`

Expected: clean worktree or only files assigned to this task.

- [ ] **Step 2: Create the Module 2 hints file**

Create `02-spreadsheets/hints/lesson_06_hints.md` with a hint section for each of the five exercises. Preserve the current inline hint content, expand it slightly for beginners, and do not include final answers in this file.

Required hint topics:

- Exercise 1: `SUM`, `AVERAGE`, `COUNTA` or row count, `COUNTIF`, `SUMIF`.
- Exercise 2: single-column sort, salary descending sort, multi-level department then salary sort.
- Exercise 3: turn on filters, count visible rows, use status bar or subtotal/SUM on visible filtered data.
- Exercise 4: pivot tables with Rows, Columns, Values, Sum, Average, and Count.
- Exercise 5: create pivot summaries before charts, then add titles, labels, and clean formatting.

- [ ] **Step 3: Create the Module 2 expected outputs file**

Create `02-spreadsheets/expected_outputs/lesson_06_expected_outputs.md` with these exact objective answers:

```text
Exercise 1:
Total payroll: 4,037,000
Average salary: 84,104.17
Employee count: 50
Sales employees: 11
Engineering salary spend: 1,720,000

Exercise 2:
First hire: Mark Hernandez
Highest salary: Monica Cook
Highest-paid HR employee: Michelle Thomas

Exercise 3:
Furniture sales: 24
Sales where revenue > 1,000: 20
Electronics North total revenue: 16,269.68

Exercise 4:
Revenue by region:
North 22,819.07
South 21,008.90
West 15,619.18
East 14,829.03

Average sale by product:
Laptop 2,384.59
Standing Desk 824.98
Monitor 729.15
Desk Chair 699.98
Keyboard 461.48
Webcam 329.96
Mouse 272.05
Headset 223.60

Category by region counts:
Accessories: East 11, North 10, South 10, West 9
Electronics: East 9, North 11, South 10, West 9
Furniture: East 6, North 6, South 6, West 6

Highest total customer spending state: TX, 24,328.74
Highest average orders per state: MN, 43.00
```

For Exercise 5, describe expected chart features instead of pixel-perfect output:

- Column chart shows total revenue by region, sorted highest to lowest.
- Line chart shows revenue over time by month.
- Pie chart shows revenue share by category.
- Each chart has a descriptive title and readable labels.

- [ ] **Step 4: Create the Module 2 written solutions file**

Create `02-spreadsheets/solutions/lesson_06_solutions.md` with a worked solution for each exercise. Include exact formulas for Exercise 1:

```text
=SUM(F2:F51)
=AVERAGE(F2:F51)
=COUNTA(A2:A51)
=COUNTIF(D2:D51,"Sales")
=SUMIF(D2:D51,"Engineering",F2:F51)
```

Include step-by-step instructions for sort, filter, pivot table, and chart exercises. Use the same expected values from Step 3.

- [ ] **Step 5: Update the Module 2 exercise file**

Modify `02-spreadsheets/lesson_06_exercises.md`:

- Add a `## Support Ladder` section near the top with links to hints, expected outputs, and solutions.
- Remove the current bottom `## Hints` section.
- Preserve all five exercise prompts.

Use this ladder text:

```markdown
## Support Ladder

Use these only after you have tried:

1. [Hints](hints/lesson_06_hints.md) if you are stuck.
2. [Expected outputs](expected_outputs/lesson_06_expected_outputs.md) to check your answers.
3. [Full written solutions](solutions/lesson_06_solutions.md) after you have tried and compared your work.
```

- [ ] **Step 6: Verify links and commit**

Run:

```powershell
$paths = @(
  '02-spreadsheets/hints/lesson_06_hints.md',
  '02-spreadsheets/expected_outputs/lesson_06_expected_outputs.md',
  '02-spreadsheets/solutions/lesson_06_solutions.md'
)
foreach ($path in $paths) {
  if (-not (Test-Path -LiteralPath $path)) { throw "Missing $path" }
}
```

Expected: no output and exit code `0`.

Commit:

```bash
git add 02-spreadsheets/lesson_06_exercises.md 02-spreadsheets/hints/lesson_06_hints.md 02-spreadsheets/expected_outputs/lesson_06_expected_outputs.md 02-spreadsheets/solutions/lesson_06_solutions.md
git commit -m "docs: add module 2 answer ladder"
```

## Task 2: Module 4 SQL Answer Ladder

**Files:**
- Create: `04-databases-and-sql/hints/lesson_07_hints.md`
- Create: `04-databases-and-sql/expected_outputs/lesson_07_expected_outputs.md`
- Create: `04-databases-and-sql/solutions/lesson_07_solutions.sql`
- Create: `04-databases-and-sql/solutions/lesson_07_python_sql_solution.py`
- Modify: `04-databases-and-sql/lesson_07_exercises.md`

- [ ] **Step 1: Create the SQL hints file**

Move the current inline `<details>` hints from `lesson_07_exercises.md` into `04-databases-and-sql/hints/lesson_07_hints.md`. Keep one section per exercise, including Exercise 9.

- [ ] **Step 2: Create the SQL expected outputs file**

Create `04-databases-and-sql/expected_outputs/lesson_07_expected_outputs.md` using the SQL setup data from `00_setup_database.sql`. Include these exact answer anchors:

```text
Exercise 1 Sales employees:
Sarah Johnson, James Wilson, Jennifer Anderson, Kevin Clark, Laura King

Exercise 2 top 5 salaries:
Maria Garcia 115000.00
Laura King 105000.00
Robert Taylor 98000.00
Brian Robinson 95000.00
Michael Chen 92000.00

Exercise 3 total revenue by product:
Laptop 7999.92
Monitor 3149.91
Desk Chair 2999.88
Standing Desk 1799.97
Keyboard 1279.84
Webcam 909.87
Notebook Pack 584.55
Pen Set 404.55

Exercise 4 customer signups by year:
2022 5
2023 8
2024 7

Exercise 5 company average salary:
74000.00

Exercise 6 region transaction counts:
South 6
East 5
North 5
West 4

Exercise 7 highest average salary department:
Engineering 89000.00

Exercise 8 products never sold in West:
Keyboard
Notebook Pack
Standing Desk
Webcam
```

- [ ] **Step 3: Create the SQL solution file**

Create `04-databases-and-sql/solutions/lesson_07_solutions.sql` with executable T-SQL solutions for Exercises 1-8.

The file must start with:

```sql
USE DataAnalytics101;
GO
```

Include these query patterns:

```sql
SELECT first_name, last_name, job_title, salary
FROM Employees
WHERE department = 'Sales';

SELECT TOP 5 first_name, last_name, department, salary
FROM Employees
ORDER BY salary DESC;

SELECT product, SUM(revenue) AS total_revenue
FROM Sales
GROUP BY product
ORDER BY total_revenue DESC;

SELECT YEAR(signup_date) AS signup_year, COUNT(*) AS customer_count
FROM Customers
GROUP BY YEAR(signup_date)
ORDER BY signup_year;

SELECT first_name, last_name, department, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees)
ORDER BY salary DESC;

SELECT region, COUNT(*) AS transaction_count
FROM Sales
GROUP BY region
ORDER BY transaction_count DESC;

WITH DepartmentAverages AS (
    SELECT department, AVG(salary) AS avg_salary
    FROM Employees
    GROUP BY department
)
SELECT TOP 1 department, avg_salary
FROM DepartmentAverages
ORDER BY avg_salary DESC;

SELECT DISTINCT product
FROM Sales
WHERE product NOT IN (
    SELECT DISTINCT product
    FROM Sales
    WHERE region = 'West'
)
ORDER BY product;
```

- [ ] **Step 4: Create the Python + SQL solution file**

Create `04-databases-and-sql/solutions/lesson_07_python_sql_solution.py`. It should mirror the connection pattern from `lesson_06_python_and_sql.py`, query total revenue by category, print the DataFrame, and save a chart to `04-databases-and-sql/solutions/python_sql_revenue_by_category.png`.

The script should catch missing `pyodbc` and SQL connection failures with beginner-friendly messages. It may require a live SQL Server connection, so final verification can compile it without running it.

- [ ] **Step 5: Update the SQL exercise file**

Modify `04-databases-and-sql/lesson_07_exercises.md`:

- Add a `## Support Ladder` section near the top.
- Link hints, expected outputs, SQL solutions, and Python + SQL solution.
- Remove the inline `<details>` hints.
- Preserve all exercise prompts.

- [ ] **Step 6: Verify and commit**

Run:

```powershell
$paths = @(
  '04-databases-and-sql/hints/lesson_07_hints.md',
  '04-databases-and-sql/expected_outputs/lesson_07_expected_outputs.md',
  '04-databases-and-sql/solutions/lesson_07_solutions.sql',
  '04-databases-and-sql/solutions/lesson_07_python_sql_solution.py'
)
foreach ($path in $paths) {
  if (-not (Test-Path -LiteralPath $path)) { throw "Missing $path" }
}
```

Run: `python -m py_compile 04-databases-and-sql/solutions/lesson_07_python_sql_solution.py`

Expected: no output and exit code `0`.

Commit:

```bash
git add 04-databases-and-sql/lesson_07_exercises.md 04-databases-and-sql/hints/lesson_07_hints.md 04-databases-and-sql/expected_outputs/lesson_07_expected_outputs.md 04-databases-and-sql/solutions/lesson_07_solutions.sql 04-databases-and-sql/solutions/lesson_07_python_sql_solution.py
git commit -m "docs: add module 4 answer ladder"
```

## Task 3: Module 5 Visualization Answer Ladder

**Files:**
- Create: `05-visualization/hints/lesson_10_hints.md`
- Create: `05-visualization/expected_outputs/lesson_10_expected_outputs.md`
- Create: `05-visualization/solutions/lesson_10_matplotlib_solutions.py`
- Create: `05-visualization/solutions/lesson_10_tableau_solution_guide.md`
- Modify: `05-visualization/lesson_10_exercises.md`

- [ ] **Step 1: Create visualization hints**

Create `05-visualization/hints/lesson_10_hints.md` with sections for all eight exercises. Move the existing inline hints into the file and expand them with beginner-friendly reminders.

- [ ] **Step 2: Create visualization expected outputs**

Create `05-visualization/expected_outputs/lesson_10_expected_outputs.md` with:

- Required file names for Exercises 1-5.
- Average salary by department values from Module 3 expected outputs.
- Department counts from Module 3 expected outputs.
- A note that customer signup line chart should have month on the x-axis and count on the y-axis.
- A checklist for Tableau dashboard requirements in Exercises 6-8.

- [ ] **Step 3: Create matplotlib solution script**

Create `05-visualization/solutions/lesson_10_matplotlib_solutions.py`.

The script should:

- Use `matplotlib.use("Agg")`.
- Read `data/employees.csv` and `data/customers.csv` using paths relative to the script file.
- Create output folder `05-visualization/exercise_outputs/`.
- Save these files:
  - `exercise_01_salary_by_dept.png`
  - `exercise_02_employees_pie.png`
  - `exercise_03_signups_per_month.png`
  - `exercise_04_salary_vs_tenure.png`
  - `exercise_05_presentation_ready.png`
- Print the output paths after saving.

Include this deterministic tenure line:

```python
reference_date = pd.Timestamp.today().normalize()
employees["years_since_hire"] = (reference_date - employees["hire_date"]).dt.days / 365.25
```

- [ ] **Step 4: Create Tableau solution guide**

Create `05-visualization/solutions/lesson_10_tableau_solution_guide.md` with checklist-style guidance for Exercises 6-8. Include expected dashboard components, filters, titles, and formatting checks. Do not imply there is one pixel-perfect dashboard.

- [ ] **Step 5: Update Module 5 exercises**

Modify `05-visualization/lesson_10_exercises.md`:

- Add a `## Support Ladder` section near the top.
- Link hints, expected outputs, matplotlib solution script, and Tableau solution guide.
- Remove the bottom inline hints.
- Preserve all eight exercise prompts.

- [ ] **Step 6: Verify and commit**

Run:

```powershell
$paths = @(
  '05-visualization/hints/lesson_10_hints.md',
  '05-visualization/expected_outputs/lesson_10_expected_outputs.md',
  '05-visualization/solutions/lesson_10_matplotlib_solutions.py',
  '05-visualization/solutions/lesson_10_tableau_solution_guide.md'
)
foreach ($path in $paths) {
  if (-not (Test-Path -LiteralPath $path)) { throw "Missing $path" }
}
```

Run: `python 05-visualization/solutions/lesson_10_matplotlib_solutions.py`

Expected: exit code `0`; five PNG files are created in `05-visualization/exercise_outputs/`.

Run: `git check-ignore 05-visualization/exercise_outputs/exercise_01_salary_by_dept.png`

Expected: path is ignored by `.gitignore`.

Remove generated `05-visualization/exercise_outputs/` after verification or leave it untracked and ignored.

Commit:

```bash
git add 05-visualization/lesson_10_exercises.md 05-visualization/hints/lesson_10_hints.md 05-visualization/expected_outputs/lesson_10_expected_outputs.md 05-visualization/solutions/lesson_10_matplotlib_solutions.py 05-visualization/solutions/lesson_10_tableau_solution_guide.md
git commit -m "docs: add module 5 answer ladder"
```

## Task 4: Module 6 Real-World Data Answer Ladder

**Files:**
- Create: `06-real-world-data/hints/05_hints.md`
- Create: `06-real-world-data/expected_outputs/05_expected_outputs.md`
- Create: `06-real-world-data/solutions/05_solutions.py`
- Modify: `06-real-world-data/05_exercises.md`

- [ ] **Step 1: Create Module 6 hints**

Create `06-real-world-data/hints/05_hints.md` by moving and expanding the current inline hints. Include guidance for Exercise 4 as a checklist for exploring any dataset.

- [ ] **Step 2: Create Module 6 expected outputs**

Create `06-real-world-data/expected_outputs/05_expected_outputs.md` with these objective values:

```text
Titanic:
Rows: 891
Columns: 12
Survival percentage: 38.38%
Average age: 29.70
Columns with missing values: 3
Missing columns: Age 177, Cabin 687, Embarked 2

Tips:
Average tip: 3.00
Highest average tip day: Sun, 3.26
Dinner average tip: 3.10
Lunch average tip: 2.73

Iris:
Average petal length:
setosa 1.46
versicolor 4.26
virginica 5.55

Widest average sepal width:
setosa 3.43
```

Exercise 4 expected output should be a checklist:

- shape printed
- column names printed
- data types printed
- missing values checked
- three answerable questions written down

- [ ] **Step 3: Create Module 6 solution script**

Create `06-real-world-data/solutions/05_solutions.py`.

The script should:

- Read `data/external/titanic.csv`, `tips.csv`, and `iris.csv` using robust paths.
- Print section headings.
- Print the objective answers from Step 2.
- Include a final printed checklist for Exercise 4.

Use `round(2)` for displayed percentages and averages.

- [ ] **Step 4: Update Module 6 exercise file**

Modify `06-real-world-data/05_exercises.md`:

- Correct heading to `# Module 6 Exercises`.
- Add support ladder links.
- Remove bottom inline hints.
- Preserve all four exercise prompts.

- [ ] **Step 5: Verify and commit**

Run: `python 06-real-world-data/solutions/05_solutions.py`

Expected: output includes `Rows: 891`, `Survival percentage: 38.38%`, `Average tip: 3.00`, `Highest average tip day: Sun`, and `Widest average sepal width species: setosa`.

Commit:

```bash
git add 06-real-world-data/05_exercises.md 06-real-world-data/hints/05_hints.md 06-real-world-data/expected_outputs/05_expected_outputs.md 06-real-world-data/solutions/05_solutions.py
git commit -m "docs: add module 6 answer ladder"
```

## Task 5: Module 7 Capstone Support

**Files:**
- Create: `07-capstone/rubric.md`
- Create: `07-capstone/writeup_template.md`
- Create: `07-capstone/example_project/README.md`
- Create: `07-capstone/example_project/titanic_example.py`
- Modify: `07-capstone/README.md`
- Modify: `07-capstone/01_project_guide.md`

- [ ] **Step 1: Create capstone rubric**

Create `07-capstone/rubric.md` with beginner-friendly criteria:

- Dataset chosen and loaded.
- Three to five focused questions.
- Basic cleaning or explanation of why cleaning was not needed.
- At least three findings.
- At least three charts.
- Optional SQL step attempted or skipped with a short explanation.
- Tableau dashboard or alternative presentation.
- Three to five sentence summary.

Use levels:

- Finished
- Strong
- Stretch

Define "Finished" as good enough to stop polishing.

- [ ] **Step 2: Create write-up template**

Create `07-capstone/writeup_template.md` with fillable sections:

- Project title
- Dataset used
- Questions
- Cleaning notes
- Key findings
- Charts created
- Dashboard link or screenshot note
- What I would improve next

- [ ] **Step 3: Create example project README**

Create `07-capstone/example_project/README.md` describing the Titanic example project and how to run:

```bash
python 07-capstone/example_project/titanic_example.py
```

Explain that outputs are saved to `07-capstone/example_project/outputs/`, which is ignored by git.

- [ ] **Step 4: Create Titanic example project script**

Create `07-capstone/example_project/titanic_example.py`.

The script should:

- Use `matplotlib.use("Agg")`.
- Read `data/external/titanic.csv`.
- Fill missing `Age` with median age for analysis.
- Answer three questions:
  - overall survival rate
  - survival rate by passenger class
  - survival rate by sex
- Save at least three charts to `07-capstone/example_project/outputs/`.
- Print a short summary.

- [ ] **Step 5: Link capstone support files**

Modify `07-capstone/README.md` and `07-capstone/01_project_guide.md` to link:

- `rubric.md`
- `writeup_template.md`
- `example_project/README.md`

Keep wording clear that the example is a model, not the only correct project.

- [ ] **Step 6: Verify and commit**

Run: `python 07-capstone/example_project/titanic_example.py`

Expected: exit code `0`, summary printed, output images created under ignored `07-capstone/example_project/outputs/`.

Run: `git check-ignore 07-capstone/example_project/outputs/survival_by_class.png`

Expected: path is ignored by `.gitignore`.

Commit:

```bash
git add 07-capstone/README.md 07-capstone/01_project_guide.md 07-capstone/rubric.md 07-capstone/writeup_template.md 07-capstone/example_project/README.md 07-capstone/example_project/titanic_example.py
git commit -m "docs: add capstone completion support"
```

## Task 6: Progress Tracker And Backlog Update

**Files:**
- Modify: `progress_tracker.md`
- Modify: `docs/ai/improvement_backlog.md`

- [ ] **Step 1: Update progress tracker**

Modify `progress_tracker.md` so Modules 2, 4, 5, and 6 include support-ladder checklist items matching Module 3:

- tried exercises
- used hints only after trying
- compared expected outputs
- reviewed solutions after trying

Modify Module 7 checklist to include:

- reviewed rubric
- used write-up template
- compared against example project only after drafting own project

- [ ] **Step 2: Update improvement backlog**

Modify `docs/ai/improvement_backlog.md`:

- Move completed answer-ladder items out of Priority 1 wording.
- Add future items for lesson-level expected outputs, Markdown link checker, dataset validation, and optional check-understanding questions.
- Keep any still-open work explicit.

- [ ] **Step 3: Commit tracker and backlog**

Run:

```bash
git add progress_tracker.md docs/ai/improvement_backlog.md
git commit -m "docs: update ladder progress tracking"
```

## Task 7: Final Verification

**Files:**
- Verify all files created or modified by Tasks 1-6.

- [ ] **Step 1: Run Python tests**

Run: `python -m unittest tests.test_check_setup -v`

Expected: 7 tests pass.

- [ ] **Step 2: Run setup checker**

Run: `python check_setup.py`

Expected: exit code `0`.

- [ ] **Step 3: Compile Python files**

Run: `python -m compileall -q .`

Expected: no output and exit code `0`.

- [ ] **Step 4: Run solution scripts that do not require SQL Server or Tableau**

Run:

```bash
python 03-data-analysis/solutions/lesson_05_solutions.py
python 05-visualization/solutions/lesson_10_matplotlib_solutions.py
python 06-real-world-data/solutions/05_solutions.py
python 07-capstone/example_project/titanic_example.py
```

Expected: all exit `0`.

- [ ] **Step 5: Compile SQL-dependent Python solution**

Run:

```bash
python -m py_compile 04-databases-and-sql/solutions/lesson_07_python_sql_solution.py
```

Expected: no output and exit code `0`.

- [ ] **Step 6: Check support paths**

Run:

```powershell
$paths = @(
  '02-spreadsheets/hints/lesson_06_hints.md',
  '02-spreadsheets/expected_outputs/lesson_06_expected_outputs.md',
  '02-spreadsheets/solutions/lesson_06_solutions.md',
  '04-databases-and-sql/hints/lesson_07_hints.md',
  '04-databases-and-sql/expected_outputs/lesson_07_expected_outputs.md',
  '04-databases-and-sql/solutions/lesson_07_solutions.sql',
  '04-databases-and-sql/solutions/lesson_07_python_sql_solution.py',
  '05-visualization/hints/lesson_10_hints.md',
  '05-visualization/expected_outputs/lesson_10_expected_outputs.md',
  '05-visualization/solutions/lesson_10_matplotlib_solutions.py',
  '05-visualization/solutions/lesson_10_tableau_solution_guide.md',
  '06-real-world-data/hints/05_hints.md',
  '06-real-world-data/expected_outputs/05_expected_outputs.md',
  '06-real-world-data/solutions/05_solutions.py',
  '07-capstone/rubric.md',
  '07-capstone/writeup_template.md',
  '07-capstone/example_project/README.md',
  '07-capstone/example_project/titanic_example.py'
)
foreach ($path in $paths) {
  if (-not (Test-Path -LiteralPath $path)) { throw "Missing $path" }
}
```

Expected: no output and exit code `0`.

- [ ] **Step 7: Check ignored generated outputs**

Run:

```bash
git check-ignore 05-visualization/exercise_outputs/exercise_01_salary_by_dept.png
git check-ignore 07-capstone/example_project/outputs/survival_by_class.png
```

Expected: both paths are ignored.

- [ ] **Step 8: Remove generated caches and review status**

Remove generated `__pycache__/` directories inside the repo if Python verification created them.

Run: `git status --short`

Expected: clean worktree after all implementation commits.

## Self-Review Notes

- Modules 2, 4, 5, and 6 get true answer ladders.
- Module 3 remains the already-implemented reference pattern.
- Module 7 gets capstone completion support instead of a false single answer.
- Modules 0 and 1 are intentionally excluded from answer ladders.
- `.gitignore` already covers Python caches and generated solution output folders.
- SQL Server and Tableau are not required for final automated verification.

