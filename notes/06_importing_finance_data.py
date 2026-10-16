# ============================================================
# 06 - IMPORTING FINANCE DATA
# Codecademy: Analyze Financial Data with Python / Importing Finance Data
# ============================================================
# Prereq:  py -m pip install pandas-datareader
#          (live APIs - needs an internet connection to run)
#          On Python 3.14, if you see a 'distutils' error:
#          py -m pip install setuptools   then reinstall.

# ------------------------------------------------------------
# What this lesson does
# ------------------------------------------------------------
# Pull public financial data from the internet, organize it with
# pandas, and combine it. Two modules:
#   pandas             -> tables (DataFrames); used all through 01-05
#   pandas-datareader  -> pulls public data from finance APIs into a
#                         DataFrame
#
# pandas-datareader only DELIVERS the data. Once it's a DataFrame,
# it's the same pandas you already know (head, groupby, pivot, ...).
#
#   Internet source
#   (FRED, World Bank, ...)
#         |
#         |   pandas-datareader  (the delivery mechanism)
#         v
#   +-------------------+   returns    +-------------------+
#   |  raw remote data  | -----------> |     DataFrame     |
#   +-------------------+              +-------------------+
#                                              |
#                                      pandas organizes,
#                                      cleans, combines
#                                              v
#                                      +-------------------+
#                                      |  insight / output |
#                                      +-------------------+
#
# gotcha: the IMPORT name uses an underscore, not a hyphen
#   import pandas_datareader as pdr    # correct
#   pandas-datareader                  # hyphen = SyntaxError
#
# R: pandas-datareader ~ quantmod::getSymbols() / tidyquant -
#    a helper that downloads market/economic data into a table.


# ============================================================
# World Bank  (wb submodule)
# ============================================================
# Task: pull GDP-per-capita (indicator NY.GDP.PCAP.KD) for the US,
#       Canada and Mexico, years 2005-2008, and print it.

from pandas_datareader import wb
from datetime import datetime

# How to read a 'from X import Y' line (handy coming from R):
#
#     from  pandas_datareader  import  wb
#           \_______________/          \/
#            package                    submodule you pull in
#
# Some imports go one level deeper - package.submodule, then a name.
# e.g. DataReader (used in the FRED section) can be pulled in directly:
#
#     from  pandas_datareader.data  import  DataReader
#           \___________________/           \________/
#            package . submodule             function name
#
# (In this file we import it the other way: 'import ... as web', then
#  call web.DataReader - same function, just reached via web.)

start = datetime(2005, 1, 1)   # datetime(year, month, day) - YEAR first
end = datetime(2008, 1, 1)     # -> Jan 1 2005  ...  Jan 1 2008
indicator_id = 'NY.GDP.PCAP.KD'   # World Bank code for GDP/capita
                                  # (constant, inflation-adjusted USD)

gdp_per_capita = wb.download(
    indicator=indicator_id,
    start=start,
    end=end,
    country=['US', 'CA', 'MX']    # 2-letter ISO country codes
)
print(gdp_per_capita)

# wb.download(indicator, start, end, country) -> DataFrame.
# Each API pandas-datareader supports has its own submodule; wb is
# World Bank. An "indicator" code IS how you ask for a dataset.
#
# NEW CONCEPT: the result has a MultiIndex (two-level index).
# 01-05 all had a single index (0,1,2,...). This is keyed by TWO
# columns at once: country + year.
#
#                        NY.GDP.PCAP.KD
#   country       year
#   Canada        2008     48511.33
#                 2007     48553.47   <- year not repeated; grouped
#                 2006     48036.57      under Canada
#                 2005     47283.84
#   Mexico        2008      9587.64
#                 ...
#
#   single index          MultiIndex
#   -----------           ----------------
#   row -> value          (country, year) -> value
#   one key per row       two keys per row (outer + inner)
#
# To turn country/year back into normal COLUMNS (for groupby, plots):
#   gdp_per_capita = gdp_per_capita.reset_index()
#   # index goes back to 0,1,2,... ; country & year become columns
#
# R: wb.download(...) ~ WDI(country=..., indicator=..., start=, end=)


