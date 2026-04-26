# Guided Confidence Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a lightweight guided support layer that helps private, self-paced learners get unstuck during setup and check Module 3 exercise answers through hints, expected outputs, and full solutions.

**Architecture:** Add learner-facing Markdown support files at the repo root, a small standard-library setup checker, and a Module 3 answer ladder beside the existing pandas exercise file. Keep the existing course structure intact and pilot the answer ladder in Module 3 before expanding to later modules.

**Tech Stack:** Markdown, Python standard library, pandas for the Module 3 solution script, unittest for setup-checker tests, PowerShell-compatible commands.

---

## File Structure

- Create: `START_HERE.md` - friend/family-facing course entry point.
- Create: `progress_tracker.md` - learner-owned checklist with Markdown checkboxes.
- Create: `GET_HELP.md` - template for asking for help with enough context.
- Create: `check_setup.py` - setup checker for Python, packages, expected folders, and core data files.
- Create: `tests/__init__.py` - makes the test directory importable for `unittest`.
- Create: `tests/test_check_setup.py` - lightweight unit tests for setup-checker helper functions.
- Create: `03-data-analysis/hints/lesson_05_hints.md` - hints for existing Module 3 exercises.
- Create: `03-data-analysis/expected_outputs/lesson_05_expected_outputs.md` - expected answer values for existing Module 3 exercises.
- Create: `03-data-analysis/solutions/lesson_05_solutions.py` - runnable complete solution script.
- Modify: `README.md:95-99` and `README.md:121-127` - point learners to `START_HERE.md`, `progress_tracker.md`, and `GET_HELP.md`.
- Replace: `03-data-analysis/lesson_05_exercises.md` - correct heading to Module 3 and link to the answer ladder.

## Task 1: Add Learner Entry And Help Files

**Files:**
- Create: `START_HERE.md`
- Create: `progress_tracker.md`
- Create: `GET_HELP.md`
- Modify: `README.md:95-99`
- Modify: `README.md:121-127`

- [ ] **Step 1: Check current worktree**

Run: `git status --short`

Expected: no unrelated modified files. If unrelated files appear, stop and ask the user before editing.

- [ ] **Step 2: Create `START_HERE.md`**

Create `START_HERE.md` with this exact content:

````markdown
# Start Here

Welcome to Data Analytics 101. This course is for complete beginners, especially friends and family learning on their own.

You do not need programming experience. You only need a Windows computer, an internet connection, and a willingness to try things even when they feel unfamiliar.

## What This Course Teaches

You will learn how to:

1. Understand what data analytics is.
2. Use spreadsheets for formulas, sorting, filtering, pivot tables, and charts.
3. Use Python and pandas to work with data.
4. Use SQL Server to query databases.
5. Create charts with Python.
6. Build dashboards with Tableau Public.
7. Find real-world datasets.
8. Complete a small capstone project.

## The Best Path Through The Course

Follow the numbered folders in order:

1. `00-what-is-data-analytics`
2. `01-setting-up`
3. `02-spreadsheets`
4. `03-data-analysis`
5. `04-databases-and-sql`
6. `05-visualization`
7. `06-real-world-data`
8. `07-capstone`

Each folder has a `README.md` file that tells you what to do next.

## First-Time Setup

Start with these steps:

1. Read the main `README.md`.
2. Open `progress_tracker.md` so you can check off your progress.
3. Complete Module 0.
4. Complete Module 1.
5. After installing Python and the required packages, run this command from the main course folder:

```bash
python check_setup.py
```

If the setup checker prints `[OK]` for the required checks, keep going.

If it prints `[FIX]`, read the message next to it. If you are not sure what to do, open `GET_HELP.md` and use the template there.

## How To Read Lesson Files

Lesson files use Markdown. Markdown is just text with simple formatting.

You can read lessons:

- On GitHub by clicking the `.md` file.
- In VS Code by opening a `.md` file and pressing `Ctrl+Shift+V`.
- In Notepad if you only need the plain text.

After Module 1, VS Code is the recommended place to read lessons and run code.

## How To Use Exercise Support

Try each exercise on your own first. Getting stuck is part of learning.

For supported exercises, use this order:

1. Try the exercise.
2. Open the hints only if you are stuck.
3. Compare your result to the expected output.
4. Open the full solution only after you have tried.

Module 3 is the first module with this full support ladder.

## When You Get Stuck

