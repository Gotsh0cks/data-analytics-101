# Lesson 2: Formulas and Functions

## How Formulas Work

Every formula in Excel starts with an **equals sign** (`=`). When Excel sees `=`, it knows you want it to calculate something instead of just displaying text.

Try this: click on an empty cell, type `=2+3`, and press Enter. The cell shows **5**. That is your first formula.

## Basic Math

You can use cells in formulas just like numbers:

| Formula | What It Does | Example |
|---------|-------------|---------|
| `=A2+B2` | Add two cells | |
| `=G2-F2` | Subtract | |
| `=E2*F2` | Multiply (quantity * price) | |
| `=G2/E2` | Divide (revenue / quantity) | |

### Try It (using sales_data.xlsx)

1. Click on an empty cell (like H2)
2. Type `=E2*F2` and press Enter
3. This multiplies quantity by unit_price — it should match the revenue in G2

## Functions: Built-In Formulas

Functions are pre-built formulas that do common calculations. Here are the ones you will use most:

### SUM — Add Up a Range

```
=SUM(G2:G103)
```

Adds up all revenue values. Much easier than typing `=G2+G3+G4+...`

### AVERAGE — Find the Mean

```
=AVERAGE(G2:G103)
```

Calculates the average revenue per sale.

### COUNT — Count How Many

```
=COUNT(G2:G103)
```

Counts how many cells in the range contain numbers. Use `COUNTA` to count cells that contain *anything* (including text).

### MIN and MAX — Find Extremes

```
=MIN(G2:G103)
=MAX(G2:G103)
```

Find the smallest and largest revenue values.

### Try It

Open `data/excel/sales_data.xlsx` and go to an empty area (like column I). In separate cells, enter:

1. `=SUM(G2:G103)` — total revenue
2. `=AVERAGE(G2:G103)` — average sale amount
3. `=COUNT(G2:G103)` — number of sales
4. `=MIN(G2:G103)` — smallest sale
5. `=MAX(G2:G103)` — largest sale

Now check the Summary sheet — you will see similar formulas already built for you.

## IF — Make Decisions

The IF function checks a condition and returns different values based on whether it is true or false:

```
=IF(G2 > 1000, "Large Sale", "Small Sale")
```

This says: "If the revenue in G2 is greater than 1000, show 'Large Sale'. Otherwise, show 'Small Sale'."

### Try It

1. Click on cell H1 and type `Sale Size` (as a header)
2. In H2, type: `=IF(G2>1000, "Large", "Small")`
3. Press Enter — you should see "Large" or "Small"
4. To apply to all rows: click H2, then drag the small square in the bottom-right corner of the cell down to the last row

## VLOOKUP — Find Data in Another Table

VLOOKUP searches for a value in one column and returns a corresponding value from another column. It stands for "Vertical Lookup."

```
=VLOOKUP(lookup_value, table_range, column_number, FALSE)
```

For example, if you had a product price list on a separate sheet and wanted to look up the price for "Laptop":

```
=VLOOKUP("Laptop", A2:F50, 6, FALSE)
```

- `"Laptop"` — what to search for
- `A2:F50` — where to search (the table)
- `6` — return the value from the 6th column
- `FALSE` — require an exact match (almost always use FALSE)

VLOOKUP is one of the most asked-about functions in interviews. Do not worry if it feels confusing at first — it becomes natural with practice.

## COUNTIF and SUMIF — Conditional Counting and Summing

These are powerful for answering questions like "How many Electronics sales were there?" or "What is the total revenue for the North region?"

```
=COUNTIF(C2:C103, "Electronics")
=SUMIF(D2:D103, "North", G2:G103)
```

- **COUNTIF** counts how many cells in a range match a condition
- **SUMIF** adds up values in one range where a corresponding range matches a condition

### Try It

In an empty area:
1. `=COUNTIF(C2:C103, "Electronics")` — how many Electronics sales?
2. `=SUMIF(D2:D103, "North", G2:G103)` — total revenue for North region?
3. `=SUMIF(C2:C103, "Furniture", G2:G103)` — total revenue for Furniture?

## Common Mistakes

1. **Forgetting the `=` sign.** Without it, Excel treats your formula as plain text.
2. **Wrong range.** `G2:G103` includes all data rows. `G1:G103` includes the header, which can cause errors.
3. **Circular reference.** If cell A1 contains `=A1+1`, Excel cannot calculate it because it references itself. You will see a warning.
4. **Text vs. numbers.** If a "number" is stored as text (left-aligned instead of right-aligned), math functions will not work on it.

---

Next up: [Sorting and Filtering](lesson_03_sorting_filtering.md) — find exactly what you need in your data.
