import numpy as np
import pickle
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import io
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

# Loading the saved model
try:
    loaded_model = pickle.load(open('gold_price_prediction_model.sav', 'rb'))
except Exception as e:
    st.error(f"Error loading model: {e}")

# Creating a function for prediction
def gold_price_prediction(input_data):
    try:
        # Changing the input data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # Reshape the array as we are predicting on one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        # Predicting the gold price
        prediction = loaded_model.predict(input_data_reshaped)
        return prediction[0]
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None

def load_image(image_path):
    try:
        with open(image_path, "rb") as file:
            image_data = file.read()
            if not image_data:
                st.error(f"Image file {image_path} is empty.")
                return None
            return Image.open(io.BytesIO(image_data))
    except Exception as e:
        st.error(f"Error loading image {image_path}: {e}")
        return None

def main():
    # Loading and displaying the background image
    bg_image = load_image('bg.png')
    if bg_image:
        st.image(bg_image)

    # Giving a title
    st.title('Gold Price Prediction')

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
        if price is not None:
            price= price/2.1
            st.success(f'The Predicted Gold Price per gram : {price}$')

    # Displaying images
    st.subheader('Model Statistics:')
    for img_path, caption in [('111.png', 'Actual Vs Predicted Values 1'), ('112.png', 'Actual Vs Predicted Values 2')]:
        img = load_image(img_path)
        if img:
            st.image(img, caption=caption)

if __name__ == '__main__':
    main()
