import streamlit as st
import pandas as pd
import pickle
import tensorflow as tf

# Load model & preprocesser
model = tf.keras.models.load_model('model.h5')
with open('preprocesser.pkl', 'rb') as file:
    preprocesser = pickle.load(file)

st.title('Customer Churn Prediction')

# User inputs
geography = st.selectbox('Geography', ['France', 'Germany', 'Spain'])
gender = st.selectbox('Gender', ['Male', 'Female'])
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])

# Prepare raw input DataFrame
input_df = pd.DataFrame({
    'CreditScore': [credit_score],
    'Geography': [geography],
    'Gender': [gender],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

# Apply preprocessing
input_processed = preprocesser.transform(input_df)

# Predict
prediction_proba = model.predict(input_processed)[0][0]

st.write(f'Churn Probability: {prediction_proba:.2f}')
if prediction_proba > 0.5:
    st.error('The customer is likely to churn.')
else:
    st.success('The customer is not likely to churn.')
