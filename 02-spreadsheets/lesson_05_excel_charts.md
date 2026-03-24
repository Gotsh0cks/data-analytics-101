# Lesson 5: Excel Charts

## Why Charts?

A table of numbers is precise. A chart is *understandable*. When you show a manager that "North region generated $15,340 in revenue, South generated $12,450, East generated $10,880, and West generated $9,230," their eyes glaze over. When you show them a bar chart, they immediately see that North leads by a wide margin.

Charts are how you **communicate** data. They are the bridge between your analysis and someone else's understanding.

## Creating a Bar Chart

Bar charts compare categories. They answer the question: "How do these groups compare?"

### From Raw Data

1. Open `data/excel/sales_data.xlsx`
2. First, create a small summary (or use a pivot table) with categories and their totals
3. Select the summary data (including headers)
4. Go to **Insert** tab > **Charts** section
5. Click **Bar Chart** (or **Column Chart** for vertical bars)
6. A chart appears on the sheet

### From a Pivot Table (Easiest Method)

1. Create a pivot table with **category** in Rows and **Sum of revenue** in Values
2. Click anywhere in the pivot table
3. Go to **Insert** > **Column Chart** (or **PivotChart**)
4. Done — the chart automatically uses the pivot table data

### Customizing the Chart

Click on the chart to select it. You will see three buttons on the right:

- **+** (Chart Elements) — add/remove title, axis labels, data labels, gridlines
- **Paintbrush** (Chart Styles) — change colors and style
- **Funnel** (Chart Filters) — filter what data appears

#### Adding a Title
1. Click the chart title (or click **+** > check **Chart Title**)
2. Type a descriptive title like "Total Revenue by Product Category"

#### Adding Data Labels
1. Click **+** > check **Data Labels**
2. Numbers appear on each bar showing the exact value

## Creating a Line Chart

Line charts show trends over time. They answer: "How has this changed?"

1. Create a pivot table with **date** in Rows and **Sum of revenue** in Values
   - Right-click the date field > **Group** > select **Months** (this groups daily data into monthly totals)
2. Select the pivot table
3. Go to **Insert** > **Line Chart**
4. You now see revenue trend over time

### When to Use Lines vs. Bars

- **Line chart** — data has a natural order (time, sequence). Shows trends.
- **Bar chart** — data is categorical (regions, products). Shows comparisons.

Do not use a line chart for categories — a line implies continuity between points, which does not make sense for "Electronics, Furniture, Supplies."

## Creating a Pie Chart

Pie charts show proportions — what percentage of the total each category represents.

1. Create a summary of revenue by category (pivot table or manual)
2. Select the data
3. **Insert** > **Pie Chart**

### A Warning About Pie Charts

Pie charts are popular but often misleading. The human eye is bad at comparing slice sizes. If you have more than 4-5 categories, use a bar chart instead. If two slices are similar in size, a pie chart makes them look equal even when they are not.

**Rule of thumb:** Use pie charts only when you have 3-5 categories and one category clearly dominates.

## Formatting Tips

### Colors
- Right-click any bar/slice > **Format Data Series** > choose colors
- Stick to 2-3 colors for clarity. Do not use rainbow colors.

### Axes
- Right-click an axis > **Format Axis** to change the scale, number format, or font size
- Always start bar chart y-axes at zero. Starting at a higher number exaggerates differences.

### Legends
- If your chart has only one series (one color), remove the legend — it adds clutter
- Click the legend and press Delete

### Chart Size
- Drag the corners of the chart to resize
- Make it large enough to read. Small charts are useless charts.

## Choosing the Right Chart

| Question | Chart Type |
|----------|------------|
| Compare categories | Bar / Column chart |
| Show change over time | Line chart |
| Show proportions (few categories) | Pie chart |
| Show relationship between two numbers | Scatter plot (Insert > Scatter) |

## Try It Yourself

Using `data/excel/sales_data.xlsx`:

1. Create a bar chart showing total revenue by product (use a pivot table)
2. Create a line chart showing revenue by month
3. Create a pie chart showing the proportion of sales by region
4. Add titles, data labels, and clean formatting to each chart

Using `data/excel/employees.xlsx`:

5. Create a bar chart showing average salary by department
6. Create a bar chart showing employee count by city

---

You have completed the Excel module. You now know how to navigate spreadsheets, write formulas, sort and filter, build pivot tables, and create charts. These are foundational skills that you will use throughout your career.

Next up: [Module 3: Data Analysis with Python](../03-data-analysis/) — learn to do everything you just did, but with code that scales to millions of rows.