# ============================================================
# World Bank catalog  (wb.get_countries)
# ============================================================
# Task: list every country/economy you can query. One call, one big
#       reference table.
#
# NOTE: the course teaches get_nasdaq_symbols() from a nasdaq_trader
# submodule. That submodule was REMOVED from pandas-datareader in the
# 0.11 release, so it won't import locally (it still works on
# Codecademy's older version). Same idea - "one call returns a big
# catalog DataFrame" - shown here with a source that still works.

countries = wb.get_countries()
print(countries)

# wb.get_countries() takes no required arguments and returns a
# DataFrame of ~300 countries/economies with columns like: name,
# iso3c/iso2c codes, region, incomeLevel, capitalCity, lat/long.
#
# Point worth noticing: a single submodule can expose SEVERAL
# functions -
#   wb.download(...)      -> get the DATA
#   wb.get_countries()    -> get the CATALOG of what you can query
#
# Habit: print(countries) and check what it's indexed by - same
# first question you ask after every import (see the table below).


# ============================================================
# FRED via DataReader
# ============================================================
# Task: pull the S&P 500 series (id 'SP500') for Jan 2019, print it.

from datetime import datetime
import pandas_datareader.data as web

start = datetime(2019, 1, 1)   # datetime(year, month, day) - YEAR first
end = datetime(2019, 2, 1)     # -> Jan 1 2019  ...  Feb 1 2019

sap_data = web.DataReader('SP500', 'fred', start, end)
print(sap_data)

# Output (structure; use whatever values FRED returns):
# ->                SP500
# -> DATE
# -> 2019-01-01       NaN    <- New Year's Day, market CLOSED (not a bug)
# -> 2019-01-02   2510.03
# -> 2019-01-03   2447.89
# -> ...
# -> 2019-02-01   2706.53
#
# DataReader - the GENERIC reader (source chosen by a string):
#
#     web.DataReader('SP500', 'fred', start, end)
#                     \____/   \___/  \________/
#                     series   which   date range
#                     id       API
#
#   - 'SP500'    = the FRED series id (the dataset you want)
#   - 'fred'     = the SOURCE name. DataReader is generic: it can talk
#                  to several APIs, and you pick which one with this
#                  string (e.g. 'fred').
#   - start/end  = datetime objects that filter the date range.
#
# Two call styles seen this lesson:
#   wb.download(...) / wb.get_countries()  -> dedicated submodule
#   web.DataReader('x', 'fred', ...)       -> generic, source = string
#
# Finance note: FRED's SP500 is the INDEX LEVEL (the ~2500 value),
# NOT market capitalisation. The lesson's wording is loose - keep
# the two concepts separate.

# ------------------------------------------------------------
# The recurring question: "what is my index?"
# ------------------------------------------------------------
# Every import hands you data keyed some way, and the index decides
# how you filter, group and plot. Three common kinds:
#
#   keyed by...            example key            seen in
#   -----------            -----------            -------
#   MultiIndex             ('Canada', '2008')     wb.download
#   a label / string       'AAPL' (a ticker)      symbol tables*
#   a date (DatetimeIndex) 2019-01-02             FRED / SP500
#
#   *symbol-keyed tables are what the retired NASDAQ reader returned;
#    the shape is the point, even though we don't run it here.
#
# reset_index() flattens any of these into ordinary columns.
#
# R: web.DataReader('SP500','fred',...) ~ getSymbols("SP500", src="FRED");
#    a DatetimeIndex is like an xts/zoo object keyed by date.

# ============================================================
# API Keys
# ============================================================
# Task: run a Tiingo request with a fake key -> expect an
#       "invalid API key" error. (Error is the point of the task.)

# An API key = a long random string that identifies YOU to the API.
#   e.g. 003026bbc133714df1834b8638bb496e-8f4b3d9a-e931
# Most finance APIs require one (FRED / World Bank above don't).
# You get one by signing up on the provider's website.
#
# RULE: treat an API key like a PASSWORD.
#   - never share it
#   - never hardcode it in a script that goes to GitHub
#     (bots scan public repos for keys within minutes)
#   - never paste it into an online editor (incl. Codecademy)

