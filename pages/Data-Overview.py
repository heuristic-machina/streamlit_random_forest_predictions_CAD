import streamlit as st
from data_utils import load_heart


st.title('Overview')
#load dataset


df=load_heart()
# Data Overview

st.title("🔢 Data Overview")

st.subheader("About the Data")
st.write("""
        The Heart dataset combines four medical centers: Cleveland Clinic Foundation, Hungarian Institute of Cardiology, University Hospital (Zurich), and V.A. Medical Center (Long Beach).
        It contains 1025 samples of redacted patients exhibiting 14 different features in testing coronary artery disease.
    """)

st.image('imgs/scope.jpg', caption="4 Medical Centers")

    # Dataset Display
st.subheader("Quick Glance at the Data")
if st.checkbox("Show DataFrame"):
        st.dataframe(df)

    # Shape of Dataset
if st.checkbox("Show Shape of Data"):
        st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

