# ============================================
# A/B Testing for ShoeFly.com
# ============================================
# ShoeFly.com is running an A/B test on two versions of an ad
# placed in emails, Facebook, Twitter, and Google banner ads.
# Goal: analyze how the two ads perform by platform and day of week.
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
# Which ad platform is getting the most views?
# Count how many rows (views) came from each utm_source
ad_clicks.groupby("utm_source").count()
ad_clicks.groupby('utm_source').user_id.count().reset_index()

# TASK 3
# Create a new column called is_click
# True if ad_click_timestamp is not null, False otherwise
# Hint: look up pandas .isnull() or .notnull()



# TASK 4
# Group by utm_source AND is_click
# Count the number of user_id's in each group
# Save to variable: clicks_by_source


# TASK 5
# Pivot clicks_by_source so that:
#   - columns = is_click (True or False)
#   - index   = utm_source
#   - values  = user_id
# Save to variable: clicks_pivot


# TASK 6
# Add a new column to clicks_pivot called percent_clicked
# = the percent of users who clicked from each utm_source
# Hint: divide the True column by the sum of True + False columns
# Was there a difference in click rates between sources?


# ============================================
# ANALYZING THE A/B TEST
# ============================================

# TASK 7
# The column experimental_group shows whether the user saw Ad A or Ad B
# Were approximately the same number of people shown each ad?
# Hint: groupby experimental_group and count


# TASK 8
# Using is_click, check whether a greater percentage of users
# clicked on Ad A or Ad B
# Hint: similar approach to tasks 4-6 but group by experimental_group


# TASK 9
# Create two separate DataFrames:
#   a_clicks — only rows where experimental_group == 'A'
#   b_clicks — only rows where experimental_group == 'B'


# TASK 10
# For each group (a_clicks and b_clicks),
# calculate the percent of users who clicked on the ad by day
# Hint: same pivot approach as before, but group by day instead of utm_source


# TASK 11
# Compare the results for A and B
# What changed over the course of the week?
# Which ad do you recommend — A or B? Add your conclusion as a comment