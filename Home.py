import streamlit as st

#set page title and icon
st.set_page_config(page_title='Coronary Artery Disease Dataset Explorer', page_icon='💓')


st.title('Coronary Artery Disease Dataset Explorer')
st.subheader('Welcome to the Heart dataset explorer app')
st.write("""
    This app provides an interactive platform to explore the famous Heart dataset.
         You can visualize the distribution of data in Data-Overview and Dictionary pages, explore relationships between features on Exploratory-Analysis page, and even make your own confusion matrix model on Make-Your-Own-Matrix page!  When your done playing around check out the Prediction-Insights for results performed on this dataset using Random Forest Classifier.
""")
st.image('imgs/heart.jpg', caption="The Heart")