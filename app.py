import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load Models
with open(r'C:\Users\Administrator\Documents\ML\model_lstm.pkl', 'rb') as file:
    model_lstm = pickle.load(file)

with open(r'C:\Users\Administrator\Documents\ML\model_dnn.pkl', 'rb') as file:
    model_dnn = pickle.load(file)

# Streamlit Layout
st.title('Forecasting Crude Oil Prices with LSTM and DNN Models')

# Upload Dataset
uploaded_file = st.file_uploader("Upload your dataset (CSV file):", type=["csv"])
if uploaded_file is not None:
    try:
        # Load dataset
        data = pd.read_csv(uploaded_file)

        # Validate required columns
        required_columns = ['Date', 'Close']
        for col in required_columns:
            if col not in data.columns:
                st.error(f"Column '{col}' is missing in the uploaded file.")
                st.stop()

        # Convert and sort data
        data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
        if data['Date'].isna().any():
            st.error("Invalid date format found in the 'Date' column.")
            st.stop()

        data = data.sort_values('Date')
        data.set_index('Date', inplace=True)

        # Display data
        data_show = st.checkbox("Show Raw Data")
        if data_show:
            st.subheader("Crude Oil Dataset")
            st.dataframe(data)

        # Feature Engineering
        data['MA_10'] = data['Close'].rolling(window=10).mean()
        data['MA_30'] = data['Close'].rolling(window=30).mean()
        data['Daily_Return'] = data['Close'].pct_change()
        data['Rolling_STD'] = data['Close'].rolling(window=10).std()
        data = data.dropna()

        X = data[['MA_10', 'MA_30', 'Daily_Return', 'Rolling_STD']].values
        y = data['Close'].values

        # Scale Features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Reshape for LSTM (3D input: samples, timesteps, features)
        X_scaled_lstm = X_scaled.reshape((X_scaled.shape[0], 1, X_scaled.shape[1]))

        # Keep 2D shape for DNN (samples, features)
        X_scaled_dnn = X_scaled

        # Select Prediction Type
        model_choice = st.selectbox("Choose Model for Prediction:", ("LSTM", "DNN"))

        if st.button("Predict"):
            try:
                if model_choice == "LSTM":
                    # Predict with LSTM
                    y_pred = model_lstm.predict(X_scaled_lstm)
                elif model_choice == "DNN":
                    # Predict with DNN
                    y_pred = model_dnn.predict(X_scaled_dnn)
                else:
                    st.error("Unknown model selected.")
                    st.stop()

                # Calculate metrics
                mae = mean_absolute_error(y, y_pred)
                rmse = np.sqrt(mean_squared_error(y, y_pred))

                # Accuracy calculation
                error_percentage = 100 * (np.abs(y - y_pred.flatten()) / y)
                accuracy = 100 - np.mean(error_percentage)

                # Display results
                st.subheader(f"Model: {model_choice}")
                st.write(f"MAE: {mae:.2f}")
                st.write(f"RMSE: {rmse:.2f}")
                st.write(f"Accuracy: {accuracy:.2f}%")

                # Visualization
                st.subheader("Predictions vs Actual Data")
                plt.figure(figsize=(10, 6))
                plt.plot(data.index, y, label="Actual Prices", linewidth=2)
                plt.plot(data.index, y_pred.flatten(), label="Predicted Prices", linewidth=2, linestyle='--')
                plt.title(f"{model_choice} Predictions vs Actual Prices", fontsize=14)
                plt.xlabel("Date", fontsize=12)
                plt.ylabel("Price", fontsize=12)
                plt.legend(fontsize=10)
                plt.grid(True, linestyle="--", alpha=0.7)
                st.pyplot(plt)

            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
