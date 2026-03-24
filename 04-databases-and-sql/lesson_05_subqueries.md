# Lesson 5: Subqueries and CTEs

## What Is a Subquery?

A **subquery** is a query inside a query. It sounds complicated, but the idea is simple: sometimes you need to answer one question before you can answer another.

For example: "Show me employees who earn more than the average salary." To answer this, SQL first needs to figure out what the average salary is, and *then* use that number to filter the employees. The inner query that calculates the average is the subquery.

```sql
SELECT first_name, last_name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);
```

The part in parentheses runs first, returns a single number (the average salary), and then the outer query uses that number in its WHERE clause.

## When to Use Subqueries

Subqueries are useful when:

- You need to filter based on an aggregated value ("above average," "more than the maximum of another group").
- You want to compare a row's value to a calculated result.
- You need to create a temporary result set to query against.

## Subqueries in WHERE

This is the most common type. The subquery calculates a value, and the outer query filters by it.

```sql
-- Employees earning above the average salary
SELECT first_name, last_name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);
```

You can also use `IN` with a subquery that returns multiple values:

```sql
-- Products that have been sold in the "North" region
SELECT DISTINCT product
FROM Sales
WHERE product IN (
    SELECT product FROM Sales WHERE region = 'North'
);
```

## Subqueries in FROM

You can also use a subquery as a temporary table in the FROM clause. SQL runs the inner query first, creates a result set, and then the outer query works with that result set.

```sql
-- Get the average revenue per region, then find the max of those averages
SELECT MAX(avg_revenue) AS highest_avg_revenue
FROM (
    SELECT region, AVG(revenue) AS avg_revenue
    FROM Sales
    GROUP BY region
) AS region_averages;
```

**Important:** When you put a subquery in FROM, you *must* give it an alias (the `AS region_averages` part). Think of it as naming your temporary table.

## Introduction to CTEs (Common Table Expressions)

CTEs solve the same problems as subqueries but in a way that's much easier to read. A CTE is basically a **named subquery** that you define at the top of your query using the **WITH** keyword.

Here's the same "average revenue per region" example, rewritten as a CTE:

```sql
WITH RegionAverages AS (
    SELECT region, AVG(revenue) AS avg_revenue
    FROM Sales
    GROUP BY region
)
SELECT MAX(avg_revenue) AS highest_avg_revenue
FROM RegionAverages;
```

See how that reads more naturally? You define `RegionAverages` up front, and then you use it like a regular table.

## Why CTEs Are Better Than Subqueries (Usually)

1. **Readability.** The query reads top to bottom instead of inside out.
2. **Reusability.** You can reference the CTE multiple times in the same query.
3. **Debugging.** You can run just the CTE part to check its results.

That said, simple subqueries in WHERE (like the "above average" example) are perfectly fine. Use whichever is clearer for the situation.

## CTE Syntax

```sql
WITH NameOfYourCTE AS (
    -- Your query goes here
    SELECT ...
    FROM ...
)
-- Now use it
SELECT ...
FROM NameOfYourCTE;
```

A few rules:
- The CTE name can be anything descriptive.
- The CTE must be followed immediately by a SELECT, INSERT, UPDATE, or DELETE.
- You can define multiple CTEs separated by commas.

## Multiple CTEs

You can chain CTEs together when you need multiple steps:

```sql
WITH
    -- Step 1: Calculate total revenue per product
    ProductTotals AS (
        SELECT product, SUM(revenue) AS total_revenue
        FROM Sales
        GROUP BY product
    ),
    -- Step 2: Find the average of those totals
    AvgProductRevenue AS (
        SELECT AVG(total_revenue) AS avg_revenue
        FROM ProductTotals
    )
-- Step 3: Find products above the average
SELECT p.product, p.total_revenue
FROM ProductTotals p, AvgProductRevenue a
WHERE p.total_revenue > a.avg_revenue
ORDER BY p.total_revenue DESC;
```

## Keep It Simple

This is just an introduction. Subqueries and CTEs can get very complex, but for now, focus on these two patterns:

1. **Subquery in WHERE** for filtering by a calculated value.
2. **CTE with WITH** for building up a result step by step.

As you get more comfortable with SQL, you'll naturally start using these for more advanced analysis.

## Key Takeaways

| Concept | What It Does |
|---------|-------------|
| Subquery in WHERE | Filters rows based on a calculated value |
| Subquery in FROM | Creates a temporary result set to query against |
| CTE (`WITH ... AS`) | A named query you define up front for better readability |
| Multiple CTEs | Chain steps together for complex calculations |

## What's Next?

Congratulations! You've completed all five lessons. Head over to `exercises.md` to practice everything you've learned with hands-on problems.
