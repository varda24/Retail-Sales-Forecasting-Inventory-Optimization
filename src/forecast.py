from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import numpy as np

def forecast_product_series(series):
    from statsmodels.tsa.arima.model import ARIMA
    import pandas as pd

    series.index = pd.DatetimeIndex(series.index, freq='D')

    model = ARIMA(series, order=(5,1,0))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=30)

    return forecast

import matplotlib.pyplot as plt
import os

def plot_forecast(daily_sales, forecast, product_name):
    os.makedirs("outputs/plots", exist_ok=True)

    plt.figure(figsize=(10,5))

    # Plot actual sales
    plt.plot(daily_sales.index, daily_sales.values, label="Actual Sales")

    # Create future dates
    future_dates = pd.date_range(
        start=daily_sales.index[-1],
        periods=len(forecast)+1,
        freq='D'
    )[1:]

    # Plot forecast
    plt.plot(future_dates, forecast.values, label="Forecast", linestyle='dashed')

    plt.title(f"Forecast vs Actual - {product_name}")
    plt.legend()

    plt.savefig(f"outputs/plots/{product_name}_forecast.png")
    plt.close()


def calculate_accuracy(actual, forecast):
    actual = actual[-len(forecast):]
    mae = np.mean(np.abs(actual - forecast))
    rmse = np.sqrt(((actual - forecast) ** 2).mean())
    
    return mae, rmse