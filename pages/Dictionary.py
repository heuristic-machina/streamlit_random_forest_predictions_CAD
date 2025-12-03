import streamlit as st

#container
st.title('Heart Data Dictionary 📖')
container = st.container(border=True)
container.write('age: Age of the patient')
container.write('sex: Gender of the patient (0: female, 1: male)')
container.write('cp: Chest pain type (0: typical angina, 1: atypical angina, 2: non-anginal pain, 3: asymptomatic)')
container.write('trestbps: Resting blood pressure (in mm/Hg)')
container.write('chol: Serum cholesterol (in mg/dl)')
container.write('trestbps: Resting blood pressure (in mm/Hg)')
container.write('fbs: Fasting blood sugar (> 120 mg/dl) 0: true, 1: false')
container.write('restecg: Resting electrocardiographic results (0: normal, 1: ST-T wave abnormality, 2: left ventricular hypertrophy sign)')
container.write('thalach: Maximum heart rate achieved')
container.write('exang: Exercise-induced angina (0: no, 1: yes)')
container.write('oldpeak: ST depression induced by exercise relative to rest')
container.write('slope: The slope of the peak exercise ST segment')
container.write('ca: Number of major vessels (0-3) colored by fluoroscopy')
container.write('thal: A blood disorder called Thalassemia (0: error, 1: fixed defect, 2: normal, 3: reversible defect)')
