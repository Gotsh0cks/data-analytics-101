# Module 6 Exercises

These exercises guide you through building complete dashboards. Each one uses datasets you've already downloaded and prepared.

---

## Exercise 1: Sales Performance Dashboard

Build a dashboard using `data/tableau_ready/sales_data.csv` that answers: **"How is our sales performance across categories and regions?"**

Create these charts:
1. A horizontal bar chart: total revenue by product (sorted highest to lowest)
2. A line chart: revenue over time (by month)
3. A stacked bar chart: revenue by region, broken down by category

Combine them into a dashboard with:
- A Region filter that controls all three charts
- A descriptive title
- Clean formatting (no default "Sheet 1" names)

---

## Exercise 2: Employee Overview Dashboard

Build a dashboard using `data/tableau_ready/employees.csv` that answers: **"What does our workforce look like?"**

Create these charts:
1. A bar chart: number of employees per department
2. A bar chart: average salary by department
3. A scatter plot: hire date vs. salary (are newer employees paid more or less?)

Combine them into a dashboard with:
- A Department filter
- Labels showing actual values on the bar charts

---

## Exercise 3: Titanic Survival Analysis

Build a dashboard using `data/tableau_ready/titanic.csv` that answers: **"Who survived the Titanic and why?"**

Create these charts:
1. A bar chart: survival rate by passenger class (1st, 2nd, 3rd)
2. A bar chart: survival rate by sex
3. A histogram: age distribution, colored by survival status

Combine them into a dashboard with:
- Use one chart as a filter for the others
- A title and explanatory text box

**Bonus:** Add a calculated field for survival rate: `SUM([Survived]) / COUNT([Survived])`

---

## Exercise 4: Tipping Patterns Dashboard

Build a dashboard using `data/tableau_ready/tips.csv` that answers: **"What affects how much people tip?"**

Create these charts:
1. A bar chart: average tip percentage by day of the week
   - Tip percentage = tip / total_bill * 100 (create a calculated field)
2. A scatter plot: total bill vs. tip amount, colored by time (lunch/dinner)
3. A bar chart: average tip by party size

Combine them into an interactive dashboard.

---

## Exercise 5: Portfolio Project (Open-Ended)

Choose one of the external datasets (or find a new one from the sources in Module 4) and build a complete dashboard that:

1. Has at least 3 different chart types
2. Includes at least 1 interactive filter
3. Has a clear title and descriptive subtitle
4. Answers a specific question about the data
5. Is published to your Tableau Public profile

This is your portfolio piece — take your time and make it look professional.

---

## Tips for All Exercises

- **Start with questions.** Before building charts, write down 3 questions you want to answer.
- **One chart per question.** Each chart should answer one specific question.
- **Iterate.** Your first version won't be perfect. Build, review, improve.
- **Get feedback.** Show your dashboard to someone and ask if they understand it without explanation.
- **Save often.** Ctrl+S is your friend.
