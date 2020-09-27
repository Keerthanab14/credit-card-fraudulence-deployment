
import streamlit as st
import pickle as pickle
import numpy as np
model = pickle.load(open('C:/Users/kavya/AppData/Local/Programs/Python/Python36/Scripts/Technocolabs-credit_card_fraudulence/credit_card.pickle', 'rb'))

st.title("Credit Card Default Prediction")
st.subheader("Please Enter the following details :")

limitbal = st.number_input('Limitbal')
education = st.selectbox("Education ", ["Graduate school", "University", "High school", "others"])
marriage = st.selectbox("Marriage", ["Married", "Single", "Others"])
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

st.subheader("Bill Amount for past 6 months")
b_month1 = st.number_input('Last month Bill amount (in NT dollar)')
b_month2 = st.number_input('Last 2nd month Bill amount (in NT dollar)')
b_month3 = st.number_input('Last 3rd month Bill amount (in NT dollar)')
b_month4 = st.number_input('Last 4th month Bill amount (in NT dollar)')
b_month5 = st.number_input('Last 5th month Bill amount (in NT dollar)')
b_month6 = st.number_input('Last 6th month Bill amount (in NT dollar)')

st.subheader("Paid Amount for past 6 months")
p_month1 = st.number_input('Amount paid in last month (in NT dollar)')
p_month2 = st.number_input('Amount paid in 2nd month (in NT dollar)')
p_month3 = st.number_input('Amount paid in 3rd month (in NT dollar)')
p_month4 = st.number_input('Amount paid in 4th month (in NT dollar)')
p_month5 = st.number_input('Amount paid in 5th month  (in NT dollar)')
p_month6 = st.number_input('amount paid in 6th month (in NT dollar)')

Education = ["Graduate school", "University", "High school", "others"]
Marriage = ["Married", "Single", "Others"]
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
edu = Education.index(education) + 1
mar = Marriage.index(marriage) + 1
stats = Pay_status.index(payment_status) - 2

features = [int(limitbal), edu, mar, int(age), stats, int(b_month1), int(b_month2), int(b_month3), int(b_month4),
            int(b_month5), int(b_month6), int(p_month1), int(p_month2), int(p_month3), int(p_month4), int(p_month5),
            int(p_month6)]

if st.button("Predict"):
    predicts = model.predict([features])
    x = round(predicts[0], 2)
    prob = model.predict_proba([features])
    y = prob[0]
    y = max(y)
    z = int(round(y * 100))
    if x == 1:
        st.warning("This account will be defaulted with a probability of {}%.".format(z))
    else:
        st.success("This account will not be defaulted with a probability of {}%.".format(z))
        st.balloons()

st.sidebar.header("About Project")
st.sidebar.text(
    " This project is all about predicting \n whether in the next month after the six\n month historical data period,\n an account owner has defaulted, or\n in other words,failed to make the \n minimum payment.\n It takes all the input mentioned\n beside and predicts the output")

st.sidebar.markdown("#### Done by: Bharath C S :smiley:")
st.sidebar.markdown("#### This is part of Technocolab internship miniproject 2")

st.markdown("""
<style>
body {
    color: #111;
    background-color:#DBF3FA;
}
</style>
    """, unsafe_allow_html=True)

st.text('\n')
st.text('\n')
st.text('\n')
st.markdown('### Made with :gift_heart: Streamlit !!')