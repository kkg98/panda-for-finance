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