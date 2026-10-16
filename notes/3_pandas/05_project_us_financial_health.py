# ============================================================
# 05 - PROJECT: US FINANCIAL HEALTH (1999-2019)
# Codecademy: Analyze Financial Data with Python / Importing Finance Data
# ============================================================
# Goal: judge the financial health and volatility of the US over
#       20 years using stock, commodity and macro data.
#
# Data sources (everything from section 06 in one project):
#   CSV files       -> gold prices, crude oil prices   (pd.read_csv)
#   FRED API        -> stock index data                (web.DataReader)
#   World Bank API  -> GDP, goods & services exports   (wb.download)
#
# Method:
#   prices  ->  log returns  ->  variance (= volatility)
#
# Locally: gold_prices.csv / crude_oil_prices.csv go in data/
#          run from the project root (C:\Python\panda-for-finance)

# import codecademylib3_seaborn   # Codecademy-only - DELETE locally
import numpy as np                # needed for task 12 (course: "import at top")


# ============================================================
# Importing Commodity Prices
# ============================================================

# Task 1: import pandas as pd (needed for read_csv).
import pandas as pd

# Task 2: load gold_prices.csv into gold_prices, print it.
gold_prices = pd.read_csv("data/gold_prices.csv", parse_dates=['Date'])
gold_prices = gold_prices.sort_values('Date')
print(gold_prices)

# Task 3: load crude_oil_prices.csv into crude_oil_prices, print it.
crude_oil_prices = pd.read_csv("data/crude_oil_prices.csv", parse_dates=['Date'])
crude_oil_prices = crude_oil_prices.sort_values('Date')
print(crude_oil_prices)

# EXTRA: both CSVs are stored NEWEST-first:
#   gold_prices.csv          crude_oil_prices.csv
#   2019-08-30  (top)        "Sep 11, 2018"  (top)
#   ...                      ...
#   1999-01-01  (bottom)     "Jan 04, 1999"  (bottom)
#
#   parse_dates=['Date']  -> text becomes real dates. Needed for oil:
#                            "Sep 11, 2018" as TEXT would sort
#                            alphabetically (Apr < Aug < Dec ...)
#   sort_values('Date')   -> oldest first, so shift(1) = previous day
#                            (sort_values = by a COLUMN;
#                             sort_index  = by the INDEX)
#
# Data quirks worth knowing:
#   - date ranges differ: gold ends Aug 2019, oil ends Sep 2018
#     (the CSVs are not trimmed to 1999-2019 like the FRED pulls)
#   - gold repeats prices on holidays (e.g. 2018-12-21..25 all
#     1258.15) -> zero returns, pulls variance down slightly


# ============================================================
# Importing Stock Prices  (FRED)
# ============================================================

# Task 4: import pandas_datareader.data as web.
import pandas_datareader.data as web

# Task 5: import datetime; create start = Jan 1 1999, end = Jan 1 2019.
from datetime import datetime

start = datetime(1999, 1, 1)
end = datetime(2019, 1, 1)

# Task 6: pull NASDAQ 100 from FRED (id 'NASDAQ100') into nasdaq_data,
#         print it.
nasdaq_data = web.DataReader("NASDAQ100", "fred", start, end)
print(nasdaq_data)

# Task 7: same for the S&P 500 (id 'SP500') into sap_data, print it.
sap_data = web.DataReader("SP500", "fred", start, end)
print(sap_data)

# FRED data already comes OLDEST-first -> no sorting needed.


# ============================================================
# Importing World Bank Data
# ============================================================

# Task 8: import pandas_datareader.wb as wb.
import pandas_datareader.wb as wb

# Task 9: download US GDP (indicator NY.GDP.MKTP.CD) into gdp_data.
gdp_data = wb.download(indicator='NY.GDP.MKTP.CD', country=['US'],
                       start=start, end=end)
print(gdp_data)

# Task 10: download US exports of goods & services
#          (indicator NE.EXP.GNFS.CN) into export_data, print it.
export_data = wb.download(indicator='NE.EXP.GNFS.CN', country=['US'],
                          start=start, end=end)
print(export_data)

# EXTRA: World Bank returns years NEWEST-first (2018, 2017, ...).
gdp_data = gdp_data.sort_index()
export_data = export_data.sort_index()
#
#   unsorted:  2018 / 2019 -> wrong sign on every return
#   sorted:    2019 / 2018 -> correct
#   (variance is the same either way - flipping signs doesn't change
#    spread - which is why the course doesn't catch it)
#
# RULE: check date order before every shift().
#   source         order          fix
#   ------         -----          ---
#   gold CSV       newest-first   parse_dates + sort_values('Date')
#   oil CSV        newest-first   parse_dates + sort_values('Date')
#   FRED           oldest-first   none
#   World Bank     newest-first   sort_index()


# ============================================================
# Calculating Log Return
# ============================================================

# Task 11: define a function log_return with one parameter, prices.
# Task 12: body = natural log of (current price / previous price).
def log_return(prices):
    return np.log(prices / prices.shift(1))

# log return = ln( price_t / price_t-1 )
#
# Python function vs R:
#   R:       log_return <- function(prices) { ... }
#   Python:  def log_return(prices):
#                return ...
#   - colon after the def line
#   - INDENTATION = the body (no { })
#   - explicit 'return' needed (R returns the last value
#     automatically; Python returns None without it)
#   - empty body placeholder: pass

# Task 13: gold_returns = log_return of the Gold_Price column.
gold_returns = log_return(gold_prices['Gold_Price'])

