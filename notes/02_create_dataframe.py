# ============================================
# Lesson 2: Creating a DataFrame
# ============================================

import pandas as pd

# A DataFrame is like a spreadsheet or SQL table
# Create one from a dictionary:
# - keys = column names
# - values = lists of column data (all must be same length!)

df1 = pd.DataFrame({
    'Product ID': [1, 2, 3, 4],
    'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
    'Color': ['blue', 'green', 'red', 'black']
})

print(df1)

# ============================================
# Creating, Loading, and Selecting Data
# ============================================

import pandas as pd

# ---- METHOD 1: Create from Dictionary ----
# keys = column names, values = lists of data
df1 = pd.DataFrame({
    'Product ID': [1, 2, 3, 4],
    'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
    'Color': ['blue', 'green', 'red', 'black']
})

# ---- METHOD 2: Create from List of Lists ----
# Each inner list = one row, columns defined separately
df2 = pd.DataFrame([
    [1, 'San Diego', 100],
    [2, 'Los Angeles', 120],
    [3, 'San Francisco', 90],
    [4, 'Sacramento', 115]
],
    columns=['Store ID', 'Location', 'Number of Employees']
)

# ---- LOADING FROM CSV ----
df = pd.read_csv('filename.csv')   # load CSV into DataFrame
df.to_csv('new_file.csv')          # save DataFrame to CSV

# ---- INSPECTING A DATAFRAME ----
print(df.head())      # first 5 rows (default)
print(df.head(10))    # first 10 rows
print(df.info())      # column names, data types, non-null counts