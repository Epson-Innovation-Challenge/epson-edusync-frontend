import streamlit as st
import pandas as pd
from docx import Document

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

def save_to_word(text, filename):
    doc = Document()

    lines = text.split('\n')
    for line in lines:
        doc.add_paragraph(line)
    
    doc.save(filename)