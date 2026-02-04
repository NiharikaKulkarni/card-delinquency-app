import streamlit as st
from predictor import predict_customer

st.set_page_config(page_title="Card Delinquency Predictor", layout="centered")

st.title("Credit Card Delinquency Prediction System")
st.write("Enter customer details to predict delinquency risk.")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Annual Income", value=500000)
score = st.number_input("Credit Score", value=650)
util = st.slider("Credit Utilization", 0.0, 1.0, 0.4)
missed = st.number_input("Missed Payments", min_value=0, max_value=10, value=1)
loan = st.number_input("Loan Balance", value=200000)
dti = st.slider("Debt to Income Ratio", 0.0, 1.0, 0.3)
tenure = st.number_input("Account Tenure (months)", value=24)

if st.button("Predict Delinquency Risk"):
    data = {
        "Age": age,
        "Income": income,
        "Credit_Score": score,
        "Credit_Utilization": util,
        "Missed_Payments": missed,
        "Loan_Balance": loan,
        "Debt_to_Income_Ratio": dti,
        "Account_Tenure": tenure
    }

    risk = predict_customer(data)
    risk_percent = round(risk * 100, 2)

    if risk > 0.7:
        st.error(f"High Risk: {risk_percent}% chance of delinquency")
    elif risk > 0.4:
        st.warning(f"Medium Risk: {risk_percent}% chance of delinquency")
    else:
        st.success(f"Low Risk: {risk_percent}% chance of delinquency")
