# Lesson 2: WHERE and ORDER BY

## Filtering Rows with WHERE

In Lesson 1, you learned how to choose which *columns* to see. But what if you don't want every *row*? That's where **WHERE** comes in.

WHERE filters your results so you only see rows that match a condition. Think of it as setting a rule: "Only show me rows where [this is true]."

```sql
SELECT * FROM Sales
WHERE region = 'North';
```

This says: "Give me all sales, but only the ones where the region is North."

**Important:** In T-SQL, text values go inside single quotes (`'North'`), but numbers do not (`quantity > 5`).

## Comparison Operators

You can use these operators in a WHERE clause:

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` | Equals | `region = 'North'` |
| `<>` | Not equal to | `region <> 'North'` |
| `<` | Less than | `quantity < 5` |
| `>` | Greater than | `salary > 70000` |
| `<=` | Less than or equal to | `unit_price <= 100` |
| `>=` | Greater than or equal to | `revenue >= 1000` |

## Combining Conditions with AND / OR

You can combine multiple conditions:

- **AND** means *both* conditions must be true.
- **OR** means *at least one* condition must be true.

```sql
-- Both must be true: Electronics AND in the North region
SELECT * FROM Sales
WHERE category = 'Electronics' AND region = 'North';

-- Either can be true: North OR South region
SELECT * FROM Sales
WHERE region = 'North' OR region = 'South';
```

When mixing AND and OR, use parentheses to be clear about what you mean:

```sql
-- Electronics in the North OR South region
SELECT * FROM Sales
WHERE category = 'Electronics' AND (region = 'North' OR region = 'South');
```

Without the parentheses, you might get unexpected results because AND is evaluated before OR.

## IN Matching a List

Instead of writing multiple OR conditions, you can use **IN**:

```sql
-- Instead of: region = 'North' OR region = 'South' OR region = 'East'
SELECT * FROM Sales
WHERE region IN ('North', 'South', 'East');
```

This is cleaner and easier to read, especially with long lists.

## LIKE Pattern Matching

**LIKE** lets you search for patterns in text using the `%` wildcard:

- `%` matches any number of characters (including zero).

```sql
-- Products that start with "Desk"
SELECT * FROM Sales
WHERE product LIKE 'Desk%';

-- Employees whose last name ends with "son"
SELECT * FROM Employees
WHERE last_name LIKE '%son';

-- Emails that contain "email"
SELECT * FROM Customers
WHERE email LIKE '%email%';
```

## BETWEEN Range Matching

**BETWEEN** is a shortcut for checking if a value falls within a range (inclusive on both ends):

```sql
-- Sales from January through March 2024
SELECT * FROM Sales
WHERE sale_date BETWEEN '2024-01-01' AND '2024-03-31';

-- Employees earning between 50,000 and 80,000
SELECT * FROM Employees
WHERE salary BETWEEN 50000 AND 80000;
```

BETWEEN includes both endpoints, so `BETWEEN 50000 AND 80000` includes 50,000 and 80,000.

## IS NULL / IS NOT NULL

Sometimes data is missing. In databases, a missing value is called **NULL**. You can't check for NULL with `=` you have to use **IS NULL** or **IS NOT NULL**:

```sql
-- Find rows where a value is missing
SELECT * FROM Customers
WHERE email IS NULL;

-- Find rows where a value is present
SELECT * FROM Customers
WHERE email IS NOT NULL;
```

**Note:** Our sample data doesn't have NULLs, but in real-world databases, you'll encounter them constantly. Always remember: use `IS NULL`, never `= NULL`.

## Sorting Results with ORDER BY

By default, SQL doesn't guarantee any particular order for your results. If you want them sorted, use **ORDER BY**:

```sql
-- Sort employees by salary (lowest to highest)
SELECT first_name, last_name, salary FROM Employees
ORDER BY salary;
```

## ASC vs DESC

- **ASC** (ascending) = lowest to highest, A to Z, earliest to latest. This is the default.
- **DESC** (descending) = highest to lowest, Z to A, latest to earliest.

```sql
-- Highest salary first
SELECT first_name, last_name, salary FROM Employees
ORDER BY salary DESC;

-- Most recent sales first
SELECT * FROM Sales
ORDER BY sale_date DESC;
```

You can sort by multiple columns. The second column breaks ties from the first:

```sql
-- Sort by department (A-Z), then by salary (highest first) within each department
SELECT first_name, last_name, department, salary FROM Employees
ORDER BY department ASC, salary DESC;
```

## Putting It All Together

You can use SELECT, WHERE, and ORDER BY in the same query:

```sql
SELECT product, region, revenue
FROM Sales
WHERE revenue > 1000
ORDER BY revenue DESC;
```

This says: "Show me the product, region, and revenue for all sales over $1,000, sorted from highest to lowest revenue."

## Key Takeaways

| Concept | What It Does |
|---------|-------------|
| `WHERE` | Filters rows based on conditions |
| `=, <>, <, >, <=, >=` | Compare values |
| `AND, OR` | Combine conditions |
| `IN (...)` | Match against a list of values |
| `LIKE '%pattern%'` | Pattern matching with wildcards |
| `BETWEEN x AND y` | Check if a value is in a range |
| `IS NULL / IS NOT NULL` | Check for missing values |
| `ORDER BY` | Sort results |
| `ASC / DESC` | Control sort direction |

## Next Up

In Lesson 3, you'll learn how to **summarize** data with aggregations like COUNT, SUM, and AVG.
