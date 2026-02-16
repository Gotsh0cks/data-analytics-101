# SQLite Cheatsheet

Quick reference for SQLite syntax. Print this out and keep it nearby.

---

## Connecting (Python)

```python
import sqlite3
conn = sqlite3.connect("data/analytics.db")
cursor = conn.cursor()
```

## Queries with pandas

```python
import pandas as pd
df = pd.read_sql("SELECT * FROM table_name", conn)
```

---

## SELECT Queries

```sql
-- All columns
SELECT * FROM sales_data;

-- Specific columns
SELECT product, revenue FROM sales_data;

-- With alias
SELECT product AS item, revenue AS total FROM sales_data;

-- Limit rows
SELECT * FROM sales_data LIMIT 10;

-- Remove duplicates
SELECT DISTINCT category FROM sales_data;
```

## Filtering (WHERE)

```sql
SELECT * FROM sales_data WHERE category = 'Electronics';
SELECT * FROM employees WHERE salary > 70000;
SELECT * FROM employees WHERE department IN ('Sales', 'Marketing');
SELECT * FROM employees WHERE hire_date BETWEEN '2020-01-01' AND '2022-12-31';
SELECT * FROM titanic WHERE Age IS NULL;
SELECT * FROM titanic WHERE Age IS NOT NULL;
SELECT * FROM customers WHERE email LIKE '%@gmail.com';
```

## Sorting (ORDER BY)

```sql
SELECT * FROM employees ORDER BY salary DESC;
SELECT * FROM employees ORDER BY department ASC, salary DESC;
```

## Aggregations

```sql
SELECT COUNT(*) FROM sales_data;
SELECT SUM(revenue) FROM sales_data;
SELECT AVG(salary) FROM employees;
SELECT MIN(salary), MAX(salary) FROM employees;
SELECT ROUND(AVG(salary), 2) FROM employees;

-- Group by
SELECT category, SUM(revenue) as total
FROM sales_data
GROUP BY category;

-- Filter groups
SELECT category, SUM(revenue) as total
FROM sales_data
GROUP BY category
HAVING total > 1000;
```

## JOINs

```sql
-- Inner join (only matching rows)
SELECT a.name, b.order_total
FROM customers a
INNER JOIN orders b ON a.id = b.customer_id;

-- Left join (all rows from left table)
SELECT a.name, b.order_total
FROM customers a
LEFT JOIN orders b ON a.id = b.customer_id;
```

## Subqueries

```sql
-- Subquery in WHERE
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Subquery in FROM
SELECT dept, avg_sal
FROM (
    SELECT department AS dept, AVG(salary) AS avg_sal
    FROM employees
    GROUP BY department
) sub
WHERE avg_sal > 60000;
```

## CREATE / INSERT / UPDATE / DELETE

```sql
-- Create a table
CREATE TABLE projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    budget REAL,
    status TEXT DEFAULT 'Active'
);

-- Insert rows
INSERT INTO projects (name, budget) VALUES ('Website', 25000);

-- Update rows (always use WHERE!)
UPDATE projects SET budget = 30000 WHERE name = 'Website';

-- Delete rows (always use WHERE!)
DELETE FROM projects WHERE status = 'Cancelled';

-- Drop a table
DROP TABLE IF EXISTS projects;

-- Add a column
ALTER TABLE projects ADD COLUMN end_date TEXT;
```

## Useful Functions

```sql
-- String
LENGTH(column)                    -- String length
UPPER(column)                     -- Uppercase
LOWER(column)                     -- Lowercase
column || ' ' || column2          -- Concatenate (use || not +)
TRIM(column)                      -- Remove whitespace

-- Numeric
ROUND(column, 2)                  -- Round to 2 decimals
ABS(column)                       -- Absolute value
MAX(column), MIN(column)          -- Min/max

-- Date
DATE('now')                       -- Today's date
DATE('now', '-7 days')            -- 7 days ago
strftime('%Y', date_col)          -- Extract year
strftime('%m', date_col)          -- Extract month

-- NULL handling
COALESCE(column, 'default')       -- Use default if NULL
IFNULL(column, 0)                 -- SQLite-specific version
```

## Database Info

```sql
-- List all tables
SELECT name FROM sqlite_master WHERE type='table';

-- Table structure
PRAGMA table_info(table_name);

-- Row count
SELECT COUNT(*) FROM table_name;
```

## SQLite vs T-SQL Differences

| SQLite | T-SQL (SQL Server) |
|--------|--------------------|
| `LIMIT 10` | `TOP 10` |
| `||` (concat) | `+` (concat) |
| `LENGTH()` | `LEN()` |
| `DATE('now')` | `GETDATE()` |
| `IFNULL()` | `ISNULL()` |
| `INTEGER PRIMARY KEY` | `INT IDENTITY(1,1)` |
| `TEXT` | `VARCHAR(n)` |
| `REAL` | `FLOAT` / `DECIMAL` |
