# Credit Card Delinquency Prediction System

An end-to-end machine learning application that predicts the likelihood of a customer defaulting on credit card payments based on financial and behavioral attributes. The project includes data preprocessing, model training, and an interactive web interface for real-time predictions.

---

## Project Overview

Credit card delinquency is a major risk factor for financial institutions. This project builds a predictive system that estimates delinquency risk using customer data such as income, credit score, payment behavior, and debt ratios.

The goal of the system is to support early identification of high-risk customers and assist in proactive financial decision-making.

---

## Features

- Cleaned and preprocessed financial dataset  
- Logistic Regression classification model  
- Probability-based risk prediction  
- Real-time interactive Streamlit UI  
- Modular and production-style code structure  
- Custom styled dashboard interface  

---

## Tech Stack

- **Python**
- **Pandas & NumPy** – data handling
- **Scikit-learn** – machine learning
- **Joblib** – model persistence
- **Streamlit** – web interface
- **HTML/CSS** – UI styling

---

## Dataset & Exploratory Data Analysis (EDA)

The dataset contains customer-level financial and behavioral attributes, including:

- Age  
- Annual Income  
- Credit Score  
- Credit Utilization  
- Missed Payments  
- Loan Balance  
- Debt-to-Income Ratio  
- Account Tenure  

### EDA Performed

- Checked for missing values  
- Mean imputation for numerical features  
- Mode imputation for categorical features  
- Feature inspection and distribution analysis  
- Pattern observation for delinquency behavior  

### Key Insights

- Higher missed payments strongly increase delinquency risk  
- Lower credit scores correlate with higher default probability  
- High debt-to-income ratio is a strong negative indicator  
- Credit utilization plays a significant role in risk estimation  

---

## Model

The system uses **Logistic Regression**, a widely adopted baseline model in financial risk prediction.

### Why Logistic Regression?

- Interpretable and explainable  
- Suitable for binary classification  
- Industry standard in credit scoring  
- Easy to audit and justify  
- Avoids overfitting on small datasets  

The model outputs a probability score representing the likelihood of delinquency.

---

## System Architecture

The project follows a modular design:


---

## How to Run Locally

1. Install dependencies:

2. Run the application:

3. Enter customer details and receive real-time delinquency prediction.

---

## Output

The system returns a probability score and classifies risk into:

- **Low Risk (0% – 40%)**  
- **Medium Risk (40% – 70%)**  
- **High Risk (70% – 100%)**

---

## Example Use Case

A bank analyst can simulate different customer profiles and instantly observe how financial behavior impacts delinquency probability.

---

## Learning Outcomes

This project demonstrates:

- End-to-end ML pipeline design  
- Real-world data preprocessing  
- Feature engineering  
- Model training and persistence  
- UI integration with ML backend  
- Product-style application development  

---

## Disclaimer

This project uses a synthetic/educational dataset and is intended for academic and learning purposes only. It does not represent real financial advice or production banking systems.

---

## Author

**Niharika Kulkarni**  
Integrated M.Tech Software Engineering  
Machine Learning & Data Science Enthusiast
