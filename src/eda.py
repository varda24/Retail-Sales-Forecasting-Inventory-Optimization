import matplotlib.pyplot as plt
import os

def plot_sales(df):
    os.makedirs("outputs/plots", exist_ok=True)

    plt.figure(figsize=(10,5))
    
    # Total sales per day
    daily_sales = df.groupby('Date')['Sales'].sum()
    
    plt.plot(daily_sales.index, daily_sales.values)
    plt.title("Daily Sales Trend")
    
    plt.savefig("outputs/plots/sales_trend.png")
    plt.show()