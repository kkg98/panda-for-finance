# Key words - Visualizing Finance Data

Cheat sheet for the whole track: every function and keyword, what it does, a short example, and where it's explained in full. The section links open the notebook; scroll to that section number.

- [01 - Matplotlib basics](#01---matplotlib-basics)
- [02 - Different plot types](#02---different-plot-types)

---

## 01 - Matplotlib basics

Notebook: [01_matplotlib_basics.ipynb](01_matplotlib_basics.ipynb) - project: [01_project_sublime_limes.ipynb](01_project_sublime_limes.ipynb)

| keyword | what it does | example | explained in |
|---|---|---|---|
| `plt.plot(x, y)` | draws a line - x first, then y | `plt.plot(days, money_spent)` | [section 2](01_matplotlib_basics.ipynb) |
| `color=` / `linestyle=` / `marker=` | line colour, style, point markers | `color='purple', linestyle='--', marker='o'` | [section 4](01_matplotlib_basics.ipynb) |
| `plt.figure(figsize=(w, h))` | new, empty figure - optional size in inches | `plt.figure(figsize=(10, 5))` | [sections 2, 11](01_matplotlib_basics.ipynb) |
| `plt.show()` | displays the figure, then clears it | `plt.show()` | [section 2](01_matplotlib_basics.ipynb) |
| `plt.savefig('name.png')` | saves the figure - before `show()` | `plt.savefig('chart.png')` | [sections 2, 11](01_matplotlib_basics.ipynb) |
| `plt.close('all')` | throws away all open figures | `plt.close('all')` | [section 11](01_matplotlib_basics.ipynb) |
| `plt.axis([xmin, xmax, ymin, ymax])` | zoom - also `plt.xlim()` / `plt.ylim()` | `plt.axis([0, 12, 2900, 3100])` | [section 5](01_matplotlib_basics.ipynb) |
| `plt.xlabel` / `ylabel` / `title` | axis labels and chart title | `plt.title('Coffee spending')` | [section 6](01_matplotlib_basics.ipynb) |
| `plt.subplot(rows, cols, index)` | selects a box in a grid of charts | `plt.subplot(1, 2, 1)` | [sections 7, 8](01_matplotlib_basics.ipynb) |
| `plt.subplots_adjust(...)` | margins and gaps between boxes | `plt.subplots_adjust(wspace=0.35)` | [section 8](01_matplotlib_basics.ipynb) |
| `plt.legend(labels, loc=)` | legend - or `label=` in each `plot()` | `plt.legend(['A', 'B'], loc='best')` | [section 9](01_matplotlib_basics.ipynb) |
| `ax = plt.subplot()` | the chart as an object, for `ax.` commands | `ax = plt.subplot()` | [section 10](01_matplotlib_basics.ipynb) |
| `ax.set_xticks` / `set_xticklabels` | where ticks sit / what they say | `ax.set_xticklabels(month_names)` | [section 10](01_matplotlib_basics.ipynb) |
| `PercentFormatter(xmax)` | shows an axis as % | `ax.yaxis.set_major_formatter(PercentFormatter(1.0))` | [sections 10, 12](01_matplotlib_basics.ipynb) |
| `fig.add_subplot(rows, cols, index)` | adds a box to a named figure - for charts built across notebook cells | `ax2 = fig.add_subplot(1, 2, 2)` | [project](01_project_sublime_limes.ipynb) |
| `ax.axhline` / `axvline` | horizontal / vertical line across the chart | `ax.axhline(0, color='black')` | [section 12](01_matplotlib_basics.ipynb) |
| `ax.axvspan` / `axhspan` | shaded band | `ax.axvspan(2014.6, 2021.5, color='#f2f2f2')` | [section 12](01_matplotlib_basics.ipynb) |
| `ax.text(x, y, 'text')` | free text on the chart | `ax.text(2018, -105, 'negative-rate era')` | [section 12](01_matplotlib_basics.ipynb) |
| `ax.annotate('text', xy=, xytext=)` | text with an arrow to a point | `arrowprops=dict(arrowstyle='->')` | [section 12](01_matplotlib_basics.ipynb) |
| `ax.spines['top'].set_visible(False)` | hides a border line | loop over `['top', 'right']` | [section 12](01_matplotlib_basics.ipynb) |
| `zorder=` | drawing order - lower sits further back | `zorder=0` | [section 12](01_matplotlib_basics.ipynb) |

---

## 02 - Different plot types

Notebook: [02_different_plot_types.ipynb](02_different_plot_types.ipynb)

| keyword | what it does | example | explained in |
|---|---|---|---|
| `plt.bar(x, heights)` | bar chart - x = category slots, heights = values | `plt.bar(range(len(sales)), sales)` | [section 1](02_different_plot_types.ipynb) |
| `range(len(list))` | slots 0, 1, 2 ... one per category | `x = range(len(drinks))` | [sections 1, 2](02_different_plot_types.ipynb) |
| `list(range(...))` | shows the numbers - `print(range(6))` only shows `range(0, 6)` | `print(list(x))` | [section 2](02_different_plot_types.ipynb) |
| `rotation=` | tilts tick labels | `ax.set_xticklabels(drinks, rotation=30)` | [section 2](02_different_plot_types.ipynb) |
| side-by-side template | x-positions for bars next to each other - only `n` changes per dataset | `[t*element + w*n for element in range(d)]` | [section 3](02_different_plot_types.ipynb) |
| `bottom=` | where this bar starts - the dataset in `bottom=` is the one underneath | `plt.bar(x, sales2, bottom=sales1)` | [section 4](02_different_plot_types.ipynb) |
| `yerr=` | error bars - one number for all bars, or one per bar | `plt.bar(x, values, yerr=error)` | [section 5](02_different_plot_types.ipynb) |
| `capsize=` | width of the error bar caps | `capsize=5` | [section 5](02_different_plot_types.ipynb) |
| `plt.fill_between(x, lower, upper)` | shaded band between two y-lines - draw it before the line | `plt.fill_between(months, y_lower, y_upper, alpha=0.2)` | [section 6](02_different_plot_types.ipynb) |
| list comprehension | does a calculation on every item of a list (R: `revenue * 0.9`) | `[0.9 * i for i in revenue]` | [section 6](02_different_plot_types.ipynb) |
| `alpha=` | transparency - 0 invisible, 1 solid | `alpha=0.2` | [sections 6, 10](02_different_plot_types.ipynb) |
| `plt.pie(values)` | pie chart - each value becomes a share of the total | `plt.pie(payment_method_freqs)` | [section 7](02_different_plot_types.ipynb) |
| `plt.axis('equal')` | equal axes - the pie is a circle, not an oval | `plt.axis('equal')` | [section 7](02_different_plot_types.ipynb) |
| `labels=` | names next to each slice - or use `plt.legend(names)`, not both | `plt.pie(freqs, labels=names)` | [section 8](02_different_plot_types.ipynb) |
| `autopct=` | % share written on each slice - format codes like R's `sprintf` | `autopct='%0.1f%%'` -> `69.2%` | [section 8](02_different_plot_types.ipynb) |
| `plt.hist(data)` | histogram - how many values fall in each equal-width bin (10 by default) | `plt.hist(sales['hour'])` | [section 9](02_different_plot_types.ipynb) |
| `bins=` | number of bins - more bins = more detail, but more noise | `plt.hist(data, bins=24)` | [sections 9, 10](02_different_plot_types.ipynb) |
| `range=(min, max)` | only bins values inside this window - use the same one for histograms you compare | `plt.hist(data, range=(7, 19))` | [sections 9, 10](02_different_plot_types.ipynb) |
| `.dt.hour` / `.dt.minute` | parts of a datetime column (R: `lubridate::hour()`) | `t.dt.hour + t.dt.minute / 60` | [section 9](02_different_plot_types.ipynb) |
| `histtype='step'` | histogram outline only, no fill | `plt.hist(a, histtype='step')` | [section 10](02_different_plot_types.ipynb) |
| `density=True` | scales a histogram so its area = 1 - compares shapes of groups with different sizes | `plt.hist(a, density=True)` | [section 10](02_different_plot_types.ipynb) |

Quiz questions I got wrong: [section 11](02_different_plot_types.ipynb).
