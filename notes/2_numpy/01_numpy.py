# ============================================
# NumPy: Introduction
# ============================================
# Covers: arrays, element-wise operations,
#         indexing, slicing, boolean filtering,
#         axes, loading from CSV
# ============================================

import numpy as np


# ---- CREATING ARRAYS ----
# np.array() converts a Python list into a NumPy array
a = np.array([1, 2, 3, 4, 5])

# 2D array (list of lists = matrix)
test_scores = np.array([
    [92, 94, 88, 91, 87],   # student 1
    [79, 100, 86, 93, 91],  # student 2
    [87, 85, 72, 90, 92],   # student 3
])

# Loading from a CSV file:
# csv_array = np.genfromtxt('sample.csv', delimiter=',')


# ---- ELEMENT-WISE OPERATIONS ----
# NumPy applies operations to EVERY element automatically — no loop needed
# This is called vectorization

a = np.array([1, 2, 3])

# With a Python list you would need:
# result = []
# for i in range(len(a)):
#     result.append(a[i] + 3)

# With NumPy — one line:
# a + 3  -> [4, 5, 6]
# a - 2  -> [-1, 0, 1]
# a * 2  -> [2, 4, 6]
# a / 2  -> [0.5, 1.0, 1.5]
# a ** 2 -> [1, 4, 9]
# np.sqrt(a) -> [1.0, 1.414, 1.732]

# Two arrays of the SAME size can also be added element-wise:
b = np.array([6, 7, 8])
# a + b  -> [7, 9, 11]   (1+6, 2+7, 3+8)
# IMPORTANT: arrays must have the same number of elements!

# Practical rule: if you catch yourself writing
#   for i in range(len(...))
# stop and ask: "Can NumPy do this directly?"


# ---- INDEXING ----
# Zero-indexed, same as Python lists
a = np.array([5, 2, 7, 0, 11])
# a[0]  -> 5    (first element)
# a[-1] -> 11   (last element)
# a[-2] -> 0    (second-to-last)

# Slicing: a[start:stop]  — includes start, EXCLUDES stop
# a[1:3]  -> [2, 7]   (index 1 and 2, not 3)
# a[:3]   -> [5, 2, 7]
# a[-3:]  -> [7, 0, 11]

# 2D indexing: array[row, column]
# array[0, :]    -> first row, all columns
# array[:, 1]    -> all rows, second column
# array[0, 0:3]  -> first row, first three columns


# ---- AXES ----
# axis = the DIMENSION you collapse (reduce)
# Think of it as: "which index in .shape disappears"
#
# For a 2D array with shape (rows, columns):
#
#                  axis = 0
#                     |
#                     v
#         +-------+-------+-------+
#         | [0,0] | [0,1] | [0,2] |  ---> axis = 1
#         +-------+-------+-------+
#         | [1,0] | [1,1] | [1,2] |  ---> axis = 1
#         +-------+-------+-------+
#         | [2,0] | [2,1] | [2,2] |  ---> axis = 1
#         +-------+-------+-------+
#
#   axis=0  collapses DOWN the rows   -> result has 1 value per COLUMN
#   axis=1  collapses ACROSS the cols -> result has 1 value per ROW
#
# Memory rule (2D):
#   axis=0  ↓  rows collapse,    columns survive
#   axis=1  →  columns collapse, rows survive

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

# np.sum(a, axis=0)  -> [12, 15, 18]
# Why: 1+4+7=12, 2+5+8=15, 3+6+9=18  (summed down each column)

# np.sum(a, axis=1)  -> [6, 15, 24]
# Why: 1+2+3=6, 4+5+6=15, 7+8+9=24  (summed across each row)

# General rule for any number of dimensions:
# axis = its position in .shape
# e.g. shape (2, 3, 4): axis=0 is size-2, axis=1 is size-3, axis=2 is size-4
# Negative axes: axis=-1 always means the LAST dimension

# Finance example — returns matrix shape (time_periods, assets):
returns = np.array([
    [0.01,  0.02, -0.01],   # period 1
    [0.03, -0.02,  0.01],   # period 2
])
# np.mean(returns, axis=0)
# -> mean per ASSET (average down rows)
# [(0.01+0.03)/2, (0.02-0.02)/2, (-0.01+0.01)/2]
# -> [0.02, 0.0, 0.0]

# np.mean(returns, axis=1)
# -> mean per TIME PERIOD (average across columns)
# [(0.01+0.02-0.01)/3, (0.03-0.02+0.01)/3]
# -> [0.00667, 0.00667]

# Common mistake:
# WRONG: axis = direction you move
# RIGHT: axis = dimension you collapse (it disappears from the shape)


# ---- BOOLEAN FILTERING ----
# Comparing an array to a value returns a boolean array element-wise
a = np.array([10, 2, 2, 4, 5, 3, 9, 8, 9, 7])
# a > 5  -> [True, False, False, False, False, False, True, True, True, True]

# Use that boolean array as a mask to select values:
# a[a > 5]  -> [10, 9, 8, 9, 7]

# Multiple conditions — use & (AND) and | (OR), NOT 'and'/'or'
# Important: wrap each condition in parentheses!
porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

# cold = porridge[porridge < 60]
# -> [50, 56, 51]

# hot = porridge[porridge > 80]
# -> [90, 85, 98, 79... wait, 79 < 80, so: [90, 85, 98]]

# just_right = porridge[(porridge >= 60) & (porridge <= 80)]
# -> [79, 65, 63, 79]

# Rules of thumb:
# Outside a range  ->  use |   (a < low) | (a > high)
# Inside a range   ->  use &   (a >= low) & (a <= high)


# ---- PUTTING IT TOGETHER: TEMPERATURE EXERCISE ----
# temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')
# Shape: (5 days, 3 time-of-day readings)  e.g. morning/afternoon/evening

# Fix a recording error — add 3 to every value:
# temperatures_fixed = temperatures + 3

# Select all Monday (row 0) temperatures:
# monday_temperatures = temperatures_fixed[0, :]

# Select morning (column 1) temps for Thu & Fri (last two rows):
# thursday_friday_morning = temperatures_fixed[[-2, -1], 1]

# Select extreme values — below 50 OR above 60:
# temperature_extremes = temperatures_fixed[
#     (temperatures_fixed < 50) | (temperatures_fixed > 60)
# ]