Getting stuck does not mean you are bad at this. It usually means one small step, package, folder, or command needs attention.

When you need help:

1. Run `python check_setup.py`.
2. Open `GET_HELP.md`.
3. Copy the template.
4. Fill in what file you were on, what command you ran, and what happened.

That information makes it much easier to help you quickly.

## Keep Going

You do not need to understand everything perfectly before moving on. The goal is to practice the workflow, build confidence, and finish a small project you can explain in your own words.
````

- [ ] **Step 3: Create `progress_tracker.md`**

Create `progress_tracker.md` with this exact content:

```markdown
# Progress Tracker

Use this checklist to track your progress. In VS Code, you can edit this file and change `[ ]` to `[x]` when you finish something.

## Getting The Course Ready

- [ ] Downloaded or received the course files.
- [ ] Extracted the ZIP file if needed.
- [ ] Opened the main course folder.
- [ ] Read `START_HERE.md`.
- [ ] Read the main `README.md`.

## Module 0: What Is Data Analytics

- [ ] Read the Module 0 README.
- [ ] Read `01_what_is_data_analytics.md`.
- [ ] Read `02_common_tools_overview.md`.
- [ ] Read `03_careers_and_skills.md`.

## Module 1: Setting Up

- [ ] Read the Module 1 README.
- [ ] Installed Python.
- [ ] Installed VS Code.
- [ ] Installed the VS Code Python extension.
- [ ] Installed the VS Code SQL Server extension.
- [ ] Installed SQL Server Express.
- [ ] Installed Tableau Public.
- [ ] Ran your first script.
- [ ] Reviewed common errors.
- [ ] Ran `python check_setup.py`.

## Module 2: Spreadsheets

- [ ] Read the Module 2 README.
- [ ] Completed Lesson 1: Spreadsheet Basics.
- [ ] Completed Lesson 2: Formulas and Functions.
- [ ] Completed Lesson 3: Sorting and Filtering.
- [ ] Completed Lesson 4: Pivot Tables.
- [ ] Completed Lesson 5: Excel Charts.
- [ ] Tried the Module 2 exercises.

## Module 3: Data Analysis With Python

- [ ] Read the Module 3 README.
- [ ] Completed Lesson 1: Loading Data.
- [ ] Completed Lesson 2: Filtering and Sorting.
- [ ] Completed Lesson 3: Aggregations.
- [ ] Completed Lesson 4: Data Cleaning.
- [ ] Tried the Module 3 exercises.
- [ ] Used Module 3 hints only after trying.
- [ ] Compared your work to the expected outputs.
- [ ] Reviewed the full solution after trying.

## Module 4: Databases And SQL

- [ ] Read the Module 4 README.
- [ ] Ran the database setup script.
- [ ] Completed Lesson 1: SELECT and FROM.
- [ ] Completed Lesson 2: WHERE and ORDER BY.
- [ ] Completed Lesson 3: Aggregations.
- [ ] Completed Lesson 4: Joins.
- [ ] Completed Lesson 5: Subqueries and CTEs.
- [ ] Completed Lesson 6: Python and SQL.
- [ ] Tried the Module 4 exercises.

## Module 5: Visualization

- [ ] Read the Module 5 README.
- [ ] Completed matplotlib bar charts.
- [ ] Completed matplotlib line charts.
- [ ] Completed pie and scatter charts.
- [ ] Completed styling and polish.
- [ ] Prepared data for Tableau.
- [ ] Connected Tableau to data.
- [ ] Built a first Tableau chart.
- [ ] Built a Tableau dashboard.
- [ ] Published or saved your Tableau work.
- [ ] Tried the Module 5 exercises.

## Module 6: Real-World Data

- [ ] Read the Module 6 README.
- [ ] Read the dataset guide.
- [ ] Downloaded public datasets.
- [ ] Explored downloaded datasets.
- [ ] Tried the Module 6 exercises.

## Module 7: Capstone Project

- [ ] Read the Module 7 README.
- [ ] Chose a dataset.
- [ ] Wrote 3 to 5 questions.
- [ ] Explored the data.
- [ ] Cleaned the data.
- [ ] Analyzed the data with Python or SQL.
- [ ] Created at least 3 charts.
- [ ] Built a Tableau dashboard.
- [ ] Wrote a short summary of findings.
- [ ] Saved or shared the finished project.
```

