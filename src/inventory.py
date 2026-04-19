import numpy as np
import pandas as pd

def calculate_inventory(product_name, forecast):
    demand_mean = forecast.mean()
    demand_std = forecast.std()

    lead_time = 7
    service_level = 1.65

    safety_stock = service_level * demand_std * np.sqrt(lead_time)
    reorder_point = (demand_mean * lead_time) + safety_stock

    return {
        "Product": product_name,
        "Safety Stock": round(safety_stock, 2),
        "Reorder Point": round(reorder_point, 2)
    }