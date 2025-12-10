import streamlit as st

#tabs
st.title('Insights and Conclusion')
tab1, tab2, tab3, tab4 = st.tabs(['Top Factors', 'Machine Learning', 'Precision', 'Recall'])

with tab1:
    st.header('💓 Top Factors')
    st.markdown("""
The most influential important factors in predicting coronary artery disease are:
 - Chest pain
 - Number of vessels colored by fluroscopy
 - Max heart rate
 - Exercise-induced vs resting ST depression
 - Thalassemia blood disorder        
""")
    st.image('imgs/factors_hd.png', caption="Important Factors")
with tab2:
    st.header('🌳 Random Forest Classifier')
    st.write('Using replacement random selection on the dataset\'s 14 predictor features yeilded 99.5 % accuracy and is very reliable in predicting heart disease in patients')
    st.divider()
    st.header('Reduce Noise')
    container = st.container(border=True)
    container.write('Random trees reduce the variance and avoids correlation of the trees giving the classification model a more reliable majority vote')
    st.write('The prediction of x is the average of B predictions:')
    st.latex(r'''
    y = f(x) =
    \frac{1}{B}\ \sum_{b=1}^{B} f_{b}(x)
    ''')
with tab3:
    st.header('🧪 Precision')
    st.write('The model predicted the true positives 100% of the time and is impactful for customer care as unnessessary testing is avoided')
    st.image('imgs/matrix_hd.png', width=500, caption="Confusion Matrix True Positives: 100")
    st.divider()
    st.header('Precision')
    container = st.container(border=True)
    container.write('Precision is the ratio of true positives to the total of true positives and false positives')
    st.latex(r'''
        Precision = \left(\frac{True Positives}{True Positives + False Positives}\right)
    ''')    
with tab4:
    st.header('🔬 Test Sensitivity')
    st.write('The testing sensitivity is clinically safe detecting 97% of all patients with heart disease')
    st.image('imgs/matrix_hd.png', width=500, caption="Confusion Matrix")
    st.divider()
    st.header('Recall')
    container = st.container(border=True)
    container.write('Recall measures the proportion of actual positive cases that were correctly identified by a model or test')
    st.latex(r'''
        Recall = \left(\frac{True Positives}{True Positives + False Negatives}\right)
    ''')    