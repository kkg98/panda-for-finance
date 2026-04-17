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