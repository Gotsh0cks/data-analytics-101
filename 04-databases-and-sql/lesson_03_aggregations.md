# Lesson 3: Aggregations

## Summarizing Data

So far, you've been looking at individual rows. But in data analytics, you often need *summaries* totals, averages, counts. That's what **aggregate functions** do. They take many rows and crunch them down into a single value.

## The Big Five Aggregate Functions

| Function | What It Does | Example |
|----------|-------------|---------|
| `COUNT()` | Counts how many rows | How many sales did we make? |
| `SUM()` | Adds values together | What's our total revenue? |
| `AVG()` | Calculates the average | What's the average salary? |
| `MIN()` | Finds the smallest value | What's the lowest price? |
| `MAX()` | Finds the largest value | Who earns the most? |

Here's a quick example:

```sql
-- How many rows are in the Sales table?
SELECT COUNT(*) AS total_sales FROM Sales;

-- What's the total revenue across all sales?
SELECT SUM(revenue) AS total_revenue FROM Sales;
```

## COUNT(*) vs COUNT(column_name)

This is a subtle but important difference:

- `COUNT(*)` counts **all rows**, no matter what.
- `COUNT(column_name)` counts only rows where **that column is not NULL**.

In our sample data, they return the same number because we don't have NULLs. But in real-world data, they can differ. For example, if 5 out of 100 customers don't have an email address, `COUNT(*)` returns 100 but `COUNT(email)` returns 95.

**Rule of thumb:** Use `COUNT(*)` when you want to count rows. Use `COUNT(column_name)` when you specifically want to know how many non-empty values exist in that column.

## GROUP BY Totals for EACH Group

Aggregate functions become really powerful when you combine them with **GROUP BY**. This tells SQL: "Don't just give me one total give me a total for *each* group."

```sql
-- Total revenue for EACH region
SELECT region, SUM(revenue) AS total_revenue
FROM Sales
GROUP BY region;
```

This returns one row per region, with the total revenue for that region. It's like creating a pivot table in Excel.

More examples:

```sql
-- Average salary by department
SELECT department, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department;

-- Number of customers by state
SELECT state, COUNT(*) AS customer_count
FROM Customers
GROUP BY state;
```

**Important rule:** When you use GROUP BY, every column in your SELECT must either be (1) in the GROUP BY clause, or (2) inside an aggregate function. You can't just throw random columns in there SQL wouldn't know which value to show for the group.

## HAVING Filtering Groups

You know that WHERE filters individual rows. But what if you want to filter *groups* after aggregating? That's what **HAVING** does.

```sql
-- Only show regions with total revenue over $3,000
SELECT region, SUM(revenue) AS total_revenue
FROM Sales
GROUP BY region
HAVING SUM(revenue) > 3000;
```

## WHERE vs HAVING

This trips up a lot of beginners, so let's be clear:

| | WHERE | HAVING |
|---|-------|--------|
| **When it runs** | Before grouping | After grouping |
| **Filters** | Individual rows | Groups (aggregated results) |
| **Can use aggregates?** | No | Yes |

Think of it this way:
1. **WHERE** filters the raw data first (removes rows you don't want).
2. **GROUP BY** groups the remaining rows together.
3. **HAVING** filters the groups (removes groups you don't want).

You can use both in the same query:

```sql
-- Total revenue by region, but only for Electronics,
-- and only show regions where total revenue is over $1,000
SELECT region, SUM(revenue) AS total_revenue
FROM Sales
WHERE category = 'Electronics'    -- Step 1: filter to Electronics only
GROUP BY region                   -- Step 2: group by region
HAVING SUM(revenue) > 1000       -- Step 3: keep only groups over $1,000
ORDER BY total_revenue DESC;      -- Step 4: sort the results
```

## ORDER BY with Aggregations

You can sort your aggregated results just like any other query:

```sql
-- Departments ranked by average salary, highest first
SELECT department, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department
ORDER BY avg_salary DESC;
```

## Key Takeaways

| Concept | What It Does |
|---------|-------------|
| `COUNT()` | Counts rows |
| `SUM()` | Adds up values |
| `AVG()` | Calculates the mean |
| `MIN() / MAX()` | Finds smallest / largest value |
| `GROUP BY` | Creates groups to aggregate within |
| `HAVING` | Filters groups after aggregation |
| WHERE filters rows, HAVING filters groups | |

## The Query Execution Order

This is the order SQL actually processes a query (not the order you write it):

1. `FROM` which table?
2. `WHERE` filter individual rows
3. `GROUP BY` create groups
4. `HAVING` filter groups
5. `SELECT` choose columns and calculate aggregates
6. `ORDER BY` sort the final results

Understanding this order helps you know when to use WHERE vs HAVING.

## Next Up

In Lesson 4, you'll learn how to **combine data from multiple tables** using JOINs.