# What the course runs (fails on purpose - placeholder key):
#   import pandas_datareader as pdr
#   df = pdr.get_data_tiingo('GOOG', api_key='my-api-key')
#   # -> error: invalid API key

# ------------------------------------------------------------
# The safe pattern: environment variable
# ------------------------------------------------------------
# Store the key in the OPERATING SYSTEM, read it from the script.
# The script contains only the variable NAME -> safe to commit.
#
#   +----------------------+        +--------------------------+
#   |  Windows (setx)      |        |  script.py  (on GitHub)  |
#   |  TIINGO_API_KEY =    | -----> |  os.environ.get(         |
#   |  "real-secret-key"   |  read  |     "TIINGO_API_KEY")    |
#   +----------------------+        +--------------------------+
#      secret lives here               only the NAME lives here
#
# Set once in cmd (then close + reopen terminal / VS Code -
# setx only applies to NEW sessions):
#   setx TIINGO_API_KEY "your-real-key-here"

import os

api_key = os.environ.get("TIINGO_API_KEY")   # None if not set
# df = pdr.get_data_tiingo('GOOG', api_key=api_key)
#
# Shortcut: the Tiingo reader looks for TIINGO_API_KEY by itself,
# so  pdr.get_data_tiingo('GOOG')  works once the variable is set.

# LEARNING POINT - the course's Quandl example:
#   os.environ["QUANDL_API_KEY"] = "demo"
# This SETS the key inside the script. Fine for a dummy value like
# "demo"; with a real key it's hardcoding again -> don't commit it.
# (Also: Quandl is now Nasdaq Data Link; the 'quandl' reader may no
#  longer work - same kind of drift as nasdaq_trader above.)
#
# R: os.environ["KEY"] = "x"   ~ Sys.setenv(KEY = "x")
#    os.environ.get("KEY")     ~ Sys.getenv("KEY")
#    setx (OS env var)         ~ keys stored in .Renviron


# ============================================================
# Flaky APIs and Changing Contracts
# ============================================================
# Task: reading only - browse the pandas-datareader docs.
#
#   Flaky API          -> service sometimes down/slow (TEMPORARY)
#                         fix: retry later
#   Changing contract  -> API/library changes how it works (PERMANENT)
#                         fix: update your code
#                         e.g. nasdaq_trader removed in v0.11 (above)
#
# Course tips:
#   1. test your code often
#   2. check the pandas-datareader docs when something breaks
#      -> "Data Readers" page: every source + its functions
#      -> "What's New" page: what was added / removed
#   3. watch the GitHub repo (github.com/pydata/pandas-datareader)
#      - sometimes the bug is in datareader, not the API
#
# Extra habit: wrap API calls so a failure is readable, not a crash.
#   try:
#       df = pdr.get_data_fred('GS10')
#   except Exception as e:
#       print(f"FRED request failed: {e}")
#
# R: try/except ~ tryCatch()
# ============================================================
# Shift  (.shift)
# ============================================================
# Task: pull quarterly GDP from FRED (2008-2018), add a 'growth'
#       column = change vs. previous quarter.

# import codecademylib3_seaborn   # Codecademy-only - DELETE locally
#                                 # (ModuleNotFoundError otherwise)
import pandas_datareader.data as web
from datetime import datetime

start = datetime(2008, 1, 1)
end = datetime(2018, 1, 1)

gdp = web.DataReader('GDP', 'fred', start, end)   # quarterly data
gdp['growth'] = gdp['GDP'] - gdp['GDP'].shift(1)
print(gdp)

# shift(n) moves every row of a column (or whole DataFrame)
#   n > 0  -> DOWN  (row sees the PAST value)
#   n < 0  -> UP    (row sees the FUTURE value)
#
#          GDP     GDP.shift(1)   growth
#   Q1   14706         NaN          NaN    <- no previous row
#   Q2   14866       14706          159
#   Q3   14899       14866           33
#   Q4   14608       14899         -291    <- 2008 crisis
#
# 'growth' here = ABSOLUTE change (billions USD), not a percentage.
#
# Shortcuts:
#   df['col'].diff()         == df['col'] - df['col'].shift(1)
#   df['col'].pct_change()   == (x - x.shift(1)) / x.shift(1)
#
# R: shift(1) ~ dplyr::lag(x, 1)   shift(-1) ~ dplyr::lead(x, 1)


