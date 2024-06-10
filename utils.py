import streamlit as st
import pandas as pd

def load_page_config():
    st.set_page_config(
    page_title="EPSON EDUSYNC",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
    )

    with st.sidebar:
        st.subheader("Teacher")

@st.cache_data
def load_data(data_path):
    df = pd.read_csv(data_path)
    return df