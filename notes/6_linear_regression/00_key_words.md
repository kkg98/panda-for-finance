# Key words - Linear Regression

Cheat sheet for the whole track: every function and keyword, what it does, a short example, and where it's explained in full. The section links open the notebook; scroll to that section number.

- [01 - The Model](#01---the-model)

---

## 01 - The Model

Notebook: [01_the_model.ipynb](01_the_model.ipynb)

| keyword | what it does | example | explained in |
|---|---|---|---|
| linear regression | find the line that best fits the data, to predict y from x (R: `lm(y ~ x)`) | `y = m * x + b` | [section 1](01_the_model.ipynb) |
| dependent / independent variable | y = what we predict, x = what we predict it from | revenue (y) from months (x) | [section 1](01_the_model.ipynb) |
| slope `m` | change in y for one unit of x | `m = 11` | [section 1](01_the_model.ipynb) |
| intercept `b` | value of y when x = 0 | `b = 45` | [section 1](01_the_model.ipynb) |
| `[... for i in list]` | list comprehension - applies a formula to every item, builds a new list | `[i * m + b for i in months]` | [section 1](01_the_model.ipynb) |
| `plt.plot(x, y, "o")` | dots only, no connecting line | `plt.plot(months, revenue, "o")` | [section 1](01_the_model.ipynb) |
| loss / SSE | sum of squared errors - how badly the line fits; lower = better | `sum((a - p) ** 2 for a, p in zip(y, y_pred))` | [section 2](01_the_model.ipynb) |
| `zip(a, b)` | pairs two lists item by item | `for a, p in zip(y, y_predicted)` | [section 2](01_the_model.ipynb) |
| `+=` | add to a running total | `total_loss += (y[i] - y_pred[i]) ** 2` | [section 2](01_the_model.ipynb) |
| MSE | mean squared error = SSE / N - the loss gradient descent minimises | `np.mean((y - y_pred) ** 2)` | [section 3](01_the_model.ipynb) |
| gradient descent | step each parameter downhill on the loss curve until the loss stops falling | `b = b - rate * b_gradient` | [section 3](01_the_model.ipynb) |
| gradient | slope of the loss curve; < 0 → increase the parameter, > 0 → decrease it | `get_gradient_at_b(x, y, m, b)` | [section 3](01_the_model.ipynb) |
| b gradient | `-2/N * sum(residuals)` | `-2 / N * np.sum(y - (m * x + b))` | [section 3](01_the_model.ipynb) |
| m gradient | like the b gradient, but each residual is weighted by its x | `-2 / N * np.sum(x * (y - (m * x + b)))` | [section 4](01_the_model.ipynb) |
| learning rate | how big each step is - too big overshoots, too small is slow | `0.01` | [section 5](01_the_model.ipynb) |
| `step_gradient()` | one step: get both gradients, move `b` and `m` downhill | `b, m = step_gradient(months, revenue, b, m)` | [section 5](01_the_model.ipynb) |
| keyword arguments | pass by name, so order doesn't matter (like R's named args) | `get_gradient_at_b(x, y, m=m, b=b)` | [section 5](01_the_model.ipynb) |
| unpacking | assign a returned list to several variables in order | `b, m = [2.355, 17.78]` | [section 5](01_the_model.ipynb) |
| `gradient_descent()` | loop `step_gradient` n times, reassigning `b, m` each pass → returns the fitted `b, m` | `b, m = gradient_descent(months, revenue, 0.01, 1000)` | [section 7](01_the_model.ipynb) |
| `LinearRegression()` | sklearn's linear regression model: create → `.fit()` → `.predict()` | `line_fitter = LinearRegression()` | [section 9](01_the_model.ipynb) |
| `.fit(X, y)` | train the model on the data (R: `lm(y ~ x)`) | `line_fitter.fit(temperature, sales)` | [section 9](01_the_model.ipynb) |
| `.predict(X)` | fitted y-values for given x (R: `predict()`) | `line_fitter.predict(temperature)` | [section 9](01_the_model.ipynb) |
| `.coef_` / `.intercept_` | learned slope(s) / intercept; `_` = set by `.fit()`; `coef_` is an array | `line_fitter.coef_[0]` | [section 9](01_the_model.ipynb) |
| `.reshape(-1, 1)` | 1D array → one-column 2D array, which sklearn needs for X | `temperature.reshape(-1, 1)` | [section 9](01_the_model.ipynb) |
