# Where to Find Free Datasets

One of the most valuable skills as a data analyst is knowing **where to find data**. Below is a curated list of the best free sources, organized by type. All of these are free to use.

---

## General-Purpose Dataset Repositories

### Kaggle (kaggle.com/datasets)

**What it is:** The largest community for data science. Thousands of datasets on every topic imaginable from house prices to Spotify playlists to hospital readmissions.

**Good for:** Practice projects, building a portfolio, exploring diverse topics.

**How to use it:**
1. Create a free account at kaggle.com
2. Browse or search for datasets
3. Download directly from the website, or use the Kaggle API (see `03_download_kaggle_dataset.py`)

**Tip:** Look at the "Usability" rating on each dataset. Higher ratings mean better documentation and cleaner data.

---

### Google Dataset Search (datasetsearch.research.google.com)

**What it is:** A search engine specifically for datasets. It indexes datasets published across the web.

**Good for:** Finding datasets on a specific topic when you're not sure where to look.

**How to use it:** Search just like you would on Google, but the results are all datasets. Each result tells you the format, who published it, and when it was last updated.

---

### UCI Machine Learning Repository (archive.ics.uci.edu)

**What it is:** A classic academic dataset collection maintained by UC Irvine. Many famous datasets live here (Iris, Wine Quality, Adult Census, etc.).

**Good for:** Well-documented, clean datasets that are great for learning.

**How to use it:** Browse by topic or search. Most datasets include documentation explaining every column.

---

## Government Data

### data.gov (United States)

**What it is:** The U.S. government's open data portal. Over 250,000 datasets covering health, education, transportation, climate, finance, and more.

**Good for:** Real-world data with real-world messiness. Great for portfolio projects that show you can work with imperfect data.

**Popular datasets:**
- Consumer complaint database (financial products)
- Hospital quality ratings
- Air quality measurements
- Federal employee salaries

---

### Census Bureau (data.census.gov)

**What it is:** Detailed demographic data about the United States population, income, education, housing, and more.

**Good for:** Geographic analysis, demographic trends, understanding populations.

**Tip:** The American Community Survey (ACS) is updated yearly and is one of the most widely used datasets in business analytics.

---

## Curated / Pre-Cleaned Collections

### FiveThirtyEight (github.com/fivethirtyeight/data)

**What it is:** The data behind FiveThirtyEight's articles. Well-documented, clean datasets on politics, sports, economics, and culture.

**Good for:** Clean, well-structured data that's ready to analyze immediately. Each dataset comes with the article that used it, so you can see what questions were asked.

---

### TidyTuesday (github.com/rfordatascience/tidytuesday)

**What it is:** A weekly data project. Every Tuesday, a new dataset is posted for the community to analyze and visualize.

**Good for:** Regular practice. Datasets are varied and interesting everything from Broadway shows to penguin measurements.

---

### Our World in Data (github.com/owid/owid-datasets)

**What it is:** Research and data on global problems poverty, disease, hunger, climate change, inequality, and more.

**Good for:** Time-series data, country comparisons, global trends.

---

## Datasets Used in This Course

The `02_download_public_datasets.py` script downloads these specific datasets for use in later modules:

| Dataset | Source | Description | Rows (approx.) |
|---------|--------|-------------|-----------------|
| Titanic Passengers | Stanford/Kaggle | Passenger survival data from the Titanic | ~890 |
| World Happiness Report | GitHub (public) | Country happiness scores and factors | ~150/year |
| Iris Flowers | UCI ML Repository | Classic dataset: flower measurements by species | 150 |
| Restaurant Tips | Seaborn (public) | Tipping data: bill, tip, day, time, party size | ~244 |

These were chosen because they are:
- **Free** with no account required
- **Small enough** to load quickly on any computer
- **Well-documented** so you know what every column means
- **Interesting** enough to ask real questions about

---

## How to Evaluate a Dataset

Before you commit to working with a dataset, ask yourself:

1. **Is it the right size?** Too small and you can't find meaningful patterns. Too large and your computer might struggle (as a beginner, aim for under 1 million rows).

2. **Is it well-documented?** Do you know what each column means? Are units specified (dollars vs. euros, Celsius vs. Fahrenheit)?

3. **Is it recent enough?** A 2005 salary dataset won't reflect today's job market.

4. **Can you ask interesting questions?** A good dataset should spark at least 3-5 questions you'd want to answer.

5. **Is the license clear?** Most government and academic datasets are public domain. Kaggle datasets usually specify their license on the download page.

---

## Next Steps

Now that you know where to find data, run `02_download_public_datasets.py` to grab some datasets automatically, or visit any of these sources and download something that interests you.
