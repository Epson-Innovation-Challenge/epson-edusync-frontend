import streamlit as st
from st_pages import show_pages_from_config
from utils import load_page_config

show_pages_from_config()

load_page_config()

class1, clss2, class3 = st.tabs(["1-1", "1-2", "1-3"])

with class1:
    st.title("1-1 학생 정보")

    row1 = st.columns(4)
    row2 = st.columns(4)

    for col in row1 + row2:
        tile = col.container(height=120)
        tile.write("📌")

with clss2:
    st.title("1-2 학생 정보")

    row1 = st.columns(4)
    row2 = st.columns(4)

    for col in row1 + row2:
        tile = col.container(height=120)
        tile.write("📌")

with class3:
    st.title("1-3 학생 정보")

    row1 = st.columns(4)
    row2 = st.columns(4)

    for col in row1 + row2:
        tile = col.container(height=120)
        tile.write("📌")