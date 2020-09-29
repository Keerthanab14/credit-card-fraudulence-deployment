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


edu = Education_inp.index(education) + 1
mar = Marriage_inp.index(marriage) + 1
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
        st.warning("This account might be defaulted with a probability of {}%.".format(z))
    else:
        st.success("This account might not be defaulted with a probability of {}%.".format(z))
        st.balloons()

st.sidebar.header("About this Project")
st.sidebar.text(
    " This project is about predicting \n whether in the next month after the six\n month historical data period,\n an account owner has defaulted, or\n in other words,failed to make the \n minimum payment.\n It takes all the input mentioned\n beside and predicts the output")

st.markdown("""
<style>
body {
    color: #111;
    background-image: url("https://www.google.com/imgres?imgurl=https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F5e7df71b08eb080006520247%2F960x0.jpg%3Ffit%3Dscale&imgrefurl=https%3A%2F%2Fwww.forbes.com%2Fsites%2Fleemathews%2F2020%2F03%2F27%2Fa-massive-credit-card-fraud-ring-just-got-shut-down-by-russian-authorities%2F&tbnid=Ya7qrCNmQt3ruM&vet=12ahUKEwj6xd2Iwo3sAhWaeH0KHV25ClUQMygKegUIARCzAQ..i&docid=sHA6cA4QKCGtMM&w=960&h=488&q=credit%20card%20fraud&ved=2ahUKEwj6xd2Iwo3sAhWaeH0KHV25ClUQMygKegUIARCzAQ#imgrc=Ya7qrCNmQt3ruM&imgdii=t9SLR7tDyW9PvM");
    background-size: cover;
    .sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
    }
    background-opacity: 0.5;
}
</style>
    """, unsafe_allow_html=True)
