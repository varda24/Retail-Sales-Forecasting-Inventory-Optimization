# 📊 Retail Sales Forecasting & Inventory Optimization System

🚀 End-to-end retail analytics system for product-level demand forecasting and inventory optimization using ARIMA and an interactive Streamlit dashboard.

---

## 🚀 Overview

This project simulates a real-world retail system that predicts product demand and optimizes inventory decisions.
It helps businesses avoid overstocking and stockouts by using data-driven forecasting and statistical inventory models.

---

## 💡 Problem Statement

Retail businesses often struggle with:

* Overstock → Increased storage cost
* Stockouts → Lost sales
* Poor demand planning

This system solves these issues by forecasting future demand and recommending optimal inventory levels.

---

## 🧠 Features

* 📈 Product-level sales forecasting using ARIMA
* 📊 Actual vs Forecast visualization
* 📦 Safety Stock calculation
* 🔁 Reorder Point optimization
* 📉 Model performance evaluation (MAE, RMSE)
* 🖥 Interactive dashboard using Streamlit

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Matplotlib
* Statsmodels (ARIMA)
* Streamlit
* Scikit-learn

---

## 📁 Dataset

Synthetic retail dataset generated with trend, seasonality, and noise to simulate real-world sales behavior.

---

## 📂 Project Structure

```
Retail-Sales-Forecasting-Inventory-Optimization/
│
├── data/
│   └── raw/
│       └── retail_data.csv
│
├── src/
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── forecast.py
│   ├── inventory.py
│   ├── metrics.py
│
├── outputs/
│   └── plots/
│
├── images/
│   ├── dashboard.png
│   ├── actual_vs_forecast.png
│   ├── sales_trend.png
│   ├── forecast.png
│   ├── inventory.png
│   ├── model_performance.png
│
├── app.py
├── generate_data.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate dataset

```bash
python generate_data.py
```

### 3. Run dashboard

```bash
streamlit run app.py
```

---

## 🎥 Demo

Run locally using:

```bash
streamlit run app.py
```

---

## 📊 Model Performance

* MAE: ~10 units
* RMSE: ~14 units

The model captures trend and seasonality effectively, enabling stable and reliable inventory planning.

---

## 📸 Screenshots

### Dashboard

![Dashboard](images/dashboard.png)

### Actual vs Forecast

![Forecast](images/actual_vs_forecast.png)

### Sales Trend

![Sales](images/sales_trend.png)

### Forecast

![Forecast Graph](images/forecast.png)

### Inventory Recommendation

![Inventory](images/inventory.png)

### Model Performance

![Performance](images/model_performance.png)

---

## 📈 Business Value

* Reduces stockouts and overstock situations
* Improves demand planning
* Enables data-driven inventory decisions
* Supports efficient supply chain management

---

## 🚀 Future Improvements

* Multi-store forecasting
* Advanced ML models (XGBoost, LSTM)
* Real-time data integration
* Promotion and pricing impact analysis

---

## 👤 Author

**Varda**
B.Tech CSE (AI/ML)
