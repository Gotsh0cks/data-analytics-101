# Installing SQLite Tools

## The Python Module (Required — Already Installed!)

Great news: the `sqlite3` module comes built into Python. You don't need to install anything. If you have Python, you have SQLite.

You can verify by opening a terminal and running:

```bash
python -c "import sqlite3; print(sqlite3.sqlite_version)"
```

This should print a version number like `3.39.4`. If it does, you're all set.

## DB Browser for SQLite (Optional — Recommended)

DB Browser for SQLite is a free, visual tool for working with SQLite databases. Think of it as the SQLite equivalent of Azure Data Studio for SQL Server. It lets you browse tables, run queries, and see results without writing Python code.

### How to Install

1. Go to **sqlitebrowser.org/dl/**
2. Under "Windows", click the **Standard installer for 64-bit Windows** link
3. Run the downloaded installer
4. Accept the defaults and click through the installation
5. Launch "DB Browser for SQLite" from your Start menu

### How to Use It

Once you've created the database (by running `setup_database.py`), you can open it in DB Browser:

1. Open DB Browser for SQLite
2. Click **Open Database** (top left)
3. Navigate to this project's `data/` folder
4. Select `analytics.db`
5. Click **Open**

You'll see your tables listed on the left. Click on a table name, then click the **Browse Data** tab to see its contents.

To run SQL queries:

1. Click the **Execute SQL** tab
2. Type your query in the text box
3. Click the **Play** button (or press F5) to run it
4. Results appear below

### Why Both Tools?

- **DB Browser** is great for exploring data visually and experimenting with queries
- **Python + sqlite3** is great for automating queries and combining SQL with data analysis

Most working analysts use both approaches — a GUI for exploration and code for repeatable analysis.
