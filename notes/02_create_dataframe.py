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
print(df.describe())  # summary stats for numeric columns

# ---- SELECTING COLUMNS ----
# Single column -> returns a Series
clinic_north = df['clinic_north']   # dictionary style (always works)
clinic_north = df.clinic_north      # dot style (only if no spaces in name)

# Multiple columns -> returns a DataFrame
# Note the double brackets [[]]
clinic_north_south = df[['clinic_north', 'clinic_south']]

# ---- SELECTING ROWS ----
# Single row by index position -> returns a Series
march = df.iloc[2]        # zero-indexed, so row 2 = 3rd row

# Multiple rows -> returns a DataFrame
df.iloc[3:6]    # rows 3, 4, 5 (not including 6)
df.iloc[:4]     # rows 0, 1, 2, 3
df.iloc[-3:]    # last 3 rows

# Same slicing rules as Python lists!

# ---- SERIES vs DATAFRAME ----
# Single column or row -> Series
# Multiple columns or rows -> DataFrame


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

df3 = df2.reset_index(drop=True)   # returns NEW DataFrame, old index dropped
# df3 output:
#       month  clinic_east  clinic_north  clinic_south  clinic_west
# 0  February           51            45           145           45
# 1     April           80            80            54          180
# 2      June          112           109            79          129

df2.reset_index(drop=True, inplace=True)  # modifies EXISTING DataFrame

