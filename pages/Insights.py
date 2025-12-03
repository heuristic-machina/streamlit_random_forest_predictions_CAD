import streamlit as st

#tabs
st.title('Insights and Conclusion')
tab1, tab2, tab3, tab4 = st.tabs(['Machine Learning', 'Precision', 'Recall', 'Top Factors'])

with tab1:
    st.write('🌳 Random Forest is very reliable and accurate with a score of 99.5 % percent accuracy in predicting patients with heart disease given the 14 tested features')
with tab2:
    st.write('🧪 The precision scored perfectly at 100 % and saves the patient from unnecessary stress tests and unneeded costs')
with tab3:
    st.write('🔬 The recall of 97 % detected virtually all patients with heart disease which is insightful as being clinically safe')
with tab4:
    st.write('💓 The most influential/important factors are: chest pain, number of vessels colored by fluroscopy, max heart rate, exercise-induced vs resting ST depression, and the Thalassemia blood disorder')
    
st.image('imgs/insights.jpg', caption="Insights")