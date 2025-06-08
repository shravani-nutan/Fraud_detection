import streamlit as st
import pandas as pd

import joblib
model=joblib.load("fraud_detection_pipeline.pkl")

st.title(" fraud dtetection predection model")

st.markdown("please enter the transaction details and use predict button")

st.divider()

transaction_type = st.selectbox("transaction type",["PAYMENT","TRANSFER","CASH_OUT","DEPOSITE"])
amount = st.number_input("Amount",min_value=0.0,value=1000.0 )
oldbalanceOrg =st.number_input("old balance(Sender)",min_value=0.0,value=10000.0)
newbalanceOrig =  st.number_input("new balance(sender)",min_value=0.0,value=9000.0)
oldbalanceDest  =st.number_input("old balance(receiver)",min_value=0.0,value=0.0)
newbalanceDest =  st.number_input("new balance(receiver)",min_value=0.0,value=0.0)

if st.button("predict"):
    input_data=pd.DataFrame([{
        "type": transaction_type,
        "amount" : amount,
        "oldbalanceOrg":oldbalanceOrg,
        "newbalanceOrig ":newbalanceOrig ,
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest":newbalanceDest

    }])
prediction = model.predict(input_data)[0]

st.subheader("prediction:'{int(prediction)}'")

if prediction == 1:
    st.error("this transaction is fraud")
else :
    st.success("this transaction looks like it is not fraud")
