# Lesson 2: Querying Real-World Data

## Moving Beyond Sample Data

In the previous modules, you worked with small, clean datasets created for learning. Now you'll write SQL queries against **real-world datasets** — the Titanic passenger data, restaurant tips, iris flower measurements, and more.

Real data is messier. Column names might not be obvious. Values might be missing. But that's exactly what makes it realistic.

## Exploring an Unfamiliar Table

When you encounter a new table, always start with exploration:

```sql
-- What columns does this table have?
-- (In DB Browser: just click the table name)
PRAGMA table_info(titanic);

-- How many rows?
SELECT COUNT(*) FROM titanic;

-- Peek at a few rows
SELECT * FROM titanic LIMIT 10;
```

`PRAGMA table_info()` is SQLite's way of showing you a table's columns and their types. It's like `df.info()` in pandas.

## Titanic Queries

The Titanic dataset has columns like `Survived`, `Pclass` (passenger class: 1, 2, or 3), `Name`, `Sex`, `Age`, and `Fare`.

### Survival rate by class

```sql
SELECT
    Pclass,
    COUNT(*) AS total_passengers,
    SUM(Survived) AS survived,
    ROUND(100.0 * SUM(Survived) / COUNT(*), 1) AS survival_rate
FROM titanic
GROUP BY Pclass
ORDER BY Pclass;
```

Notice the `100.0 *` — without that decimal, SQL would do integer division and you'd get 0% or 100%. This is a common gotcha.

### Average fare by class

```sql
SELECT
    Pclass,
    ROUND(AVG(Fare), 2) AS avg_fare,
    MIN(Fare) AS min_fare,
    MAX(Fare) AS max_fare
FROM titanic
GROUP BY Pclass;
```

### Passengers with missing ages

```sql
SELECT COUNT(*) AS missing_age
FROM titanic
WHERE Age IS NULL;
```

In SQL, missing values are `NULL` — not blank, not zero, not "N/A". You check for them with `IS NULL`, never with `= NULL` (that doesn't work in SQL).

## Tips Dataset Queries

The tips dataset has columns: `total_bill`, `tip`, `sex`, `smoker`, `day`, `time`, `size` (party size).

### Average tip percentage by day

```sql
SELECT
    day,
    COUNT(*) AS num_meals,
    ROUND(AVG(tip), 2) AS avg_tip,
    ROUND(AVG(100.0 * tip / total_bill), 1) AS avg_tip_pct
FROM tips
GROUP BY day
ORDER BY avg_tip_pct DESC;
```

### Lunch vs. dinner comparison

```sql
SELECT
    time,
    COUNT(*) AS num_meals,
    ROUND(AVG(total_bill), 2) AS avg_bill,
    ROUND(AVG(tip), 2) AS avg_tip
FROM tips
GROUP BY time;
```

## Combining Tables with JOIN

Now that you have multiple tables in one database, you can combine them — even if they weren't originally related. For example, let's compare the original course data:

```sql
SELECT
    e.department,
    COUNT(*) AS num_employees,
    ROUND(AVG(e.salary), 0) AS avg_salary
FROM employees e
GROUP BY e.department
ORDER BY avg_salary DESC;
```

## NULL Handling in Real Data

Real datasets have missing values. Here are the essential patterns:

```sql
-- Count missing values in a column
SELECT COUNT(*) - COUNT(Age) AS missing_ages FROM titanic;

-- Exclude missing values
SELECT AVG(Age) FROM titanic WHERE Age IS NOT NULL;

-- Replace missing values with a default (COALESCE)
SELECT Name, COALESCE(Age, 0) AS age_or_zero FROM titanic LIMIT 10;
```

`COALESCE` is incredibly useful — it returns the first non-NULL value. Think of it as a "use this if the value is missing" function.

## Try It Yourself

Open `lesson_02_querying_real_data.sql` in DB Browser for SQLite and run the queries one by one. Modify them, break them, fix them — that's how you learn.
