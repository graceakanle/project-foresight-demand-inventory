# Project FORESIGHT: Retail Demand Forecasting and Inventory Risk Dashboard

## Project Overview

Project FORESIGHT is a data analytics and machine learning project designed to support retail demand forecasting and inventory risk management.

The project analyzes historical retail sales, inventory levels, product information, pricing, promotions, and other business factors to generate useful insights for inventory planning and decision-making.

## Business Problem

Retail businesses may experience stockouts, excess inventory, and inefficient replenishment when demand is not accurately estimated.

Project FORESIGHT addresses this challenge by combining exploratory data analysis, demand forecasting, and inventory risk classification in an interactive dashboard.

## Project Objectives

The objectives of this project are to:

- Analyze retail sales and inventory data.
- Identify sales patterns across products, categories, and stores.
- Develop a machine learning model for weekly demand forecasting.
- Compare model predictions with historical demand.
- Classify products according to inventory risk.
- Provide recommended inventory management actions.
- Present findings through an interactive Streamlit dashboard.

## Dataset Description

The dataset contains retail transaction and inventory-related information, including:

- Date
- Store ID
- Product ID
- Category
- Region
- Inventory Level
- Units Sold
- Units Ordered
- Demand Forecast
- Price
- Discount
- Weather Condition
- Holiday/Promotion
- Competitor Pricing
- Seasonality

The dataset covers multiple stores, products, and retail categories.

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Random Forest Regression
- Google Colab
- GitHub
- Streamlit Community Cloud

## Methodology

### 1. Data Preparation

The data was loaded, inspected, cleaned, and prepared for analysis.

Additional features were created, including:

- Year
- Month
- Week
- Day of the week
- Revenue
- Potential stockout indicator
- Potential overstock indicator

### 2. Exploratory Data Analysis

Sales performance was analyzed by:

- Product category
- Store
- Time period
- Inventory level

Visualizations were created to identify patterns and business insights.

### 3. Demand Forecasting

Weekly demand was calculated for each product.

Lag and rolling-average features were created, including:

- One-week lag
- Two-week lag
- Four-week lag
- Four-week rolling mean
- Week number
- Month

A Random Forest Regression model was trained to estimate weekly product demand.

### 4. Inventory Risk Analysis

Products were classified into inventory risk categories using inventory levels, average demand, lead-time demand, safety stock, and reorder-point calculations.

The risk categories include:

- Stockout Risk
- Overstock Risk
- Healthy Stock

Recommended actions were generated to support inventory decisions.

## Model Performance

The Random Forest model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Weighted Absolute Percentage Error (WAPE)

A four-week lag baseline was also prepared for comparison.

The model performance results are available in:

`foresight_model_performance.csv`

## Dashboard Features

The Streamlit dashboard provides:

- Business performance KPIs
- Sales analysis by category
- Sales analysis by store
- Product-level demand forecasting
- Actual versus predicted demand visualization
- Model performance comparison
- Inventory risk distribution
- Recommended inventory actions
- Product and category filters

## Project Files

| File | Description |
|------|-------------|
| `app.py` | Streamlit dashboard application |
| `requirements.txt` | Required Python libraries |
| `foresight_category_sales.csv` | Category sales summary |
| `foresight_forecast_results.csv` | Actual and predicted demand |
| `foresight_inventory_risk.csv` | Inventory risk assessment |
| `foresight_kpis.csv` | Business performance indicators |
| `foresight_model_performance.csv` | Model evaluation results |
| `foresight_prepared_data.csv` | Prepared analytical dataset |
| `foresight_store_sales.csv` | Store sales summary |
| `foresight_weekly_demand.csv` | Weekly product demand |

## Deployment

The dashboard was developed using Streamlit and deployed through Streamlit Community Cloud.

Live Dashboard:

[View the Live Project FORESIGHT Dashboard](https://project-foresight-demand-inventory-bwa4cxlfsqnfyfvsiply5v.streamlit.app/)

## Limitations

- The analysis is based on the available historical dataset.
- Forecast accuracy may vary across products.
- Inventory risk calculations use defined assumptions for lead time and safety stock.
- The deployed dashboard displays exported forecasting results rather than generating new predictions in real time.

## Future Improvements

Future improvements may include:

- Connecting the dashboard to a live database.
- Adding automated model retraining.
- Testing additional forecasting algorithms.
- Incorporating real-time inventory updates.
- Adding automated alerts for high-risk products.
- Improving forecast accuracy through advanced time-series models.

## Author

**Grace Akanle**

Data Analyst | Academic Research Writer

## Project Theme

Retail Demand Forecasting and Inventory Risk Management
