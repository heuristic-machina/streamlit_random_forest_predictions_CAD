import pandas as pd
import streamlit as st

DATA_PATH = "data/heart.csv"

@st.cache_data
def load_heart():
    """Load the Heart dataset from local file, cached by Streamlit."""
    return pd.read_csv(DATA_PATH)