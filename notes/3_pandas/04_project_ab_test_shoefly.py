# ============================================
# A/B Testing for ShoeFly.com — Project Notes
# ============================================
# Concepts: boolean columns, groupby, pivot,
#           percent calculation, filtering
# Dataset: ad_clicks.csv
# Columns: user_id, utm_source, day,
#          ad_click_timestamp, experimental_group
# ============================================

import pandas as pd

ad_clicks = pd.read_csv('data/ad_clicks.csv')


# ============================================
# ANALYZING AD SOURCES
# ============================================

# TASK 1
# Examine the first few rows of ad_clicks
print(ad_clicks.head())


# TASK 2
# Your manager wants to know which ad platform is getting you the most views.
# How many views (i.e., rows of the table) came from each utm_source?
#
# TWO-QUESTION RULE:
#   "I want one row per utm_source"  -> groupby('utm_source')
#   "I want to count visits (rows)"  -> ['user_id'].count()
# "Group by source, count user IDs"
#
# WRONG: ad_clicks.groupby('user_id')['utm_source'].count()
# Group by user, count sources" — one row per user, not source

print(ad_clicks.groupby('utm_source')['user_id'].count().reset_index())


# TASK 3
# If the column ad_click_timestamp is not null, then someone actually
# clicked on the ad that was displayed.
# Create a new column called is_click, which is True if ad_click_timestamp
# is not null and False otherwise.
#
# .notnull() -> True if there IS a value (click happened)     CORRECT
# .isnull()  -> True if the value is MISSING (no click)       WRONG for this task
#
# MISTAKE TO AVOID:
# ad_clicks['is_click'] = ad_clicks['ad_click_timestamp'].isnull()
# This gives True when there is NO click — the opposite of what you want.

ad_clicks['is_click'] = ad_clicks['ad_click_timestamp'].notnull()


# TASK 4
# We want to know the percent of people who clicked on ads from each utm_source.
# Start by grouping by utm_source and is_click and counting the number of
# user_id's in each of those groups. Save your answer to the variable clicks_by_source.
#
# NOTE: .count() vs .nunique()
# .count()   -> counts total ROWS in each group (correct — counts visits)
# .nunique() -> counts DISTINCT user_ids in each group
# They give the same result here because each user_id appears only once,
# but .count() is the correct intent when counting visits/rows.

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click'])['user_id'].count().reset_index()
print(clicks_by_source)


# TASK 5
# Now let's pivot the data so that the columns are is_click (either True or False),
# the index is utm_source, and the values are user_id.
# Save your results to the variable clicks_pivot.
#
# HOW TO DECIDE index vs columns:
#   Look at the final table shape you want first, then work backwards.
#   "What do I want as row labels?"     -> index=
#   "What do I want as column headers?" -> columns=
#   "What numbers fill the cells?"      -> values=
#
# BEFORE pivot (long):                AFTER pivot (wide):
# +------------+----------+---------+ +------------+-------+------+
# | utm_source | is_click | user_id | | utm_source | False | True |
# +------------+----------+---------+ +------------+-------+------+
# | email      | False    |     175 | | email      |   175 |   80 |
# | email      | True     |      80 | | facebook   |   324 |  180 |
# | facebook   | False    |     324 | | google     |   410 |  239 |
# | facebook   | True     |     180 | +------------+-------+------+
# +------------+----------+---------+      ^             ^      ^
#                                        index=       columns= (fans out)
#                                        (stays)      values= fills cells
#
# MISTAKE TO AVOID — swapping index and columns:
# clicks_pivot = clicks_by_source.pivot(
#     columns='utm_source',  # utm_source fans out into headers — WRONG
#     index='is_click',      # True/False become rows — WRONG
#     values='user_id'
# )

clicks_pivot = clicks_by_source.pivot(
    columns='is_click',
    index='utm_source',
    values='user_id'
).reset_index()


