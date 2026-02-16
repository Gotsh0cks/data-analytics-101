# Lesson 3: CREATE, INSERT, UPDATE, DELETE

## Beyond Reading Data

So far, all your SQL work has been about **reading** data — SELECT queries that pull information out of tables. But databases also need to **store** data. In this lesson, you'll learn the four operations that modify data:

- **CREATE** — make a new table
- **INSERT** — add rows to a table
- **UPDATE** — change existing rows
- **DELETE** — remove rows

Together, these are called **DDL** (Data Definition Language — CREATE) and **DML** (Data Manipulation Language — INSERT, UPDATE, DELETE).

## CREATE TABLE

Creating a table means defining its structure — what columns it has and what type of data each column holds.

```sql
CREATE TABLE projects (
    project_id   INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL,
    department   TEXT,
    budget       REAL,
    start_date   TEXT,
    status       TEXT DEFAULT 'Active'
);
```

Let's break this down:

- `INTEGER PRIMARY KEY` — a unique number that identifies each row. In SQLite, this auto-increments automatically.
- `TEXT` — a string (like VARCHAR in SQL Server)
- `REAL` — a decimal number (like FLOAT or DECIMAL)
- `NOT NULL` — this column cannot be empty
- `DEFAULT 'Active'` — if no value is provided, use 'Active'

### SQLite Data Types

SQLite is simpler than SQL Server when it comes to types:

| SQLite Type | What It Stores | SQL Server Equivalent |
|-------------|----------------|----------------------|
| `INTEGER` | Whole numbers | INT |
| `REAL` | Decimal numbers | FLOAT, DECIMAL |
| `TEXT` | Text/strings | VARCHAR, NVARCHAR |
| `BLOB` | Binary data (files, images) | VARBINARY |
| `NULL` | No value | NULL |

## INSERT INTO

To add rows to a table:

```sql
-- Insert a single row
INSERT INTO projects (project_name, department, budget, start_date)
VALUES ('Website Redesign', 'Marketing', 25000.00, '2024-06-01');

-- Insert multiple rows at once
INSERT INTO projects (project_name, department, budget, start_date, status)
VALUES
    ('Data Pipeline', 'Engineering', 50000.00, '2024-07-15', 'Active'),
    ('Office Move', 'HR', 15000.00, '2024-08-01', 'Planning'),
    ('Q3 Campaign', 'Marketing', 35000.00, '2024-09-01', 'Planning');
```

Notice that we didn't include `project_id` — SQLite fills it in automatically because it's an `INTEGER PRIMARY KEY`.

We also didn't include `status` in the first row — it defaults to 'Active'.

## UPDATE

To change existing data:

```sql
-- Change the budget for a specific project
UPDATE projects
SET budget = 30000.00
WHERE project_name = 'Website Redesign';

-- Change multiple columns at once
UPDATE projects
SET status = 'In Progress', budget = 55000.00
WHERE project_name = 'Data Pipeline';
```

**WARNING:** Always include a WHERE clause with UPDATE. Without it, you'll change **every row** in the table:

```sql
-- THIS CHANGES EVERY PROJECT'S STATUS!
UPDATE projects SET status = 'Cancelled';
-- Don't do this unless you mean it!
```

## DELETE

To remove rows:

```sql
-- Delete a specific project
DELETE FROM projects
WHERE project_name = 'Office Move';

-- Delete all cancelled projects
DELETE FROM projects
WHERE status = 'Cancelled';
```

**Same warning as UPDATE:** Always include WHERE. `DELETE FROM projects;` deletes **everything**.

## DROP TABLE

To remove an entire table (structure and all data):

```sql
DROP TABLE IF EXISTS projects;
```

`IF EXISTS` prevents an error if the table doesn't exist. This is handy in scripts where you might run the same code twice.

## ALTER TABLE

To modify a table's structure after it's created:

```sql
-- Add a new column
ALTER TABLE projects ADD COLUMN end_date TEXT;

-- Rename a table
ALTER TABLE projects RENAME TO company_projects;
```

Note: SQLite's ALTER TABLE is more limited than SQL Server's — you can add columns and rename the table, but you can't drop columns or change column types (in older versions).

## Try It Yourself

Open `lesson_03_create_insert_update.sql` in DB Browser for SQLite and work through the examples. Creating and modifying your own tables is one of the most satisfying parts of learning SQL.
