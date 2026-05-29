import pandas as pd
import numpy as np
orders = pd.read_csv('orders.csv')
pricey_shoes = orders.groupby("shoe_type").price.max()
print(pricey_shoes)
print(type(pricey_shoes))
orders = pd.read_csv('orders.csv')
print(orders)
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x,25)).reset_index()
print(cheap_shoes)
