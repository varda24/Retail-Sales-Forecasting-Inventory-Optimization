import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.forecast import forecast_product_series
from src.inventory import calculate_inventory
from src.metrics import calculate_accuracy   # ✅ IMPORT FIX

st.title("📊 Retail Sales Forecasting Dashboard")

# Load data
df = load_data("data/raw/retail_data.csv")
df = preprocess_data(df)

# Product selector
products = df['Product'].unique()
selected_product = st.selectbox("Select Product", products)

# Filter data
product_df = df[df['Product'] == selected_product]
daily_sales = product_df.groupby('Date')['Sales'].sum()

# Split data (train/test)
train = daily_sales[:-30]
test = daily_sales[-30:]

# Forecast
forecast = forecast_product_series(train)

# =========================
# 📊 ACTUAL VS FORECAST
# =========================
st.subheader("Actual vs Forecast")

future_dates = pd.date_range(
    start=daily_sales.index[-1],
    periods=len(forecast)+1,
    freq='D'
)[1:]

fig, ax = plt.subplots()

ax.plot(daily_sales.index, daily_sales.values, label="Actual")
ax.plot(future_dates, forecast.values, label="Forecast", linestyle="dashed")

ax.axvline(x=daily_sales.index[-1], color='red', linestyle='--')

ax.legend()

st.pyplot(fig)

# =========================
# 📈 SALES TREND
# =========================
st.subheader("Sales Trend")
st.line_chart(daily_sales)

# =========================
# 📉 FORECAST
# =========================
st.subheader("Forecast")

forecast_df = pd.DataFrame({
    "Date": future_dates,
    "Forecast": forecast.values
})

forecast_df.set_index("Date", inplace=True)

st.line_chart(forecast_df)
st.info("Forecast shows expected demand for next 30 days based on historical patterns.")

# =========================
# 📦 INVENTORY
# =========================
inventory = calculate_inventory(selected_product, forecast)

st.subheader("Inventory Recommendation")
st.metric("Safety Stock", inventory["Safety Stock"])
st.metric("Reorder Point", inventory["Reorder Point"])

# =========================
# 📊 MODEL PERFORMANCE
# =========================
# Use test set for accuracy
forecast_test = forecast[:len(test)]

mae, rmse = calculate_accuracy(test, forecast_test)

st.subheader("Model Performance")
st.write(f"MAE: {round(mae,2)}")
st.write(f"RMSE: {round(rmse,2)}")