-- ============================================================
-- Lesson 1: SELECT and FROM
-- ============================================================
-- Make sure you've run setup_database.sql first!
-- Run each query one at a time to see the results.
-- ============================================================

-- Switch to our practice database
USE DataAnalytics101;
GO

-- ============================================================
-- 1. SELECT * (all columns)
-- ============================================================
-- The asterisk (*) means "give me every column."
-- Great for exploring, but avoid it in production queries.

-- Get all columns from the Sales table
SELECT * FROM Sales;

-- Get all columns from the Employees table
SELECT * FROM Employees;

-- Get all columns from the Customers table
SELECT * FROM Customers;


-- ============================================================
-- 2. Selecting specific columns
-- ============================================================
-- List only the columns you care about, separated by commas.
-- This is faster and easier to read.

-- Get just the product name and revenue from Sales
SELECT product, revenue FROM Sales;

-- Get employee names and their departments
SELECT first_name, last_name, department FROM Employees;

-- Get customer names and how much they've spent
SELECT first_name, last_name, total_spent FROM Customers;


-- ============================================================
-- 3. Column aliases with AS
-- ============================================================
-- AS lets you rename a column in the output.
-- It doesn't change the actual table — just the display name.

-- Give the "revenue" column a friendlier name
SELECT product, revenue AS total_sale FROM Sales;

-- You can alias multiple columns at once
SELECT
    first_name AS [First Name],     -- Square brackets let you use spaces
    last_name  AS [Last Name],
    salary     AS [Annual Salary]
FROM Employees;

-- Aliases are especially useful for calculated columns (we'll cover these later)
SELECT
    product,
    quantity,
    unit_price,
    revenue AS [Total Revenue]
FROM Sales;


-- ============================================================
-- 4. SELECT TOP N
-- ============================================================
-- TOP limits how many rows come back.
-- Useful when you just want a quick peek at the data.

-- Get only the first 10 rows from Sales
SELECT TOP 10 * FROM Sales;

-- Get just the first 5 products and their prices
SELECT TOP 5 product, unit_price FROM Sales;

-- You can also use TOP with a percentage (less common, but good to know)
-- This returns the top 25% of rows
SELECT TOP 25 PERCENT * FROM Sales;


-- ============================================================
-- 5. SELECT DISTINCT
-- ============================================================
-- DISTINCT removes duplicate values from the results.
-- Think of it as "give me the unique values only."

-- Get unique product names (no repeats)
SELECT DISTINCT product FROM Sales;

-- Get unique regions
SELECT DISTINCT region FROM Sales;

-- Get unique categories
SELECT DISTINCT category FROM Sales;

-- Get unique departments from the Employees table
SELECT DISTINCT department FROM Employees;

-- Get unique states from the Customers table
SELECT DISTINCT state FROM Customers;

-- DISTINCT with multiple columns gives unique COMBINATIONS
-- Each row in the result is a unique pairing of category and region
SELECT DISTINCT category, region FROM Sales;


-- ============================================================
-- Try it yourself!
-- ============================================================
-- 1. Select just the email and city columns from the Customers table.
-- 2. Use an alias to rename "total_orders" to "Number of Orders."
-- 3. Get the first 3 rows from the Employees table.
-- 4. Find all the unique cities in the Employees table.
-- 5. Find all unique combinations of department and city from Employees.
