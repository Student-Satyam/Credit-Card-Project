import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("xgb_model.pkl")

st.set_page_config(page_title="Credit Default Prediction", layout="wide")
st.title("💳 Credit Card Default Prediction App")

st.write("Fill in the client details below to predict whether they will pay next month.")

# --- Input fields ---
col1, col2, col3 = st.columns(3)

with col1:
    LIMIT_BAL = st.number_input("Credit Limit (NT$)", min_value=1000, step=1000)
    SEX = st.selectbox("Gender", [1, 2], format_func=lambda x: "Male" if x == 1 else "Female")
    EDUCATION = st.selectbox("Education", [1, 2, 3, 4], format_func=lambda x: {1:"Graduate", 2:"University", 3:"High School", 4:"Others"}[x])
    MARRIAGE = st.selectbox("Marriage", [1, 2, 3], format_func=lambda x: {1:"Married", 2:"Single", 3:"Others"}[x])
    AGE = st.number_input("Age", min_value=18, max_value=100)

with col2:
    PAY_0 = st.selectbox("Repayment Status (Sep)", list(range(-2, 10)))
    PAY_2 = st.selectbox("Repayment Status (Aug)", list(range(-2, 10)))
    PAY_3 = st.selectbox("Repayment Status (Jul)", list(range(-2, 10)))
    PAY_4 = st.selectbox("Repayment Status (Jun)", list(range(-2, 10)))
    PAY_5 = st.selectbox("Repayment Status (May)", list(range(-2, 10)))
    PAY_6 = st.selectbox("Repayment Status (Apr)", list(range(-2, 10)))

with col3:
    BILL_AMT1 = st.number_input("Bill Amount (Sep)", value=0)
    BILL_AMT2 = st.number_input("Bill Amount (Aug)", value=0)
    BILL_AMT3 = st.number_input("Bill Amount (Jul)", value=0)
    BILL_AMT4 = st.number_input("Bill Amount (Jun)", value=0)
    BILL_AMT5 = st.number_input("Bill Amount (May)", value=0)
    BILL_AMT6 = st.number_input("Bill Amount (Apr)", value=0)

PAY_AMT1 = st.number_input("Payment Amount (Sep)", value=0)
PAY_AMT2 = st.number_input("Payment Amount (Aug)", value=0)
PAY_AMT3 = st.number_input("Payment Amount (Jul)", value=0)
PAY_AMT4 = st.number_input("Payment Amount (Jun)", value=0)
PAY_AMT5 = st.number_input("Payment Amount (May)", value=0)
PAY_AMT6 = st.number_input("Payment Amount (Apr)", value=0)

# --- Prediction button ---
if st.button("🔮 Predict"):
    # Create dataframe from inputs
    input_data = pd.DataFrame([[LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE,
                                PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
                                BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6,
                                PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6]],
                              columns=['LIMIT_BAL','SEX','EDUCATION','MARRIAGE','AGE',
                                       'PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6',
                                       'BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6',
                                       'PAY_AMT1','PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6'])

    # Make prediction
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Customer will NOT pay next month (default).")
    else:
        st.success("✅ Customer WILL pay next month.")