- [ ] **Step 4: Create `GET_HELP.md`**

Create `GET_HELP.md` with this exact content:

````markdown
# Get Help

Getting stuck is normal. Most beginner problems come from one small detail: a folder, command, package, file name, or setup step.

Before asking for help, run this command from the main course folder:

```bash
python check_setup.py
```

If you still need help, copy the template below and fill it in.

## Help Request Template

```text
I need help with Data Analytics 101.

Module:
Lesson or file:

What I was trying to do:

The command I ran or step I tried:

What happened:

What I expected to happen:

Error message, if there was one:

Did I run python check_setup.py?

What did check_setup.py print?
```

## Tips For Copying Error Messages

- Copy the exact error text if you can.
- If copying is hard, send a screenshot.
- Include the command you ran right before the error appeared.
- Mention whether you are using GitHub, VS Code, or Notepad to read the lesson.

## Common Quick Checks

- Make sure you opened the main `data-analytics-101` folder in VS Code.
- Make sure you extracted the ZIP file before running scripts.
- Make sure the terminal is open inside VS Code.
- Make sure Python installed correctly by running `python --version`.
- Make sure packages installed by running `python -m pip install -r requirements.txt`.

You do not need to solve the problem before asking. The goal is to share enough context that someone can help you quickly.
````

- [ ] **Step 5: Update `README.md` getting-started block**

In `README.md`, replace lines 95-99 with this exact block:

```markdown
## Getting Started

**First time here?** Start with [START_HERE.md](START_HERE.md). It explains how to use this course, how to check your setup, and how to ask for help if you get stuck.

After that, begin with [Module 0 - What Is Data Analytics](00-what-is-data-analytics/).

Module 0 is just reading no installing or coding. It explains what data analytics is, what tools you will learn, and what kind of career it can lead to. Then Module 1 walks you through installing everything.
```

- [ ] **Step 6: Update `README.md` quick links**

In `README.md`, replace lines 121-127 with this exact block:

```markdown
## Quick Links

| Resource | What It Is |
|----------|-----------|
| [Start Here](START_HERE.md) | Friendly first stop for self-paced learners |
| [Progress Tracker](progress_tracker.md) | Checklist for tracking your course progress |
| [Get Help](GET_HELP.md) | Template for asking for help when you are stuck |
| [Cheatsheets](cheatsheets/) | Printable quick-reference sheets for Excel, pandas, SQL, matplotlib, Tableau |
| [Sample Data](data/) | The CSV files used throughout the course |
| [Module 0](00-what-is-data-analytics/) | First course module |
```

- [ ] **Step 7: Verify Task 1 Markdown links**

Run:

```powershell
$paths = @('START_HERE.md','progress_tracker.md','GET_HELP.md','README.md')
foreach ($path in $paths) {
  if (-not (Test-Path -LiteralPath $path)) { throw "Missing $path" }
}
```

Expected: no output and exit code `0`.

- [ ] **Step 8: Commit Task 1**

Run:

```bash
git add START_HERE.md progress_tracker.md GET_HELP.md README.md
git commit -m "docs: add learner guidance entry points"
```

Expected: commit succeeds with the four intended files.

## Task 2: Add Setup Checker With Lightweight Tests

**Files:**
- Create: `tests/__init__.py`
- Create: `tests/test_check_setup.py`
- Create: `check_setup.py`

- [ ] **Step 1: Create `tests/__init__.py`**

Create `tests/__init__.py` as an empty file.

- [ ] **Step 2: Write the failing setup-checker tests**

Create `tests/test_check_setup.py` with this exact content:

```python
import tempfile
import unittest
from pathlib import Path

import check_setup


class SetupCheckTests(unittest.TestCase):
    def test_format_result_includes_status_name_and_detail(self):
        result = check_setup.CheckResult("OK", "Python", "Version is available")
        self.assertEqual(check_setup.format_result(result), "[OK] Python: Version is available")

    def test_path_exists_reports_existing_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            data_file = root / "data" / "sales_data.csv"
            data_file.parent.mkdir()
            data_file.write_text("date,revenue\n2024-01-01,10\n", encoding="utf-8")

            result = check_setup.check_path(root, "data/sales_data.csv", "Sales data")

        self.assertEqual(result.status, "OK")
        self.assertEqual(result.name, "Sales data")

    def test_path_exists_reports_missing_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            result = check_setup.check_path(root, "data/sales_data.csv", "Sales data")

        self.assertEqual(result.status, "FIX")
        self.assertIn("Missing data/sales_data.csv", result.detail)

    def test_check_package_reports_missing_required_package(self):
        result = check_setup.check_package(
            "not_a_real_package_for_this_course",
            required=True,
            module_available_fn=lambda package_name: False,
        )

        self.assertEqual(result.status, "FIX")
        self.assertTrue(result.required)

    def test_check_working_directory_reports_wrong_folder(self):
        with tempfile.TemporaryDirectory() as root_dir, tempfile.TemporaryDirectory() as other_dir:
            result = check_setup.check_working_directory(Path(root_dir), Path(other_dir))

        self.assertEqual(result.status, "FIX")
        self.assertIn("Run this from the main course folder", result.detail)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run tests to confirm they fail before implementation**

Run: `python -m unittest tests.test_check_setup -v`

Expected: failure with `ModuleNotFoundError: No module named 'check_setup'`.

- [ ] **Step 4: Create `check_setup.py`**

Create `check_setup.py` with this exact content:

```python
from dataclasses import dataclass
from importlib.util import find_spec
from pathlib import Path
import platform
import sys


MIN_PYTHON = (3, 10)

REQUIRED_PACKAGES = [
    ("pandas", "Module 3 data analysis"),
    ("matplotlib", "Module 5 charts"),
    ("seaborn", "Module 5 chart styling"),
    ("openpyxl", "Module 2 Excel files"),
    ("requests", "Module 6 dataset downloads"),
]

LATER_PACKAGES = [
    ("pyodbc", "Module 4 Python and SQL Server"),
]

COURSE_FOLDERS = [
    "00-what-is-data-analytics",
    "01-setting-up",
    "02-spreadsheets",
    "03-data-analysis",
    "04-databases-and-sql",
    "05-visualization",
    "06-real-world-data",
    "07-capstone",
    "cheatsheets",
    "data",
]

CORE_DATA_FILES = [
    ("data/sales_data.csv", "Sales data"),
    ("data/employees.csv", "Employee data"),
    ("data/customers.csv", "Customer data"),
]


@dataclass(frozen=True)
class CheckResult:
    status: str
    name: str
    detail: str
    required: bool = True


def format_result(result):
    return f"[{result.status}] {result.name}: {result.detail}"


def module_available(package_name):
    return find_spec(package_name) is not None


def check_python_version():
    current = sys.version_info
    current_text = platform.python_version()
    minimum_text = ".".join(str(part) for part in MIN_PYTHON)
    if current >= MIN_PYTHON:
        return CheckResult("OK", "Python", f"Version {current_text} is installed")
    return CheckResult(
        "FIX",
        "Python",
        f"Version {current_text} is installed, but this course expects Python {minimum_text} or newer",
    )


def check_working_directory(root, cwd):
    root = root.resolve()
    cwd = cwd.resolve()
    if cwd == root:
        return CheckResult("OK", "Course folder", f"Running from {root}")
    return CheckResult(
        "FIX",
        "Course folder",
        f"Run this from the main course folder: {root}",
    )


def check_package(package_name, required=True, module_available_fn=module_available):
    if module_available_fn(package_name):
        return CheckResult("OK", package_name, "Package is installed", required=required)

    if required:
        return CheckResult(
            "FIX",
            package_name,
            "Package is missing. Run: python -m pip install -r requirements.txt",
            required=True,
        )

    return CheckResult(
        "LATER",
        package_name,
        "Not installed yet. You only need this later for SQL Server lessons.",
        required=False,
    )


def check_path(root, relative_path, name):
    path = root / relative_path
    if path.exists():
        return CheckResult("OK", name, f"Found {relative_path}")
    return CheckResult(
        "FIX",
        name,
        f"Missing {relative_path}. Confirm you extracted the full course folder.",
    )


def collect_results(root, cwd):
    results = [
        check_python_version(),
        check_working_directory(root, cwd),
    ]

    for folder in COURSE_FOLDERS:
        results.append(check_path(root, folder, f"Folder {folder}"))

    for relative_path, name in CORE_DATA_FILES:
        results.append(check_path(root, relative_path, name))

    for package_name, purpose in REQUIRED_PACKAGES:
        result = check_package(package_name, required=True)
        if result.status == "OK":
            results.append(CheckResult("OK", package_name, f"Installed for {purpose}"))
        else:
            results.append(result)

    for package_name, purpose in LATER_PACKAGES:
        result = check_package(package_name, required=False)
        if result.status == "OK":
            results.append(CheckResult("OK", package_name, f"Installed for {purpose}", required=False))
        else:
            results.append(result)

    return results


