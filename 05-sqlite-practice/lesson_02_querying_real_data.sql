-- ============================================================
-- Lesson 2: Querying Real-World Data
-- ============================================================
-- Run these queries in DB Browser for SQLite after opening
-- data/analytics.db. Try each one, then modify them!
-- ============================================================

-- ============================================================
-- EXPLORING TABLES
-- ============================================================

-- See all tables in the database
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;

-- Check the structure of the titanic table
PRAGMA table_info(titanic);

-- Peek at the data
SELECT * FROM titanic LIMIT 10;

-- How many rows?
SELECT COUNT(*) AS total_passengers FROM titanic;


-- ============================================================
-- TITANIC QUERIES
-- ============================================================

-- Survival rate by passenger class
SELECT
    Pclass,
    COUNT(*) AS total_passengers,
    SUM(Survived) AS survived,
    ROUND(100.0 * SUM(Survived) / COUNT(*), 1) AS survival_rate_pct
FROM titanic
GROUP BY Pclass
ORDER BY Pclass;

-- Average age by class (excluding missing ages)
SELECT
    Pclass,
    ROUND(AVG(Age), 1) AS avg_age,
    COUNT(Age) AS passengers_with_age
FROM titanic
WHERE Age IS NOT NULL
GROUP BY Pclass;

-- Fare ranges by class
SELECT
    Pclass,
    ROUND(AVG(Fare), 2) AS avg_fare,
    ROUND(MIN(Fare), 2) AS cheapest,
    ROUND(MAX(Fare), 2) AS most_expensive
FROM titanic
GROUP BY Pclass;

-- Count of missing values per key column
SELECT
    COUNT(*) - COUNT(Age) AS missing_age,
    COUNT(*) - COUNT(Cabin) AS missing_cabin,
    COUNT(*) - COUNT(Embarked) AS missing_embarked
FROM titanic;


-- ============================================================
-- TIPS QUERIES
-- ============================================================

-- Quick look
SELECT * FROM tips LIMIT 10;

-- Average tip percentage by day of the week
SELECT
    day,
    COUNT(*) AS num_meals,
    ROUND(AVG(tip), 2) AS avg_tip,
    ROUND(AVG(100.0 * tip / total_bill), 1) AS avg_tip_pct
FROM tips
GROUP BY day
ORDER BY avg_tip_pct DESC;

-- Lunch vs. dinner spending
SELECT
    time,
    COUNT(*) AS num_meals,
    ROUND(AVG(total_bill), 2) AS avg_bill,
    ROUND(AVG(tip), 2) AS avg_tip,
    ROUND(AVG(size), 1) AS avg_party_size
FROM tips
GROUP BY time;

-- Tip percentage by party size
SELECT
    size AS party_size,
    COUNT(*) AS num_meals,
    ROUND(AVG(100.0 * tip / total_bill), 1) AS avg_tip_pct
FROM tips
GROUP BY size
ORDER BY size;


-- ============================================================
-- IRIS QUERIES
-- ============================================================

-- Average measurements by species
SELECT
    species,
    ROUND(AVG(sepal_length), 2) AS avg_sepal_len,
    ROUND(AVG(sepal_width), 2) AS avg_sepal_wid,
    ROUND(AVG(petal_length), 2) AS avg_petal_len,
    ROUND(AVG(petal_width), 2) AS avg_petal_wid
FROM iris
GROUP BY species;

-- Which species has the largest petals?
SELECT species, MAX(petal_length) AS max_petal_length
FROM iris
GROUP BY species
ORDER BY max_petal_length DESC;


-- ============================================================
-- COURSE DATA QUERIES
-- ============================================================

-- Revenue by category from the original sales data
SELECT
    category,
    SUM(revenue) AS total_revenue,
    COUNT(*) AS num_sales
FROM sales_data
GROUP BY category
ORDER BY total_revenue DESC;

-- Highest-paid employees by department
SELECT
    department,
    first_name || ' ' || last_name AS employee_name,
    salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees e2
    WHERE e2.department = employees.department
)
ORDER BY salary DESC;
