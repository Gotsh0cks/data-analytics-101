# Lesson 4: JOINs

## Why JOINs Matter

So far, every query has pulled data from a single table. But in the real world, data is spread across multiple tables. For example, an "Orders" table might have a customer ID, and a "Customers" table has the customer's name and email. To see the customer name alongside their order, you need to **join** the two tables.

If you've used VLOOKUP in Excel, a JOIN does the same thing: it looks up a matching value in another table and pulls in related columns.

## How JOINs Work

A JOIN connects two tables based on a **shared column** a column that appears in both tables and holds matching values. For example, both tables might have a `department_id` column. The JOIN says: "For each row in table A, find the matching row(s) in table B where the values in this column are equal."

## A Quick Note About Our Sample Data

Our three practice tables (Sales, Employees, Customers) don't share foreign keys with each other they're independent tables. So for this lesson, we'll create small temporary tables that *do* have a shared column. This way you can see JOINs in action clearly.

## INNER JOIN

An **INNER JOIN** returns only the rows where there's a match in *both* tables.

Picture two circles overlapping (a Venn diagram). An INNER JOIN gives you only the overlapping part the data that exists in both tables.

```sql
SELECT Orders.order_id, Products.product_name, Orders.quantity
FROM Orders
INNER JOIN Products ON Orders.product_id = Products.product_id;
```

If an order references a product ID that doesn't exist in the Products table, that order won't appear in the results. And if a product has never been ordered, it won't appear either.

## LEFT JOIN

A **LEFT JOIN** returns *all* rows from the left table (the first one), and the matching rows from the right table. If there's no match, the right side shows NULL.

Back to the Venn diagram: a LEFT JOIN gives you the entire left circle, plus whatever overlaps with the right.

```sql
SELECT Products.product_name, Orders.order_id, Orders.quantity
FROM Products
LEFT JOIN Orders ON Products.product_id = Orders.product_id;
```

This shows every product, even ones that have never been ordered. For products with no orders, the order columns will show NULL.

LEFT JOIN is incredibly useful in analytics. Whenever you want "show me everything from table A, and attach matching info from table B if it exists," LEFT JOIN is your tool.

## Table Aliases

When you join tables, you have to type table names repeatedly. **Aliases** make this much shorter:

```sql
-- Without aliases (verbose)
SELECT Orders.order_id, Products.product_name
FROM Orders
INNER JOIN Products ON Orders.product_id = Products.product_id;

-- With aliases (cleaner)
SELECT o.order_id, p.product_name
FROM Orders AS o
INNER JOIN Products AS p ON o.product_id = p.product_id;
```

You can even drop the `AS` keyword just write `FROM Orders o`.

## When You Need JOINs in Real Life

Here are common real-world scenarios:

- **Sales report:** Join an Orders table with a Products table to get product names alongside order details.
- **Employee directory:** Join an Employees table with a Departments table to show department names instead of just IDs.
- **Customer analysis:** Join Customers with Orders to see who bought what.
- **Missing data investigation:** Use a LEFT JOIN to find records in one table that *don't* have matches in another (look for NULLs in the joined columns).

## Other JOIN Types (Good to Know)

There are two other types you might encounter:

- **RIGHT JOIN** The mirror of LEFT JOIN. Returns all rows from the right table. In practice, most people just use LEFT JOIN and swap the table order.
- **FULL OUTER JOIN** Returns all rows from both tables, with NULLs where there's no match. Less common but useful in certain comparisons.

We'll focus on INNER JOIN and LEFT JOIN since those cover the vast majority of real-world needs.

## Key Takeaways

| Concept | What It Does |
|---------|-------------|
| `INNER JOIN` | Returns only matching rows from both tables |
| `LEFT JOIN` | Returns all rows from the left table, matches from the right (NULLs if no match) |
| `ON` | Specifies which columns to match between the tables |
| Table aliases | Shorter names for tables (`FROM Orders AS o`) |

## The JOIN Process in Plain English

1. Pick two tables that share a related column.
2. Decide which JOIN type you need (INNER or LEFT are most common).
3. Write the ON clause to tell SQL which columns to match.
4. SELECT the columns you want from either table.

## Next Up

In Lesson 5, you'll learn about **subqueries and CTEs** queries inside queries that let you tackle more complex questions.