def print_next_steps(failure_count):
    print()
    if failure_count:
        print("Some required checks need attention.")
        print("Start with the [FIX] messages above.")
        print("If you are not sure what to do, open GET_HELP.md and copy the help template.")
    else:
        print("Core setup looks ready.")
        print("If you are early in the course, you can continue with Module 0 or Module 1.")
        print("Items marked [LATER] are only needed in later modules.")


def main():
    root = Path(__file__).resolve().parent
    cwd = Path.cwd()

    print("=" * 60)
    print("Data Analytics 101 Setup Check")
    print("=" * 60)
    print()

    results = collect_results(root, cwd)
    failure_count = 0

    for result in results:
        print(format_result(result))
        if result.required and result.status == "FIX":
            failure_count += 1

    print_next_steps(failure_count)
    return 1 if failure_count else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 5: Run setup-checker tests**

Run: `python -m unittest tests.test_check_setup -v`

Expected: all 5 tests pass and output includes `OK`.

- [ ] **Step 6: Run the setup checker**

Run: `python check_setup.py`

Expected: exit code `0` in a correctly configured environment. Output includes:

```text
Data Analytics 101 Setup Check
[OK] Python:
[OK] Course folder:
[OK] Sales data:
[OK] Employee data:
[OK] Customer data:
Core setup looks ready.
```

If `pyodbc` is missing, `[LATER] pyodbc` may appear and the command should still exit `0`.

- [ ] **Step 7: Commit Task 2**

Run:

```bash
git add check_setup.py tests/__init__.py tests/test_check_setup.py
git commit -m "feat: add course setup checker"
```

Expected: commit succeeds with setup checker and tests.

## Task 3: Add Module 3 Answer Ladder

**Files:**
- Create: `03-data-analysis/hints/lesson_05_hints.md`
- Create: `03-data-analysis/expected_outputs/lesson_05_expected_outputs.md`
- Create: `03-data-analysis/solutions/lesson_05_solutions.py`

- [ ] **Step 1: Create `03-data-analysis/hints/lesson_05_hints.md`**

Create `03-data-analysis/hints/lesson_05_hints.md` with this exact content:

````markdown
# Module 3 Exercise Hints

Try each exercise on your own before reading the hint. If the hint is enough to get you moving, go back to your own file and keep working.

## Exercise 1: Load and Inspect

Use `pd.read_csv()` to load `../data/employees.csv`.

Use `.head(10)` to see the first 10 rows.

Use `.shape` to get the number of rows and columns.

## Exercise 2: Employees Per Department

Select the `department` column.

Use `.value_counts()` to count each department. It sorts from most to least by default.

## Exercise 3: Average Salary by Department

Use `.groupby("department")["salary"].mean()`.

To see the highest average first, add `.sort_values(ascending=False)`.

To get only the department name with the highest average, use `.idxmax()`.

## Exercise 4: Filter by Hire Date

First convert the `hire_date` column:

```python
employees["hire_date"] = pd.to_datetime(employees["hire_date"])
```

Then filter rows where the date is after `"2022-01-01"`.

Use `len()` to count the filtered rows.

## Exercise 5: Find Missing Data

Use `.isnull().sum()` to count missing values in each column.

To show only columns with missing data:

```python
missing = employees.isnull().sum()
print(missing[missing > 0])
```

## Exercise 6: Top Customer State

Load `../data/customers.csv`.

Select the `state` column and use `.value_counts()`.

Use `.head(5)` to show only the top five states.
````

- [ ] **Step 2: Create `03-data-analysis/expected_outputs/lesson_05_expected_outputs.md`**

Create `03-data-analysis/expected_outputs/lesson_05_expected_outputs.md` with this exact content:

````markdown
# Module 3 Exercise Expected Outputs

Your formatting may look slightly different, but your answers should match these values.

## Exercise 1: Load and Inspect

The employee dataset has:

```text
50 rows
9 columns
```

The first row should be employee `E001`, James Mitchell, in Engineering.

## Exercise 2: Employees Per Department

