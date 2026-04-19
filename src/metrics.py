from sklearn.metrics import mean_absolute_error
import numpy as np

def calculate_accuracy(actual, forecast):
    mae = mean_absolute_error(actual, forecast)
    rmse = np.sqrt(((actual - forecast) ** 2).mean())
    return mae, rmse