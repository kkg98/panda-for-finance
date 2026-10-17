# ============================================================
# 01 - MATPLOTLIB BASICS  (Line Graphs in Matplotlib)
# Codecademy: Analyze Financial Data with Python / Visualizing Finance Data
# ============================================================
# Prereq:  py -m pip install matplotlib
#
# Section goal: chart financial data with Matplotlib, then use it
# for mean-variance portfolio optimization (choosing assets that
# balance expected return against risk).
#
# Every example saves its chart to charts/ -> all charts are shown
# together in README.md in this folder (the gallery page).
#
# Run from the project root:
#   py notes\4_visualizing_finance_data\01_matplotlib_basics.py
# Each chart opens in a window; the script PAUSES until you close it.
#
# R: matplotlib ~ base R plot() / ggplot2
#    (closer to base R: you build a chart step by step with calls)

# import codecademylib   # Codecademy-only - DELETE locally


# ============================================================
# 1. Importing Matplotlib
# ============================================================
# Task: import the plotting functions as plt.

from matplotlib import pyplot as plt

#     from  matplotlib  import  pyplot  as  plt
#           \________/          \____/      \_/
#            package            submodule   short nickname
#                               (the plotting functions)
#
# Same thing, the form you'll see more often online:
#   import matplotlib.pyplot as plt
#
# plt / np / pd are conventions everyone uses.

CHARTS = 'notes/4_visualizing_finance_data/charts/'   # where PNGs go


# ============================================================
# 2. Basic Line Plot
# ============================================================
# Task: plot lunch spending (money_spent) over 7 days, show it.

days = [0, 1, 2, 3, 4, 5, 6]
money_spent = [10, 12, 12, 10, 14, 22, 24]

plt.figure()                                   # start a new, empty chart
plt.plot(days, money_spent)                    # build the line (in memory)
plt.savefig(CHARTS + '01_basic_line_plot.png') # save it (optional)
plt.show()                                     # display it

# ------------------------------------------------------------
# THE PATTERN - every chart in this file follows it
# ------------------------------------------------------------
#   1. prepare data      x = [...], y = [...]   (same length!)
#   2. new figure        plt.figure()           (blank canvas)
#   3. build the chart   plt.plot(x, y)         <- nothing visible yet,
#                        + labels, title...        it only draws in memory
#   4. save it           plt.savefig('...png')  <- optional, BEFORE show
#   5. display it        plt.show()             <- opens the window
#
#   plt.plot() alone shows NOTHING - like a value without print().
#   savefig() AFTER show() -> blank image (show clears the figure).
#
#   plt.figure() isn't in the course code - Codecademy shows every
#   exercise separately. Locally it guarantees each chart starts
#   empty, so lines from the previous example can't leak in.
#
#   plt.plot(x, y)
#            ^  ^
#            |  +-- y: goes UP the vertical axis
#            +----- x: goes ALONG the bottom   (x ALWAYS first)


# ============================================================
# 3. Basic Line Plot II - multiple lines
# ============================================================
# Task: plot revenue vs time and costs vs time on the same axes.

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.figure()
plt.plot(time, revenue)        # 1st line -> blue by default
plt.plot(time, costs)          # 2nd line -> orange by default
plt.savefig(CHARTS + '02_multiple_lines.png')
plt.show()

# RULE: everything plotted between two show() calls lands on ONE chart.
#
#   plt.plot(time, revenue)
#   plt.plot(time, costs)      <- both collect on the same figure
#   plt.show()                 <- displays both
#
# LEARNING POINT (found by experimenting):
#   plt.plot(time, revenue)
#   plt.show()                 <- shows revenue, then CLEARS
#   plt.plot(time, costs)
#   plt.show()                 <- new empty figure -> only costs
#
# Finance reading: the gap between the lines = profit.
#   time 1: costs 500 > revenue 400 -> a loss period
#   after that revenue pulls ahead and the gap widens.


# ============================================================
# 4. Linestyles
# ============================================================
# Task: revenue as a purple dashed line; costs in #82edc9 with
#       square markers.

plt.figure()
plt.plot(time, revenue, color='purple', linestyle='--')
plt.plot(time, costs, color='#82edc9', marker='s')
plt.savefig(CHARTS + '03_linestyles.png')
plt.show()

