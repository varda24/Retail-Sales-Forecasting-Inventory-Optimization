from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.eda import plot_sales
from src.forecast import forecast_product
from src.inventory import calculate_inventory
import pandas as pd

def main():
    print("🚀 Starting Product-wise Forecasting System...")

    # Load data
    df = load_data("data/raw/retail_data.csv")

    # Preprocess
    df = preprocess_data(df)

    # Plot total sales
    plot_sales(df)

    # Get unique products
    products = df['Product'].unique()

    results = []

    for product in products:
        print(f"\n📊 Processing {product}...")

        # Forecast
        forecast = forecast_product(df, product)

        # Inventory
        inventory = calculate_inventory(product, forecast)

        results.append(inventory)

    # Final results
    result_df = pd.DataFrame(results)

    print("\n📦 FINAL INVENTORY RECOMMENDATIONS:")
    print(result_df)

    # Save output
    result_df.to_csv("outputs/inventory_results.csv", index=False)


if __name__ == "__main__":
    main()