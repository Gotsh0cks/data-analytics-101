# Module 2 Exercises

Practice your spreadsheet skills. Open the Excel files in `data/excel/` and work through these exercises.

---

## Exercise 1: Formulas Practice

Open `data/excel/employees.xlsx` and in empty cells:

1. Calculate the total payroll (sum of all salaries)
2. Find the average salary
3. Count how many employees are in the dataset
4. Use COUNTIF to count how many employees are in the "Sales" department
5. Use SUMIF to find the total salary spend for the "Engineering" department

```
Your formulas here (write them down to remember)
```

---

## Exercise 2: Sorting Challenge

Using `data/excel/employees.xlsx`:

1. Sort by hire_date (oldest first). Who was hired first?
2. Sort by salary (highest first). Who earns the most?
3. Sort by department (A-Z), then by salary (highest first) within each department. Who is the highest-paid person in HR?

---

## Exercise 3: Filtering Drill

Using `data/excel/sales_data.xlsx`:

1. Filter to show only "Furniture" sales. How many are there?
2. Filter to show sales where revenue > $1,000. How many are there?
3. Filter to show "Electronics" sales in the "North" region. What is the total revenue? (Use the SUM formula on the visible cells, or check the status bar at the bottom)
4. Clear all filters when done

---

## Exercise 4: Pivot Table Challenges

Using `data/excel/sales_data.xlsx`, create pivot tables to answer:

1. What is the total revenue for each region?
2. What is the average sale amount for each product?
3. How many sales occurred in each category per region? (Hint: category in Rows, region in Columns, any field in Values set to Count)

Using `data/excel/customers.xlsx`:

4. Which state has the highest total spending?
5. What is the average number of orders per state?

---

## Exercise 5: Chart Building

Create the following charts from the sales data:

1. A column chart showing total revenue by region (sorted highest to lowest)
2. A line chart showing revenue trend over time (grouped by month)
3. A pie chart showing the share of total revenue by category

For each chart:
- Add a descriptive title
- Add data labels
- Remove unnecessary gridlines or legends

---

## Hints

**Exercise 1:** Use `=SUM(F2:F51)` for total payroll (adjust the range to match your data). `=COUNTIF(D2:D51, "Sales")` counts Sales employees.

**Exercise 2:** Use Data > Sort. For multi-level sorting, use Data > Sort and add levels.

**Exercise 3:** Remember to turn on filters first (Data > Filter). The status bar at the bottom-right shows Sum/Average/Count of selected or visible cells.

**Exercise 4:** Insert > PivotTable. Drag fields to Rows, Columns, and Values. Change the value calculation by clicking the dropdown in the Values area.

**Exercise 5:** Create a pivot table first to get the summary data, then insert a chart from the pivot table.
