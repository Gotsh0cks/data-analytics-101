-- ============================================================
-- Lesson 3: Aggregations
-- ============================================================
-- Now we're getting into the good stuff! Aggregations let you
-- summarize data — counts, totals, averages, and more.
-- ============================================================

USE DataAnalytics101;
GO

-- ============================================================
-- 1. Basic aggregate functions
-- ============================================================

-- How many rows are in the Sales table?
SELECT COUNT(*) AS total_rows FROM Sales;

-- What is the total revenue across all sales?
SELECT SUM(revenue) AS total_revenue FROM Sales;

-- What is the average unit price?
SELECT AVG(unit_price) AS avg_price FROM Sales;

-- What is the cheapest product price?
SELECT MIN(unit_price) AS lowest_price FROM Sales;

-- What is the most expensive product price?
SELECT MAX(unit_price) AS highest_price FROM Sales;

-- You can put multiple aggregates in one query
SELECT
    COUNT(*)         AS total_sales,
    SUM(revenue)     AS total_revenue,
    AVG(revenue)     AS avg_revenue,
    MIN(revenue)     AS smallest_sale,
    MAX(revenue)     AS largest_sale
FROM Sales;


-- ============================================================
-- 2. COUNT(*) vs COUNT(column_name)
-- ============================================================
-- COUNT(*) counts all rows.
-- COUNT(column) counts only rows where that column is not NULL.
-- In our data both return 20 because we have no NULLs.

SELECT COUNT(*) AS count_all_rows FROM Customers;
SELECT COUNT(email) AS count_non_null_emails FROM Customers;


-- ============================================================
-- 3. GROUP BY — totals for each group
-- ============================================================

-- Total revenue for EACH region
-- GROUP BY creates one row per region
SELECT
    region,
    SUM(revenue) AS total_revenue
FROM Sales
GROUP BY region;

-- Average salary by department
SELECT
    department,
    AVG(salary) AS avg_salary
FROM Employees
GROUP BY department;

-- Number of sales per product
SELECT
    product,
    COUNT(*) AS number_of_sales
FROM Sales
GROUP BY product;

-- Number of customers per state
SELECT
    state,
    COUNT(*) AS customer_count
FROM Customers
GROUP BY state;

-- Revenue by category — with multiple aggregates
SELECT
    category,
    COUNT(*)       AS num_sales,
    SUM(revenue)   AS total_revenue,
    AVG(revenue)   AS avg_revenue,
    MIN(revenue)   AS min_sale,
    MAX(revenue)   AS max_sale
FROM Sales
GROUP BY category;


-- ============================================================
-- 4. HAVING — filter groups (not rows)
-- ============================================================

-- Only show products with MORE than 3 sales
SELECT
    product,
    COUNT(*) AS number_of_sales
FROM Sales
GROUP BY product
HAVING COUNT(*) > 3;

-- Only show regions with total revenue over $3,000
SELECT
    region,
    SUM(revenue) AS total_revenue
FROM Sales
GROUP BY region
HAVING SUM(revenue) > 3000;

-- Departments with an average salary above $75,000
SELECT
    department,
    AVG(salary) AS avg_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > 75000;


-- ============================================================
-- 5. WHERE vs HAVING — used together
-- ============================================================

-- Total revenue by region, but only for Electronics,
-- and only show regions where that total is over $1,000.

-- Here's what happens step by step:
--   1. WHERE filters to Electronics rows only
--   2. GROUP BY groups those rows by region
--   3. HAVING keeps only groups with total > 1,000
--   4. ORDER BY sorts the results
SELECT
    region,
    SUM(revenue) AS total_revenue
FROM Sales
WHERE category = 'Electronics'       -- Filter ROWS first
GROUP BY region                      -- Then group
HAVING SUM(revenue) > 1000          -- Then filter GROUPS
ORDER BY total_revenue DESC;         -- Then sort


-- ============================================================
-- 6. ORDER BY with aggregations
-- ============================================================

-- Products ranked by total revenue, highest first
SELECT
    product,
    SUM(revenue) AS total_revenue
FROM Sales
GROUP BY product
ORDER BY total_revenue DESC;

-- Departments ranked by headcount
SELECT
    department,
    COUNT(*) AS employee_count
FROM Employees
GROUP BY department
ORDER BY employee_count DESC;

-- Min and max salary per department, sorted by department name
SELECT
    department,
    MIN(salary) AS lowest_salary,
    MAX(salary) AS highest_salary
FROM Employees
GROUP BY department
ORDER BY department;


-- ============================================================
-- Try it yourself!
-- ============================================================
-- 1. What is the total quantity sold across all sales?
-- 2. How many employees are in each city?
-- 3. What is the average total_spent per state in the Customers table?
-- 4. Which products have total revenue over $2,000?
-- 5. What is the total revenue per month? (Hint: try grouping by sale_date
--    or look into MONTH() and YEAR() functions)
