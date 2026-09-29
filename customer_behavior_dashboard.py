import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Behavior Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Behavior Prediction Platform")
st.write(
    "Machine Learning Dashboard for Customer Churn, "
    "CLV and Customer Segmentation"
)

customer_data = pd.read_csv("customer_features.csv")

try:
    shap_data = pd.read_csv("shap_feature_importance.csv")
except FileNotFoundError:
    shap_data = None

st.sidebar.header("Dashboard Filters")

segments = customer_data["SegmentName"].dropna().unique()

selected_segment = st.sidebar.selectbox(
    "Select Customer Segment",
    ["All"] + sorted(segments.tolist())
)

if selected_segment != "All":
    filtered_data = customer_data[
        customer_data["SegmentName"] == selected_segment
    ]
else:
    filtered_data = customer_data

st.subheader("📈 Customer Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Customers",
    len(filtered_data)
)

col2.metric(
    "Churned Customers",
    int(filtered_data["Churn"].sum())
)

col3.metric(
    "Average Monetary Value",
    f"{filtered_data['Monetary'].mean():.2f}"
)

col4.metric(
    "Average Recency",
    f"{filtered_data['Recency'].mean():.2f}"
)

st.subheader("👥 Customer Segments")

segment_counts = (
    filtered_data["SegmentName"]
    .value_counts()
    .reset_index()
)

segment_counts.columns = ["Segment", "Customers"]

st.bar_chart(
    segment_counts.set_index("Segment")
)

st.subheader("⚠️ Churn Distribution")

churn_counts = (
    filtered_data["Churn"]
    .value_counts()
    .rename(index={0: "Active", 1: "Churned"})
)

st.bar_chart(churn_counts)

st.subheader("🔍 Churn Feature Importance")

if shap_data is not None:
    st.bar_chart(
        shap_data.set_index("Feature")["Mean_ABS_SHAP"]
    )
else:
    st.info("SHAP data not available.")

st.subheader("📋 Customer Data")

st.dataframe(
    filtered_data,
    use_container_width=True
  )
