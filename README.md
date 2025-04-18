
# 📡 Antenna S11 Predictor (Machine Learning + Streamlit)

This project is a web-based tool that predicts the S11 (return loss) of a rectangular microstrip patch antenna using a tuned **XGBoost** machine learning model trained on HFSS simulation data.

## 🔍 Description
- Input antenna parameters: `feed_x`, `feed_y`, `L_Patch`, `W_Patch`, `Frequency`
- Output: Predicted S11 (dB) using ML
- Built with **Streamlit** and deployed on **Streamlit Cloud**

## 🧠 Machine Learning Model
- Model: XGBoost Regressor (tuned)
- Best Parameters:
  ```
  learning_rate: 0.05
  max_depth: 7
  n_estimators: 300
  subsample: 1.0
  ```
- Test MSE: **1.3618**
- R² Score: **0.8072**

## 🗂️ Files in This Repo
- `app.py` – Streamlit interface for input and prediction
- `xgb_s11_tuned.pkl` – Trained ML model
- `requirements.txt` – Required libraries to run the app

## 🚀 How to Use
1. Open the app on [Streamlit Cloud](https://streamlit.io/cloud)
2. Enter your antenna design parameters
3. Click “Predict S11” and view the result

---

This project is part of an academic research study on machine learning-based optimization of microstrip patch antennas.
