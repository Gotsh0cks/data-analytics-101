# Lesson 3: Sorting and Filtering

## Why Sort and Filter?

When you have 100 rows, you can scan through them. When you have 10,000, you cannot. Sorting and filtering let you focus on exactly the data you need.

- **Sorting** rearranges rows in order (A-Z, smallest to largest, newest to oldest)
- **Filtering** hides rows that do not match your criteria (show only Electronics, show only the North region)

## Sorting Data

### Sort by One Column

Open `data/excel/sales_data.xlsx` and try this:

1. Click anywhere in the **revenue** column (column G)
2. Go to the **Data** tab in the ribbon
3. Click **Sort Largest to Smallest** (the Z-A button with the down arrow)
4. The entire table rearranges so the highest-revenue sales are at the top

To sort alphabetically: click a text column (like product), then click **Sort A to Z**.

**Important:** Excel sorts the *entire row* together. When you sort by revenue, the product name, region, and all other columns move with their revenue value. Your data stays intact.

### Sort by Multiple Columns

Sometimes you need to sort by more than one column. For example: sort by region first, then by revenue within each region.

1. Go to **Data** tab > **Sort**
2. A dialog box appears
3. Set "Sort by" to **region** (A to Z)
4. Click **Add Level**
5. Set "Then by" to **revenue** (Largest to Smallest)
6. Click **OK**

Now your data is grouped by region, with the highest-revenue sale at the top of each region.

### Keyboard Shortcut

In Google Sheets: select a column and use **Data > Sort sheet by column**.

## Filtering Data

Filtering temporarily hides rows that do not match your criteria. The hidden rows are not deleted they are just invisible until you remove the filter.

### Turning On Filters

1. Click anywhere in your data
2. Go to **Data** tab > **Filter** (or press Ctrl + Shift + L)
3. Small dropdown arrows appear in each header cell

### Using a Filter

1. Click the dropdown arrow in the **category** column header
2. A list of all unique values appears (Accessories, Electronics, Furniture)
3. Uncheck **Select All**
4. Check only **Electronics**
5. Click **OK**

Now you see only Electronics sales. The row numbers on the left turn blue to indicate filtering is active, and some row numbers are missing (those rows are hidden, not deleted).

### Filtering by Multiple Columns

You can filter multiple columns at once:

1. Filter **category** to "Electronics"
2. Then filter **region** to "North"
3. Now you see only Electronics sales in the North region

### Number Filters

For numeric columns like revenue, the dropdown offers additional options:

1. Click the dropdown in the **revenue** column
2. Select **Number Filters** > **Greater Than**
3. Type **1000**
4. Click **OK**

Now you see only sales over $1,000.

### Removing Filters

- To clear a single column's filter: click the dropdown arrow > **Clear Filter**
- To remove all filters: **Data** tab > **Filter** (toggles it off)

## Find and Replace

To find specific values:

1. Press **Ctrl + F** (Find)
2. Type what you are looking for (e.g., "Laptop")
3. Click **Find All** to see every occurrence
4. Click **Find Next** to jump to them one by one

To replace values:

1. Press **Ctrl + H** (Replace)
2. Type the old value and the new value
3. Click **Replace All** to change every occurrence

This is useful for fixing typos or renaming categories consistently.

## Conditional Formatting

Conditional formatting changes a cell's appearance based on its value. This makes patterns visible at a glance.

### Highlighting High Values

1. Select the revenue column (G2:G103)
2. Go to **Home** tab > **Conditional Formatting** > **Highlight Cells Rules** > **Greater Than**
3. Type **1000**
4. Choose a formatting style (like "Light Red Fill")
5. Click **OK**

Now every sale over $1,000 is highlighted in red. You can instantly see the big sales.

### Color Scales

1. Select the revenue column
2. **Conditional Formatting** > **Color Scales** > choose a green-yellow-red scale
3. The highest values turn green, the lowest turn red, and middle values are yellow

This gives you a heat map effect that makes patterns visible immediately.

## Try It Yourself

Open `data/excel/employees.xlsx` and try these:

1. Sort employees by salary (highest first). Who is the highest-paid?
2. Filter to show only the Engineering department. How many engineers are there?
3. Filter to show employees hired after 2021. Who are the newest hires?
4. Apply conditional formatting to the salary column. Which department has the most green (high-salary) cells?
5. Clear all filters when done

---

Next up: [Pivot Tables](lesson_04_pivot_tables.md) the most powerful feature in Excel.
