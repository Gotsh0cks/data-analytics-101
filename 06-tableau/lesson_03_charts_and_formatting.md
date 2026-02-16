# Lesson 3: Chart Types and Formatting

## Choosing the Right Chart

Different questions call for different chart types. Here's a quick guide:

| Question Type | Best Chart | Example |
|--------------|------------|---------|
| "How do categories compare?" | Bar chart | Revenue by region |
| "How has something changed over time?" | Line chart | Monthly sales trend |
| "What's the proportion?" | Pie chart or treemap | Market share by category |
| "Is there a relationship?" | Scatter plot | Price vs. quantity sold |
| "How is data distributed?" | Histogram | Salary distribution |
| "Where is it happening?" | Map | Sales by state |

## Bar Charts (Horizontal and Vertical)

### Vertical bar chart (default)
- Dimension on Columns, Measure on Rows
- Good for: comparing categories with short names

### Horizontal bar chart
- Dimension on Rows, Measure on Columns
- Good for: categories with long names (they're easier to read horizontally)

### Stacked bar chart
1. Create a basic bar chart (e.g., Revenue by Region)
2. Drag a second dimension (e.g., Category) to the **Color** box in the Marks card
3. Each bar is now split by color, showing the breakdown within each region

## Line Charts

Line charts are for time-based data:

1. Drag a **date field** to Columns
2. Drag a **measure** to Rows
3. Tableau automatically creates a line chart

### Multiple lines
- Drag a dimension (like Category or Region) to **Color** in the Marks card
- You get one line per category, each in a different color

### Adjusting date granularity
- Right-click the date on the Columns shelf
- Choose: Year > Quarter > Month > Week > Day
- Or click the small **+** button on the date pill to drill down

## Scatter Plots

Show the relationship between two numeric fields:

1. Drag one measure to Columns (e.g., **Quantity**)
2. Drag another measure to Rows (e.g., **Revenue**)
3. Each dot represents one row of data

### Add meaning with color and size
- Drag a dimension to **Color** to color-code the dots
- Drag a measure to **Size** to make dots bigger or smaller based on value

## Pie Charts

Use sparingly — they're hard to read with more than 5 slices:

1. Click **Show Me** (top right)
2. Select the **pie chart** icon
3. Drag a dimension to **Color** (e.g., Category)
4. Drag a measure to **Angle** or **Size** (e.g., Revenue)

## Formatting Your Charts

### Titles
- Double-click the chart title to edit it
- Make it descriptive: "Total Revenue by Product Category, 2024" is better than "Sheet 1"

### Axis Labels
- Right-click an axis > **Edit Axis** to change the title
- Right-click > **Format** to change font, color, and number format

### Number Formatting
- Right-click a measure pill > **Format** > **Numbers**
- Choose: Currency, Percentage, Number (with decimal places)
- Example: `$1,234.56` instead of `1234.56`

### Colors
- Click the **Color** box in the Marks card
- Click **Edit Colors** to choose a color palette
- Tableau offers color-blind-friendly palettes — use them for accessibility

### Gridlines and Borders
- Go to **Format** menu > **Lines** to control gridlines
- Go to **Format** menu > **Borders** to add or remove borders

### Font Size
- Go to **Format** menu > **Font** to change the default font
- Or right-click specific elements (title, axis, labels) to format individually

## Tooltips

Tooltips are the pop-up boxes that appear when you hover over a data point:

1. Click the **Tooltip** box in the Marks card
2. Edit the text — you can include any field using the **Insert** dropdown
3. Example: "Region: <Region>\nRevenue: <SUM(Revenue)>"

## Professional Tips

1. **Remove clutter.** Hide unnecessary gridlines and borders. Less is more.
2. **Use consistent colors.** If "Electronics" is blue on one chart, keep it blue everywhere.
3. **Right-align numbers.** Numbers are easier to compare when right-aligned.
4. **Start bar charts at zero.** Never truncate the axis — it misleads viewers.
5. **Add context.** Include time periods, units, and data sources in titles or captions.

## Practice

Try creating each chart type using the sales_data:
1. A horizontal bar chart of revenue by product
2. A line chart of revenue over time, colored by region
3. A scatter plot of quantity vs. revenue, colored by category

Experiment with formatting each one until it looks clean and professional.
