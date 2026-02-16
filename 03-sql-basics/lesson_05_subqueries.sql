-- ============================================================
-- Lesson 5: Subqueries and CTEs
-- ============================================================
-- Subqueries are queries inside queries.
-- CTEs (Common Table Expressions) are named subqueries that
-- make complex queries easier to read and write.
-- ============================================================

USE DataAnalytics101;
GO

-- ============================================================
-- 1. Subqueries in WHERE
-- ============================================================

-- First, let's see what the average salary is (for reference)
SELECT AVG(salary) AS avg_salary FROM Employees;

-- Now find employees who earn MORE than the average salary
-- The subquery (in parentheses) calculates the average first,
-- then the outer query filters employees by that number
SELECT first_name, last_name, department, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees)
ORDER BY salary DESC;

-- Find employees who earn LESS than the average
SELECT first_name, last_name, department, salary
FROM Employees
WHERE salary < (SELECT AVG(salary) FROM Employees)
ORDER BY salary;

-- Find products with above-average revenue per sale
SELECT product, revenue
FROM Sales
WHERE revenue > (SELECT AVG(revenue) FROM Sales)
ORDER BY revenue DESC;


-- ============================================================
-- 2. Subqueries with IN
-- ============================================================

-- Find all products that have been sold in the North region
-- The subquery returns a LIST of products, and IN checks the list
SELECT DISTINCT product
FROM Sales
WHERE product IN (
    SELECT product FROM Sales WHERE region = 'North'
);

-- Find employees in departments that have an average salary above $75,000
SELECT first_name, last_name, department, salary
FROM Employees
WHERE department IN (
    SELECT department
    FROM Employees
    GROUP BY department
    HAVING AVG(salary) > 75000
);


-- ============================================================
-- 3. Subqueries in FROM
-- ============================================================

-- Calculate average revenue per region, then find the highest
-- The inner query creates a "temporary table" of region averages
-- The outer query finds the max of those averages
SELECT MAX(avg_revenue) AS highest_regional_avg
FROM (
    SELECT region, AVG(revenue) AS avg_revenue
    FROM Sales
    GROUP BY region
) AS region_stats;    -- You MUST give the subquery an alias

-- Show department stats, then filter to "large" departments
SELECT dept_name, emp_count, avg_salary
FROM (
    SELECT
        department AS dept_name,
        COUNT(*)   AS emp_count,
        AVG(salary) AS avg_salary
    FROM Employees
    GROUP BY department
) AS dept_stats
WHERE emp_count >= 3     -- Only departments with 3+ employees
ORDER BY avg_salary DESC;


-- ============================================================
-- 4. CTEs — the cleaner way to write subqueries
-- ============================================================

-- Same as the "above average salary" query, but using a CTE
-- WITH defines the CTE, then we use it like a regular table
WITH AvgSalary AS (
    -- Step 1: Calculate the average salary
    SELECT AVG(salary) AS avg_sal
    FROM Employees
)
-- Step 2: Use that value to filter employees
SELECT e.first_name, e.last_name, e.department, e.salary
FROM Employees e, AvgSalary a
WHERE e.salary > a.avg_sal
ORDER BY e.salary DESC;


-- ============================================================
-- 5. CTE that calculates regional totals, then filters
-- ============================================================

-- Find regions with total revenue above the overall average revenue per region
WITH RegionalTotals AS (
    -- Step 1: Get total revenue for each region
    SELECT
        region,
        SUM(revenue) AS total_revenue,
        COUNT(*)     AS num_sales
    FROM Sales
    GROUP BY region
)
-- Step 2: Show all regional totals, sorted from highest to lowest
SELECT
    region,
    total_revenue,
    num_sales
FROM RegionalTotals
WHERE total_revenue > 4000     -- Only show regions with revenue over $4,000
ORDER BY total_revenue DESC;


-- ============================================================
-- 6. CTE that ranks products by total revenue
-- ============================================================

WITH ProductRevenue AS (
    -- Step 1: Calculate total revenue per product
    SELECT
        product,
        category,
        SUM(revenue)  AS total_revenue,
        SUM(quantity)  AS total_units_sold,
        COUNT(*)       AS number_of_sales
    FROM Sales
    GROUP BY product, category
)
-- Step 2: Display the results, ranked by total revenue
SELECT
    product,
    category,
    total_revenue,
    total_units_sold,
    number_of_sales
FROM ProductRevenue
ORDER BY total_revenue DESC;


-- ============================================================
-- 7. Multiple CTEs chained together
-- ============================================================

-- Find products whose total revenue is above the average product revenue
WITH
    -- Step 1: Calculate total revenue per product
    ProductTotals AS (
        SELECT
            product,
            SUM(revenue) AS total_revenue
        FROM Sales
        GROUP BY product
    ),
    -- Step 2: Calculate the average of those product totals
    AvgProductRevenue AS (
        SELECT AVG(total_revenue) AS avg_revenue
        FROM ProductTotals
    )
-- Step 3: Show products above the average
SELECT
    pt.product,
    pt.total_revenue,
    apr.avg_revenue AS overall_avg_revenue
FROM ProductTotals pt, AvgProductRevenue apr
WHERE pt.total_revenue > apr.avg_revenue
ORDER BY pt.total_revenue DESC;


-- ============================================================
-- 8. Practical example: Department salary analysis
-- ============================================================

-- For each department, show how its average salary compares
-- to the company-wide average
WITH
    CompanyAvg AS (
        SELECT AVG(salary) AS company_avg_salary
        FROM Employees
    ),
    DeptAvg AS (
        SELECT
            department,
            AVG(salary)  AS dept_avg_salary,
            COUNT(*)     AS headcount
        FROM Employees
        GROUP BY department
    )
SELECT
    d.department,
    d.headcount,
    d.dept_avg_salary,
    c.company_avg_salary,
    (d.dept_avg_salary - c.company_avg_salary) AS difference_from_avg
FROM DeptAvg d, CompanyAvg c
ORDER BY d.dept_avg_salary DESC;


-- ============================================================
-- Try it yourself!
-- ============================================================
-- 1. Find all sales where the revenue is above the average sale revenue.
-- 2. Use a CTE to calculate the total orders per state from Customers,
--    then show only states with more than 15 total orders.
-- 3. Write a subquery to find which categories contain products that
--    have been sold in all four regions.
-- 4. Use multiple CTEs to find the employee with the highest salary
--    in the department that has the lowest average salary.
