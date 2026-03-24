# Module 4 Exercises

Time to practice finding and working with external data. These exercises build on the datasets you downloaded with `download_public_datasets.py`.

---

## Exercise 1: Explore the Titanic Dataset

Load `../data/external/titanic.csv` and answer these questions:

1. How many passengers are in the dataset?
2. What percentage of passengers survived?
3. What is the average age of passengers?
4. How many columns have missing values?

```python
# Your code here
```

---

## Exercise 2: Tipping Patterns

Load `../data/external/tips.csv` and find out:

1. What is the average tip amount?
2. Which day of the week has the highest average tip?
3. Do dinner parties tip more than lunch parties on average?

```python
# Your code here
```

---

## Exercise 3: Iris Species Comparison

Load `../data/external/iris.csv` and compare the three flower species:

1. What is the average petal length for each species?
2. Which species has the widest sepals on average?

```python
# Your code here
```

---

## Exercise 4: Find Your Own Dataset

Visit one of the sources listed in `dataset_guide.md` and download a dataset that interests you. Then:

1. Load it into pandas
2. Print the shape, column names, and data types
3. Check for missing values
4. Write down 3 questions you could answer with this data

This is an open-ended exercise — there's no single right answer. The goal is to practice the full workflow of finding, loading, and exploring unfamiliar data.

---

## Hints

**Exercise 1:**
Use `pd.read_csv()` to load the file. For survival percentage: the "Survived" column is 0 or 1, so `.mean() * 100` gives you the percentage. For missing values: `df.isnull().sum()`.

**Exercise 2:**
Use `.groupby("day")["tip"].mean()` to get average tip by day. For dinner vs. lunch, group by the "time" column instead.

**Exercise 3:**
Use `.groupby("species")` and then select the column you want to average. For widest sepals, look at the "sepal_width" column.

**Exercise 4:**
Start with `df.shape`, `df.dtypes`, `df.head()`, and `df.isnull().sum()`. These four commands tell you most of what you need to know about any new dataset.
