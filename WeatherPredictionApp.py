import streamlit as st
import pandas as pd
import joblib

# Load your trained model and label encoder
model = joblib.load("weather_model.pkl")      # Update filename as needed
le = joblib.load("label_encoder.pkl")         # Update filename as needed

# Streamlit UI
st.title("🌤️ Weather Prediction App")

st.write("Enter the weather conditions below to predict the weather category:")

# Input fields
precip = st.number_input("Precipitation (mm)", min_value=0.0, max_value=100.0, value=0.0)
temp_max = st.number_input("Max Temperature (°C)", min_value=-10.0, max_value=50.0, value=20.0)
temp_min = st.number_input("Min Temperature (°C)", min_value=-20.0, max_value=40.0, value=10.0)
wind = st.number_input("Wind Speed (m/s)", min_value=0.0, max_value=50.0, value=2.0)

# Predict button
if st.button("Predict Weather"):
    # Create input DataFrame
    input_data = pd.DataFrame([[precip, temp_max, temp_min, wind]],
        columns=["precipitation", "temp_max", "temp_min", "wind"])

    # Predict
    prediction = model.predict(input_data)
    predicted_label = le.inverse_transform(prediction)[0]

    # Display result
    st.success(f"🌈 Predicted Weather: **{predicted_label}**")
