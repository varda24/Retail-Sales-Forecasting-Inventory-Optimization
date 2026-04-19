import pandas as pd
import numpy as np
import os

# Create folders automatically
os.makedirs("data/raw", exist_ok=True)

np.random.seed(42)

dates = pd.date_range(start='2023-01-01', periods=365)

products = ['Product_A', 'Product_B', 'Product_C']
categories = ['Electronics', 'Grocery', 'Clothing']

data = []

for product, category in zip(products, categories):
    base = np.random.randint(80, 120)

    for i, date in enumerate(dates):
        weekend = 20 if date.weekday() >= 5 else 0
        trend = i * 0.1
        seasonality = 15 * np.sin(i / 30)
        noise = np.random.normal(0, 5)

        sales = base + weekend + trend + seasonality + noise

        data.append([
            date,
            product,
            category,
            max(0, int(sales))
        ])

df = pd.DataFrame(data, columns=["Date", "Product", "Category", "Sales"])

df.to_csv("data/raw/retail_data.csv", index=False)

print("✅ Dataset created successfully!")