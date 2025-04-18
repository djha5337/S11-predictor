import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("xgb_s11_tuned.pkl")

# Streamlit UI
st.set_page_config(page_title="Antenna S11 Predictor", page_icon="📡")
st.title("📡 Antenna S11 Prediction using ML")
st.markdown("Enter antenna parameters to predict **S11 (dB)** at your desired frequency.")

# Input fields
feed_x = st.number_input("Feed X [mm]", min_value=0.0, max_value=50.0, value=4.5, step=0.1)
feed_y = st.number_input("Feed Y [mm]", min_value=0.0, max_value=50.0, value=30.0, step=0.1)
L_patch = st.number_input("Patch Length [mm]", min_value=10.0, max_value=50.0, value=28.5, step=0.1)
W_patch = st.number_input("Patch Width [mm]", min_value=10.0, max_value=50.0, value=37.0, step=0.1)
freq = st.number_input("Operating Frequency [GHz]", min_value=1.0, max_value=5.0, value=2.5, step=0.01)

# Predict button
if st.button("Predict S11"):
    input_df = pd.DataFrame([[feed_x, feed_y, L_patch, W_patch, freq]],
                            columns=['feed_x_mm', 'feed_y_mm', 'L_Patch_mm', 'W_Patch_mm', 'Freq_GHz'])
    s11_pred = model.predict(input_df)[0]
    st.success(f"📉 Predicted S11 at {freq:.2f} GHz: **{s11_pred:.2f} dB**")
