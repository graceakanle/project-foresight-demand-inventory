import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Project FORESIGHT Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Dashboard Title
# -----------------------------
st.title("📊 Project FORESIGHT")
st.subheader("Retail Demand Forecasting and Inventory Risk Dashboard")

st.markdown(
    """
    This dashboard presents retail sales performance, demand forecasting results,
    and inventory risk insights to support data-driven inventory decisions.
    """
)

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    kpis = pd.read_csv("foresight_kpis.csv")
    category_sales = pd.read_csv("foresight_category_sales.csv")
    store_sales = pd.read_csv("foresight_store_sales.csv")
    weekly_demand = pd.read_csv("foresight_weekly_demand.csv")
    forecast_results = pd.read_csv("foresight_forecast_results.csv")
    inventory_risk = pd.read_csv("foresight_inventory_risk.csv")
    model_performance = pd.read_csv("foresight_model_performance.csv")

    weekly_demand["Date"] = pd.to_datetime(weekly_demand["Date"])
    forecast_results["Date"] = pd.to_datetime(forecast_results["Date"])

    return (
        kpis,
        category_sales,
        store_sales,
        weekly_demand,
        forecast_results,
        inventory_risk,
        model_performance
    )


try:
    (
        kpis,
        category_sales,
        store_sales,
        weekly_demand,
        forecast_results,
        inventory_risk,
        model_performance
    ) = load_data()

except Exception as error:
    st.error("The dashboard could not load the required data files.")
    st.write("Error:", error)
    st.stop()

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Dashboard Filters")

selected_categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(inventory_risk["Category"].dropna().unique()),
    default=sorted(inventory_risk["Category"].dropna().unique())
)

selected_products = st.sidebar.multiselect(
    "Select Product",
    options=sorted(inventory_risk["Product ID"].dropna().unique()),
    default=sorted(inventory_risk["Product ID"].dropna().unique())
)

filtered_inventory = inventory_risk[
    (inventory_risk["Category"].isin(selected_categories)) &
    (inventory_risk["Product ID"].isin(selected_products))
]

filtered_forecast = forecast_results[
    forecast_results["Product ID"].isin(selected_products)
]

# -----------------------------
# KPI Section
# -----------------------------
st.header("Business Performance Overview")

kpi_values = {}

for _, row in kpis.iterrows():
    metric_name = str(row.iloc[0])
    metric_value = row.iloc[1]
    kpi_values[metric_name] = metric_value

kpi_columns = st.columns(4)

kpi_items = list(kpi_values.items())

for index, (metric_name, metric_value) in enumerate(kpi_items[:4]):
    with kpi_columns[index]:
        st.metric(
            label=metric_name.replace("_", " ").title(),
            value=f"{metric_value:,.2f}" if isinstance(
                metric_value, (int, float)
            ) else metric_value
        )

st.divider()

# -----------------------------
# Sales Analysis
# -----------------------------
st.header("Sales Analysis")

sales_col1, sales_col2 = st.columns(2)

with sales_col1:
    st.subheader("Sales by Category")

    category_chart_data = category_sales.copy()

    if "Category" in category_chart_data.columns:
        category_chart_data = category_chart_data[
            category_chart_data["Category"].isin(selected_categories)
        ]

    category_chart_data = category_chart_data.set_index("Category")

    st.bar_chart(category_chart_data)

with sales_col2:
    st.subheader("Sales by Store")

    store_chart_data = store_sales.copy()

    if "Store ID" in store_chart_data.columns:
        store_chart_data = store_chart_data.set_index("Store ID")

    st.bar_chart(store_chart_data)

st.divider()

# -----------------------------
# Demand Forecasting
# -----------------------------
st.header("Demand Forecasting")

st.write(
    "The chart compares historical weekly demand with the Random Forest "
    "forecasting results."
)

forecast_product = st.selectbox(
    "Choose a product to view demand forecasting results",
    options=sorted(filtered_forecast["Product ID"].dropna().unique())
)

product_forecast = filtered_forecast[
    filtered_forecast["Product ID"] == forecast_product
].sort_values("Date")

if not product_forecast.empty:
    forecast_chart = product_forecast.set_index("Date")[
        ["Weekly_Demand", "Predicted_Demand"]
    ]

    st.line_chart(forecast_chart)

    st.subheader("Forecast Data")

    display_forecast = product_forecast.copy()
    display_forecast["Date"] = display_forecast["Date"].dt.strftime("%Y-%m-%d")

    st.dataframe(
        display_forecast,
        use_container_width=True
    )

# -----------------------------
# Model Performance
# -----------------------------
st.subheader("Model Performance Comparison")

st.dataframe(
    model_performance,
    use_container_width=True
)

st.divider()

# -----------------------------
# Inventory Risk Analysis
# -----------------------------
st.header("Inventory Risk Analysis")

risk_col1, risk_col2 = st.columns(2)

with risk_col1:
    st.subheader("Inventory Risk Distribution")

    risk_counts = (
        filtered_inventory["Risk_Status"]
        .value_counts()
        .rename_axis("Risk_Status")
        .reset_index(name="Product_Count")
    )

    st.bar_chart(
        risk_counts.set_index("Risk_Status")
    )

with risk_col2:
    st.subheader("Recommended Inventory Actions")

    action_counts = (
        filtered_inventory["Recommended_Action"]
        .value_counts()
        .rename_axis("Recommended_Action")
        .reset_index(name="Product_Count")
    )

    st.bar_chart(
        action_counts.set_index("Recommended_Action")
    )

st.subheader("Product Inventory Risk Details")

st.dataframe(
    filtered_inventory,
    use_container_width=True
)

st.divider()

# -----------------------------
# Key Findings
# -----------------------------
st.header("Key Dashboard Insights")

st.markdown(
    """
    - The dashboard summarizes retail sales and inventory performance.
    - Demand forecasting results are presented at product and weekly levels.
    - Inventory risk categories identify products requiring management attention.
    - Recommended actions support stock replenishment and overstock reduction.
    - Filters allow users to examine selected products and categories.
    """
)

st.caption(
    "Project FORESIGHT | Retail Demand Forecasting and Inventory Risk Analysis"
)
