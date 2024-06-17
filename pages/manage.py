import streamlit as st
import pandas as pd
from utils import load_page_config

def load_data(file_path):
    return pd.read_csv(file_path)

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

def load_progress(class_name):
    df = load_data("due.csv")
    df_class = df[df["Class"] == class_name].copy()
    
    subjects = ["Math_due", "English_due", "Korean_due"]

    st.subheader(f"{class_name}반 진도관리")
    for subject in subjects:
        with st.container(border=True):
            progress = df_class[subject].str.replace('p', '').astype(int)
            total_progress = progress.sum()
            st.markdown(f"<span style='font-weight:bold; color:green;'>  {total_progress} 페이지</span>", unsafe_allow_html=True)
            
            new_progress = st.number_input(f"{subject.split('_')[0]} 진도 페이지 수정", min_value=0, value=int(total_progress), step=1)
            
            if st.button("Update", key=f"{class_name}반 {subject}"):
                df.loc[df["Class"] == class_name, subject] = f"{new_progress}p"
                save_data(df, "due.csv")
                st.success(f"{subject.split('_')[0]} 진도가 업데이트되었습니다!")

if __name__ == "__main__":
    load_page_config()

    tab1, tab2, tab3 = st.tabs(["1-1", "1-2", "1-3"])

    with tab1:
        load_progress("1-1")

    with tab2:
        load_progress("1-2")

    with tab3:
        load_progress("1-3")

