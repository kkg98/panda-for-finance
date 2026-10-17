# 4 - Visualizing Finance Data: chart gallery

Every chart in this folder is produced by the notes scripts next to this page and saved to `charts/`.
Run from the repo root, e.g. `py notes\4_visualizing_finance_data\01_matplotlib_basics.py`.

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

### Concept guides

**`plt.subplot(rows, cols, index)`** - blue = rows, orange = columns, green = which box

![](charts/guide_subplot_grid.png)

**Mixed layouts** - every box picks its own grid

![](charts/guide_subplot_mixed_layout.png)

**`plt.subplots_adjust(...)`** - margins and gaps

![](charts/guide_subplots_adjust.png)
