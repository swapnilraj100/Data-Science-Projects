import streamlit as st
import pandas as pd
import pickle

# Load models and feature names
with open("risk_models.pkl", "rb") as file:
    models = pickle.load(file)
with open("feature_names.pkl", "rb") as file:
    feature_names = pickle.load(file)

diagnosis_labels = [col.replace("diagnosis_", "") for col in models.keys()]

st.title("Diagnosis Prediction")
st.write("Enter patient details to predict the most likely diagnosis.")

# Input fields
age = st.number_input("Age", min_value=0, max_value=120, value=50)
lab_test_value = st.number_input("Lab Test Value", min_value=0.0, max_value=20.0, value=5.0)
gender = st.selectbox("Gender", ["M", "F"])
medication = st.multiselect("Medication", ["Insulin", "Aspirin", "Lisinopril", "Tamiflu", "Remdesivir", "Chemotherapy"])

# Convert inputs to match model features
input_data = {
    "age": age,
    "lab_test_value": lab_test_value,
    "gender_M": 1 if gender == "M" else 0,
    "medication_Insulin": 1 if "Insulin" in medication else 0,
    "medication_Aspirin": 1 if "Aspirin" in medication else 0,
    "medication_Lisinopril": 1 if "Lisinopril" in medication else 0,
    "medication_Tamiflu": 1 if "Tamiflu" in medication else 0,
    "medication_Remdesivir": 1 if "Remdesivir" in medication else 0,
    "medication_Chemotherapy": 1 if "Chemotherapy" in medication else 0,
}

# Ensure input matches the trained feature set
input_df = pd.DataFrame([input_data])
input_df = input_df.reindex(columns=feature_names, fill_value=0)  # Reorder and add missing columns

# Predict diagnoses
predictions = {label: models[f"diagnosis_{label}"].predict_proba(input_df)[0][1] for label in diagnosis_labels}

# Get the highest probability diagnosis
most_likely_diagnosis = max(predictions, key=predictions.get)
highest_probability = predictions[most_likely_diagnosis]

# Display result
if st.button("Predict"):
    st.write(f"### Most Likely Diagnosis: {most_likely_diagnosis} ({highest_probability:.2%} likelihood)")
