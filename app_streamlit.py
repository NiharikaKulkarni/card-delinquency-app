import streamlit as st
from predictor import predict_customer

st.set_page_config(page_title="Card Delinquency Predictor", layout="centered")

# ---------- Custom CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1220, #1e293b);
    color: white;
}

h1 {
    color: white;
    text-align: center;
    font-size: 44px;
    margin-bottom: 0px;
}

h3 {
    text-align: center;
    color: #e5e7eb;
    font-size: 18px;
    margin-top: 5px;
    margin-bottom: 15px;
}

/* Force all labels to white */
label, .stNumberInput label, .stSlider label {
    color: white !important;
    font-size: 15px !important;
}

/* Input card */
.card {
    background: #0f172a;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}

/* Button */
.stButton button {
    width: 100%;
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    color: white;
    font-size: 18px;
    padding: 10px;
    border-radius: 10px;
    margin-left:120%;
}

/* Remove weird streamlit blocks */
[data-testid="stHeader"] { display: none; }
[data-testid="stToolbar"] { display: none; }

.footer {
    text-align: center;
    margin-top: 20px;
    font-size: 12px;
    color: #9ca3af;
}
</style>
""", unsafe_allow_html=True)

# ---------- Smaller Hero Image ----------
st.image("assets/banner.webp", width=800)   # <-- reduced size

# ---------- Headings (no extra box now) ----------
st.markdown("<h1>Credit Card Delinquency Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h3>AI-powered credit risk assessment</h3>", unsafe_allow_html=True)

# ---------- Input Card ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Annual Income", value=500000)
score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
util = st.slider("Credit Utilization", 0.0, 1.0, 0.4)
missed = st.number_input("Missed Payments", min_value=0, max_value=10, value=1)
loan = st.number_input("Loan Balance", value=200000)
dti = st.slider("Debt to Income Ratio", 0.0, 1.0, 0.3)
tenure = st.number_input("Account Tenure (months)", value=24)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Prediction ----------
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

    st.markdown('<div class="card">', unsafe_allow_html=True)
    if risk > 0.7:
        st.error(f"High Risk: {risk_percent}% chance of delinquency")
    elif risk > 0.4:
        st.warning(f"Medium Risk: {risk_percent}% chance of delinquency")
    else:
        st.success(f"Low Risk: {risk_percent}% chance of delinquency")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("""
<div class="footer">
Built by Niharika Kulkarni • ML Credit Risk System
</div>
""", unsafe_allow_html=True)
