USE DataAnalytics101;
GO

-- ============================================================
-- Module 4 Exercise Solutions
-- ============================================================
-- Try the exercises yourself before using this file.
-- Run one query at a time so you can connect each answer to
-- the exercise question.
-- ============================================================

-- ============================================================
-- Exercise 1: Employees in the Sales Department
-- ============================================================

SELECT
    first_name,
    last_name,
    job_title,
    CAST(salary AS INT) AS salary
FROM Employees
WHERE department = 'Sales'
ORDER BY employee_id;


-- ============================================================
-- Exercise 2: Top 5 Highest-Paid Employees
-- ============================================================

SELECT TOP 5
    first_name,
    last_name,
    department,
    CAST(salary AS INT) AS salary
FROM Employees
ORDER BY salary DESC;


-- ============================================================
-- Exercise 3: Total Revenue by Product
-- ============================================================

SELECT
    product,
    CAST(SUM(revenue) AS DECIMAL(10,2)) AS total_revenue
FROM Sales
GROUP BY product
ORDER BY total_revenue DESC;


-- ============================================================
-- Exercise 4: Customer Signups by Year
-- ============================================================

SELECT
    YEAR(signup_date) AS signup_year,
    COUNT(*) AS customer_count
FROM Customers
GROUP BY YEAR(signup_date)
ORDER BY signup_year;


-- ============================================================
-- Exercise 5: Above-Average Earners
-- ============================================================

-- First, check the company average salary.
SELECT CAST(AVG(salary) AS INT) AS company_average_salary
FROM Employees;

-- Then use that average in a subquery.
SELECT
    first_name,
    last_name,
    department,
    CAST(salary AS INT) AS salary
FROM Employees
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees
)
ORDER BY salary DESC;


-- ============================================================
-- Exercise 6: Region with the Most Sales
-- ============================================================

SELECT
    region,
    COUNT(*) AS transaction_count
FROM Sales
GROUP BY region
ORDER BY transaction_count DESC, region ASC;


-- ============================================================
-- Exercise 7: Department with the Highest Average Salary (CTE)
-- ============================================================

WITH DepartmentAverages AS (
    SELECT
        department,
        AVG(salary) AS avg_salary
    FROM Employees
    GROUP BY department
)
SELECT TOP 1
    department,
    CAST(avg_salary AS INT) AS avg_salary
FROM DepartmentAverages
ORDER BY avg_salary DESC;


-- ============================================================
-- Exercise 8 (BONUS): Products Never Sold in the West
-- ============================================================

SELECT p.product
FROM (
    SELECT DISTINCT product
    FROM Sales
    WHERE product IS NOT NULL
) AS p
WHERE NOT EXISTS (
    SELECT 1
    FROM Sales AS west_sales
    WHERE west_sales.product = p.product
      AND west_sales.region = 'West'
)
ORDER BY p.product;


-- ============================================================
-- Exercise 9: Python + SQL Query
-- ============================================================
-- This is the query the Python solution loads into pandas.

SELECT
    category,
    CAST(SUM(revenue) AS DECIMAL(10,2)) AS total_revenue
FROM Sales
GROUP BY category
ORDER BY total_revenue DESC;
