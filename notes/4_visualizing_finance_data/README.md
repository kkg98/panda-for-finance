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

### Concept guides

**`plt.subplot(rows, cols, index)`** - blue = rows, orange = columns, green = which box

![](charts/guide_subplot_grid.png)

**Mixed layouts** - every box picks its own grid

![](charts/guide_subplot_mixed_layout.png)

**`plt.subplots_adjust(...)`** - margins and gaps

![](charts/guide_subplots_adjust.png)
