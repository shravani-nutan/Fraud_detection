import streamlit as st
import pandas as pd
import joblib

model_path = "fraud_detection_pipeline.pkl"

# Check and load the model
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    st.error(f"Model file not found at: {model_path}")
    st.stop()

st.title("Fraud Detection Prediction Model")
st.markdown("Please enter the transaction details and click the Predict button.")
st.divider()

transaction_type = st.selectbox("Transaction type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

if st.button("predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]
    st.subheader(f"Prediction: {int(prediction)}")

    if prediction == 1:
        st.error("This transaction is fraud")
    else:
        st.success("This transaction looks like it is not fraud")
