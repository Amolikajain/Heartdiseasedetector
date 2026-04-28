# import streamlit as st
# import pickle
# import numpy as np

# # Load model & scaler
# model = pickle.load(open('heart_model.pkl', 'rb'))
# scaler = pickle.load(open('scaler.pkl', 'rb'))

# st.set_page_config(page_title="Heart Disease Predictor ❤️", layout="centered")

# st.title("❤️ Heart Disease Prediction")
# st.write("Fill patient details to check risk")

# # Inputs
# age = st.number_input("Age", 1, 120)
# sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")

# cp = st.selectbox("Chest Pain Type (cp)", [0,1,2,3])
# trestbps = st.number_input("Resting Blood Pressure", 80, 200)
# chol = st.number_input("Cholesterol", 100, 600)

# fbs = st.selectbox("Fasting Blood Sugar > 120 (1=True, 0=False)", [0,1])
# restecg = st.selectbox("Rest ECG", [0,1,2])

# thalach = st.number_input("Max Heart Rate Achieved", 60, 220)
# exang = st.selectbox("Exercise Induced Angina", [0,1])

# oldpeak = st.number_input("Oldpeak (ST depression)", 0.0, 10.0)
# slope = st.selectbox("Slope", [0,1,2])

# ca = st.selectbox("Number of Major Vessels (ca)", [0,1,2,3])
# thal = st.selectbox("Thal", [0,1,2,3])

# # Predict
# if st.button("Predict"):

#     input_data = np.array([[
#         age, sex, cp, trestbps, chol, fbs,
#         restecg, thalach, exang, oldpeak,
#         slope, ca, thal
#     ]])

#     input_scaled = scaler.transform(input_data)
#     prediction = model.predict(input_scaled)

#     if prediction[0] == 1:
#         st.error("⚠️ High Risk of Heart Disease")
#     else:
#         st.success("✅ Low Risk of Heart Disease")



import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open('heart_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

st.title("❤️ Heart Disease Risk Predictor")
st.write("Fill patient details to check risk")

# ---------------- INPUTS ---------------- #

age = st.number_input("Age", min_value=1, max_value=120, value=25)

sex = st.selectbox("Sex", ["Male", "Female"])
sex_value = 1 if sex == "Male" else 0

cp = st.selectbox(
    "Chest Pain Type",
    ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"]
)
cp_mapping = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "Asymptomatic": 3
}
cp_value = cp_mapping[cp]

trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)

chol = st.number_input("Cholesterol Level (mg/dl)", 100, 600, 200)

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
fbs_value = 1 if fbs == "Yes" else 0

restecg = st.selectbox(
    "Resting ECG Results",
    ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"]
)
restecg_mapping = {
    "Normal": 0,
    "ST-T Wave Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}
restecg_value = restecg_mapping[restecg]

thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)

exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
exang_value = 1 if exang == "Yes" else 0

oldpeak = st.number_input("ST Depression (Oldpeak)", 0.0, 10.0, 1.0)

slope = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    ["Upsloping", "Flat", "Downsloping"]
)
slope_mapping = {
    "Upsloping": 0,
    "Flat": 1,
    "Downsloping": 2
}
slope_value = slope_mapping[slope]

ca = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])

thal = st.selectbox(
    "Thalassemia",
    ["Normal", "Fixed Defect", "Reversible Defect"]
)
thal_mapping = {
    "Normal": 1,
    "Fixed Defect": 2,
    "Reversible Defect": 3
}
thal_value = thal_mapping[thal]

# ---------------- PREDICTION ---------------- #

if st.button("Predict"):
    input_data = np.array([[
        age, sex_value, cp_value, trestbps, chol,
        fbs_value, restecg_value, thalach,
        exang_value, oldpeak, slope_value,
        ca, thal_value
    ]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    # Output
    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")