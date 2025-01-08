import streamlit as st
import numpy as np
from tensorflow import keras
import pickle

# Load the pre-trained model and scaler
model = keras.models.load_model('crop_recommendation_model.keras')
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Load label encoder
with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Title and instructions
st.title("GreenPath")
st.write("Masukkan parameter lingkungan untuk mendapatkan rekomendasi tanaman yang cocok.")

# Input fields
nitrogen = st.number_input("Masukkan Kandungan Nitrogen (ppm)", format="%.2f")
phosphorus = st.number_input("Masukkan Kandungan Fosfor (ppm)", format="%.2f")
potassium = st.number_input("Masukkan Kandungan Kalium (ppm)", format="%.2f")
temperature = st.number_input("Masukkan Suhu (°C)", format="%.2f")
humidity = st.number_input("Masukkan Kelembapan (%)", format="%.2f")
ph = st.number_input("Masukkan pH Tanah", format="%.2f")
rainfall = st.number_input("Masukkan Curah Hujan (mm)", format="%.2f")

# Button to predict
if st.button("Prediksi"):
    # Prepare input for the model
    input_data = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]]) 
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)
    predicted_crop = label_encoder.inverse_transform([np.argmax(prediction)])[0]

    # Prepare image URL for the predicted crop
    image_url = f'static/images/{predicted_crop}.jpg'

    # Display results
    st.success(f"Tanaman yang disarankan: {predicted_crop}")
    print(f"Image URL: {image_url}")
    st.image(image_url, caption=predicted_crop)


# Run the app using `streamlit run <filename>.py`
