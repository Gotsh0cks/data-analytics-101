# Module 5 Exercises

This module covers two tools, so the exercises are split into two parts.

---

# Part 1: Code-Based Visualization (matplotlib / seaborn)

Save each chart as a PNG file. Remember the basics:
- A clear, descriptive title
- Labeled axes
- `plt.tight_layout()` before saving
- `plt.savefig("filename.png")` to save
- `plt.show()` to display

---

## Exercise 1: Average Salary by Department (Bar Chart)

Using `../data/employees.csv`, create a **vertical bar chart** showing the **average salary** for each department.

- Title: "Average Salary by Department"
- Labeled axes
- Save as `exercise_01_salary_by_dept.png`

---

## Exercise 2: Employees per Department (Pie Chart)

Using `../data/employees.csv`, create a **pie chart** showing how many employees are in each department.

- Labels for each department with percentages (`autopct`)
- Save as `exercise_02_employees_pie.png`

---

## Exercise 3: Customer Signups per Month (Line Chart)

Using `../data/customers.csv`, create a **line chart** showing new customer signups each month.

- Convert `signup_date` to datetime, group by month
- Add markers at each data point
- Save as `exercise_03_signups_per_month.png`

---

## Exercise 4: Salary vs. Tenure (Scatter Plot)

Using `../data/employees.csv`, create a **scatter plot** showing salary vs. years since hire.

- Semi-transparent dots (`alpha=0.6`)
- Save as `exercise_04_salary_vs_tenure.png`

---

## Exercise 5: Presentation-Ready Chart

Take any chart above and make it presentation-ready with seaborn styling:

- Use `sns.set_style("whitegrid")`
- Bold title with larger font
- Save with `dpi=150` for higher quality

---

# Part 2: Tableau Dashboards

Run `prepare_data_for_tableau.py` first, then open files from `data/tableau_ready/` in Tableau Public.

---

## Exercise 6: Sales Performance Dashboard

Build a dashboard using `sales_data.csv` answering: **"How is our sales performance across categories and regions?"**

Create:
1. A horizontal bar chart: total revenue by product (sorted)
2. A line chart: revenue over time (by month)
3. A stacked bar chart: revenue by region, broken down by category

Dashboard requirements:
- A Region filter that controls all three charts
- A descriptive title
- Clean formatting (no "Sheet 1" names)

---

## Exercise 7: Employee Overview Dashboard

Build a dashboard using `employees.csv` answering: **"What does our workforce look like?"**

Create:
1. A bar chart: number of employees per department
2. A bar chart: average salary by department
3. A scatter plot: hire date vs. salary

Dashboard requirements:
- A Department filter
- Data labels on the bar charts

---

## Exercise 8: Portfolio Project (Open-Ended)

Choose any dataset and build a complete dashboard that:

1. Has at least 3 different chart types
2. Includes at least 1 interactive filter
3. Has a clear title and subtitle
4. Answers a specific question about the data
5. Is published to your Tableau Public profile

---

## Hints

**Exercise 1:** `avg_salary = df.groupby("department")["salary"].mean()`

**Exercise 2:** `dept_counts = df["department"].value_counts()` then `plt.pie(dept_counts.values, labels=dept_counts.index, autopct="%1.1f%%")`

**Exercise 3:** Convert dates: `df["signup_date"] = pd.to_datetime(df["signup_date"])`, group with `.dt.to_period("M")`

**Exercise 4:** Calculate years: `(datetime.now() - df["hire_date"]).dt.days / 365.25`

**Exercise 5:** `import seaborn as sns; sns.set_style("whitegrid"); plt.savefig("file.png", dpi=150)`

**Exercise 6-8:** Create pivot-style summaries in Tableau first, then build charts. Use the funnel icon to make charts act as filters.
