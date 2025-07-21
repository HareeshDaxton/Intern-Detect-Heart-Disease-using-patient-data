# 🫀 Heart Disease Prediction App

This project is a **Machine Learning-powered diagnostic tool** that predicts the likelihood of a patient having heart disease based on clinical data. It integrates rigorous data processing, EDA, feature engineering, and a Random Forest classifier into a real-time, interactive Streamlit web interface.

---

## 🚀 Features

- ✅ Real-time heart disease prediction
- 📊 Uses clinical indicators such as chest pain, ECG results, and cholesterol/BP ratio
- 🌲 Trained using Random Forest classifier for high interpretability and robustness
- 🧪 EDA and feature engineering built from scratch in Jupyter notebooks
- 🧠 Scalable architecture for additional features or improved models
- 🔐 Model and scaler artifacts are saved for reproducibility

---

## 🧪 Tech Stack

- **Programming Language:** Python 3.11 🐍  
- **ML Frameworks:** Scikit-learn, Joblib  
- **Data Handling:** Pandas, NumPy  
- **Web Framework:** Streamlit  
- **Model Used:** RandomForestClassifier  
- **Visualizations & Analysis:** Matplotlib, Seaborn (in EDA)

---

## 📂 Project Structure

```
├── app.py                 # Streamlit app to serve the model
├── main.ipynb             # Model training, validation, and artifact generation
├── EDA_FE.ipynb           # Exploratory Data Analysis and Feature Engineering
├── cleaned_data.csv       # Cleaned and processed dataset
├── int_ht.csv             # Raw dataset
├── rf_model.pkl           # Trained Random Forest model (joblib format)
├── rf_scl.pkl             # Fitted StandardScaler for input transformation
```

---

## 🔍 Workflow Summary

1. **Data Cleaning**: Raw clinical records cleaned and exported to `cleaned_data.csv`.
2. **EDA & Feature Engineering**:
   - Correlation checks
   - Outlier detection
   - Feature synthesis: e.g., `age * max_heart_rate`, `cholesterol / BP`
3. **Modeling**:
   - Features scaled using `StandardScaler`
   - Model trained using `RandomForestClassifier` with balanced classes
   - Model and scaler saved as `.pkl` files
4. **App Interface**:
   - Clinical inputs collected through Streamlit form
   - Input transformed using fitted scaler
   - Model predicts and returns probability of heart disease

---

## 💡 Key Highlights

- **Domain-specific features** such as `age × max HR` and `cholesterol / BP` ratios were engineered based on cardiovascular medical literature.
- **Interactive UI** facilitates real-time predictions without code.
- **Balanced risk messaging** via probability outputs and conditional formatting.

---

## 📈 Example Clinical Features Used

- Sex (Binary)
- Chest Pain Type (1–4)
- Fasting Blood Sugar
- Resting ECG Result
- Exercise-Induced Angina
- Oldpeak (ST Depression)
- ST Slope
- Cholesterol / BP Ratio
- Age × Max Heart Rate

---

## 📜 License

This project is licensed under the MIT License.