# TASK 6
# Create a new column in clicks_pivot called percent_clicked which is equal
# to the percent of users who clicked on the ad from each utm_source.
# Was there a difference in click rates for each source?
#
# clicks_pivot[True]  -> column where is_click == True  (clicked)
# clicks_pivot[False] -> column where is_click == False (not clicked)
# Note: True and False here are boolean column names, not strings

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)


# ============================================
# ANALYZING THE A/B TEST
# ============================================

# TASK 7
# The column experimental_group tells us whether the user was shown Ad A or Ad B.
# Were approximately the same number of people shown both ads?

print(ad_clicks.groupby('experimental_group')['user_id'].count().reset_index())


# TASK 8
# Using the column is_click that we defined earlier, check to see if a greater
# percentage of users clicked on Ad A or Ad B.
#
# This is the SAME groupby -> pivot -> percent chain as tasks 4-6.
# The only difference: swap utm_source for experimental_group.
# When confused about what to group by, ask:
#   "I want one row per experimental_group" -> groupby('experimental_group')
#   "I want to compare clicks"              -> also group by 'is_click'

clicks_by_group = ad_clicks.groupby(['experimental_group', 'is_click'])['user_id'].count().reset_index()
clicks_group_pivot = clicks_by_group.pivot(
    columns='is_click',
    index='experimental_group',
    values='user_id'
).reset_index()
clicks_group_pivot['percent_clicked'] = clicks_group_pivot[True] / (clicks_group_pivot[True] + clicks_group_pivot[False])
print(clicks_group_pivot)
# experimental_group  False  True  percent_clicked
# A                     517   310         0.374...
# B                     572   255         0.308...
# -> Ad A has a higher overall click rate


# TASK 9
# The Product Manager for the A/B test thinks that the clicks might have
# changed by day of the week.
# Start by creating two DataFrames: a_clicks and b_clicks, which contain
# only the results for A group and B group, respectively.

a_clicks = ad_clicks[ad_clicks['experimental_group'] == 'A']
b_clicks = ad_clicks[ad_clicks['experimental_group'] == 'B']


# TASK 10
# For each group (a_clicks and b_clicks), calculate the percent of users
# who clicked on the ad by day.
#
# Same chain again — now grouping by day instead of utm_source/experimental_group.
# Apply it once for a_clicks, once for b_clicks.

# --- Ad A ---
a_by_day = a_clicks.groupby(['day', 'is_click'])['user_id'].count().reset_index()
a_pivot = a_by_day.pivot(
    columns='is_click',
    index='day',
    values='user_id'
).reset_index()
a_pivot['percent_clicked'] = a_pivot[True] / (a_pivot[True] + a_pivot[False])
print(a_pivot)

# --- Ad B ---
b_by_day = b_clicks.groupby(['day', 'is_click'])['user_id'].count().reset_index()
b_pivot = b_by_day.pivot(
    columns='is_click',
    index='day',
    values='user_id'
).reset_index()
b_pivot['percent_clicked'] = b_pivot[True] / (b_pivot[True] + b_pivot[False])
print(b_pivot)


# TASK 11
# Compare the results for A and B. What happened over the course of the week?
# Do you recommend that your company use Ad A or Ad B?
#
# Ad A click rates by day: ~38%, ~36%, ~31%, ~41%, ~40%, ~38%, ~39%
# Ad B click rates by day: ~28%, ~38%, ~28%, ~25%, ~30%, ~36%, ~31%
# Ad A wins across every day of the week.
# The gap is largest on Thursday (~40% vs ~25%) and Monday (~38% vs ~28%).
# Recommendation: use Ad A.


# ============================================
# KEY PATTERN — the repeating three-step chain:
# ============================================
# 1. groupby([category, 'is_click'])['user_id'].count().reset_index()
# 2. .pivot(columns='is_click', index=category, values='user_id').reset_index()
# 3. df['percent_clicked'] = df[True] / (df[True] + df[False])
#
# This same chain appeared THREE times in this project:
#   - utm_source vs clicks       (tasks 4-6)
#   - experimental_group vs clicks (task 8)
#   - day vs clicks              (task 10, once for A, once for B)
# ============================================
