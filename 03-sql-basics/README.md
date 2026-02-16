# Module 3: Beginner T-SQL

## What This Module Covers

In this module, you'll learn SQL — the language used to talk to databases. Almost every company stores its data in a database, and SQL is how you ask questions and get answers from that data. We'll use T-SQL, which is Microsoft's version of SQL that runs on SQL Server.

By the end of this module, you'll be able to:

- Pull data from a database table
- Filter and sort results to find exactly what you need
- Summarize data using counts, sums, and averages
- Combine data from multiple tables using JOINs
- Write more advanced queries with subqueries and CTEs

## Before You Start

> **Important:** Before starting this module, make sure you've completed the SQL Server setup in Module 0. Then open Azure Data Studio, connect to your local SQL Server, and run the `setup_database.sql` script to create the practice tables. This will give you the sample data you need for every lesson.

To run the setup script:

1. Open Azure Data Studio
2. Connect to your SQL Server instance
3. Open the file `setup_database.sql` from this folder
4. Click **Run** (or press F5) to execute the entire script
5. You should see messages confirming the database and tables were created

## Lessons

| Lesson | Topic | Files |
|--------|-------|-------|
| 1 | SELECT and FROM | `lesson_01_select_from.md` / `.sql` |
| 2 | WHERE and ORDER BY | `lesson_02_where_orderby.md` / `.sql` |
| 3 | Aggregations | `lesson_03_aggregations.md` / `.sql` |
| 4 | JOINs | `lesson_04_joins.md` / `.sql` |
| 5 | Subqueries and CTEs | `lesson_05_subqueries.md` / `.sql` |

## Practice

After completing all five lessons, head to `exercises.md` for hands-on practice problems that cover everything you've learned.

## Tips for Learning SQL

- **Type out every query yourself.** Don't copy and paste. Typing builds muscle memory.
- **Experiment.** Change a column name, add a filter, break something on purpose — then fix it.
- **Read the error messages.** SQL Server gives you helpful clues about what went wrong.
- **Run queries in small pieces.** If a big query doesn't work, try running just the inner part first.
