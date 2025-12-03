import streamlit as st

#set page title and icon
st.set_page_config(page_title='Coronary Artery Disease Dataset Explorer', page_icon='💓')


st.title('Coronary Artery Disease Dataset Explorer')
st.subheader('Welcome the the Heart dataset explorer app')
st.write("""
    This app provides an interactive platform to explore the famous Heart dataset.
         You can visualize the distribution of data, explore relationships between features, and even make predictions on new data!
""")
st.image('imgs/heart.jpg', caption="The Heart")