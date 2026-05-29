import pandas as pd
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Carol', 'David'],
    'portfolio_value': [10000, 25000, 8000, 150000],
    'risk_tolerance': ['low', 'high', 'low', 'high']
})


df["recommendation"] = df.apply(lambda row: "Aggressive growth" if row["portfolio_value"] > 100000 and row["risk_tolerance"] == "high" 
                                else  "Conservative growth" if row["portfolio_value"] > 100000 and row["risk_tolerance"] == "low"
                                else "Balanced" if row["portfolio_value"] <= 100000 and row["risk_tolerance"] == "high"
                                else "Capital preservation",
                                 axis=1)



print(df)