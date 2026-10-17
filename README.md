# Python for Finance

Personal learning repo for Codecademy's **[Analyze Financial Data with Python](https://www.codecademy.com/learn/paths/finance-python)** skill path.
Coming from an R / RStudio background, I document every concept as runnable Python notes, with finance examples, output shown as comments, and R equivalents where they help.

## Progress

| # | Track | Status |
|---|-------|--------|
| 1 | Introduction to Python | Done |
| 2 | Introduction to NumPy | Done |
| 3 | Introduction to Pandas (incl. importing finance data) | Done |
| 4 | Visualizing Finance Data (Matplotlib, portfolio optimization) | In progress |
| 5 | Regression | Planned |
| 6 | Capstone | Planned |

## Highlights

| Project | What it does |
|---------|--------------|
| [US Financial Health 1999-2019](notes/3_pandas/05_project_us_financial_health.py) | Pulls stock indexes (FRED), commodities (CSV) and GDP / exports (World Bank), computes log returns and compares volatility across assets. Includes fixes the course skips: sorting newest-first data before `shift()`, and annualizing daily volatility so daily and yearly series can be compared. |
| [ShoeFly A/B test](notes/3_pandas/04_project_ab_test_shoefly.py) | Ad-campaign analysis with `groupby`, pivot tables and click-through percentages. |

## Repo structure

```
notes/
├── 1_python/                    core concepts: returns, risk, variance
├── 2_numpy/                     arrays and element-wise operations
├── 3_pandas/                    DataFrames, aggregates, importing finance data
└── 4_visualizing_finance_data/  Matplotlib, portfolio optimization
data/                            CSV files used by the notes
```

**File naming:** `<module>_<type>_<topic>.py`. The number is the module within its track; `practice` and `project` files share the number of the lesson they belong to, e.g. `04_aggregates.py`, `04_practice_aggregates_orders.py`, `04_project_ab_test_shoefly.py`.

## How the notes are written

Each notes file is a runnable script:
- condensed task description, then the working code
- output shown inline as `# ->` comments
- ASCII diagrams for concepts like MultiIndex, `shift()` or covariance matrices
- mistakes I made, flagged as learning points
- R equivalents (e.g. `shift(1)` ~ `dplyr::lag()`)

> **A historic moment, October 2026:** halfway through the Matplotlib lesson, after typing `# ->` output comments by hand for five whole sections, I discovered Jupyter notebooks - where the output simply appears under the code by itself, just like I was used to with R Markdown. Everything up to `3_pandas` stays as `.py` scripts, a monument to my patience. From `4_visualizing_finance_data` onwards it's `.ipynb` all the way: code, then the chart right below it. You live and you learn..

## Setup

```
py -m pip install pandas numpy matplotlib pandas-datareader ipykernel
```

On Python 3.12+, if `pandas-datareader` fails with a `distutils` error, run `py -m pip install setuptools` and install it again.

Run scripts from the repo root so the `data/...` paths resolve, e.g.

```
py notes\3_pandas\05_project_us_financial_health.py
```

Some notes pull live data from FRED and the World Bank and need an internet connection. No API keys are stored in this repo.

## Tools

Python 3.14 · pandas · NumPy · Matplotlib · pandas-datareader · VS Code · Git
