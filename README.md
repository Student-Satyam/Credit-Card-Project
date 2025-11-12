💳 Credit Card Default Prediction App

An interactive Streamlit web application that predicts whether a credit card customer will default on their next payment.
This app uses a trained XGBoost model to analyze client details and predict credit default risk.

🚀 Features

🧠 Predicts next-month payment default risk for clients

⚙️ Powered by a trained XGBoost model (xgb_model.pkl)

🧾 Accepts detailed client financial and repayment history

📊 Displays easy-to-read results: ✅ Will Pay or ⚠️ Will Not Pay

🧍‍♂️ Clean and responsive Streamlit interface with 3-column layout

🧠 Model Details

Algorithm: XGBoost (eXtreme Gradient Boosting)

Dataset: UCI Credit Card Default Dataset

Target: default.payment.next.month

Input Features:

Demographics: Age, Gender, Education, Marital Status

Credit Limit (LIMIT_BAL)

Repayment Status (PAY_0 → PAY_6)

Bill Amounts (BILL_AMT1 → BILL_AMT6)

Payment Amounts (PAY_AMT1 → PAY_AMT6)

Model File:

xgb_model.pkl → Trained XGBoost classification model
