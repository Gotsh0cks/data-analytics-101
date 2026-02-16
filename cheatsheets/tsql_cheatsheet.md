# T-SQL Quick Reference

## Basic Queries

```sql
-- Select specific columns
SELECT col1, col2 FROM table_name;

-- Select all columns
SELECT * FROM table_name;

-- Filter rows
SELECT * FROM table_name WHERE col1 > 100;

-- Sort results
SELECT * FROM table_name ORDER BY col1 ASC;

-- Limit rows returned
SELECT TOP 10 * FROM table_name;

-- Unique values only
SELECT DISTINCT col1 FROM table_name;

-- Column alias
SELECT col1 AS "Readable Name" FROM table_name;
```

## Operators

| Operator | Meaning |
|---|---|
| `=` | Equal to |
| `<>` | Not equal to |
| `<`, `>` | Less than, greater than |
| `<=`, `>=` | Less than or equal, greater than or equal |
| `AND` | Both conditions must be true |
| `OR` | Either condition can be true |
| `NOT` | Negates a condition |
| `IN` | Matches any value in a list |
| `BETWEEN` | Within a range (inclusive) |
| `LIKE` | Pattern matching (% = any chars, _ = one char) |
| `IS NULL` | Value is missing |
| `IS NOT NULL` | Value is not missing |

```sql
-- IN: match any value in a list
SELECT * FROM orders WHERE status IN ('Shipped', 'Delivered');

-- BETWEEN: filter within a range
SELECT * FROM products WHERE price BETWEEN 10 AND 50;

-- LIKE: pattern matching
SELECT * FROM customers WHERE name LIKE 'J%';
```

## Aggregations

```sql
-- Count all rows
SELECT COUNT(*) FROM table_name;

-- Sum, average, min, max
SELECT SUM(amount), AVG(amount), MIN(amount), MAX(amount)
FROM orders;

-- Group by category
SELECT category, COUNT(*) AS total
FROM products GROUP BY category;

-- Filter groups with HAVING
SELECT category, AVG(price) AS avg_price
FROM products GROUP BY category HAVING AVG(price) > 50;
```

## Joins

```sql
-- INNER JOIN: only matching rows from both tables
SELECT a.col1, b.col2
FROM table_a a INNER JOIN table_b b ON a.id = b.a_id;

-- LEFT JOIN: all rows from left table, matching from right
SELECT a.col1, b.col2
FROM table_a a LEFT JOIN table_b b ON a.id = b.a_id;
```

## Subqueries and CTEs

```sql
-- Subquery in WHERE: filter using another query's result
SELECT * FROM employees
WHERE department_id IN (SELECT id FROM departments WHERE region = 'West');

-- CTE: name a temporary result set for readability
WITH top_customers AS (
    SELECT customer_id, SUM(amount) AS total
    FROM orders GROUP BY customer_id
)
SELECT * FROM top_customers WHERE total > 1000;
```

## Common Patterns

```sql
-- Top N by value
SELECT TOP 5 * FROM products ORDER BY price DESC;

-- Count per category
SELECT category, COUNT(*) AS cnt
FROM products GROUP BY category ORDER BY cnt DESC;

-- Filter by date range
SELECT * FROM orders
WHERE order_date BETWEEN '2025-01-01' AND '2025-12-31';

-- Find duplicates
SELECT email, COUNT(*) AS cnt
FROM customers GROUP BY email HAVING COUNT(*) > 1;

-- Find NULLs
SELECT * FROM orders WHERE shipped_date IS NULL;
```
