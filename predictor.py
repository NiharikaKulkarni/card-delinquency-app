import joblib
import pandas as pd

model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")
features = joblib.load("models/features.pkl")

def predict_customer(input_dict):
    df = pd.DataFrame([input_dict])
    df = pd.get_dummies(df)
    df = df.reindex(columns=features, fill_value=0)
    df_scaled = scaler.transform(df)
    prob = model.predict_proba(df_scaled)[0][1]
    return prob
if __name__ == "__main__":
    sample = {
        "Age": 30,
        "Income": 500000,
        "Credit_Score": 700,
        "Credit_Utilization": 0.4,
        "Missed_Payments": 1,
        "Loan_Balance": 200000,
        "Debt_to_Income_Ratio": 0.3,
        "Account_Tenure": 24
    }
    print(predict_customer(sample))
