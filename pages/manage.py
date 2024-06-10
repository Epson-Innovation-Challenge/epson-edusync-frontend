import streamlit as st

st.set_page_config(
    page_title="EPSON EDUSYNC",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.subheader("Teacher")

class1, clss2, class3 = st.tabs(["1-1", "1-2", "1-3"])

with class1:
    st.subheader("1-1 진도 관리")

    row1 = st.columns(4)
    row2 = st.columns(4)

    for idx, col in enumerate(row1 + row2):
        tile = col.popover(f"학생 {idx+1}", use_container_width=True)
        tile.write("📌")

with clss2:
    st.subheader("1-2 진도 관리")

    row1 = st.columns(4)
    row2 = st.columns(4)

    for idx, col in enumerate(row1 + row2):
        tile = col.popover(f"학생 {idx+1}", use_container_width=True)
        tile.write("📌")

with class3:
    st.subheader("1-3 진도 관리")

    row1 = st.columns(4)
    row2 = st.columns(4)

    for idx, col in enumerate(row1 + row2):
        tile = col.popover(f"학생 {idx+1}", use_container_width=True)
        tile.write("📌")