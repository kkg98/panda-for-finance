# ============================================
# Modifying DataFrames
# ============================================

import pandas as pd

# ---- ADDING A COLUMN FROM A LIST ----
# Assign a list directly to a new column name
# List must be the same length as the DataFrame!
df['Quantity'] = [100, 150, 50, 35]
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']

# Coming up next:
# - Adding columns using lambda functions
# - Renaming columns

# ============================================================
# Section 3: Modifying DataFrames
# ============================================================

import pandas as pd


# ------------------------------------------------------------
# 1. Adding a Column from a List
# ------------------------------------------------------------
# Assign a list directly to a new column name.
# The list must be the same length as the DataFrame.

df = pd.DataFrame({
    'Product ID': [1, 2, 3, 4],
    'Price': [0.75, 0.25, 5.50, 3.00]
})

df['Color'] = ['blue', 'red', 'green', 'yellow']
# Each value in the list maps to the corresponding row


# ------------------------------------------------------------
# 2. Adding a Constant Column
# ------------------------------------------------------------
# Assign a single value — every row gets that same value.

df['In Stock?'] = True
df['Is taxed?'] = 'Yes'


# ------------------------------------------------------------
# 3. Adding a Column from Existing Columns
# ------------------------------------------------------------
# Perform row-wise arithmetic between columns.
# Similar to vectorized operations in R.

df['Cost to Manufacture'] = [0.50, 0.10, 3.00, 2.50]
df['Margin'] = df['Price'] - df['Cost to Manufacture']
# Each row: Margin = Price - Cost to Manufacture

df['Sales Tax'] = df.Price * 0.075
# Dot notation works for simple column names (no spaces)
# Bracket notation is safer for column names with spaces

# Finance use cases: margins, returns, spreads, P&L
# e.g. df['Return'] = (df['End Price'] - df['Start Price']) / df['Start Price']


# ------------------------------------------------------------
# 4. Applying a Built-in Function with .apply()
# ------------------------------------------------------------
# .apply() runs a function on every value in a column, row by row.
# Syntax: df['col'].apply(some_function)

df2 = pd.DataFrame({
    'Name': ['JOHN SMITH', 'Jane Doe', 'joe schmo'],
    'Email': ['john.smith@gmail.com', 'jdoe@yahoo.com', 'joeschmo@hotmail.com']
})

df2['Lowercase Name'] = df2.Name.apply(str.lower)
# str.lower is passed as a function reference (no parentheses!)
# pandas calls it on each value: str.lower('JOHN SMITH') -> 'john smith'


# ------------------------------------------------------------
# 5. Lambda Functions
# ------------------------------------------------------------
# A lambda is a short, anonymous function defined in one line.
# Syntax: lambda <input> : <what to return>
# Equivalent to defining a full def function, just more compact.

# Basic numeric example:
mylambda = lambda x: (x * 2) + 3
# mylambda(5) -> 13

# String example — negative indexing:
# x[0]  -> first character
# x[-1] -> last character (negative index counts from the end, like in R)
mylambda = lambda x: x[0] + x[-1]
# mylambda('This is a string') -> 'Tg'

# IMPORTANT: lambdas must RETURN a value, not print() it
# WRONG:
# mylambda = lambda x: print("Welcome!") if x >= 13 else print("Too young")
# print() returns None — the column would be filled with None

# CORRECT:
mylambda = lambda x: "Welcome to BattleCity!" if x >= 13 else "You must be 13 or older"
# Returns the string itself — pandas can store it in the column


# ------------------------------------------------------------
# 6. Lambda with If/Else
# ------------------------------------------------------------
# Syntax: lambda x: [value if true] if [condition] else [value if false]

# Overtime pay example:
overtime = lambda x: 40 + (x - 40) * 1.50 if x > 40 else x
# overtime(50) -> 40 + 10 * 1.5 -> 55.0
# overtime(35) -> 35

# Finance example:
grade = lambda x: 'Pass' if x >= 50 else 'Fail'
# grade(72) -> 'Pass'
# grade(40) -> 'Fail'


# ------------------------------------------------------------
# 7. Applying a Lambda to a Column
# ------------------------------------------------------------
# The most common pattern: combine .apply() with a lambda.
# Syntax: df['new_col'] = df['col'].apply(lambda x: ...)

# --- String method: .split() ---
# .split() breaks a string into a LIST of parts.
# By default it splits on spaces:
#   'John Smith'.split()     -> ['John', 'Smith']
#   'John Smith'.split()[0]  -> 'John'   (first element)
#   'John Smith'.split()[-1] -> 'Smith'  (last element, negative index)
#
# You can split on any character by passing it as an argument:
#   'john@gmail.com'.split('@')      -> ['john', 'gmail.com']
#   'john@gmail.com'.split('@')[-1]  -> 'gmail.com'

# Extract email provider:
df2['Email Provider'] = df2.Email.apply(lambda x: x.split('@')[-1])
# 'john.smith@gmail.com'.split('@') -> ['john.smith', 'gmail.com']
# [-1] grabs the last element -> 'gmail.com'

# Extract last name (split on space, grab last element):
get_last_name = lambda x: x.split()[-1]
df2['Last Name'] = df2.Name.apply(get_last_name)
# 'Jane Doe'.split() -> ['Jane', 'Doe']
# [-1]               -> 'Doe'

# Another example — extract domain without the extension:
# 'gmail.com'.split('.')[0] -> 'gmail'
df2['Domain'] = df2['Email Provider'].apply(lambda x: x.split('.')[0])
# 'gmail.com'   -> 'gmail'
# 'yahoo.com'   -> 'yahoo'
# 'hotmail.com' -> 'hotmail'