# Lesson 4: Interactive Dashboards

## What is a Dashboard?

A dashboard combines multiple charts (worksheets) onto a single screen. Instead of flipping between separate charts, viewers see everything at once with interactive filters that update all charts simultaneously.

Dashboards are what stakeholders and managers actually look at. Individual charts are the building blocks; the dashboard is the finished product.

## Before You Start

Make sure you have at least 2-3 worksheets created from the previous lessons. For example:
- A bar chart of revenue by category
- A line chart of revenue over time
- A bar chart of revenue by region

## Creating a Dashboard

### Step 1: Open a New Dashboard

- Click the **New Dashboard** icon at the bottom of the screen (looks like a grid with a plus sign)
- Or go to **Dashboard** menu > **New Dashboard**

### Step 2: Set the Size

On the left side, under **Size**:
- Click the dropdown and choose a size
- **Automatic** adapts to the viewer's screen (good for web)
- **Fixed size** > **Laptop Browser (1366 x 768)** is a safe default

### Step 3: Add Your Charts

The left sidebar shows all your worksheets:
1. **Drag a worksheet** from the sidebar onto the dashboard canvas
2. It fills the available space
3. **Drag a second worksheet** drop it to the left, right, top, or bottom of the first one
4. Tableau shows a gray shading to indicate where the new chart will go
5. Repeat for additional charts

### Step 4: Arrange the Layout

- **Drag the edges** between charts to resize them
- **Click a chart** then drag it to rearrange
- Delete a chart from the dashboard by clicking the **X** in its top-right corner (this doesn't delete the worksheet itself)

## Adding Interactive Filters

This is where dashboards become powerful. A single filter can control multiple charts:

### Method 1: Use a chart as a filter

1. Click on one of your charts in the dashboard
2. Click the **funnel icon** in the small toolbar that appears (top-right of the chart)
3. Now, when you click a bar or point in that chart, the other charts filter to match

For example: click "Electronics" on the bar chart, and the line chart updates to show only Electronics revenue over time.

### Method 2: Add a standalone filter

1. Click a chart in the dashboard
2. In the chart's small toolbar, click the **down arrow** > **Filters**
3. Choose a field to filter on (e.g., Region)
4. A dropdown filter appears on the dashboard
5. Right-click the filter > **Apply to Worksheets** > **All Using This Data Source**

Now this single filter controls all charts on the dashboard.

## Adding a Title

1. Check the **Show Dashboard Title** checkbox at the bottom of the left sidebar
2. Double-click the title to edit it
3. Write something descriptive: "Sales Performance Dashboard 2024"

## Adding Text Boxes

For additional context (data source notes, date ranges, instructions):

1. In the left sidebar, find **Objects** at the bottom
2. Drag **Text** onto the dashboard
3. Type your text (e.g., "Data source: Company sales database, Jan-Apr 2024")

## Layout Tips

### The "T" Layout

A common dashboard layout:
```
┌─────────────────────────────┐
│         TITLE / KPIs        │
├──────────────┬──────────────┤
│              │              │
│  Main Chart  │  Supporting  │
│              │    Chart     │
│              │              │
├──────────────┴──────────────┤
│        Detail Table         │
└─────────────────────────────┘
```

### The "Side-by-Side" Layout

Good for comparing two views:
```
┌──────────────┬──────────────┐
│   Filter Bar │   Filter Bar │
├──────────────┼──────────────┤
│              │              │
│   Chart A    │   Chart B    │
│              │              │
└──────────────┴──────────────┘
```

## Tiled vs. Floating

- **Tiled** (default): Charts snap into a grid. Easier to keep organized.
- **Floating**: Charts can overlap and be placed anywhere. More flexible but harder to align.

Stick with tiled layouts while learning. You can switch to floating for specific elements later.

## Making It Look Professional

1. **Consistent fonts.** Right-click any text > Format to change fonts. Use the same font everywhere.
2. **Aligned elements.** Use the layout containers (horizontal and vertical) to keep things aligned.
3. **White space.** Don't cram everything together. Add padding (right-click a chart > **Padding**).
4. **Muted colors.** Avoid bright neon colors. Tableau's default palettes are usually fine.
5. **Clear labels.** Every chart should have a descriptive title. Axes should be labeled.

## Try It Yourself

Build a dashboard with:
1. A bar chart showing total revenue by category (top)
2. A line chart showing revenue trend over time (bottom left)
3. A bar chart showing revenue by region (bottom right)
4. A Region filter that controls all three charts
5. A descriptive title

Click around the dashboard try using charts as filters and see how the other charts respond.
