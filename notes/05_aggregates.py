# ============================================
# Aggregates in Pandas
# ============================================
# Covers: column statistics, groupby,
#         aggregate functions, pivot tables
# ============================================

import pandas as pd
import numpy as np

# Load the sample dataset (save orders.csv to your data/ folder)
# Columns: id, first_name, last_name, email,
#          shoe_type, shoe_color, shoe_material, price, quantity
orders = pd.read_csv('data/orders.csv')
 

# print(orders.head())
#    id first_name last_name                    email    shoe_type shoe_color shoe_material  price  quantity
# 0   1       Anna     Smith    anna.smith@email.com  ballet flats      black       leather  45.99         1
# 1   2       Beth     Jones    beth.jones@email.com  ballet flats      black       leather  45.99         2
# 2   3      Clara     Brown   clara.brown@email.com  ballet flats      brown         suede  49.99         1
# 3   4      Diana     White   diana.white@email.com  ballet flats      brown         suede  49.99         1
# 4   5        Eva     Green    eva.green@email.com  ballet flats      brown         suede  49.99         3


# ---- COLUMN STATISTICS ----
# Calculate a single summary statistic for a column
# General syntax: df['column_name'].method()

orders['price'].mean()         # -> 69.02  (average price)
orders['price'].std()          # -> 18.25  (standard deviation)
orders['price'].median()       # -> 69.99
orders['price'].max()          # -> 95.99
orders['price'].min()          # -> 39.99
orders['price'].count()        # -> 60     (number of non-null rows)
orders['shoe_type'].nunique()  # -> 4      (ballet flats, sandals, stilettos, wedges)
orders['shoe_type'].unique()   # -> array(['ballet flats', 'sandals', 'stilettos', 'wedges'])


# ---- AGGREGATE FUNCTIONS I & II: .groupby() ----
# Group rows by a column, then apply a summary statistic
# Equivalent to GROUP BY in SQL

# Syntax:
# df.groupby('column_to_group_by')['column_to_aggregate'].method()

# Example: average price by shoe type
orders.groupby('shoe_type')['price'].mean()
# -> returns a Series with shoe_type as index

# Always use .reset_index() to convert back to a clean DataFrame:
orders.groupby('shoe_type')['price'].mean().reset_index()
# -> returns a proper DataFrame

# Common aggregation methods (interchangeable at the end of the chain):
# .mean()     - average
# .count()    - number of rows in each group
# .sum()      - total
# .min()      - smallest value in each group
# .max()      - largest value in each group
# .median()   - middle value
# .std()      - standard deviation (useful for volatility in finance!)
# .nunique()  - number of distinct values per group


# ---- AGGREGATE FUNCTIONS III: .agg() ----
# Apply multiple aggregation functions at once
# Pass a dictionary: {column: aggregation_method_as_string}

# df.groupby('column').agg({'col_1': 'max', 'col_2': 'mean'}).reset_index()

# Example: get the cheapest and most expensive shoe per type
orders.groupby('shoe_type').agg(
    {'price': 'max', 'quantity': 'count'}
).reset_index()


# ---- AGGREGATE FUNCTIONS IV: groupby WITH MULTIPLE COLUMNS ----
# Pass a LIST of column names to groupby to group by more than one column

# df.groupby(['col_1', 'col_2'])['col_to_aggregate'].method().reset_index()

# Example: count shoe sales by shoe_type AND shoe_color combination
shoe_counts = orders.groupby(['shoe_type', 'shoe_color'])['id'].count().reset_index()
# -> one row per unique (shoe_type, shoe_color) pair

# print(shoe_counts)
# shoe_type    shoe_color  id
# ballet flat  black       2
# ballet flat  brown       4
# ballet flat  navy        7
# ...


# ---- PIVOT TABLES ----
# Reorganises a grouped DataFrame so that:
#   - one column's values become the ROW index
#   - another column's values become the COLUMN headers
#   - a third column fills in the values
#
# Useful for comparing combinations at a glance (like a crosstab)
# Think of it like going from "long format" to "wide format" (familiar from R!)

# Syntax:
# df.pivot(
#     columns='ColumnToPivot',    # unique values become new column headers
#     index='ColumnToBeRows',     # unique values become row labels
#     values='ColumnToBeValues'   # fills the cells
# ).reset_index()

# Generic example using a stores/sales dataset:
# unpivoted = df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
# pivoted = unpivoted.pivot(
#     columns='Day of Week',
#     index='Location',
#     values='Total Sales'
# ).reset_index()

# -> Before pivot (long):
# Location      Day of Week   Total Sales
# Chelsea       M             300
# Chelsea       Tu            310
# West Village  M             300
# West Village  Tu            310

# -> After pivot (wide):
# Location      M     Tu    W     Th
# Chelsea       300   310   375   390
# West Village  300   310   400   450

# ShoeFly example: count per shoe_type/shoe_color, pivoted for easy comparison
shoe_counts = orders.groupby(['shoe_type', 'shoe_color'])['id'].count().reset_index()

shoe_counts_pivot = shoe_counts.pivot(
    columns='shoe_color',
    index='shoe_type',
    values='id'
).reset_index()

# print(shoe_counts_pivot)
# shoe_type     black  brown  navy  red  white
# ballet flats  ...    ...    ...   ...  ...
# sandals       ...    ...    ...   ...  ...
# stilettos     ...    ...    ...   ...  ...
# wedges        ...    ...    ...   ...  ...


# ============================================
# REMEMBER from 03_modifying_dataframes.py:
# .apply() + lambda can transform values before aggregating
# e.g. df['price_usd'] = df['price_eur'].apply(lambda x: x * 1.08)
# ============================================


# ============================================
# Aggregates in Pandas — Review Exercise
# ============================================
# Dataset: user_visits.csv
# Columns: id, first_name, last_name, email, month, utm_source
#
# utm_source = how the user arrived at ShoeFly.com
# e.g. facebook, google, yahoo, twitter, email
# ============================================

import pandas as pd
import numpy as np

# --- SETUP ---
# Load user_visits.csv into a DataFrame called user_visits
user_visits = pd.read_csv('data/user_visits.csv')
print(user_visits.head())

# ============================================
# CHECKPOINT 1
# The column utm_source contains information about how users got to ShoeFly's homepage.
# Use groupby to calculate how many visits came from each utm_source.
# Save to variable: click_source
# Remember to use reset_index()!
click_source = user_visits.groupby("utm_source")["id"].count().reset_index()
print(click_source)

# ============================================
# CHECKPOINT 2
# Marketing thinks traffic has been changing over the past few months.
# Use groupby to calculate the number of visits from each utm_source for each month.
# Save to variable: click_source_by_month
# Hint: you need to group by TWO columns this time
click_source_by_month = user_visits.groupby(["utm_source", "month"])["id"].count().reset_index()
print(click_source_by_month)

# ============================================
# CHECKPOINT 3
# The head of Marketing finds the table hard to read.
# Use pivot to create a pivot table where:
#   - rows    = utm_source
#   - columns = month
#   - values  = id (the count)
# Save to variable: click_source_by_month_pivot

click_source_by_month_pivot = click_source_by_month.pivot(
    columns="month",
    index="utm_source",
    values="id"
).reset_index()

print(click_source_by_month_pivot)
# Expected output shape:
# utm_source   1 - January   2 - February   3 - March
# email        ...           ...            ...
# facebook     ...           ...            ...
# google       ...           ...            ...
# twitter      ...           ...            ...
# yahoo        ...           ...            ...