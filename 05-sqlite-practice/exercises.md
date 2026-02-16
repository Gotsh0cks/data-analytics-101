# Module 5 Exercises

Time to practice your SQLite skills. Open `data/analytics.db` in DB Browser for SQLite (or use Python with `pd.read_sql()`), and work through these exercises.

---

## Exercise 1: Explore the Tips Data

Write SQL queries to answer:

1. How many meals are in the tips dataset?
2. What is the average total bill?
3. What is the highest tip anyone left?

```sql
-- Your queries here
```

---

## Exercise 2: Titanic Deep Dive

Write SQL queries to find:

1. How many female passengers survived vs. did not survive?
2. What was the average fare for survivors vs. non-survivors?
3. What was the youngest and oldest passenger age in each class?

```sql
-- Your queries here
```

---

## Exercise 3: Create Your Own Table

1. Create a table called `study_log` with columns: `id` (INTEGER PRIMARY KEY), `topic` (TEXT), `minutes_spent` (INTEGER), `study_date` (TEXT), `notes` (TEXT)
2. Insert at least 5 rows tracking your study sessions for this course
3. Write a query that shows total minutes spent per topic

```sql
-- Your queries here
```

---

## Exercise 4: Python + SQL

Write a Python script that:

1. Connects to `analytics.db`
2. Queries the tips table to get average tip percentage by day
3. Creates a bar chart of the results using matplotlib
4. Saves the chart as `tip_percentages.png`

```python
# Your code here
```

---

## Exercise 5: Cross-Table Analysis

Using Python and `pd.read_sql()`:

1. Load the sales_data table into a DataFrame
2. Load the employees table into a DataFrame
3. Find which department has the most employees AND which product category generates the most revenue
4. Print both results in a clear format

```python
# Your code here
```

---

## Exercise 6: Data Entry Challenge

1. Create a new table called `favorite_datasets` with columns for: name, source (e.g., "Kaggle"), topic, num_rows, and your_rating (1-5)
2. Insert entries for at least 3 datasets you've worked with in this course
3. Query your table to find the highest-rated dataset

```sql
-- Your queries here
```

---

## Hints

**Exercise 1:**
`SELECT COUNT(*) FROM tips;` for the count. `AVG(total_bill)` and `MAX(tip)` for the others.

**Exercise 2:**
Group by `Sex` and `Survived`. Remember that Survived is 0 or 1. For age ranges, use `MIN(Age)` and `MAX(Age)` with `GROUP BY Pclass` and `WHERE Age IS NOT NULL`.

**Exercise 3:**
Use `CREATE TABLE`, then `INSERT INTO ... VALUES`, then `SELECT topic, SUM(minutes_spent) FROM study_log GROUP BY topic`.

**Exercise 4:**
Use `pd.read_sql()` with a GROUP BY query. Calculate tip percentage as `100.0 * tip / total_bill` in the SQL. Use `df.plot(kind="bar")` for the chart.

**Exercise 5:**
Load each table with `pd.read_sql("SELECT * FROM table_name", conn)`. Use `.groupby()` and `.agg()` in pandas, or do the grouping in SQL.

**Exercise 6:**
Similar to Exercise 3. Use `ORDER BY your_rating DESC LIMIT 1` to find the top-rated dataset.
