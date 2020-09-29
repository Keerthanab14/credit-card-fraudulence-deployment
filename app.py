import streamlit as st
import pickle as pickle
import numpy as np
model = pickle.load(open('credit_card.pickle', 'rb'))

st.title("Credit Card Default Prediction")
st.subheader("Please Enter the following details :")
Education_inp = ["Graduate school", "University", "High school", "others"]
Marriage_inp = ["Married", "Single", "Others"]
Pay_status = [
    "Account started that month with a zero balance, and never used any credit",
    "Account had a balance that was paid in full",
    "At least the minimum payment was made, but the entire balance wasn't paid",
    "Payment delay for 1 month",
    "Payment delay for 2 month",
    "Payment delay for 3 month",
    "Payment delay for 4 month",
    "Payment delay for 5 month",
    "Payment delay for 6 month",
    "Payment delay for 7 month",
    "Payment delay for 8 month",
]

limitbal_value = st.number_input('Limitbal')
education = st.selectbox("Education ", ["Graduate school", "University", "High school", "others"])
education_index = Education_inp.index(education) + 1
marriage = st.selectbox("Marriage", ["Married", "Single", "Others"])
marriage_index = Marriage_inp.index(marriage) + 1
age = st.number_input('Age in years')
payment_status = st.selectbox('Payment status', [
    "Account started that month with a zero balance, and never used any credit",
    "Account had a balance that was paid in full",
    "At least the minimum payment was made, but the entire balance wasn't paid",
    "Payment delay for 1 month",
    "Payment delay for 2 month",
    "Payment delay for 3 month",
    "Payment delay for 4 month",
    "Payment delay for 5 month",
    "Payment delay for 6 month",
    "Payment delay for 7 month",
    "Payment delay for 8 month",
]
 )
status = Pay_status.index(payment_status) - 2

st.subheader("Bill Amount for past 6 months")
bill_month1 = st.number_input('Last month Bill amount ')
bill_month2 = st.number_input('Last 2nd month Bill amount ')
bill_month3 = st.number_input('Last 3rd month Bill amount ')
bill_month4 = st.number_input('Last 4th month Bill amount ')
bill_month5 = st.number_input('Last 5th month Bill amount ')
bill_month6 = st.number_input('Last 6th month Bill amount ')

st.subheader("Paid Amount for past 6 months")
paid_month1 = st.number_input('Amount paid in last month (in NT dollar)')
paid_month2 = st.number_input('Amount paid in 2nd month (in NT dollar)')
paid_month3 = st.number_input('Amount paid in 3rd month (in NT dollar)')
paid_month4 = st.number_input('Amount paid in 4th month (in NT dollar)')
paid_month5 = st.number_input('Amount paid in 5th month (in NT dollar)')
paid_month6 = st.number_input('amount paid in 6th month (in NT dollar)')

features = [int(limitbal_value), education_index, marriage_index, int(age), status, int(bill_month1), int(bill_month2), int(bill_month3), int(bill_month4),
            int(bill_month5), int(bill_month6), int(paid_month1), int(paid_month2), int(paid_month3), int(paid_month4), int(paid_month5),
            int(paid_month6)]

if st.button("Predict"):
    predicts = model.predict([features])
    output = round(predicts[0], 2)
    probability = model.predict_proba([features])
    y = probability[0]
    y = max(y)
    z = int(round(y * 100))
    if output == 1:
        st.warning("This account will be defaulted with a probability of {}%.".format(z))
    else:
        st.success("This account will not be defaulted with a probability of {}%.".format(z))
        st.balloons()

st.sidebar.header("     About this App")
st.sidebar.text(
    " This app predicts if the user will \n default in the next month \n based on the previous month \n payment and bill amount details \n or in other words,\n failed to make the minimum payment.")

st.markdown("""
<style>
body {
    color: #111;
    background-color:#AB9F38;
}
.sidebar .sidebar-content {
        background-image:
        background-color:linear-gradient(#474D49,#474D49);
        color: black;
    }
</style>
    """, unsafe_allow_html=True)
