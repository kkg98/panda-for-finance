# ============================================
# Lesson 1: Importing Pandas
# ============================================

import pandas as pd
# Pandas is aliased as 'pd' by convention
# Used for tabular data (rows + columns)
# Similar to SQL/Excel but with Python's power

# Core objects:
# - DataFrame = full table
# - Series = single column

# Load a CSV into a DataFrame
# df = pd.read_csv('filename.csv')

# Preview first N rows
# df.head(10)

# Filter rows (like SQL WHERE)
# df[(df.column == 'value') & (df.other_column == 'value')]

