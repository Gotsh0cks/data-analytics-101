# Module 4 Exercise Hints

Try each exercise on your own before reading the hint. If the hint is enough to get you moving, go back to your query and keep working.

## Exercise 1: Employees in the Sales Department

Start with `SELECT` and name only the columns the exercise asks for.

Use `FROM Employees`, then add a `WHERE` clause that filters the `department` column. Remember that text values go in single quotes.

## Exercise 2: Top 5 Highest-Paid Employees

Use `SELECT TOP 5` so SQL Server only returns five rows.

Sort by `salary` with `ORDER BY salary DESC`. `DESC` means highest to lowest.

## Exercise 3: Total Revenue by Product

This is a `GROUP BY` problem.

Select the `product` column and use `SUM(revenue)` for the total. Because you are grouping by product, `product` also needs to appear in the `GROUP BY` clause.

Add `ORDER BY` at the end so the largest total appears first.

## Exercise 4: Customer Signups by Year

T-SQL has a `YEAR()` function that pulls the year out of a date.

Use `YEAR(signup_date)` in your `SELECT` list and again in your `GROUP BY` clause. Then use `COUNT(*)` to count customers in each year.

## Exercise 5: Above-Average Earners

First answer the smaller question: what is the company-wide average salary?

Then use that average inside a subquery in the `WHERE` clause:

```sql
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees
)
```

Finish with `ORDER BY salary DESC`.

## Exercise 6: Region with the Most Sales

Each row in the `Sales` table is one sales transaction.

Use `COUNT(*)` with `GROUP BY region` to count transactions per region. Then sort the counts from highest to lowest with `ORDER BY`.

## Exercise 7: Department with the Highest Average Salary (CTE)

Build this in two steps.

First, write a CTE that groups employees by `department` and calculates `AVG(salary)`.

Second, select from that CTE and sort the average salary from highest to lowest. Use `TOP 1` if you only want the highest department.

## Exercise 8 (BONUS): Products Never Sold in the West

This is a "find what is missing" problem.

A safer anti-join approach uses `NOT EXISTS`:

1. Make a list of all distinct products from `Sales`.
2. For each product, check whether a matching West-region row exists.
3. Keep products where that West-region row does not exist.

You may also see this solved with `NOT IN`, but `NOT EXISTS` is a safer habit because `NOT IN` can behave unexpectedly if the subquery ever contains `NULL`.

## Exercise 9: Python + SQL

Use the same workflow from Lesson 6:

1. Put your SQL query in a triple-quoted Python string.
2. Use `pd.read_sql(query, conn)` to run the query and load the result into a DataFrame.
3. Print the DataFrame with `to_string(index=False)`.
4. Use `df.plot(kind="bar", x="category", y="total_revenue")` for the chart.

Keep the connection string easy to edit, and only connect inside your script's `main()` function so the file can be imported safely.