# ============================================================
# Variance & Covariance  (.var / .cov)
# ============================================================
# Task: load TSP fund prices from CSV, print variance of every
#       column, then the covariance matrix.

import pandas as pd

tsp_data = pd.read_csv("data/tsp_data.csv", header=0, index_col=0)
print(tsp_data.var())    # -> Series: one variance per column
print(tsp_data.cov())    # -> DataFrame: column x column matrix

# VARIANCE = spread around the mean -> VOLATILITY in finance
#   df['stocks'].var()  # -> 106427   (big swings)
#   df['bonds'].var()   # -> 2272     (calm)
#
# COVARIANCE = do two columns move together?
#
#              stocks     bonds
#   stocks   [ 106427 ]   -15300     diagonal     = own variance
#   bonds      -15300   [ 2272 ]     off-diagonal = pair covariance
#                                    (symmetric)
#   +  -> same direction      -  -> opposite directions
#
# LEARNING POINTS:
#   - course says .var() on a DataFrame returns a DataFrame -> it's
#     actually a SERIES. .cov() returns the DataFrame.
#   - covariance gives DIRECTION, not strength (scale-dependent).
#     Strength -> df.corr()   (always between -1 and +1)
#   - real finance work uses RETURNS, not prices:
#       tsp_data.pct_change().cov()
#
# R: same names - var(), cov(), cor()  (also sample / n-1 default)


# ============================================================
# Review exercise  (section 06 recap)
# ============================================================
# Uses: read_csv, .var(), web.DataReader + datetime

# ------------------------------------------------------------
# Task 1 - Import a CSV
# ------------------------------------------------------------
# The file apple_prices.csv holds historical Apple stock prices.
# Load it into a DataFrame called apple_prices and print it.

apple_prices = pd.read_csv('data/apple_prices.csv')
print(apple_prices)

# MISTAKE MADE: typed 'apple_prices.cvs' (cvs, not csv)
#   -> [Errno 2] File b'apple_prices.cvs' does not exist
#   Errno 2 = file not found -> check spelling, extension, folder.
#   Python stops at the FIRST error, so later lines never ran.

# ------------------------------------------------------------
# Task 2 - Variance of one column
# ------------------------------------------------------------
# Measure how volatile Apple's stock is: print the variance of
# the 'open' column (opening price).

print(apple_prices['open'].var())
# -> a single number (one column -> one value)
#    compare: df.var() on a whole DataFrame -> Series, one per column

# ------------------------------------------------------------
# Task 3 - Pull data from FRED
# ------------------------------------------------------------
# FRED series APUS12A74714 = average gasoline price, New York State.
# Fetch it for Jan 1 2008 - Jan 1 2018, store it in gas_prices,
# print it.

start = datetime(2008, 1, 1)
end = datetime(2018, 1, 1)

gas_prices = web.DataReader('APUS12A74714', 'fred', start, end)
print(gas_prices)
# -> DatetimeIndex (one row per date), one column named after the
#    series id

# LEARNING POINT (R habit): in a .py script, an expression on its
# own line is calculated and DISCARDED - nothing is shown.
#   apple_prices['open'].var()          # runs, shows nothing
#   print(apple_prices['open'].var())   # shows the result
#   pd.read_csv('file.csv')             # loads, then throws away
#   df = pd.read_csv('file.csv')        # keeps it in a variable
# (R console / Jupyter auto-print the last value; scripts don't.)


# ============================================================
# Review - section 06 in one screen
# ============================================================
#   read data       pd.read_csv("data/file.csv")
#                   wb.download(indicator, start, end, country)
#                   web.DataReader('SERIES_ID', 'fred', start, end)
#   date ranges     datetime(year, month, day)
#   API keys        password rules; os.environ, never on GitHub
#   flaky APIs      test often; check datareader docs + GitHub
#   row-to-row      df['col'].shift(1) / .diff() / .pct_change()
#   statistics      .var()  .cov()  .corr()
#
# Locally: drop 'import codecademylib3_seaborn'; keep CSVs in data/
#          run from the project root so 'data/...' paths resolve