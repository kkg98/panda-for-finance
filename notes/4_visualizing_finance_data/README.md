# 4 - Visualizing Finance Data: chart gallery

Every chart in this folder is produced by the notebooks next to this page and saved to `charts/`.
Open a notebook (e.g. [01_matplotlib_basics.ipynb](01_matplotlib_basics.ipynb)) to see each chart directly under the code that made it.

## 01 - Matplotlib basics (Line Graphs in Matplotlib)

The pattern every chart follows:

```python
plt.figure()                     # 1. new, empty chart
plt.plot(x, y)                   # 2. build it (nothing visible yet)
plt.savefig('charts/name.png')   # 3. save - BEFORE show
plt.show()                       # 4. display it
```

| | |
|---|---|
| **Basic line plot** - `plt.plot(days, money_spent)`<br>![](charts/01_basic_line_plot.png) | **Multiple lines** - two `plot()` calls before one `show()`<br>![](charts/02_multiple_lines.png) |
| **Linestyles** - `color=`, `linestyle='--'`, `marker='s'`<br>![](charts/03_linestyles.png) | **Mistake: x and y swapped** - "revenue vs time" is `plot(time, revenue)`<br>![](charts/03b_mistake_xy_swapped.png) |
| **Zooming** - `plt.axis([0, 12, 2900, 3100])` (truncated y-axis exaggerates changes)<br>![](charts/04_axis_zoom.png) | **Labels and title** - `plt.xlabel / ylabel / title`<br>![](charts/05_labels.png) |
| **Subplots** - `plt.subplot(1, 2, 1)` and `(1, 2, 2)`; right box is a scatter (`'o'`)<br>![](charts/06_subplots.png) | **Mixed layout** - `(2, 1, 1)` on top, `(2, 2, 3)` and `(2, 2, 4)` below<br>![](charts/07_subplots_mixed_layout.png) |
| **Legend** - `plt.legend(legend_labels, loc=8)`<br>![](charts/08_legend.png) | **Mistake: list inside a list** - `[legend_labels]` gives one label<br>![](charts/08b_mistake_legend_double_list.png) |
| **Custom ticks** - `ax.set_xticks` / `set_xticklabels`, hand-typed `'10%'` labels<br>![](charts/09_ticks.png) | **Faster way** - `PercentFormatter(1.0)` formats the whole axis<br>![](charts/09b_ticks_percentformatter.png) |
| **Figures** - default `plt.figure()`<br>![](charts/10_winning_word_lengths.png) | **Figures** - `plt.figure(figsize=(7, 3))`, wide and flat<br>![](charts/10_power_generated.png) |
| **Mistake: no new figure** - both lines land on one sheet<br>![](charts/10b_mistake_no_new_figure.png) | **Review** - ECB deposit rate vs Austrian inflation, 2015-2025<br>![](charts/11_review_ecb_vs_inflation.png) |

### Project: Sublime Limes' Line Graphs

[01_project_sublime_limes.ipynb](01_project_sublime_limes.ipynb) - website visits and lime sales per month for an online lime retailer: two subplots, markers, custom ticks, legend, `subplots_adjust`.

![](charts/sublime_limes_visits_and_sales.png)

### Concept guides

**`plt.subplot(rows, cols, index)`** - blue = rows, orange = columns, green = which box

![](charts/guide_subplot_grid.png)

**Mixed layouts** - every box picks its own grid

![](charts/guide_subplot_mixed_layout.png)

**`plt.subplots_adjust(...)`** - margins and gaps

![](charts/guide_subplots_adjust.png)

## 02 - Different Plot Types

Notebook: [02_different_plot_types.ipynb](02_different_plot_types.ipynb)

| | |
|---|---|
| **Simple bar** - `plt.bar(range(len(sales)), sales)`<br>![](charts/02_01_simple_bar.png) | **Bar labels** - `ax.set_xticks` / `set_xticklabels(drinks)`<br>![](charts/02_02_bar_labels.png) |
| **Side-by-side bars** - x positions `[t*element + w*n for element in range(d)]`<br>![](charts/02_03_side_by_side.png) | **Stacked bars** - `bottom=sales1`: the dataset in `bottom=` is the one underneath<br>![](charts/02_04_stacked_bars.png) |
| **Error bars** - `yerr=error, capsize=5`<br>![](charts/02_05_error_bars.png) | **Fill between** - `plt.fill_between(months, y_lower, y_upper, alpha=0.2)`, band first, line on top<br>![](charts/02_06_fill_between.png) |
| **Mistake: line drawn twice** - the second (orange) line hides the first<br>![](charts/02_06b_mistake_line_drawn_twice.png) | **Pie chart** - `plt.pie(freqs)` + `plt.axis('equal')`<br>![](charts/02_07_pie.png) |
| **Pie labels** - legend + `autopct='%0.1f%%'`<br>![](charts/02_08_pie_labels.png) | **Mistake: names twice, no %** - `labels=` and a legend, `autopct='%0.1f'`<br>![](charts/02_08b_mistake_double_labels.png) |
| **Histogram** - default 10 bins vs `range=(7, 19), bins=24`<br>![](charts/02_09_histogram.png) | **Multiple histograms** - raw counts vs `density=True`<br>![](charts/02_10_multiple_histograms.png) |

### Project: Recreate Graphs using Matplotlib

[02_project_recreate_graphs.ipynb](02_project_recreate_graphs.ipynb) - a math teacher's class results, rebuilt chart by chart: error bars, side-by-side and stacked bars, two histograms, a labeled pie and a shaded error band.

| | |
|---|---|
| **1. Bar chart with error** - `yerr=error, capsize=5`, y-axis cut at 70<br>![](charts/recreate_01_bar_chart_error.png) | **Cut-off vs honest axis** - same data, y from 70 vs from 0<br>![](charts/recreate_01b_truncated_vs_honest.png) |
| **2. Side-by-side bars** - `create_x`, ticks at `middle_x`, all in `ax.` style<br>![](charts/recreate_02_side_by_side.png) | **3. Stacked bars** - five layers, bottoms with `np.add`<br>![](charts/recreate_03_stacked_bars.png) |
| **Faster way: one loop** - `bottom = bottom + grades`, `label=` per layer<br>![](charts/recreate_03b_stacked_bars_loop.png) | **4. Two histograms** - `density=True`, `histtype='step'`, each with its own bins<br>![](charts/recreate_04_two_histograms.png) |
| **Same bins for both** - `range=(50, 100), bins=10`<br>![](charts/recreate_04b_two_histograms_same_bins.png) | **5. Labeled pie** - `labels=unit_topics, autopct='%.0f%%'`<br>![](charts/recreate_05_pie.png) |
| **Mistake: names twice** - `labels=` and a legend, `%d` cuts off decimals<br>![](charts/recreate_05b_mistake_pie_double_labels.png) | **6. Line with shaded error** - line drawn before the band<br>![](charts/recreate_06_line_shaded_error.png) |
| **Band first, line on top**<br>![](charts/recreate_06b_band_first.png) | **Scatter instead of line** - hours vs score, correlation 0.90<br>![](charts/recreate_06c_scatter_relationship.png) |
