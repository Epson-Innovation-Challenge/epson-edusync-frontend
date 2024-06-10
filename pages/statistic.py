import streamlit as st

st.set_page_config(
    page_title="EPSON EDUSYNC",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

@st._cache_data
def load_dataframe(data_path):
    return None

with st.sidebar:
    st.subheader("Teacher")

class1, class2, class3 = st.tabs(["1-1", "1-2", "1-3"])

with class1:
    st.subheader("1-1 점수 통계")
    container = st.container(border=True, height=600)
    col1, col2 = container.columns([2, 5])
    with col1:
        st.markdown("##### 1학년 1반")
        for idx in range(1, 9):
            student_info = st.container(border=True, height=50)
            student_info.write(f"학생{idx}")

    with col2:
        st.markdown ("##### 점수 통계")
        

with class2:
    st.subheader("1-2 점수 통계")

with class3:
    st.subheader("1-3 점수 통계")