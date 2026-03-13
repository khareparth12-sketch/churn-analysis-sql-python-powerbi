import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Customer Churn Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction & Analytics Dashboard")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/telco_final_processed.csv")
    return df

df = load_data()

# -----------------------------
# KPI METRICS
# -----------------------------

total_customers = df.shape[0]
churn_rate = df["Churn"].mean() * 100
avg_monthly = df["MonthlyCharges"].mean()
avg_tenure = df["tenure"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", total_customers)
col2.metric("Churn Rate", f"{churn_rate:.2f}%")
col3.metric("Avg Monthly Charges", f"${avg_monthly:.2f}")
col4.metric("Avg Tenure", f"{avg_tenure:.1f} months")

st.divider()

# -----------------------------
# CHURN ANALYSIS CHARTS
# -----------------------------

st.subheader("Churn Analysis")

col1, col2 = st.columns(2)

with col1:
    churn_counts = df["Churn"].value_counts()
    fig = px.pie(
        values=churn_counts.values,
        names=["No Churn", "Churn"],
        title="Customer Churn Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.box(
        df,
        x="Churn",
        y="tenure",
        title="Tenure vs Churn"
    )
    st.plotly_chart(fig, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    fig = px.box(
        df,
        x="Churn",
        y="MonthlyCharges",
        title="Monthly Charges vs Churn"
    )
    st.plotly_chart(fig, use_container_width=True)

with col4:
    fig = px.histogram(
        df,
        x="Contract",
        color="Churn",
        title="Contract Type vs Churn"
    )
    st.plotly_chart(fig, use_container_width=True)