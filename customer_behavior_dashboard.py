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

st.subheader("🤖 Churn Model Performance")

model_data = pd.read_csv("final_churn_model_comparison.csv")
st.dataframe(model_data, use_container_width=True)

st.subheader("🧪 Final Test Results")

test_data = pd.read_csv("final_test_results.csv")
st.dataframe(test_data, use_container_width=True)

st.dataframe(test_data, use_container_width=True)
