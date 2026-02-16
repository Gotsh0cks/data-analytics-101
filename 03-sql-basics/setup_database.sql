-- ============================================================
-- Module 3: Setup Script
-- ============================================================
-- This script creates the DataAnalytics101 database and three
-- practice tables: Sales, Employees, and Customers.
-- Run this entire script in Azure Data Studio before starting
-- the lessons.
-- ============================================================

-- ------------------------------------------------------------
-- STEP 1: Create the database
-- ------------------------------------------------------------
-- We check if the database already exists first so you can
-- safely re-run this script without errors.

IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'DataAnalytics101')
BEGIN
    CREATE DATABASE DataAnalytics101;
END
GO

-- Switch to our new database
USE DataAnalytics101;
GO

-- ------------------------------------------------------------
-- STEP 2: Create the Sales table
-- ------------------------------------------------------------
-- This table stores individual sales transactions.
-- IDENTITY means sale_id auto-increments (1, 2, 3, ...).
-- PRIMARY KEY means each sale_id is unique and identifies the row.

-- Drop the table if it already exists (so you can re-run this script cleanly)
IF OBJECT_ID('Sales', 'U') IS NOT NULL DROP TABLE Sales;

CREATE TABLE Sales (
    sale_id     INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-incrementing unique ID
    sale_date   DATE,                            -- When the sale happened
    product     VARCHAR(50),                     -- Name of the product sold
    category    VARCHAR(50),                     -- Product category (e.g., Electronics)
    region      VARCHAR(20),                     -- Sales region (North, South, East, West)
    quantity    INT,                             -- How many units were sold
    unit_price  DECIMAL(10,2),                   -- Price per unit in dollars
    revenue     DECIMAL(10,2)                    -- Total revenue (quantity * unit_price)
);
GO

-- ------------------------------------------------------------
-- STEP 3: Create the Employees table
-- ------------------------------------------------------------
-- This table stores information about company employees.

IF OBJECT_ID('Employees', 'U') IS NOT NULL DROP TABLE Employees;

CREATE TABLE Employees (
    employee_id  INT PRIMARY KEY,       -- Unique employee ID
    first_name   VARCHAR(50),           -- Employee's first name
    last_name    VARCHAR(50),           -- Employee's last name
    department   VARCHAR(50),           -- Department they work in
    job_title    VARCHAR(100),          -- Their job title
    salary       DECIMAL(10,2),         -- Annual salary in dollars
    hire_date    DATE,                  -- Date they were hired
    city         VARCHAR(50),           -- City where they work
    state        VARCHAR(2)             -- Two-letter state code
);
GO

-- ------------------------------------------------------------
-- STEP 4: Create the Customers table
-- ------------------------------------------------------------
-- This table stores customer information and order summaries.

IF OBJECT_ID('Customers', 'U') IS NOT NULL DROP TABLE Customers;

CREATE TABLE Customers (
    customer_id   INT PRIMARY KEY,      -- Unique customer ID
    first_name    VARCHAR(50),          -- Customer's first name
    last_name     VARCHAR(50),          -- Customer's last name
    email         VARCHAR(100),         -- Customer's email address
    city          VARCHAR(50),          -- City they live in
    state         VARCHAR(2),           -- Two-letter state code
    signup_date   DATE,                 -- When they created their account
    total_orders  INT,                  -- How many orders they've placed
    total_spent   DECIMAL(10,2)         -- Total amount they've spent
);
GO

-- ============================================================
-- STEP 5: Insert sample data into Sales
-- ============================================================
-- These 20 rows give us enough data to practice with.
-- The data includes different products, categories, and regions.

