# Lesson 4: Pivot Tables

## The Most Powerful Feature in Excel

If you learn one thing in this entire Excel module, make it pivot tables. They are the single most useful feature for data analysis in a spreadsheet.

A pivot table takes a big table of raw data and **summarizes it instantly** by any category you choose. Want to know total revenue by region? Five clicks. Average salary by department? Five clicks. Count of sales by product and month? Five clicks.

## Creating Your First Pivot Table

Open `data/excel/sales_data.xlsx` and follow these steps:

### Step 1: Select Your Data

1. Click anywhere inside the data table
2. Press **Ctrl + A** to select all of it (or manually select A1 through the last row)

### Step 2: Insert the Pivot Table

1. Go to the **Insert** tab
2. Click **PivotTable**
3. A dialog appears — it should automatically detect your data range
4. Choose **New Worksheet** (the default)
5. Click **OK**

A new sheet appears with an empty pivot table and a **PivotTable Fields** panel on the right.

### Step 3: Build the Summary

The Fields panel shows all your column names. You drag them into four areas:

| Area | What It Does | Example |
|------|-------------|---------|
| **Rows** | Categories to group by (left side of the table) | Product, Region |
| **Columns** | Categories to spread across the top | Region, Category |
| **Values** | Numbers to calculate (sum, average, count) | Revenue, Quantity |
| **Filters** | Dropdown filters for the whole table | Category, Region |

### Try It: Total Revenue by Category

1. Drag **category** to the **Rows** area
2. Drag **revenue** to the **Values** area
3. The pivot table instantly shows total revenue for each category

You just summarized 100+ rows into 3 rows. That is the power of pivot tables.

## Changing the Calculation

By default, Values shows **Sum**. To change it:

1. Click the dropdown arrow next to "Sum of revenue" in the Values area
2. Select **Value Field Settings**
3. Choose **Average**, **Count**, **Min**, **Max**, or other options
4. Click **OK**

### Try It: Average Revenue per Sale by Category

1. With your existing pivot table, change the Value Field Settings from Sum to Average
2. Now you see the average sale amount for each category

## Adding More Dimensions

### Rows + Columns: A Two-Way Summary

1. Keep **category** in Rows
2. Drag **region** to the **Columns** area
3. Keep **revenue** in Values (set to Sum)

Now you see a grid: categories down the left, regions across the top, with revenue at each intersection. This is called a **cross-tabulation** — it shows how two categories interact.

### Multiple Row Fields

1. Drag **category** to Rows
2. Drag **product** to Rows (below category)
3. Now you see categories as groups, with individual products nested underneath

## Filtering a Pivot Table

### Using the Filters Area

1. Drag **region** to the **Filters** area
2. A dropdown appears above the pivot table
3. Select a specific region to see only that region's data
4. Select **(All)** to go back to the full view

### Using Slicers (Visual Filters)

Slicers are clickable buttons that filter your pivot table:

1. Click anywhere in the pivot table
2. Go to **PivotTable Analyze** tab (or **Options** tab in older Excel)
3. Click **Insert Slicer**
4. Check **category** and **region**
5. Click **OK**

Two slicer panels appear. Click any button to filter instantly. Hold Ctrl to select multiple values.

## Refreshing Data

If the underlying data changes, the pivot table does not update automatically. To refresh:

1. Right-click anywhere in the pivot table
2. Select **Refresh**

Or click **PivotTable Analyze** > **Refresh**.

## Common Pivot Table Patterns

| Question | Rows | Values |
|----------|------|--------|
| Revenue by category | category | Sum of revenue |
| Average salary by department | department | Average of salary |
| Number of employees per city | city | Count of employee_id |
| Sales by product and region | product, region | Sum of revenue |

## Try It Yourself

Open `data/excel/employees.xlsx` and create pivot tables to answer:

1. How many employees are in each department? (Drag department to Rows, employee_id to Values, set to Count)
2. What is the average salary by department? (department in Rows, salary in Values, set to Average)
3. Which city has the most employees? (city in Rows, employee_id in Values, set to Count)

## Google Sheets Differences

In Google Sheets:
1. Select your data
2. Go to **Insert** > **Pivot table**
3. The interface is slightly different but the concept is identical
4. Drag fields to Rows, Columns, Values, and Filters

---

Next up: [Excel Charts](lesson_05_excel_charts.md) — visualize your data without leaving Excel.
