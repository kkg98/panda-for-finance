# ============================================
# Python for Finance: Core Concepts
# ============================================
# Covers: returns, risk, variance, std dev,
#         correlation — from the Codecademy
#         "Analyze Financial Data with Python" path
# ============================================

import numpy as np
from math import log, sqrt


# ---- SIMPLE RATE OF RETURN ----
# R = (E - S + D) / S
#   R = simple rate of return
#   S = starting price
#   E = ending price
#   D = dividend (optional, defaults to 0)

def display_as_percentage(val):
    return '{:.1f}%'.format(val * 100)

def calculate_simple_return(start_price, end_price, dividend=0):
    return (end_price - start_price + dividend) / start_price

simple_return = calculate_simple_return(200, 250, 20)
# print(display_as_percentage(simple_return))
# -> '35.0%'


# ---- LOGARITHMIC RATE OF RETURN ----
# r = log(E) - log(S) = log(E/S)
#
# Advantage: easy to aggregate a SINGLE asset over time
# (log returns are additive across periods)
# Simple return is easier when comparing MULTIPLE assets
# at the same point in time

def calculate_log_return(start_price, end_price):
    return log(end_price) - log(start_price)

log_return = calculate_log_return(200, 250)
# print(display_as_percentage(log_return))
# -> '22.3%'


# ---- ANNUALIZING RETURNS (single return) ----
# r = r0 * t
#   r0 = original log return
#   t  = number of original periods in the new horizon
#
# Daily -> Annual : multiply by 252  (trading days in a year)
# Monthly -> Annual : multiply by 12

def annualize_return(log_return, t):
    return log_return * t

daily_return_a = 0.001
annual_return_a = annualize_return(daily_return_a, 252)
# print(display_as_percentage(annual_return_a))
# -> '25.2%'

monthly_return_b = 0.022
annual_return_b = annualize_return(monthly_return_b, 12)
# print(display_as_percentage(annual_return_b))
# -> '26.4%'


# ---- ANNUALIZING RETURNS (multiple returns) ----
# r = (sum of all log returns / n) * t
#
# Special case: if you already have ALL t periods,
# just sum them directly — no averaging needed
# (this is the additive property of log returns)

daily_returns = [0.002, -0.002, 0.003, 0.002, -0.001]

def convert_returns(log_returns, t):
    return (sum(log_returns) * t) / len(log_returns)

annual_return = convert_returns(daily_returns, 252)
# print(display_as_percentage(annual_return))
# -> '25.2%'

# Weekly return via additivity (you have all 5 days):
weekly_return = sum(daily_returns)
# print(display_as_percentage(weekly_return))
# -> '0.4%'


# ---- PORTFOLIO RETURN (aggregate across assets) ----
# R = (W1 * R1) + (W2 * R2) + ... + (Wn * Rn)
#   Wi = weight of asset i = Si / (S1 + S2 + ... + Sn)
#   Ri = simple rate of return of asset i
#
# Example: 3 assets with prices $500, $200, $300
# and returns 2%, 10%, 5%
# R = (0.5 * 0.02) + (0.2 * 0.10) + (0.3 * 0.05) = 4.5%


# ---- VARIANCE ----
# sigma^2 = sum((Xi - X_mean)^2) / n
#   Xi     = i-th value in dataset
#   X_mean = mean of dataset
#   n      = number of values
#
# Higher variance = more spread = riskier asset

returns_disney = [0.22, 0.12, 0.01, 0.05, 0.04]
returns_cbs    = [-0.13, -0.15, 0.31, -0.06, -0.29]

# Using numpy (production way):
variance_disney = np.var(returns_disney)
variance_cbs    = np.var(returns_cbs)

# Manual implementation (builds intuition):
def calculate_variance(dataset):
    mean = sum(dataset) / len(dataset)
    my_sum = 0
    for data in dataset:
        my_sum += (data - mean) ** 2
    return my_sum / len(dataset)

# print(calculate_variance(returns_disney))  # -> 0.005236
# print(calculate_variance(returns_cbs))     # -> 0.041436


# ---- STANDARD DEVIATION ----
# sigma = sqrt(variance)
# Same unit as the original data -> easier to interpret than variance

def calculate_stddev(dataset):
    return sqrt(calculate_variance(dataset))

# print(display_as_percentage(calculate_stddev(returns_disney)))  # -> '7.2%'
# print(display_as_percentage(calculate_stddev(returns_cbs)))     # -> '20.4%'

# CBS has ~3x the std dev of Disney -> much riskier


# ---- CORRELATION ----
# r_xy = [n*sum(Xi*Yi) - sum(Xi)*sum(Yi)] /
#        sqrt([n*sum(Xi^2) - (sum(Xi))^2] * [n*sum(Yi^2) - (sum(Yi))^2])
#
# Interpretation:
#   +1 = perfect positive correlation  (move together)
#    0 = no correlation
#   -1 = perfect negative correlation  (move opposite)

# In practice, always use numpy:
returns_gm    = [0.018, -0.005, -0.047, -0.009, -0.012, 0.003, -0.027, -0.014,  0.029, -0.062,  0.009]
returns_ford  = [0.002, -0.004, -0.027, -0.022, -0.001, 0.002, -0.006, -0.017,  0.035, -0.029,  0.002]
returns_exxon = [0.008,  0.015,  0.009,  0.012,  0.003,-0.007,  0.006,  0.005, -0.048,  0.025, -0.012]
returns_apple = [-0.002, 0.007, -0.004, -0.004,  0.002, 0.013, -0.011,  0.017, -0.001,  0.012,  0.006]

corrcoef_matrix = np.corrcoef([returns_gm, returns_ford, returns_exxon, returns_apple])
# print(corrcoef_matrix)
# GM vs Ford  ~ 0.95  (highly positive: same industry)
# GM vs Exxon ~ 0.00  (no relationship)
# GM vs Apple ~ -0.3  (slight negative)

# zip() reminder: pairs elements, does NOT sum
# for x, y in zip(set_x, set_y): gives (x0,y0), (x1,y1), ...
# sum([x*y for x, y in zip(set_x, set_y)]) -> dot product

# Manual implementation (for understanding / interviews):
def calculate_correlation(set_x, set_y):
    n      = len(set_x)
    sum_x  = sum(set_x)
    sum_y  = sum(set_y)
    sum_x2 = sum([x ** 2 for x in set_x])
    sum_y2 = sum([y ** 2 for y in set_y])
    sum_xy = sum([x * y for x, y in zip(set_x, set_y)])
    numerator   = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)) ** 0.5
    return numerator / denominator


# ---- PUTTING IT TOGETHER: FINANCIAL STATS REVIEW ----
# Always compute on RAW (decimal) values first, format only at the end
annual_returns = [0.02, 0.05, -0.04, 0.04, 0.02, -0.02, 0.01, 0.03, 0.05, 0.02]

# Convert to display strings (AFTER computation, not before)
annual_returns_pct = [display_as_percentage(r) for r in annual_returns]
# print(', '.join(annual_returns_pct))

variance = calculate_variance(annual_returns)
# print('Variance:', variance)               # -> 0.000556

stddev_display = display_as_percentage(calculate_stddev(annual_returns))
# print('Std Dev:', stddev_display)           # -> '2.4%'

# Common mistake — wrong order:
# stddev = calculate_stddev(display_as_percentage(stddev))  # NameError + TypeError
# Fix: calculate first, then format