#   keyword      short   values
#   color        c       'green', '#82edc9' (HEX), 'b' 'g' 'r' 'k' ...
#   linestyle    ls      '-' solid  '--' dashed  ':' dotted
#                        '-.' dash-dot  '' no line
#   marker               'o' circle  's' square  '*' star
#                        '^' triangle  'D' diamond
#   linewidth    lw      number, e.g. 2
#   markersize   ms      number, e.g. 8
#
# Shortcut from the docs - format string '[marker][line][color]':
#   plt.plot(x, y, 'o--g')   # circles, dashed, green
#   plt.plot(x, y, '^k:')    # black triangles, dotted
#   = plt.plot(x, y, marker='o', linestyle='--', color='green')
#   Keywords are easier to read; if both are given, the keyword wins.
#   HEX colours don't fit in the shortcut -> keyword: color='#82edc9'
#
# ------------------------------------------------------------
# MISTAKE MADE: x and y swapped
# ------------------------------------------------------------
#   plt.plot(revenue, time)   # WRONG - revenue along the bottom,
#                             # time going up. No error, just a
#                             # wrong-looking chart.
#   plt.plot(time, revenue)   # RIGHT
#
# The trap: "plot A vs B" -> plt.plot(B, A)
#   "revenue vs time" -> plt.plot(time, revenue)
#   In words y comes first, in code x comes first.

plt.figure()
plt.plot(revenue, time, color='purple', linestyle='--')
plt.plot(costs, time, color='#82edc9', marker='s')
plt.title('MISTAKE: x and y swapped - time runs up the side')
plt.savefig(CHARTS + '03b_mistake_xy_swapped.png')
plt.show()


# ============================================================
# 5. Axis and Labels - zooming
# ============================================================
# Task: coffee spending over 12 years; zoom to x 0-12, y 2900-3100.

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]

plt.figure()
plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])
plt.savefig(CHARTS + '04_axis_zoom.png')
plt.show()

#   plt.axis([xmin, xmax, ymin, ymax])
#             \_________/ \_________/
#              x-range     y-range       <- always 4 numbers, x first
#
#   one axis at a time (same result):
#     plt.xlim(0, 12)
#     plt.ylim(2900, 3100)
#
#   range(12) -> 0..11 (end excluded), so x up to 12 leaves a little
#   empty space on the right.
#
# CAUTION - truncated y-axis:
#   y from 2900 to 3100 makes the line look wild, but the real
#   variation is only ~7%. Starting the y-axis far above zero
#   exaggerates changes - useful for detail, classic way charts
#   mislead. Always check where the y-axis starts.


# ============================================================
# 6. Labeling the Axes
# ============================================================
# Task: x-label 'Time', y-label 'Dollars spent on coffee',
#       title 'My Last Twelve Years of Coffee Drinking'.

plt.figure()
plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])
plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')
plt.title('My Last Twelve Years of Coffee Drinking')
plt.savefig(CHARTS + '05_labels.png')
plt.show()

#   plt.xlabel('...')   -> text under the x-axis
#   plt.ylabel('...')   -> text beside the y-axis
#   plt.title('...')    -> text above the chart
#   all take a string: 'single' or "double" quotes - but matching
#
# TIP: put units in labels. 'Time' -> days? years? -> 'Year'.
#      Money -> 'Coffee spending (USD)'.


# ============================================================
# 7. Subplots
# ============================================================
# Task: 1 row x 2 columns - temperature vs months on the left,
#       flights_to_hawaii vs temperature (scatter) on the right.

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.figure()
plt.subplot(1, 2, 1)                          # LEFT box
plt.plot(months, temperature)

plt.subplot(1, 2, 2)                          # RIGHT box
plt.plot(temperature, flights_to_hawaii, 'o') # 'o' = markers only -> scatter
plt.savefig(CHARTS + '06_subplots.png')
plt.show()

