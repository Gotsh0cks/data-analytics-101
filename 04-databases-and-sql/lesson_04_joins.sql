-- ============================================================
-- Lesson 4: JOINs
-- ============================================================
-- JOINs combine data from two tables based on a shared column.
-- Since our main tables don't share foreign keys, we'll create
-- small demo tables to illustrate how JOINs work.
-- ============================================================

USE DataAnalytics101;
GO

-- ============================================================
-- SETUP: Create demo tables for JOIN practice
-- ============================================================

-- Drop the demo tables if they already exist (safe to re-run)
IF OBJECT_ID('OrderItems', 'U') IS NOT NULL DROP TABLE OrderItems;
IF OBJECT_ID('Products', 'U') IS NOT NULL DROP TABLE Products;
IF OBJECT_ID('DeptLookup', 'U') IS NOT NULL DROP TABLE DeptLookup;
GO

-- A small Products table with product IDs and names
CREATE TABLE Products (
    product_id   INT PRIMARY KEY,      -- Unique product identifier
    product_name VARCHAR(50),          -- Product display name
    price        DECIMAL(10,2)         -- Product price
);

-- A small OrderItems table that references Products
CREATE TABLE OrderItems (
    order_id    INT,                   -- Order number
    product_id  INT,                   -- Links to Products table
    quantity    INT                    -- How many were ordered
);

-- A department lookup table (for a second JOIN example)
CREATE TABLE DeptLookup (
    dept_name   VARCHAR(50) PRIMARY KEY,   -- Department name
    building    VARCHAR(50),               -- Office building
    floor_num   INT                        -- Floor number
);
GO

-- Insert product data
-- Notice: product_id 5 exists but won't have any orders (useful for LEFT JOIN)
INSERT INTO Products (product_id, product_name, price) VALUES
    (1, 'Wireless Mouse',    29.99),
    (2, 'USB-C Hub',         49.99),
    (3, 'Laptop Stand',      39.99),
    (4, 'Webcam HD',         69.99),
    (5, 'Monitor Light',     44.99);   -- This product has no orders

-- Insert order data
-- Notice: product_id 99 doesn't exist in Products (useful for understanding JOINs)
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES
    (1001, 1, 2),     -- Order 1001: 2 Wireless Mice
    (1001, 3, 1),     -- Order 1001: 1 Laptop Stand
    (1002, 2, 3),     -- Order 1002: 3 USB-C Hubs
    (1002, 4, 1),     -- Order 1002: 1 Webcam HD
    (1003, 1, 1),     -- Order 1003: 1 Wireless Mouse
    (1003, 2, 2),     -- Order 1003: 2 USB-C Hubs
    (1004, 99, 1);    -- Order 1004: references a product that doesn't exist!

-- Insert department locations
INSERT INTO DeptLookup (dept_name, building, floor_num) VALUES
    ('Engineering', 'Tech Tower',   3),
    ('Sales',       'Main Campus',  1),
    ('Marketing',   'Main Campus',  2),
    ('Finance',     'Main Campus',  4),
    ('HR',          'Main Campus',  1),
    ('Operations',  'Warehouse',    1);  -- No employees in this dept
GO


-- ============================================================
-- 1. INNER JOIN — only matching rows from both tables
-- ============================================================

-- Show order details with product names
-- Only rows where product_id matches in BOTH tables appear
SELECT
    o.order_id,
    p.product_name,
    p.price,
    o.quantity,
    (p.price * o.quantity) AS line_total   -- Calculate the total for this line
FROM OrderItems AS o
INNER JOIN Products AS p ON o.product_id = p.product_id;

-- Notice two things:
--   1. "Monitor Light" (product_id 5) doesn't appear — it has no orders
--   2. Order 1004 (product_id 99) doesn't appear — that product doesn't exist


-- ============================================================
-- 2. LEFT JOIN — all rows from the left table
-- ============================================================

-- Show ALL products, even ones that haven't been ordered
-- Products without orders will have NULL in the order columns
SELECT
    p.product_name,
    p.price,
    o.order_id,
    o.quantity
FROM Products AS p                                      -- Left table: ALL products kept
LEFT JOIN OrderItems AS o ON p.product_id = o.product_id;  -- Right table: orders matched where possible

-- "Monitor Light" now appears with NULL for order_id and quantity
-- because it exists in Products but has no matching orders


-- ============================================================
-- 3. LEFT JOIN to find "missing" matches
-- ============================================================

-- Which products have NEVER been ordered?
-- Use LEFT JOIN, then check for NULLs in the right table
SELECT
    p.product_name,
    p.price
FROM Products AS p
LEFT JOIN OrderItems AS o ON p.product_id = o.product_id
WHERE o.order_id IS NULL;    -- Only keep rows with no match

-- This is a very common analytics pattern:
-- "Show me items in table A that don't exist in table B"


-- ============================================================
-- 4. JOIN with our Employees table and DeptLookup
-- ============================================================

-- Show employee names with their department's building and floor
SELECT
    e.first_name,
    e.last_name,
    e.department,
    d.building,
    d.floor_num
FROM Employees AS e
INNER JOIN DeptLookup AS d ON e.department = d.dept_name;

-- LEFT JOIN version: show ALL employees, even if their dept isn't in the lookup
SELECT
    e.first_name,
    e.last_name,
    e.department,
    d.building,
    d.floor_num
FROM Employees AS e
LEFT JOIN DeptLookup AS d ON e.department = d.dept_name;


-- ============================================================
-- 5. JOIN with aggregations
-- ============================================================
-- You can combine JOINs with GROUP BY for powerful summaries

-- Total quantity ordered per product (with product names)
SELECT
    p.product_name,
    SUM(o.quantity) AS total_quantity_ordered
FROM Products AS p
INNER JOIN OrderItems AS o ON p.product_id = o.product_id
GROUP BY p.product_name
ORDER BY total_quantity_ordered DESC;

-- Number of employees per building
SELECT
    d.building,
    COUNT(*) AS employee_count
FROM Employees AS e
INNER JOIN DeptLookup AS d ON e.department = d.dept_name
GROUP BY d.building
ORDER BY employee_count DESC;


-- ============================================================
-- 6. Table aliases — shorter and cleaner
-- ============================================================

-- Without aliases — works but verbose
SELECT OrderItems.order_id, Products.product_name, OrderItems.quantity
FROM OrderItems
INNER JOIN Products ON OrderItems.product_id = Products.product_id;

-- With aliases — same result, much easier to read
SELECT o.order_id, p.product_name, o.quantity
FROM OrderItems o                               -- "o" is short for OrderItems
INNER JOIN Products p ON o.product_id = p.product_id;  -- "p" is short for Products


-- ============================================================
-- CLEANUP (optional)
-- ============================================================
-- Uncomment these lines if you want to remove the demo tables:
-- DROP TABLE OrderItems;
-- DROP TABLE Products;
-- DROP TABLE DeptLookup;


-- ============================================================
-- Try it yourself!
-- ============================================================
-- 1. Write an INNER JOIN that shows each order's product name and line total.
-- 2. Use a LEFT JOIN to show all departments from DeptLookup, even those
--    with no employees. Which department has no employees?
-- 3. Find the total revenue (price * quantity) per product using a JOIN.
-- 4. Which building has the highest average employee salary? (JOIN + GROUP BY)
