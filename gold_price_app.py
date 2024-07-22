import numpy as np
import pickle
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

# Loading the saved model
loaded_model = pickle.load(open('gold_price_prediction_model.sav', 'rb'))

# Creating a function for prediction
def gold_price_prediction(input_data):
    # Changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting on one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    return prediction[0]

def main():
    st.image('bg.png')
    # Giving a title
    st.title('Gold Price Prediction Web App')

    # Getting input data from user
    SPX = st.number_input("SPX")
    USO = st.number_input("USO")
    SLV = st.number_input("SLV")
    EUR_USD = st.number_input("EUR/USD")

    # Code for prediction
    price = ''

    # Creating a button for Prediction
    if st.button('Predict Gold Price'):
        price = gold_price_prediction([SPX, USO, SLV, EUR_USD])
        st.success(f'The Predicted Price: {price}$')

    # Displaying images
    st.subheader('Model Statistics:')
    st.image('111.png', caption='Actual Vs Predicted Values 1')
    st.image('112.png', caption='Actual Vs Predicted Values 1')

if __name__ == '__main__':
    main()