# ------------------------------------------------------------
# plt.subplot(rows, cols, index) - which box am I drawing in?
# (picture: charts/guide_subplot_grid.png)
# ------------------------------------------------------------
#
#   plt.subplot(1, 2, 1)
#               |  |  |
#               |  |  +-- index: draw in box number 1
#               |  +----- 2 columns
#               +-------- 1 row
#
#   first two numbers = SIZE of the grid
#   third number      = WHICH box in it
#
#   1 row x 2 columns = 2 boxes:
#   +-----------+-----------+
#   |  index 1  |  index 2  |
#   +-----------+-----------+
#   subplot(1, 2, 3) -> ERROR: a 1x2 grid has no box 3
#
#   2 rows x 3 columns = 6 boxes:
#   +-----+-----+-----+
#   |  1  |  2  |  3  |     subplot(2, 3, 1) -> top left
#   +-----+-----+-----+     subplot(2, 3, 3) -> top right
#   |  4  |  5  |  6  |     subplot(2, 3, 4) -> bottom left
#   +-----+-----+-----+     subplot(2, 3, 6) -> bottom right
#
#   numbered in READING ORDER: left -> right, then next row.
#   Like Excel: first two numbers = table size, third = the cell.
#   index goes from 1 to rows x cols.
#
# RULE: subplot() SELECTS a box. Every plot(), title(), label after
#       it goes into that box - until the next subplot() call.
#       (same "everything until the next switch" logic as show())
#
# MISTAKES MADE:
#   - used index 2 for the LEFT box -> left is 1
#   - plt.plot(temperature, months) -> x/y swapped again
#     ("temperature vs months" -> plot(months, temperature))
#   - forgot the 2nd plt.subplot() -> both datasets drew into the
#     same box with mismatched scales -> "seems weird"
#
# Finance reading (right box): temperature up -> flights down =
# a NEGATIVE relationship (like stocks/bonds covariance, 3_pandas/05).
# A scatter is the natural chart for "how do two variables relate"
# -> preview of the Regression track.


# ============================================================
# 8. Subplots Part II - mixed layout + spacing
# ============================================================
# Task: one plot on top (full width), two below; then
#       wspace=0.35 and bottom=0.2.

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.figure()
plt.subplot(2, 1, 1)               # top, full width
plt.plot(x, straight_line)

plt.subplot(2, 2, 3)               # bottom left
plt.plot(x, parabola)

plt.subplot(2, 2, 4)               # bottom right
plt.plot(x, cubic)

plt.subplots_adjust(wspace=0.35, bottom=0.2)
plt.savefig(CHARTS + '07_subplots_mixed_layout.png')
plt.show()

# ------------------------------------------------------------
# MIXED LAYOUTS: every box picks its OWN grid
# (picture: charts/guide_subplot_mixed_layout.png)
# ------------------------------------------------------------
# STEP 1  Draw the figure you want.
#
#         +-------------------+
#         |       star        |
#         +---------+---------+
#         | square  | triangle|
#         +---------+---------+
#
# STEP 2  For EACH box ask: "in what grid is this box exactly ONE cell?"
#         star     full width, 1 of 2 rows  -> 2 rows x 1 col  (2, 1, ?)
#         square   half width, 1 of 2 rows  -> 2 rows x 2 cols (2, 2, ?)
#         triangle same size as square      -> (2, 2, ?)
#
# STEP 3  In THAT grid, count in reading order to get the index.
#
#         2x1 grid:          2x2 grid:
#         +-----------+      +-----+-----+
#         | 1  <-star |      |  1  |  2  |   <- unused (star is there)
#         +-----------+      +-----+-----+
#         |     2     |      |  3  |  4  |   <- square = 3, triangle = 4
#         +-----------+      +-----+-----+
#
#         star = (2, 1, 1)   square = (2, 2, 3)   triangle = (2, 2, 4)
#
# CHECK: rows stay the same everywhere (2) so the boxes line up;
#        columns change with the box width.
#
# Alternative (newer, no index counting) - layout drawn as a list:
#   fig, ax = plt.subplot_mosaic([['star',   'star'],
#                                 ['square', 'triangle']])
#   ax['star'].plot(x, straight_line)
#   ax['square'].plot(x, parabola)
#   ax['triangle'].plot(x, cubic)
#
# ------------------------------------------------------------
# plt.subplots_adjust(...) - margins and gaps
# (picture: charts/guide_subplots_adjust.png)
# ------------------------------------------------------------
#   wspace   gap between boxes SIDE BY SIDE   |<->|   default 0.2
#   hspace   gap between ROWS                  ^ v    default 0.2
#   left     space before the boxes start             default 0.125
#   right    where the boxes END (from the left)      default 0.9
#   bottom   space under the boxes                    default 0.1
#   top      where the boxes END (from the bottom)    default 0.9
#   (fractions of the figure: 0 = one edge, 1 = the other edge)
#
#   bigger wspace/hspace/left/bottom = more space
#   "horizontal spacing" in the task = wspace (boxes side by side)
