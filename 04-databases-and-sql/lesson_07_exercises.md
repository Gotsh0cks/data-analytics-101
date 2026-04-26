# Module 4: Practice Exercises

Test your T-SQL skills with these practice problems. Each one builds on what you learned in the lessons. Try to write the query yourself before looking at the hints.

Make sure you're connected to the `DataAnalytics101` database before running your queries.

```sql
USE DataAnalytics101;
```

## Support Ladder

Try the exercises on your own first. When you need help, use these in order:

1. Start with [hints](hints/lesson_07_hints.md) for a small nudge.
2. Check [expected outputs](expected_outputs/lesson_07_expected_outputs.md) to see whether your result matches.
3. Compare with the [SQL solutions](solutions/lesson_07_solutions.sql) or the [Python + SQL solution](solutions/lesson_07_python_sql_solution.py) only after you have tried the problem.

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

How many customers signed up in each year? Show the year and the count of customers.

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

Find products that have never been sold in the "West" region.

---

## Exercise 9: Python + SQL

Write a Python script that:

1. Connects to SQL Server using `pyodbc`
2. Queries the Sales table for total revenue by category
3. Prints the results as a pandas DataFrame
4. Creates a bar chart of the results using matplotlib

See `lesson_06_python_and_sql.py` for connection examples.

---

## How Did You Do?

- **Exercises 1-3:** These cover SELECT, WHERE, GROUP BY, and ORDER BY the fundamentals.
- **Exercises 4-6:** These require combining multiple concepts together.
- **Exercises 7-8:** These use CTEs, joins, and subqueries for more advanced analysis.
- **Exercise 9:** This connects SQL results to Python, pandas, and a chart.

If you got through these, you have a solid foundation in T-SQL and the Python + SQL workflow.
