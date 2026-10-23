# Key words - Mean-Variance Optimization

Cheat sheet for the whole track: every function and keyword, what it does, a short example, and where it's explained in full. The section links open the notebook; scroll to that section number.

- [01 - Mean-Variance Portfolio Optimization](#01---mean-variance-portfolio-optimization)

---

## 01 - Mean-Variance Portfolio Optimization

Notebook: [01_mean_variance_optimization.ipynb](01_mean_variance_optimization.ipynb)

| keyword | what it does | example | explained in |
|---|---|---|---|
| `df.pct_change()` | return per period: (this - previous) / previous; first row is NaN | `stock_data.pct_change()` | [section 1](01_mean_variance_optimization.ipynb) |
| `.mean()` | average of each column - skips NaN automatically | `quarterly_returns.mean()` | [section 1](01_mean_variance_optimization.ipynb) |
| `pd.read_csv(..., index_col=, parse_dates=True)` | use a column as row labels, read as real dates | `pd.read_csv(path, index_col='Date', parse_dates=True)` | [section 1](01_mean_variance_optimization.ipynb) |
| compound return | the steady rate that gives the real growth - what you actually earned | `(last / first) ** (1 / periods) - 1` | [section 1](01_mean_variance_optimization.ipynb) |
| `df / df.iloc[0]` | growth of 1: every row divided by the first row | `stock_data / stock_data.iloc[0]` | [section 1](01_mean_variance_optimization.ipynb) |
| weights | share of the portfolio in each asset - add up to 1 | `weights = amounts / amounts.sum()` | [section 2](01_mean_variance_optimization.ipynb) |
| portfolio expected return | weighted average of the assets' expected returns | `weights @ returns` | [section 3](01_mean_variance_optimization.ipynb) |
| `np.dot(a, b)` / `a @ b` | dot product: multiply pairwise, then add up (R: `%*%`) | `np.dot(weights, returns)` | [section 3](01_mean_variance_optimization.ipynb) |
| variance | how much one asset's returns jump around - its risk | `quarterly_returns.var()` | [section 4](01_mean_variance_optimization.ipynb) |
| covariance | do two assets move together? > 0 same direction, < 0 opposite, 0 no pattern | `quarterly_returns.cov()` | [section 4](01_mean_variance_optimization.ipynb) |
| `df.cov()` | covariance matrix: variances on the diagonal, covariances of each pair off it | `returns_quarterly.cov()` | [section 5](01_mean_variance_optimization.ipynb) |
| `df.corr()` | correlation matrix: covariance scaled to -1 ... +1 | `returns_quarterly.corr()` | [section 5](01_mean_variance_optimization.ipynb) |
| `df.std()` | standard deviation = square root of variance = volatility | `returns_quarterly.std()` | [section 5](01_mean_variance_optimization.ipynb) |
| `plt.imshow(table, cmap=)` | heatmap - a table drawn as coloured squares | `plt.imshow(corr, cmap='RdBu', vmin=-1, vmax=1)` | [section 5](01_mean_variance_optimization.ipynb) |
| `plt.colorbar()` | legend for a heatmap's colours | `plt.colorbar(label='correlation')` | [section 5](01_mean_variance_optimization.ipynb) |
| portfolio volatility | risk of a portfolio - uses the whole covariance matrix, not a weighted average | `np.sqrt(w @ cov @ w)` | [section 6](01_mean_variance_optimization.ipynb) |
| `np.random.seed(n)` | fixed start for random numbers - same results every run | `np.random.seed(1)` | [section 6](01_mean_variance_optimization.ipynb) |
| `np.random.random(n)` | n random numbers between 0 and 1 | `np.random.random(6)` | [section 6](01_mean_variance_optimization.ipynb) |
| `df.plot.scatter(x=, y=)` | pandas scatter plot - give the column names | `random_portfolios.plot.scatter(x='Volatility', y='Returns')` | [section 7](01_mean_variance_optimization.ipynb) |
| efficient frontier | the top-left edge: max return for each risk, min risk for each return | `optimal_portfolio(returns_quarterly[1:])` | [section 8](01_mean_variance_optimization.ipynb) |
| quadratic programming (`solvers.qp`) | optimizer: minimise risk - return under constraints (weights >= 0, sum = 1) | `solvers.qp(mu*S, -pbar, G, h, A, b)` | [section 8](01_mean_variance_optimization.ipynb) |
| `'y-o'` | format string: colour + line + marker (yellow, solid, circles) | `plt.plot(x, y, 'y-o')` | [section 8](01_mean_variance_optimization.ipynb) |
| `try / except: pass` | runs code, silently ignores errors - hides bugs | `try: plt.plot(...) except: pass` | [section 8](01_mean_variance_optimization.ipynb) |
| `np.diagonal(matrix)` | the values on the diagonal - here the variances of each stock | `np.sqrt(np.diagonal(cov))` | [section 9](01_mean_variance_optimization.ipynb) |
| `marker='X', s=200` | scatter marker shape and size | `plt.scatter(x, y, marker='X', s=200)` | [section 9](01_mean_variance_optimization.ipynb) |
| `.iloc[-1]` | last item by position (safer than `[-1]` on a Series with a named index) | `expected_returns.iloc[-1]` | [section 9](01_mean_variance_optimization.ipynb) |
| diversification | uncorrelated assets cancel swings: risk falls with more assets, down to the market-risk floor | `sigma / np.sqrt(n)` (rho = 0) | [section 9](01_mean_variance_optimization.ipynb) |
| `'k-o'` | black line with circles (`k` = black; `b` would be blue) | `plt.plot(risks, returns, 'k-o')` | [section 10](01_mean_variance_optimization.ipynb) |
| `df.loc[rows, column]` | select by labels: these rows, this column | `corr.loc[six, 'Dexcom']` | [section 10](01_mean_variance_optimization.ipynb) |
| `enumerate(list, start=1)` | loop with a counter - e.g. the subplot index | `for i, pair in enumerate(pairs, start=1):` | [section 4](01_mean_variance_optimization.ipynb) |
| `'{:.2%}'` / `f'{x:.2%}'` | decimal shown as a percentage - multiplies by 100 and adds % (`'{:.2f}%'` doesn't) | `f'{0.01528:.2%}'` -> `1.53%` | [section 3](01_mean_variance_optimization.ipynb) |
