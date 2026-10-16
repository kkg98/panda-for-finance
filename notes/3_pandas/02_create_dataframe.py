# ============================================
# Creating, Loading, and Selecting Data
# ============================================

import pandas as pd

# ---- METHOD 1: Create from Dictionary ----
# keys = column names, values = lists of data
# all lists must be the same length!
df1 = pd.DataFrame({
    'Product ID': [1, 2, 3, 4],
    'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
    'Color': ['blue', 'green', 'red', 'black']
})

# ---- METHOD 2: Create from List of Lists ----
# Each inner list = one row, columns defined separately
# Use this when order of columns matters
df2 = pd.DataFrame([
    [1, 'San Diego', 100],
    [2, 'Los Angeles', 120],
    [3, 'San Francisco', 90],
    [4, 'Sacramento', 115]
],
    columns=['Store ID', 'Location', 'Number of Employees']
)

# ---- CSV FILES ----
# CSV = comma separated values, text-only spreadsheet format
# First row is always column headers:
# name,age,city
# John,34,New York

df = pd.read_csv('filename.csv')   # load CSV into DataFrame
df.to_csv('new_file.csv')          # save DataFrame to CSV

# ---- INSPECTING A DATAFRAME ----
print(df.head())      # first 5 rows (default)
print(df.head(10))    # first 10 rows
print(df.info())      # column names, data types, non-null counts
# info() output example:
# RangeIndex: 220 entries, 0 to 219
# Data columns (total 5 columns):
# id             220 non-null int64
# name           220 non-null object   <- object means string
# imdb_rating    220 non-null float64

# ---- SELECTING COLUMNS ----
# Single column -> returns a Series
clinic_north = df['clinic_north']   # dictionary style (always works)
clinic_north = df.clinic_north      # dot style (only works if no spaces in column name)

# Multiple columns -> returns a DataFrame
# Note the double brackets [[]]
# outer [] = selecting from DataFrame, inner [] = list of column names
clinic_north_south = df[['clinic_north', 'clinic_south']]

# ---- SERIES vs DATAFRAME ----
# Single column or row  -> Series   (like a 1D array)
# Multiple columns or rows -> DataFrame (like a 2D table)

# ---- SELECTING ROWS ----
# iloc = integer location, selects by POSITION (zero-indexed)
march = df.iloc[2]      # single row -> Series (row 2 = 3rd row)

# Multiple rows -> DataFrame (same slicing rules as Python lists)
df.iloc[3:6]    # rows 3, 4, 5 (not including 6)
df.iloc[:4]     # rows 0, 1, 2, 3
df.iloc[-3:]    # last 3 rows

# ---- SELECTING ROWS WITH LOGIC ----
# Single condition
january = df[df.month == 'January']      # equal
df[df.age > 30]                          # greater than
df[df.age < 30]                          # less than
df[df.name != 'Clara Oswald']            # not equal

# Multiple conditions - each must be in parentheses!
# | means OR, & means AND
march_april = df[(df.month == 'March') | (df.month == 'April')]

# isin() - cleaner than chaining multiple OR conditions
# equivalent to SQL: WHERE month IN ('January', 'February', 'March')
january_february_march = df[df.month.isin(['January', 'February', 'March'])]

# ---- RESETTING INDICES ----
# After filtering, indices are non-consecutive (e.g. 1, 3, 5)
# df2 output:
#       month  clinic_east  clinic_north  clinic_south  clinic_west
# 1  February           51            45           145           45
# 3     April           80            80            54          180
# 5      June          112           109            79          129

# drop=False (default) — keeps old index as a new column
df3 = df2.reset_index()
#    index     month  clinic_east  clinic_north  clinic_south  clinic_west
# 0      1  February           51            45           145           45
# 1      3     April           80            80            54          180
# 2      5      June          112           109            79          129

# drop=True — throws away the old index, no extra column
df3 = df2.reset_index(drop=True)
#       month  clinic_east  clinic_north  clinic_south  clinic_west
# 0  February           51            45           145           45
# 1     April           80            80            54          180
# 2      June          112           109            79          129

# inplace=False (default) — returns a NEW DataFrame, original unchanged
df3 = df2.reset_index(drop=True)  # df2 still has indices 1, 3, 5
                                   # df3 has new indices 0, 1, 2

# inplace=True — modifies EXISTING DataFrame, returns nothing
df2.reset_index(drop=True, inplace=True)  # df2 now has indices 0, 1, 2
                                           # no new variable created

# Most common usage — clean and modify in place:
df2.reset_index(drop=True, inplace=True)

# R equivalent:
# inplace=False -> df3 <- reset_index(df2)  (keep both)
# inplace=True  -> df2 <- reset_index(df2)  (overwrite original)