Expected department counts:

```text
Engineering    16
Sales          11
Marketing       8
Finance         8
HR              6
```

The missing department value is not counted by `value_counts()` unless you ask pandas to include missing values.

## Exercise 3: Average Salary by Department

Expected averages, rounded to 2 decimals:

```text
Engineering    114666.67
Sales           80181.82
Finance         72142.86
Marketing       62250.00
HR              60833.33
```

The department with the highest average salary is:

```text
Engineering
```

## Exercise 4: Filter by Hire Date

Employees hired after January 1, 2022:

```text
15
```

The filtered results should include employees such as Emily Rodriguez, Laura Anderson, Rachel White, and Lauren Collins.

## Exercise 5: Find Missing Data

Columns with missing values:

```text
department    1
salary        2
```

All other columns should show `0` missing values.

## Exercise 6: Top Customer State

Top 5 customer states:

```text
CA    10
TX     8
AZ     4
FL     4
OH     3
```

California has the most customers.
````

- [ ] **Step 3: Create `03-data-analysis/solutions/lesson_05_solutions.py`**

Create `03-data-analysis/solutions/lesson_05_solutions.py` with this exact content:

```python
"""
Module 3 Exercise Solutions
===========================
Run this after trying the exercises yourself:

    python 03-data-analysis/solutions/lesson_05_solutions.py

This script reads the course data and prints complete answers for
the Module 3 pandas exercises.
"""

from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"


def print_section(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main():
    employees = pd.read_csv(DATA_DIR / "employees.csv")
    customers = pd.read_csv(DATA_DIR / "customers.csv")

    print_section("Exercise 1: Load and Inspect")
    print(employees.head(10).to_string(index=False))
    print()
    print(f"Rows: {employees.shape[0]}")
    print(f"Columns: {employees.shape[1]}")

    print_section("Exercise 2: Employees Per Department")
    department_counts = employees["department"].value_counts()
    print(department_counts.to_string())

    print_section("Exercise 3: Average Salary by Department")
    average_salary = employees.groupby("department")["salary"].mean().sort_values(ascending=False)
    print(average_salary.round(2).to_string())
    print()
    print(f"Highest average salary department: {average_salary.idxmax()}")

    print_section("Exercise 4: Filter by Hire Date")
    employees["hire_date"] = pd.to_datetime(employees["hire_date"])
    recent_hires = employees[employees["hire_date"] > "2022-01-01"]
    print(recent_hires[["employee_id", "first_name", "last_name", "department", "hire_date"]].to_string(index=False))
    print()
    print(f"Employees hired after January 1, 2022: {len(recent_hires)}")

    print_section("Exercise 5: Find Missing Data")
    missing = employees.isnull().sum()
    print("All columns:")
    print(missing.to_string())
    print()
    print("Columns with missing values:")
    print(missing[missing > 0].to_string())

    print_section("Exercise 6: Top Customer State")
    top_states = customers["state"].value_counts().head(5)
    print(top_states.to_string())
    print()
    print(f"State with the most customers: {top_states.idxmax()}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run the solution script**

Run: `python 03-data-analysis/solutions/lesson_05_solutions.py`

Expected: exit code `0`. Output includes:

```text
Rows: 50
Columns: 9
Engineering    16
Highest average salary department: Engineering
Employees hired after January 1, 2022: 15
department    1
salary        2
CA    10
State with the most customers: CA
```

- [ ] **Step 5: Commit Task 3**

Run:

```bash
git add 03-data-analysis/hints/lesson_05_hints.md 03-data-analysis/expected_outputs/lesson_05_expected_outputs.md 03-data-analysis/solutions/lesson_05_solutions.py
git commit -m "docs: add module 3 answer ladder"
```

Expected: commit succeeds with the three answer-ladder files.

## Task 4: Update Module 3 Exercise Entry Point

**Files:**
- Replace: `03-data-analysis/lesson_05_exercises.md`

- [ ] **Step 1: Replace `03-data-analysis/lesson_05_exercises.md`**

Replace `03-data-analysis/lesson_05_exercises.md` with this exact content:

````markdown
# Module 3 Exercises

Time to practice what you have learned. These exercises use the `employees.csv` and `customers.csv` datasets in the `../data/` folder.

Try to solve each one on your own first. You can write your solutions in a new Python file, for example `exercises.py`, in this folder.

## Support Ladder

Use these only after you have tried:

1. [Hints](hints/lesson_05_hints.md) if you are stuck.
2. [Expected outputs](expected_outputs/lesson_05_expected_outputs.md) to check your answers.
3. [Full solution script](solutions/lesson_05_solutions.py) after you have tried and compared your output.

---

## Exercise 1: Load and Inspect

Load `../data/employees.csv` into a DataFrame and print the first 10 rows. How many rows and columns does the dataset have?

```python
# Your code here
```

---

## Exercise 2: Employees Per Department

How many employees are in each department? Display the counts from most to least.

```python
# Your code here
```

---

## Exercise 3: Average Salary by Department

What is the average salary for each department? Which department has the highest average salary?

```python
# Your code here
```

---

## Exercise 4: Filter by Hire Date

Find all employees who were hired after January 1, 2022. How many are there?

```python
# Your code here
```

---

## Exercise 5: Find Missing Data

Check the employees dataset for missing values. Which columns have missing data, and how many values are missing in each?

```python
# Your code here
```

---

## Exercise 6: Top Customer State

Load `../data/customers.csv`. Which state has the most customers? Show the top 5 states by customer count.

```python
# Your code here
```
````

- [ ] **Step 2: Verify Module 3 exercise links**

Run:

```powershell
$links = @(
  '03-data-analysis/hints/lesson_05_hints.md',
  '03-data-analysis/expected_outputs/lesson_05_expected_outputs.md',
  '03-data-analysis/solutions/lesson_05_solutions.py'
)
foreach ($link in $links) {
  if (-not (Test-Path -LiteralPath $link)) { throw "Missing $link" }
}
```

Expected: no output and exit code `0`.

- [ ] **Step 3: Commit Task 4**

Run:

```bash
git add 03-data-analysis/lesson_05_exercises.md
git commit -m "docs: link module 3 exercise support"
```

Expected: commit succeeds with the updated exercise entry point.

## Task 5: Final Verification

**Files:**
- Verify: all files created or modified in Tasks 1 through 4.

- [ ] **Step 1: Run setup checker tests**

Run: `python -m unittest tests.test_check_setup -v`

Expected: all 5 tests pass and output includes `OK`.

- [ ] **Step 2: Run setup checker**

Run: `python check_setup.py`

Expected: exit code `0` in a correctly configured environment. `[LATER] pyodbc` is acceptable and should not fail the command.

- [ ] **Step 3: Compile Python files**

Run: `python -m compileall -q .`

Expected: no output and exit code `0`.

- [ ] **Step 4: Run Module 3 solution script**

Run: `python 03-data-analysis/solutions/lesson_05_solutions.py`

Expected: exit code `0`. Output includes:

```text
Rows: 50
Columns: 9
Highest average salary department: Engineering
Employees hired after January 1, 2022: 15
State with the most customers: CA
```

- [ ] **Step 5: Check new Markdown paths**

Run:

```powershell
$paths = @(
  'START_HERE.md',
  'progress_tracker.md',
  'GET_HELP.md',
  '03-data-analysis/hints/lesson_05_hints.md',
  '03-data-analysis/expected_outputs/lesson_05_expected_outputs.md'
)
foreach ($path in $paths) {
  if (-not (Test-Path -LiteralPath $path)) { throw "Missing $path" }
}
```

Expected: no output and exit code `0`.

- [ ] **Step 6: Review git status**

Run: `git status --short`

Expected: no uncommitted files from the implementation. If `__pycache__/` directories appear from Python verification, remove only those generated directories inside this repo and run `git status --short` again.

- [ ] **Step 7: Report verification results**

In the final implementation summary, include:

- The setup checker test result.
- The `check_setup.py` result.
- The compile result.
- The Module 3 solution script result.
- Any skipped checks and why.

## Self-Review Notes

- Spec goal "clear starting point" is covered by Task 1.
- Spec goal "track progress" is covered by Task 1.
- Spec goal "catch setup problems" is covered by Task 2.
- Spec goal "ask for help with useful context" is covered by Task 1.
- Spec goal "hints, expected outputs, full solutions" is covered by Tasks 3 and 4.
- Spec constraint "do not rewrite all modules" is preserved; only README and Module 3 exercise support are touched.
- Spec constraint "do not make SQL Server, Tableau, or Excel block early learners" is preserved; `pyodbc` is marked `[LATER]`.
