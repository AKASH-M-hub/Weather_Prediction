# 🌦️ Weather Prediction App

A machine learning-based web application built using **Streamlit** that predicts weather conditions like **Rain, Clear, Cloudy**, etc., based on environmental input features such as temperature, humidity, wind speed, and more.

## 🚀 Features

- Predicts real-time weather condition labels (e.g., Rain, Clear, Fog)
- Trained using robust ML models like **Random Forest** and **XGBoost**
- Deployed via **Streamlit** for an interactive UI
- Fast model loading using `joblib`
- Easy to use interface — just input values and get predictions instantly!

## 🧠 ML Models Used

- Random Forest Classifier 🌲
- XGBoost Classifier ⚡

## 📁 Project Structure
```
weather_prediction/
├── weather_app.py # Streamlit app file
├── label_encoder.pkl # Fitted Label Encoder for target transformation
├── weather_model.pkl # Trained ML model (Random Forest / XGBoost)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── data/
└── weather.csv # Dataset used for training
```
