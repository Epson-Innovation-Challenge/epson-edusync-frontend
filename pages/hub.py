import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EPSON EDUSYNC",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.subheader("Teacher")

df = pd.read_csv("student_scores_with_progress.csv")

st.data_editor(
    df,
    column_config={
        "Progress" : st.column_config.ProgressColumn(
            "Total Progress",
            help="Total progress of the student",
            format="%f",
            min_value=0,
            max_value=100,
        ),
    },
    hide_index=True,
)