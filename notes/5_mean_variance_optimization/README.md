# 5 - Mean-Variance Optimization: chart gallery

Every chart in this folder is produced by the notebooks next to this page and saved to `charts/`.
Open [01_mean_variance_optimization.ipynb](01_mean_variance_optimization.ipynb) to see each chart directly under the code that made it.

## 01 - Mean-Variance Portfolio Optimization

| | |
|---|---|
| **Average vs compound return** - the average rewards volatile stocks<br>![](charts/01_01_avg_vs_compound_return.png) | **Growth of 1 EUR** - `stock_data / stock_data.iloc[0]`<br>![](charts/01_01b_growth_of_1_eur.png) |
| **Portfolio weights** - `amounts / amounts.sum()`<br>![](charts/01_02_portfolio_weights.png) | **Portfolio return** - weighted average, `weights @ returns`<br>![](charts/01_03_portfolio_return.png) |

**Covariance in pairs** - airlines together, oil together, airline vs oil about 0

![](charts/01_04_covariance_pairs.png)

**Correlation heatmap** - `plt.imshow(returns_corr, cmap='RdBu')`: airlines and oil as two blocks

![](charts/01_05_correlation_heatmap.png)

| | |
|---|---|
| **5,000 random portfolios** - `df.plot.scatter(x='Volatility', y='Returns')`<br>![](charts/01_07_random_portfolios.png) | **Portfolios vs single stocks** - mixing beats most single stocks<br>![](charts/01_07b_portfolios_vs_single_stocks.png) |

**Efficient frontier** - `optimal_portfolio()`, yellow line on the top-left edge

![](charts/01_08_efficient_frontier.png)

**Adding Nvidia** - green frontier reaches higher, never worse than yellow

![](charts/01_09_frontier_with_nvidia.png)

**Risk vs number of assets** - falls with every asset, levels off at a floor when assets are correlated

![](charts/01_09b_risk_vs_number_of_assets.png)

| | |
|---|---|
| **Adding Dexcom** - black frontier above and left of yellow and green<br>![](charts/01_10_frontier_with_dexcom.png) | **Nvidia vs Dexcom correlations** - Dexcom barely moves with the portfolio<br>![](charts/01_10b_nvidia_vs_dexcom_correlation.png) |
