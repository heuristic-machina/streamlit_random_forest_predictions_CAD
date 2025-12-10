import streamlit as st

#container
st.title('Heart Data Dictionary 📖')
st.image('imgs/ecg.png')
container = st.container(border=True)
container.write('1. age: Age of the patient')
container.markdown("""
2. sex: Gender of the patient:
 - 0: Female
 - 1: Male   
""")
container.markdown("""
3. cp: Chest pain type:
 - 0: Typical angina
 - 1: Atypical angina
 - 2: Non-anginal pain
 - 3: Asymptomatic       
""")
container.write('4. trestbps: Resting blood pressure (in mm/Hg)')
container.write('5. chol: Serum cholesterol (in mg/dl)')
container.write('6. trestbps: Resting blood pressure (in mm/Hg)')
container.markdown("""
7. fbs: Fasting blood sugar (> 120 mg/dl) 0:
 - 0: True
 - 1: False   
""")
container.markdown("""
8. restecg: Resting electrocardiographic results:
 - 0: Normal
 - 1: ST-T wave abnormality
 - 2: Left ventricular hypertrophy sign    
""")
container.write('9. thalach: Maximum heart rate achieved')
container.markdown("""
10. exang: Exercise-induced angina:
 - 0: No
 - 1: Yes   
""")
container.write('11. oldpeak: ST depression induced by exercise relative to rest')
container.write('12. slope: The slope of the peak exercise ST segment')
container.write('13. ca: Number of major vessels (0-3) colored by fluoroscopy')
container.markdown("""
14. cp: thal: A blood disorder called Thalassemia:
 - 0: Error
 - 1: Fixed defect
 - 2: Normal
 - 3: Reversible defect       
""")
