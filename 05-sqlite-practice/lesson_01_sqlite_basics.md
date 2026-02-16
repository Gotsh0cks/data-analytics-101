# Lesson 1: SQLite Basics

## What is SQLite?

SQLite is the world's most widely used database. It's inside your phone, your browser, and countless apps. Unlike SQL Server, it doesn't run as a separate program — it's just a single file on your computer.

When you ran `setup_database.py`, it created a file called `analytics.db` in the `data/` folder. That single file **is** the entire database — all the tables, all the data, everything.

## Connecting to the Database

In Python, connecting to a SQLite database takes just two lines:

```python
import sqlite3

conn = sqlite3.connect("../data/analytics.db")
```

That's it. No username, no password, no server address. You just point it at the file.

## Running Your First Query

Once connected, you can run SQL queries using a **cursor**:

```python
cursor = conn.cursor()
cursor.execute("SELECT * FROM sales_data LIMIT 5")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

Each row comes back as a **tuple** — a Python list-like object.

## Getting Column Names

One thing that's different from Azure Data Studio: when you run a query in Python, you only get the data, not the column headers. To get the column names:

```python
cursor.execute("SELECT * FROM sales_data LIMIT 1")
column_names = [description[0] for description in cursor.description]
print(column_names)
```

## Seeing All Tables

To find out which tables exist in the database:

```sql
SELECT name FROM sqlite_master WHERE type='table';
```

This is SQLite's equivalent of browsing the table list in Azure Data Studio.

## Counting Rows

Just like in SQL Server:

```sql
SELECT COUNT(*) FROM sales_data;
SELECT COUNT(*) FROM titanic;
SELECT COUNT(*) FROM iris;
```

## Key Differences from T-SQL

If you've already completed Module 3, you'll notice a few differences:

| T-SQL (SQL Server) | SQLite |
|---------------------|--------|
| `TOP 5` | `LIMIT 5` |
| `GETDATE()` | `DATE('now')` |
| `LEN(column)` | `LENGTH(column)` |
| `IDENTITY(1,1)` | `INTEGER PRIMARY KEY` (auto-increments automatically) |
| `VARCHAR(50)` | `TEXT` (SQLite is flexible about types) |

The core SQL — SELECT, FROM, WHERE, JOIN, GROUP BY, ORDER BY — works exactly the same.

## Closing the Connection

When you're done, close the connection:

```python
conn.close()
```

This is good practice, but SQLite is forgiving — if you forget, nothing bad happens for a learning project.

## Try It Yourself

Run `lesson_01_sqlite_basics.py` to see all of this in action. The script connects to your database, lists all tables, and runs a few sample queries.
