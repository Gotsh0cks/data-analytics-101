-- ============================================================
-- Lesson 2: WHERE and ORDER BY
-- ============================================================
-- These queries show you how to filter rows and sort results.
-- Run each one individually to see what it returns.
-- ============================================================

USE DataAnalytics101;
GO

-- ============================================================
-- 1. Basic WHERE — filtering rows
-- ============================================================

-- Only show sales from the North region
SELECT * FROM Sales
WHERE region = 'North';

-- Only show Electronics products
SELECT * FROM Sales
WHERE category = 'Electronics';

-- Only show employees in the Engineering department
SELECT first_name, last_name, department, salary
FROM Employees
WHERE department = 'Engineering';

-- Customers from Texas
SELECT first_name, last_name, city
FROM Customers
WHERE state = 'TX';


-- ============================================================
-- 2. Comparison operators
-- ============================================================

-- Sales where revenue is greater than $1,000
SELECT product, region, revenue
FROM Sales
WHERE revenue > 1000;

-- Employees earning less than $60,000
SELECT first_name, last_name, salary
FROM Employees
WHERE salary < 60000;

-- Sales where quantity is at least 10
SELECT product, quantity, revenue
FROM Sales
WHERE quantity >= 10;

-- Sales where the product is NOT a Laptop
SELECT product, revenue
FROM Sales
WHERE product <> 'Laptop';


-- ============================================================
-- 3. AND / OR — combining conditions
-- ============================================================

-- Electronics sold in the North region (both must be true)
SELECT product, region, revenue
FROM Sales
WHERE category = 'Electronics' AND region = 'North';

-- Sales in the North OR South region (either can be true)
SELECT product, region, revenue
FROM Sales
WHERE region = 'North' OR region = 'South';

-- Use parentheses when mixing AND and OR to be explicit
-- This finds Electronics sold in either the North or South region
SELECT product, category, region, revenue
FROM Sales
WHERE category = 'Electronics'
  AND (region = 'North' OR region = 'South');

-- Employees in Sales department earning over $60,000
SELECT first_name, last_name, department, salary
FROM Employees
WHERE department = 'Sales' AND salary > 60000;


-- ============================================================
-- 4. IN — matching a list of values
-- ============================================================

-- Sales in the North, South, or East regions
-- Much cleaner than writing three OR conditions!
SELECT product, region, revenue
FROM Sales
WHERE region IN ('North', 'South', 'East');

-- Employees in Engineering or Finance
SELECT first_name, last_name, department
FROM Employees
WHERE department IN ('Engineering', 'Finance');

-- Specific products
SELECT product, category, revenue
FROM Sales
WHERE product IN ('Laptop', 'Monitor', 'Keyboard');


-- ============================================================
-- 5. LIKE — pattern matching
-- ============================================================

-- Products that start with "Desk"
-- The % means "anything can follow"
SELECT product, category, revenue
FROM Sales
WHERE product LIKE 'Desk%';

-- Employees whose last name ends with "son"
SELECT first_name, last_name
FROM Employees
WHERE last_name LIKE '%son';

-- Employees whose first name contains "a" anywhere
SELECT first_name, last_name
FROM Employees
WHERE first_name LIKE '%a%';

-- Customers with email addresses containing "email"
SELECT first_name, last_name, email
FROM Customers
WHERE email LIKE '%email%';


-- ============================================================
-- 6. BETWEEN — range filtering
-- ============================================================

-- Sales from January 2024 through March 2024
SELECT sale_date, product, revenue
FROM Sales
WHERE sale_date BETWEEN '2024-01-01' AND '2024-03-31';

-- Employees earning between $50,000 and $80,000 (inclusive)
SELECT first_name, last_name, salary
FROM Employees
WHERE salary BETWEEN 50000 AND 80000;

-- Customers who signed up in 2023
SELECT first_name, last_name, signup_date
FROM Customers
WHERE signup_date BETWEEN '2023-01-01' AND '2023-12-31';

-- Sales with revenue between $500 and $1,500
SELECT product, region, revenue
FROM Sales
WHERE revenue BETWEEN 500 AND 1500;


-- ============================================================
-- 7. IS NULL / IS NOT NULL
-- ============================================================
-- Our sample data doesn't have NULLs, but these are essential
-- in real-world databases. Here's the syntax:

-- Find any customers with no email (would return rows if NULLs existed)
SELECT * FROM Customers
WHERE email IS NULL;

-- Find all customers who DO have an email
SELECT first_name, last_name, email
FROM Customers
WHERE email IS NOT NULL;

-- IMPORTANT: Never write "email = NULL" — it won't work!
-- Always use IS NULL or IS NOT NULL.


-- ============================================================
-- 8. ORDER BY — sorting results
-- ============================================================

-- Sort employees by salary, lowest first (ASC is the default)
SELECT first_name, last_name, salary
FROM Employees
ORDER BY salary;

-- Sort employees by salary, highest first
SELECT first_name, last_name, salary
FROM Employees
ORDER BY salary DESC;

-- Sort sales by date, most recent first
SELECT sale_date, product, revenue
FROM Sales
ORDER BY sale_date DESC;

-- Sort customers alphabetically by last name
SELECT first_name, last_name, city, state
FROM Customers
ORDER BY last_name ASC;

-- Sort by multiple columns:
-- First by department (A-Z), then by salary (highest first) within each dept
SELECT first_name, last_name, department, salary
FROM Employees
ORDER BY department ASC, salary DESC;


-- ============================================================
-- 9. Putting it all together
-- ============================================================

-- High-value Electronics sales, sorted by revenue
SELECT product, region, quantity, revenue
FROM Sales
WHERE category = 'Electronics' AND revenue > 500
ORDER BY revenue DESC;

-- Top 5 highest-paid employees who were hired after 2019
SELECT TOP 5 first_name, last_name, salary, hire_date
FROM Employees
WHERE hire_date > '2019-12-31'
ORDER BY salary DESC;

-- Customers in FL or TX who have spent over $500, sorted by spending
SELECT first_name, last_name, state, total_spent
FROM Customers
WHERE state IN ('FL', 'TX') AND total_spent > 500
ORDER BY total_spent DESC;


-- ============================================================
-- Try it yourself!
-- ============================================================
-- 1. Find all sales of the product "Keyboard."
-- 2. List employees hired in 2020, sorted by hire date.
-- 3. Find customers who have placed more than 10 orders.
-- 4. List sales in the "Supplies" category with revenue under $300.
-- 5. Find employees whose city starts with "S" and earn over $70,000.
