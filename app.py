import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime

# =====================
# LOAD MODEL
# =====================
model = joblib.load("./model/churn_model.pkl")

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

st.title("📉 Customer Churn Prediction")
st.write("Predict whether a customer is likely to churn")

# =====================
# BUSINESS CONTROLS
# =====================
st.sidebar.header("⚙️ Business Settings")
THRESHOLD = st.sidebar.slider(
    "Churn Risk Threshold",
    min_value=0.10,
    max_value=0.90,
    value=0.35,
    step=0.05
)

# =====================
# USER INPUTS
# =====================
tenure = st.number_input("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0, 800.0)

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

streaming_tv = st.selectbox("Streaming TV", ["Yes", "No"])
streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No"])
online_security = st.selectbox("Online Security", ["Yes", "No"])

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

# =====================
# INPUT DATAFRAME
# =====================
input_df = pd.DataFrame([{
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
    "Contract": contract,
    "InternetService": internet_service,
    "StreamingTV": streaming_tv,
    "StreamingMovies": streaming_movies,
    "OnlineSecurity": online_security,
    "PaymentMethod": payment_method,

    # hidden defaults
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "No",
    "Dependents": "No",
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "PaperlessBilling": "Yes"
}])

# =====================
# LOGGING FUNCTION
# =====================
def log_prediction(input_data, prob, risk):
    os.makedirs("logs", exist_ok=True)

    log_data = input_data.copy()
    log_data["churn_probability"] = prob
    log_data["risk_level"] = risk
    log_data["timestamp"] = datetime.now()

    log_file = os.path.join("logs", "predictions.csv")

    if os.path.exists(log_file):
        log_data.to_csv(log_file, mode="a", header=False, index=False)
    else:
        log_data.to_csv(log_file, index=False)


if st.button("Predict Churn"):
    prob = model.predict_proba(input_df)[0][1]

    st.subheader(f"🔢 Churn Probability: **{prob:.2%}**")
    st.progress(min(int(prob * 100), 100))

    if prob >= 0.6:
        risk = "Very High"
        st.error("🔴 Very High Risk — Immediate retention required")
    elif prob >= THRESHOLD:
        risk = "Medium"
        st.warning("🟠 Medium Risk — Monitor & engage customer")
    else:
        risk = "Low"
        st.success("🟢 Low Risk — Customer likely to stay")

    # log prediction
    log_prediction(input_df, prob, risk)

    st.caption("📁 Prediction logged successfully")

