import streamlit as st
from utils import load_page_config, load_data

if __name__ == "__main__":
    load_page_config()
    df = load_data("example.csv")

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