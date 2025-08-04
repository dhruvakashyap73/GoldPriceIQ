<p align="center">
  <img src="https://github.com/dhruvakashyap73/GoldPriceIQ/blob/main/Photos/Logo-GPP.png" alt="Logo" width="250" height="250">
</p>

<h5 align="center"><strong>A Cloud based approch</strong></h5>

## Project Overview
GoldPriceIQ (Intelligence Quotient) is an end-to-end machine learning solution developed to predict future gold prices using historical market data and key economic indicators. The project employs a Random Forest Regressor model trained on enriched feature sets derived from reliable sources, including the World Gold Council. The final model is deployed through a Streamlit-based web application that allows users to input indicator values and receive real-time gold price predictions.

The application emphasizes both prediction accuracy and usability. It provides model performance metrics and visual explanations, enabling users to understand not just what the prediction is, but also why the model made it. The solution is deployed on Streamlit Community Cloud and maintained via GitHub for reproducibility and collaboration.

## Key Features
- Built using historical gold price data sourced from the World Gold Council.
- Includes predictive features such as SPX (S&P 500 Index), USO (oil prices), SLV (silver prices), EUR/USD exchange rate, and short-term moving averages.
- Trained and evaluated multiple regression models: Linear Regression, Decision Tree Regressor, and Random Forest Regressor.
- Final application uses Random Forest Regressor based on superior accuracy and robustness.
- Provides prediction results along with evaluation metrics including Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² Score.
- User interface designed in Streamlit, allowing interactive input and instant predictions.
- Deployed via Streamlit Community Cloud for easy public access and demonstration.

## Technologies Used
- **Language:** Python
- **Machine Learning & Data Processing:** scikit-learn, pandas, numpy
- **Visualization:** matplotlib, seaborn
- **Web App Framework:** Streamlit
- **Model Deployment:** joblib (for saving/loading models), pyngrok (used for local tunneling during development)
- **Development Tools:** Jupyter Notebook (for model training and experimentation), Visual Studio Code (for app development)
- **Deployment Platform:** Streamlit Community Cloud
- **Version Control:** GitHub