INSERT INTO Sales (sale_date, product, category, region, quantity, unit_price, revenue)
VALUES
    ('2024-01-05', 'Laptop',         'Electronics', 'North', 2, 999.99, 1999.98),
    ('2024-01-08', 'Desk Chair',     'Furniture',   'South', 5, 249.99, 1249.95),
    ('2024-01-12', 'Notebook Pack',  'Supplies',    'East',  20, 12.99,  259.80),
    ('2024-01-15', 'Monitor',        'Electronics', 'West',  3, 349.99, 1049.97),
    ('2024-01-20', 'Laptop',         'Electronics', 'East',  1, 999.99,  999.99),
    ('2024-02-02', 'Desk Chair',     'Furniture',   'North', 4, 249.99,  999.96),
    ('2024-02-10', 'Keyboard',       'Electronics', 'South', 10, 79.99,  799.90),
    ('2024-02-14', 'Pen Set',        'Supplies',    'West',  15, 8.99,   134.85),
    ('2024-02-20', 'Standing Desk',  'Furniture',   'East',  2, 599.99, 1199.98),
    ('2024-03-01', 'Laptop',         'Electronics', 'South', 3, 999.99, 2999.97),
    ('2024-03-05', 'Webcam',         'Electronics', 'North', 8, 69.99,  559.92),
    ('2024-03-10', 'Notebook Pack',  'Supplies',    'South', 25, 12.99,  324.75),
    ('2024-03-15', 'Monitor',        'Electronics', 'East',  2, 349.99,  699.98),
    ('2024-03-18', 'Desk Chair',     'Furniture',   'West',  3, 249.99,  749.97),
    ('2024-03-22', 'Keyboard',       'Electronics', 'North', 6, 79.99,  479.94),
    ('2024-04-01', 'Standing Desk',  'Furniture',   'South', 1, 599.99,  599.99),
    ('2024-04-05', 'Pen Set',        'Supplies',    'East',  30, 8.99,   269.70),
    ('2024-04-10', 'Laptop',         'Electronics', 'West',  2, 999.99, 1999.98),
    ('2024-04-15', 'Webcam',         'Electronics', 'South', 5, 69.99,  349.95),
    ('2024-04-20', 'Monitor',        'Electronics', 'North', 4, 349.99, 1399.96);
GO

-- ============================================================
-- STEP 6: Insert sample data into Employees
-- ============================================================
-- 20 employees across different departments.

INSERT INTO Employees (employee_id, first_name, last_name, department, job_title, salary, hire_date, city, state)
VALUES
    (1,  'Sarah',   'Johnson',  'Sales',       'Sales Representative',     55000.00, '2020-03-15', 'Chicago',       'IL'),
    (2,  'Michael', 'Chen',     'Engineering', 'Software Engineer',        92000.00, '2019-07-01', 'San Francisco', 'CA'),
    (3,  'Emily',   'Davis',    'Marketing',   'Marketing Coordinator',    48000.00, '2021-01-10', 'New York',      'NY'),
    (4,  'James',   'Wilson',   'Sales',       'Sales Manager',            78000.00, '2018-05-20', 'Chicago',       'IL'),
    (5,  'Maria',   'Garcia',   'Engineering', 'Senior Software Engineer', 115000.00, '2017-09-12', 'San Francisco', 'CA'),
    (6,  'David',   'Brown',    'HR',          'HR Specialist',            52000.00, '2020-11-03', 'Dallas',        'TX'),
    (7,  'Lisa',    'Martinez', 'Marketing',   'Marketing Manager',        75000.00, '2019-02-28', 'New York',      'NY'),
    (8,  'Robert',  'Taylor',   'Engineering', 'Data Engineer',            98000.00, '2020-06-15', 'Seattle',       'WA'),
    (9,  'Jennifer','Anderson', 'Sales',       'Sales Representative',     54000.00, '2021-08-01', 'Dallas',        'TX'),
    (10, 'William', 'Thomas',   'Finance',     'Financial Analyst',        67000.00, '2019-04-22', 'Chicago',       'IL'),
    (11, 'Amanda',  'Jackson',  'Engineering', 'QA Engineer',              72000.00, '2020-10-05', 'Seattle',       'WA'),
    (12, 'Daniel',  'White',    'HR',          'HR Manager',               80000.00, '2018-01-15', 'Dallas',        'TX'),
    (13, 'Ashley',  'Harris',   'Finance',     'Senior Financial Analyst', 82000.00, '2017-11-20', 'New York',      'NY'),
    (14, 'Kevin',   'Clark',    'Sales',       'Account Executive',        65000.00, '2021-03-10', 'Chicago',       'IL'),
    (15, 'Rachel',  'Lewis',    'Marketing',   'Content Specialist',       50000.00, '2022-01-18', 'San Francisco', 'CA'),
    (16, 'Brian',   'Robinson', 'Engineering', 'DevOps Engineer',          95000.00, '2019-08-25', 'Seattle',       'WA'),
    (17, 'Nicole',  'Walker',   'Finance',     'Accounting Manager',       88000.00, '2018-06-30', 'New York',      'NY'),
    (18, 'Steven',  'Young',    'HR',          'Recruiter',                47000.00, '2022-04-12', 'Dallas',        'TX'),
    (19, 'Laura',   'King',     'Sales',       'Sales Director',           105000.00, '2016-12-01', 'Chicago',       'IL'),
    (20, 'Andrew',  'Wright',   'Engineering', 'Junior Developer',         62000.00, '2023-02-14', 'San Francisco', 'CA');
