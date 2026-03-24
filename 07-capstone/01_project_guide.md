# Capstone Project Guide

Follow these steps to complete your capstone project. Each step uses skills from a specific module.

---

## Step 1: Choose Your Dataset

Pick one of the external datasets from Module 6, or find your own from the sources in `01_dataset_guide.md` (in Module 6).

**Recommended options for your first project:**

| Dataset | File | Good For |
|---------|------|----------|
| Titanic | `data/external/titanic.csv` | Survival analysis, demographics |
| Restaurant Tips | `data/external/tips.csv` | Behavioral patterns, tipping factors |
| World Happiness | `data/external/world_happiness.csv` | Country comparisons, global trends |
| Iris Flowers | `data/external/iris.csv` | Species comparison, measurements |

If you did not download these yet, run:
```bash
python 06-real-world-data/02_download_public_datasets.py
```

---

## Step 2: Explore in Excel (Module 2 Skills)

Before writing any code, open your dataset in Excel to get a feel for it.

1. Open the CSV in Excel (or Google Sheets)
2. Look at the columns what does each one mean?
3. Check for obvious issues missing values, weird formatting
4. Write down **3-5 questions** you want to answer

**Example questions for the Titanic dataset:**
- Did passenger class affect survival?
- Were women more likely to survive than men?
- What was the average age of survivors vs. non-survivors?

---

## Step 3: Clean and Analyze with Python (Module 3 Skills)

Open `03_project_template.py` (or create your own script) and:

1. **Load the data** with `pd.read_csv()`
2. **Inspect it** with `.head()`, `.info()`, `.describe()`
3. **Clean it** handle missing values, fix data types
4. **Analyze it** filter, group, aggregate to answer your questions
5. **Print your findings** clearly

```python
import pandas as pd

df = pd.read_csv("../data/external/titanic.csv")

# Example: survival rate by class
survival = df.groupby("Pclass")["Survived"].mean() * 100
print("Survival rate by class:")
print(survival.round(1))
```

---

## Step 4: Query with SQL (Module 4 Skills)

If you loaded the data into SQL Server, write queries to answer your questions from a database perspective. This step is optional but demonstrates a valuable skill.

```sql
-- Example: Survival rate by class
SELECT
    Pclass,
    COUNT(*) AS total,
    SUM(Survived) AS survived,
    CAST(100.0 * SUM(Survived) / COUNT(*) AS DECIMAL(5,1)) AS survival_pct
FROM Titanic
GROUP BY Pclass
ORDER BY Pclass;
```

---

## Step 5: Visualize with matplotlib (Module 5, Part 1 Skills)

Create at least 3 charts that support your findings:

1. **A bar chart** comparing categories (e.g., survival rate by class)
2. **A chart of your choice** (line, scatter, pie whatever fits your data)
3. **A polished chart** with seaborn styling for your portfolio

Save each chart as a PNG file.

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

survival.plot(kind="bar", color=["#e74c3c", "#f39c12", "#27ae60"])
plt.title("Titanic Survival Rate by Passenger Class", fontsize=14, fontweight="bold")
plt.ylabel("Survival Rate (%)")
plt.xlabel("Passenger Class")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("survival_by_class.png", dpi=150)
plt.show()
```

---

## Step 6: Build a Tableau Dashboard (Module 5, Part 2 Skills)

1. Run `lesson_05_prepare_data_for_tableau.py` (in Module 5) if you have not already
2. Open Tableau Public and connect to your dataset CSV
3. Create 3-4 worksheets with different chart types
4. Combine them into a single interactive dashboard
5. Add filters, titles, and clean formatting

---

## Step 7: Publish and Summarize

1. **Publish** your Tableau dashboard to Tableau Public
2. **Write a brief summary** (3-5 sentences) of what you found. This could be:
   - A comment on your Tableau Public profile
   - A text file in this folder
   - Notes for a future resume or LinkedIn post

**Example summary:**
> "I analyzed the Titanic passenger dataset to understand survival patterns. First-class passengers survived at 63% vs. just 24% for third-class. Women survived at much higher rates than men across all classes. The data suggests that both wealth and gender strongly influenced survival outcomes."

---

## You Did It

If you completed all seven steps, you have just done what a professional data analyst does:

1. Found and chose relevant data
2. Explored it to understand its structure
3. Cleaned and analyzed it with code
4. Queried it with SQL
5. Created visualizations that tell a story
6. Built an interactive dashboard for stakeholders
7. Communicated your findings clearly

This is your portfolio piece. Be proud of it.
