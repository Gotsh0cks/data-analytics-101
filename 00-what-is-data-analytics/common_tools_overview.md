# Common Tools Overview

Data analysts use a handful of core tools. You do not need to master all of them before getting a job — but you should understand what each one does and when to use it. This course teaches all four.

---

## Excel (Spreadsheets)

**What it is:** The most widely used data tool in the world. If a company has data, someone is looking at it in Excel.

**What it does:**
- Organize data in rows and columns
- Calculate with formulas (SUM, AVERAGE, VLOOKUP, etc.)
- Summarize data with pivot tables
- Create basic charts and graphs

**When to use it:**
- Quick one-off analysis ("How much did we spend last month?")
- Small datasets (under ~100,000 rows)
- Sharing results with people who don't use code
- Data entry and manual review

**Strengths:** Everyone knows it. No setup required. Visual and interactive.

**Limitations:** Struggles with large datasets. Hard to reproduce your steps. Easy to make mistakes in complex formulas without realizing it.

**In this course:** Module 2 teaches hands-on Excel.

---

## Python (with pandas)

**What it is:** A programming language. Pandas is a Python library that makes working with data almost as easy as Excel — but with the power of code.

**What it does:**
- Load data from CSV files, Excel files, databases, and APIs
- Filter, sort, group, and transform data
- Clean messy data programmatically
- Create publication-quality charts (with matplotlib and seaborn)

**When to use it:**
- Datasets too large for Excel
- Repetitive tasks you want to automate ("Run this same analysis every Monday")
- Complex data cleaning that would take hours manually
- When you need to show your exact steps (reproducibility)

**Strengths:** Handles millions of rows. Scripts can be re-run and shared. Huge community and ecosystem.

**Limitations:** Requires learning to code (but simpler than you think). Setup takes a few minutes.

**In this course:** Module 3 teaches Python with pandas. Module 5 covers matplotlib for visualization.

---

## SQL (Structured Query Language)

**What it is:** The language used to talk to databases. Almost every company stores its data in a database, and SQL is how you ask questions and get answers from that data.

**What it does:**
- Pull specific data from large databases
- Filter, sort, and aggregate with precise control
- Combine data from multiple tables (JOINs)
- Create and modify database tables

**When to use it:**
- The data lives in a database (which it usually does at companies)
- You need to pull specific subsets of data for analysis
- Datasets are very large (millions or billions of rows)
- You need to combine data from different sources

**Strengths:** Fast on large datasets. Industry standard — used everywhere. You write exactly what you want in plain-English-like syntax.

**Limitations:** Read-only in most analyst roles (you query data, not design databases). Requires a database server to be running.

**In this course:** Module 4 teaches T-SQL with SQL Server — the most common SQL variant in enterprise.

---

## Tableau

**What it is:** A drag-and-drop tool for creating interactive dashboards and visualizations. It is one of the most requested skills in data analyst job postings.

**What it does:**
- Connect to CSV files, Excel files, and databases
- Build charts and graphs by dragging and dropping
- Create interactive dashboards where viewers can click and filter
- Publish dashboards to the web for anyone to see

**When to use it:**
- Presenting findings to stakeholders (managers, executives, clients)
- Building dashboards that update regularly
- When interactivity matters (let viewers explore the data themselves)
- Building a public portfolio of your work

**Strengths:** Beautiful visualizations with no code. Interactive. Industry standard for BI (Business Intelligence).

**Limitations:** The free version (Tableau Public) publishes everything publicly. Less flexible than code for custom analysis.

**In this course:** Module 5 (Part 2) teaches Tableau Public.

---

## How They Work Together

In practice, analysts rarely use just one tool. A typical workflow might look like this:

1. **SQL** to pull raw data from the company database
2. **Python** to clean the data and calculate new metrics
3. **Tableau** to build a dashboard for the sales team
4. **Excel** to share a quick summary with your manager

Or simpler:

1. **Excel** to explore a spreadsheet your coworker sent
2. **Python** to automate the same analysis for next month

The tools complement each other. This course teaches you all four so you can pick the right tool for each situation.

---

## Do I Need All of These for a Job?

Most entry-level data analyst job postings ask for:

- **Excel** — almost always required
- **SQL** — almost always required
- **Python or R** — frequently required (we teach Python; it is more versatile)
- **Tableau or Power BI** — frequently preferred

By the end of this course, you will have hands-on experience with all four. That puts you in a strong position for entry-level analyst roles.

---

## Where You Will Work: VS Code

One thing that makes this course simpler: **you will use VS Code as your home base.** VS Code is a free code editor that handles both Python and SQL through extensions. That means you write Python scripts *and* SQL queries in the same place — no jumping between applications.

| What | Where |
|------|-------|
| Python scripts (.py files) | VS Code |
| SQL queries (.sql files) | VS Code |
| Reading lesson files (.md files) | VS Code |
| Running terminal commands | VS Code (built-in terminal) |
| Excel / spreadsheets | Excel, Google Sheets, or LibreOffice |
| Interactive dashboards | Tableau Public |

You will only leave VS Code for Excel (Module 2) and Tableau (Module 5 Part 2) — both are point-and-click tools that have their own windows.

---

Next up: [Careers and Skills](careers_and_skills.md) — what data analyst jobs look like and what they pay.