GO

-- ============================================================
-- STEP 7: Insert sample data into Customers
-- ============================================================
-- 20 customers with varying order histories.

INSERT INTO Customers (customer_id, first_name, last_name, email, city, state, signup_date, total_orders, total_spent)
VALUES
    (1,  'Alice',    'Morgan',    'alice.morgan@email.com',    'Portland',      'OR', '2022-01-15',  8,  1250.50),
    (2,  'Bob',      'Reed',      'bob.reed@email.com',        'Austin',        'TX', '2022-03-20', 12,  2340.00),
    (3,  'Carol',    'Murphy',    'carol.murphy@email.com',    'Denver',        'CO', '2022-06-10',  3,   450.75),
    (4,  'Dan',      'Rivera',    'dan.rivera@email.com',      'Miami',         'FL', '2022-08-05', 15,  3100.25),
    (5,  'Elena',    'Cooper',    'elena.cooper@email.com',    'Seattle',       'WA', '2022-10-22',  6,   890.00),
    (6,  'Frank',    'Bailey',    'frank.bailey@email.com',    'Boston',        'MA', '2023-01-08', 20,  4500.00),
    (7,  'Grace',    'Howard',    'grace.howard@email.com',    'Phoenix',       'AZ', '2023-02-14',  2,   175.50),
    (8,  'Henry',    'Ward',      'henry.ward@email.com',      'Atlanta',       'GA', '2023-04-30',  9,  1680.00),
    (9,  'Irene',    'Torres',    'irene.torres@email.com',    'San Diego',     'CA', '2023-05-17', 11,  2050.75),
    (10, 'Jack',     'Peterson',  'jack.peterson@email.com',   'Minneapolis',   'MN', '2023-07-03',  4,   520.00),
    (11, 'Karen',    'Gray',      'karen.gray@email.com',      'Nashville',     'TN', '2023-08-19',  7,  1100.25),
    (12, 'Leo',      'Ramirez',   'leo.ramirez@email.com',     'Las Vegas',     'NV', '2023-09-25', 14,  2890.50),
    (13, 'Mia',      'James',     'mia.james@email.com',       'Philadelphia',  'PA', '2023-11-11',  1,    89.99),
    (14, 'Nathan',   'Watson',    'nathan.watson@email.com',   'Detroit',       'MI', '2024-01-02', 10,  1950.00),
    (15, 'Olivia',   'Brooks',    'olivia.brooks@email.com',   'Salt Lake City','UT', '2024-01-28',  5,   725.00),
    (16, 'Paul',     'Kelly',     'paul.kelly@email.com',      'Charlotte',     'NC', '2024-02-15', 18,  3750.25),
    (17, 'Quinn',    'Sanders',   'quinn.sanders@email.com',   'Tampa',         'FL', '2024-03-08',  3,   310.00),
    (18, 'Rita',     'Price',     'rita.price@email.com',      'Columbus',      'OH', '2024-04-20',  8,  1425.75),
    (19, 'Sam',      'Bennett',   'sam.bennett@email.com',     'Raleigh',       'NC', '2024-05-05',  6,   980.50),
    (20, 'Tina',     'Foster',    'tina.foster@email.com',     'Indianapolis',  'IN', '2024-06-12',  2,   200.00);
GO

-- ============================================================
-- Done! You should now have three tables with sample data.
-- ============================================================
-- To verify, try running these queries:
--
--   SELECT COUNT(*) FROM Sales;       -- Should return 20
--   SELECT COUNT(*) FROM Employees;   -- Should return 20
--   SELECT COUNT(*) FROM Customers;   -- Should return 20
--
-- You're ready to start Lesson 1!