# Task 14: log returns for every other dataset - pass in the
#          PRICE COLUMN, not the whole DataFrame.
crude_oil_returns = log_return(crude_oil_prices['Crude_Oil_Price'])
nasdaq_returns = log_return(nasdaq_data['NASDAQ100'])   # FRED: column = series id
sap_returns = log_return(sap_data['SP500'])
gdp_returns = log_return(gdp_data['NY.GDP.MKTP.CD'])    # WB: column = indicator code
export_returns = log_return(export_data['NE.EXP.GNFS.CN'])

# LEARNING POINT: first draft left out the two World Bank datasets -
# task 14 says "each additional dataset".


# ============================================================
# Comparing Return Volatility
# ============================================================

# Task 15: print the variance of every returns series. Which is most
#          volatile? Any with similar variances?
print('gold:', gold_returns.var())
print('crude_oil:', crude_oil_returns.var())
print('nasdaq:', nasdaq_returns.var())
print('sp500:', sap_returns.var())
print('gdp:', gdp_returns.var())
print('exports:', export_returns.var())

# EXTRA 1: detail - store returns next to the prices
gold_prices['Log_Return'] = gold_returns
crude_oil_prices['Log_Return'] = crude_oil_returns
nasdaq_data['Log_Return'] = nasdaq_returns
sap_data['Log_Return'] = sap_returns
gdp_data['Log_Return'] = gdp_returns
export_data['Log_Return'] = export_returns

# EXTRA 2: summary - one row per dataset
#   (variance = ONE number per dataset, so it lives here, not as a
#    column repeated on every row of the detail tables)
summary = pd.DataFrame({
    'dataset':   ['Gold', 'Crude oil', 'NASDAQ 100', 'S&P 500', 'GDP', 'Exports'],
    'frequency': ['daily', 'daily', 'daily', 'daily', 'yearly', 'yearly'],
    'n_returns': [gold_returns.count(), crude_oil_returns.count(),
                  nasdaq_returns.count(), sap_returns.count(),
                  gdp_returns.count(), export_returns.count()],
    'variance':  [gold_returns.var(), crude_oil_returns.var(),
                  nasdaq_returns.var(), sap_returns.var(),
                  gdp_returns.var(), export_returns.var()],
})
summary['volatility'] = np.sqrt(summary['variance'])   # = std deviation
summary = summary.set_index('dataset')
print(summary)

#   .count()      -> number of non-NaN values
#   volatility    -> sqrt(variance) = std dev, same units as returns;
#                    how finance usually quotes it
#
# INTERPRETATION WARNING: daily vs yearly variances are NOT directly
# comparable - variance grows with the period length. Compare daily
# with daily, yearly with yearly.
#
# R: pd.DataFrame({...}) ~ data.frame(dataset = c(...), ...)

# EXTRA 3: annualize daily volatility so all rows share one scale
#   ~252 trading days a year -> annual vol = daily vol * sqrt(252)
summary['annualized_vol'] = np.where(summary['frequency'] == 'daily',
                                     summary['volatility'] * np.sqrt(252),
                                     summary['volatility'])
print(summary)

# np.where(condition, if_true, if_false)  ~ R: ifelse()


# ============================================================
# Results & interpretation  (run: Oct 2026)
# ============================================================
#
#               frequency  n_returns  variance  volatility  annualized
#   Gold           daily       5390  0.000114    0.010666     ~17%
#   Crude oil      daily       4999  0.000556    0.023586     ~37%
#   NASDAQ 100     daily       4850  0.000328    0.018123     ~29%
#   S&P 500        daily        533  0.000059    0.007708     (excluded)
#   GDP            yearly        20  0.000346    0.018613      ~2%
#   Exports        yearly        20  0.006208    0.078794      ~8%
#
# Most volatile (daily): CRUDE OIL
#   - supply shocks, OPEC decisions, recessions
#     (crashes in 2008 and 2014-16 are both in the window)
#
# NASDAQ 100: second most volatile
#   - tech-heavy; the 20 years include the dot-com crash and 2008
#
# GOLD: calmest market asset
#   - fits its safe-haven role
#
# Yearly: EXPORTS swing ~4x as much as GDP
#   - trade collapsed in 2009 (about -14%), dipped again 2015-16
#
# GDP: most stable of everything (~2% a year)
#   - only 2009 shows a decline
#   - the "financial health" signal: the economy as a whole is far
#     steadier than any market built on top of it
#
# ------------------------------------------------------------
# "Did any datasets have similar variances?"  -> TRAP
# ------------------------------------------------------------
#   GDP     0.000346  (yearly)
#   NASDAQ  0.000328  (daily)
#   Numerically almost identical - but a coincidence: different
#   frequencies. Annualized, NASDAQ (~29%) is ~15x GDP (~2%).
#   RULE: only compare volatilities on the SAME time scale.
#
# ------------------------------------------------------------
# DATA CAVEAT - S&P 500 (changing contract, see section 06)
# ------------------------------------------------------------
#   FRED's SP500 series now only serves ~10 years (licensing).
#   Pulled in 2026, it starts 2016-10-17 -> 533 returns, a mostly
#   calm period. Not comparable with the 20-year series; excluded.
#   (Codecademy's data was pulled in 2019, so the course got more.)
#   Fix for later: pull ^GSPC via yfinance for the full period.
#
# Other caveats:
#   - gold/oil CSVs are not trimmed to 1999-2019 (gold to Aug 2019,
#     oil to Sep 2018)
#   - FRED leaves holidays as NaN -> returns on those days drop out
#     (NASDAQ: 5218 rows -> 4850 returns)
#   - gold repeats prices on holidays -> zero returns, slightly
#     lowers its variance
#   - GDP/exports are nominal (current USD), so inflation is
#     included in the growth