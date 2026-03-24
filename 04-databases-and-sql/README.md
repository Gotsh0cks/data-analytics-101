# Module 4: Databases & SQL

## What This Module Covers

So far you have worked with data stored in files — CSV files and Excel workbooks. But most companies store their data in **databases**. A database is like a super-powered filing cabinet that can hold millions of records, let multiple people access the data at once, and answer complex questions in milliseconds.

**SQL** (Structured Query Language) is how you talk to databases. It is the universal language of data. Every database understands SQL, and it appears in 85%+ of data analyst job postings.

In this module, you will learn **T-SQL** — Microsoft's version of SQL that runs on SQL Server, one of the most widely used databases in enterprise.

By the end of this module, you will be able to:

- Pull data from a database table
- Filter and sort results to find exactly what you need
- Summarize data using counts, sums, and averages
- Combine data from multiple tables using JOINs
- Write advanced queries with subqueries and CTEs
- Connect Python to SQL Server and query data into pandas DataFrames

## Why SQL Matters

You might wonder: "I can already load CSV files in pandas. Why do I need SQL?"

1. **Company data lives in databases.** You will rarely get a clean CSV — you will need to query the database directly.
2. **Databases handle big data.** When a table has 50 million rows, you need SQL to extract just the subset you need.
3. **It is a job requirement.** SQL is the #1 most requested technical skill for data analysts.
4. **SQL is declarative.** You describe *what* you want, not *how* to get it. This makes it surprisingly readable.

## Before You Start

Make sure you have completed the SQL Server setup in Module 1. Then:

1. Open **VS Code** and make sure you are in the `data-analytics-101` folder (File > Open Folder)
2. Open the file `04-databases-and-sql/setup_database.sql` from the Explorer sidebar
3. Press **Ctrl+Shift+E** to run the entire script
4. If VS Code asks which connection to use, select your **Local SQL Server** profile (the one you set up in Module 1)
5. You should see messages in the results panel confirming the database and tables were created

## Lessons

| Lesson | Topic | Files |
|--------|-------|-------|
| 1 | [SELECT and FROM](lesson_01_select_from.md) | `.md` / `.sql` |
| 2 | [WHERE and ORDER BY](lesson_02_where_orderby.md) | `.md` / `.sql` |
| 3 | [Aggregations](lesson_03_aggregations.md) | `.md` / `.sql` |
| 4 | [JOINs](lesson_04_joins.md) | `.md` / `.sql` |
| 5 | [Subqueries and CTEs](lesson_05_subqueries.md) | `.md` / `.sql` |
| 6 | [Python + SQL Server](lesson_06_python_and_sql.md) | `.md` / `.py` |

## Practice

After completing all lessons, head to [Exercises](exercises.md) for hands-on practice problems.

## Excel/pandas Parallels

| What You Want | Excel | pandas | SQL |
|---------------|-------|--------|-----|
| See all data | Open the file | `df.head()` | `SELECT * FROM table` |
| Pick columns | Hide columns | `df[["col1", "col2"]]` | `SELECT col1, col2 FROM table` |
| Filter rows | Data > Filter | `df[df["col"] > 100]` | `WHERE col > 100` |
| Sort | Data > Sort | `df.sort_values()` | `ORDER BY col` |
| Summarize | Pivot table | `df.groupby().sum()` | `GROUP BY col` |

Same concepts, three different tools. Pick the best one for the situation.

## Tips for Learning SQL

- **Type out every query yourself.** Do not copy and paste. Typing builds muscle memory.
- **Experiment.** Change a column name, add a filter, break something on purpose — then fix it.
- **Read the error messages.** SQL Server gives you helpful clues about what went wrong.
- **Run queries in small pieces.** If a big query does not work, try running just the inner part first.

## Next Steps

Once you have completed the lessons and exercises, move on to [Module 5: Visualization](../05-visualization/) — where you will learn to turn your analysis into charts and dashboards.
