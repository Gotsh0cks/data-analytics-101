# Module 5: SQL Practice with SQLite

## What This Module Covers

In Module 3, you learned SQL using T-SQL and SQL Server. That's a powerful enterprise tool, but it requires installing SQL Server — which can be tricky and uses a lot of disk space.

In this module, you'll learn to use **SQLite** — a lightweight database that comes built into Python. No installation needed. No server to run. Just a single file on your computer that holds your entire database.

By the end of this module, you'll be able to:

- Create and manage a SQLite database
- Load CSV files into database tables
- Write SQL queries against real-world datasets
- Create, insert, update, and delete data
- Use Python to run SQL queries and get results as DataFrames

## SQLite vs. SQL Server — What's the Difference?

| Feature | SQLite | SQL Server |
|---------|--------|------------|
| Cost | Free | Free (Express) or paid |
| Installation | None (built into Python) | Large installer |
| Where it runs | Your computer, as a file | As a background service |
| Best for | Personal projects, learning, small apps | Enterprise, multi-user, large-scale |
| SQL dialect | Standard SQL | T-SQL (Microsoft's version) |

**The good news:** about 90% of SQL syntax is the same between SQLite and SQL Server. What you learn here works almost everywhere.

## Before You Start

1. Complete Module 4 first — run `download_public_datasets.py` to get the external datasets
2. (Optional) Install DB Browser for SQLite — see `install_sqlite_tools.md`

## Lessons

| Lesson | Topic | Files |
|--------|-------|-------|
| Setup | Create the database | `setup_database.py` |
| 1 | SQLite basics and first queries | `lesson_01_sqlite_basics.md` / `.py` |
| 2 | Querying real-world data | `lesson_02_querying_real_data.md` / `.sql` |
| 3 | CREATE, INSERT, UPDATE, DELETE | `lesson_03_create_insert_update.md` / `.sql` |
| 4 | Python + SQL together | `lesson_04_python_and_sql.md` / `.py` |

## Practice

After completing all four lessons, head to `exercises.md` for hands-on practice problems.

## Quick Start

```bash
# Step 1: Make sure you've downloaded the external datasets
python 04-external-datasets/download_public_datasets.py

# Step 2: Create the SQLite database
python 05-sqlite-practice/setup_database.py

# Step 3: Start learning!
# Open lesson_01_sqlite_basics.md and follow along
```
