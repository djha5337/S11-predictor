
# 📡 Antenna S11 Predictor (Machine Learning + Streamlit)

🔗 **Live App**: [Click here to open the S11 Predictor](https://s11-predictor-hm5hzjpeiwjjqhkhu8ajl5.streamlit.app/)

This project is a web-based tool that predicts the S11 (return loss) of a rectangular microstrip patch antenna using a tuned **XGBoost** machine learning model trained on HFSS simulation data.

---

## 🔍 Description
- **Input parameters**:  
  `feed_x`, `feed_y`, `L_Patch`, `W_Patch`, `Frequency`
- **Output**: Predicted S11 (in dB)
- Developed using **Python + Streamlit**  
- Deployed via **Streamlit Cloud**

---

## 🧠 Machine Learning Model
- **Model**: XGBoost Regressor (hyperparameter tuned)
- **Best Parameters**:
- **Performance:**
- Mean Squared Error (MSE): **1.3618**
- R² Score: **0.8072**

---

## 🗂️ Files in This Repo
| File Name            | Purpose                                 |
|----------------------|------------------------------------------|
| `app.py`             | Streamlit interface for input + prediction |
| `xgb_s11_tuned.pkl`  | Trained ML model                         |
| `requirements.txt`   | Python libraries to run the app          |

---

## 🚀 How to Use
1. Open the app on [Streamlit Cloud](https://streamlit.io/cloud)
2. Enter your antenna design parameters
3. Click **“Predict S11”** to get the result

---

## 📘 Citation

This tool is developed as part of an academic research project focused on the machine learning-based design and optimization of microstrip patch antennas.

If you use this tool or reference it in your work, please cite:

> Durgesh kumar Jha, “S11 Predictor – ML-Based Antenna Design Tool”, GitHub, 2025.  
> [Online]. Available: https://github.com/djha5337/s11-predictor

You may also include the tool link in your paper to support reproducibility:

> *“A live web-based prototype for real-time S11 prediction is available at: https://s11-predictor-hm5hzjpeiwjjqhkhu8ajl5.streamlit.app/”*

---

## 💡 Note

This tool performs best for antenna configurations where S11 values are in the range of –10 dB or lower. For higher return loss values (e.g., –15 dB or –20 dB), prediction accuracy may slightly decrease. This limitation is discussed in the associated journal manuscript.

---

## 👨‍🎓 Academic Use

This project is intended to support:
- Research scholars and engineers working in antenna design
- Educational demonstration of applied machine learning in RF engineering
- Reproducibility in microstrip patch antenna optimization
