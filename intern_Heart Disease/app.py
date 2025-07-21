import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('rf_model.pkl')
scl = joblib.load('rf_scl.pkl')

st.title("Detect Heart Disease Using Patient Data")

st.write("""
This ML app predicts whether a patient is likely to have heart disease based on clinical input features.
""")

sex = st.selectbox("Sex", ['Female', 'Male'])
cp_typ = st.selectbox('Chest Pain Type (1-4)', [1,2,3,4])
fbs = st.number_input("Fasting Blood Sugar (mg/dL), '1 = sugar > 120mg/dL, 0 = sugar < 120mg/' ", min_value=0.0, step=.01)
rest_ecg = st.number_input("Resting ECG Result, ' 0 = normal,1 = ST-T wave abnormality,2 = Probable or Definite Left Ventricular hypertrophy ' ", min_value=0.0, max_value=2.0, step=0.1)
ex_agina = st.selectbox("Exercise Induced Angina", ['No', 'Yes'])
oldpeak = st.number_input("Oldpeak (ST depression) '0.0 = normal, 1.0 = Mild , >=2.0 = risk zone' ", min_value=0.0, step=0.1)
st_slop = st.number_input("ST Slope (0 = Upsloping/normal, 1 = Flat/risk, 2 = Downsloping/high risk)' " ,min_value=0.0, max_value=2.0, step=0.1 )
chol_bp = st.number_input("Cholesterol / BP Ratio, '<1.3 = Possibly underweight or very low cholesterol, 1.3-1.6 = normal, 1.6-2.0 = mild risk, >2.0 = High cardiovascular risk",min_value=0.0, step=0.1 )
age_hr = st.number_input("Age * Max Heart Rate '<3000 = Very low, 3000 - 6000 = avg risk, 6000 - 9000 = with higher HR", min_value=0.0,)

if st.button('Malke Prediction 🫀'):
    input_data = {
        'sex' : 1 if sex== 'Male' else 0,
        'chest pain type' : cp_typ,
        'fasting blood sugar' : i if fbs > 120 else 0, 
        'resting ecg' : rest_ecg,
        'exercise angina' : 1 if ex_agina =='Yes' else 0,
        'oldpeak' : oldpeak,
        'ST slope': st_slop,
        'cholesterol_bp': chol_bp,
        'age_max_hr': age_hr
    }
    
    inp_df = pd.DataFrame([input_data])
    scl_inp = scl.transform(inp_df)
    pred = model.predict(scl_inp)
    prob = model.predict_proba(scl_inp)
    
    
    st.subheader("Prediction Result")
    if pred[0] == 1:
         st.error("⚠️ The patient is likely to have **Heart Disease**.")
         st.write('Prediction Probabilities:')
         st.write(f"Heart Disease: {prob[0][1]:.2f}")
         
    else:
         st.success("✅ The patient is likely **Normal** (No Heart Disease).")
         st.write('Prediction Probabilities:')
         st.write(f"No Heart Disease: {prob[0][0]:.2f}")
         
    