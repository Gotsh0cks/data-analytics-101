# Lesson 1: SELECT and FROM

## The Two Most Important Words in SQL

Every SQL query starts with two keywords: **SELECT** and **FROM**.

- **SELECT** tells the database *what columns* you want to see.
- **FROM** tells the database *which table* to look in.

Think of it like this: if the database is a filing cabinet, FROM picks the drawer, and SELECT picks which pieces of information you want to pull out.

Here's the simplest possible query:

```sql
SELECT * FROM Sales;
```

This says: "Give me **all columns** from the **Sales** table."

## SELECT * (All Columns)

The asterisk `*` is a shortcut that means "every column." It's great for exploring a table quickly:

```sql
SELECT * FROM Employees;
```

This gives you every column and every row in the Employees table.

**A word of caution:** In real-world work, avoid using `SELECT *` in reports or applications. Why? Because tables can have dozens of columns, and pulling all of them is slow and wasteful when you only need a few. It's fine for quick exploration, but get in the habit of naming the columns you actually want.

## Selecting Specific Columns

Instead of `*`, list the column names you want, separated by commas:

```sql
SELECT product, revenue FROM Sales;
```

This gives you just two columns: the product name and the revenue. Much cleaner.

You can select as many columns as you need:

```sql
SELECT first_name, last_name, department, salary FROM Employees;
```

## Column Aliases with AS

Sometimes column names aren't very reader-friendly. You can rename a column in your results using **AS**:

```sql
SELECT product, revenue AS total_sale FROM Sales;
```

The column will show up as "total_sale" instead of "revenue" in your results. This doesn't change anything in the database — it only affects how the results are displayed.

You can also use aliases with spaces by wrapping them in square brackets:

```sql
SELECT first_name AS [First Name], salary AS [Annual Salary] FROM Employees;
```

## SELECT TOP N

What if a table has thousands of rows and you just want to peek at a few? Use **TOP**:

```sql
SELECT TOP 10 * FROM Sales;
```

This returns only the first 10 rows. It's very handy when you're exploring a new table and don't want to wait for millions of rows to load.

You can combine TOP with specific columns:

```sql
SELECT TOP 5 product, revenue FROM Sales;
```

## SELECT DISTINCT

Sometimes a column has repeated values. For example, the Sales table has a "region" column, but the same region appears many times. If you want to see the unique values only, use **DISTINCT**:

```sql
SELECT DISTINCT region FROM Sales;
```

This gives you a list of each region that appears in the table — no duplicates.

You can use DISTINCT with multiple columns too. It returns unique *combinations*:

```sql
SELECT DISTINCT category, region FROM Sales;
```

This shows every unique pairing of category and region.

## Key Takeaways

| Concept | What It Does |
|---------|-------------|
| `SELECT *` | Returns all columns |
| `SELECT col1, col2` | Returns only the columns you list |
| `AS` | Gives a column a temporary display name |
| `TOP N` | Limits the results to N rows |
| `DISTINCT` | Removes duplicate values from results |

## Next Up

In Lesson 2, you'll learn how to **filter** rows with WHERE and **sort** results with ORDER BY.
