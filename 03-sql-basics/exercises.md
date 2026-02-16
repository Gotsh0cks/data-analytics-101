# Module 3: Practice Exercises

Test your T-SQL skills with these practice problems. Each one builds on what you learned in the lessons. Try to write the query yourself before looking at the hints.

Make sure you're connected to the `DataAnalytics101` database before running your queries.

```sql
USE DataAnalytics101;
```

---

## Exercise 1: Employees in the Sales Department

Write a query to get all employees in the Sales department. Show their first name, last name, job title, and salary.

---

## Exercise 2: Top 5 Highest-Paid Employees

List the top 5 highest-paid employees. Include their first name, last name, department, and salary. Sort by salary from highest to lowest.

---

## Exercise 3: Total Revenue by Product

What is the total revenue for each product? Show the product name and its total revenue, sorted from highest to lowest revenue.

---

## Exercise 4: Customer Signups by Year

How many customers signed up in each year? Show the year and the count of customers. (You'll need to extract the year from the signup_date column.)

---

## Exercise 5: Above-Average Earners

Find all employees who earn more than the average salary across the company. Show their first name, last name, department, and salary, sorted by salary descending.

---

## Exercise 6: Region with the Most Sales

Which region has the most sales transactions? Show all regions with their transaction counts, sorted so the busiest region is on top.

---

## Exercise 7: Department with the Highest Average Salary (CTE)

Write a query using a CTE to find the department with the highest average salary. Your result should show the department name and its average salary.

---

## Exercise 8 (BONUS): Products Never Sold in the West

Find products that have never been sold in the "West" region. This is trickier than it looks — think about which products *do* appear in the West, and then find the ones that don't.

---

## Hints

Only look at these after you've tried each exercise on your own!

<details>
<summary>Hint for Exercise 1</summary>

Use `SELECT ... FROM Employees WHERE department = '...'`. Remember that text values go in single quotes.

</details>

<details>
<summary>Hint for Exercise 2</summary>

Use `SELECT TOP 5` with `ORDER BY salary DESC` to get the five highest salaries.

</details>

<details>
<summary>Hint for Exercise 3</summary>

You need `SUM(revenue)` combined with `GROUP BY product`. Add `ORDER BY` at the end to sort.

</details>

<details>
<summary>Hint for Exercise 4</summary>

T-SQL has a `YEAR()` function that extracts the year from a date. Use `YEAR(signup_date)` in both your SELECT and GROUP BY.

</details>

<details>
<summary>Hint for Exercise 5</summary>

Use a subquery in the WHERE clause: `WHERE salary > (SELECT AVG(salary) FROM Employees)`.

</details>

<details>
<summary>Hint for Exercise 6</summary>

Use `COUNT(*)` with `GROUP BY region`. Sort with `ORDER BY ... DESC`. If you only want the top one, add `TOP 1`.

</details>

<details>
<summary>Hint for Exercise 7</summary>

Define a CTE that calculates `AVG(salary)` grouped by department. Then select from the CTE with `ORDER BY avg_salary DESC` and use `TOP 1` to get just the highest.

</details>

<details>
<summary>Hint for Exercise 8</summary>

One approach: use `WHERE product NOT IN (SELECT DISTINCT product FROM Sales WHERE region = 'West')`. You need to search the full Sales table for products that are absent from the West-region subset.

</details>

---

## How Did You Do?

- **Exercises 1-3:** These cover SELECT, WHERE, GROUP BY, and ORDER BY — the fundamentals.
- **Exercises 4-6:** These require combining multiple concepts together.
- **Exercises 7-8:** These use CTEs and subqueries for more advanced analysis.

If you got through all eight, you have a solid foundation in T-SQL. In the next module, we'll move into more advanced topics and real-world analysis patterns.
