# Customer Behavior Prediction Platform

A machine learning based platform for analyzing customer behavior, predicting customer churn, estimating future customer value, and segmenting customers.

## Project Overview

This project analyzes historical retail transaction data and uses machine learning techniques to understand customer behavior.

The system provides:

- Customer churn analysis
- Customer value prediction
- Customer segmentation
- Feature importance using SHAP
- Interactive Streamlit dashboard

## Objectives

The main objectives of this project are:

1. Analyze historical customer transactions.
2. Create customer-level behavioral features.
3. Predict customer churn risk.
4. Estimate future 90-day customer revenue as a CLV proxy.
5. Segment customers based on purchasing behavior.
6. Provide an interactive dashboard for analysis.

## Dataset

The project uses the UCI Online Retail II dataset.

Dataset source:

https://archive.ics.uci.edu/dataset/502/online+retail+ii

The dataset contains retail transactions including:

- Invoice
- StockCode
- Description
- Quantity
- InvoiceDate
- Price
- Customer ID
- Country

## Data Preprocessing

The following preprocessing steps were performed:

- Removed records without Customer ID.
- Removed transactions with non-positive quantity.
- Removed transactions with non-positive price.
- Removed duplicate records.
- Converted dates and numerical columns to appropriate data types.
- Calculated total transaction amount.

## Feature Engineering

Customer-level features include:

- Recency
- Frequency
- Monetary value
- Average basket size
- Purchase frequency trend
- Average days between purchases
- Active months
- Unique products
- Engagement score

## Churn Prediction

Customer churn was defined using a 90-day future observation period.

Several machine learning models were compared, including:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- LightGBM
- KNN
- SVM
- Artificial Neural Network

The project uses validation and test datasets to evaluate model performance.

## Customer Segmentation

K-Means clustering was used to group customers according to their purchasing behavior.

The resulting segments are:

- Regular Customers
- At-Risk Customers
- Loyal Customers
- High-Value Customers

## Explainable AI

SHAP was used to analyze feature importance for the churn prediction model.

This helps identify which customer behavioral features have the greatest influence on model predictions.

## Streamlit Dashboard

The project includes an interactive Streamlit dashboard that provides:

- Customer overview
- Customer segment distribution
- Churn distribution
- SHAP feature importance
- Customer-level data
- Segment filtering

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- TensorFlow
- SHAP
- Streamlit

## Project Structure

```text
customer-behavior-prediction-platform/
│
├── customer_behavior_dashboard.py
├── customer_features.csv
├── shap_feature_importance.csv
├── final_churn_model_comparison.csv
├── final_test_results.csv
├── requirements.txt
├── README.md
└── LICENSE
