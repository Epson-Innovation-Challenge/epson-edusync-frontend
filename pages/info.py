import streamlit as st
from utils import load_page_config, load_data

def load_student_info(class_num):
    df = load_data("example.csv")
    df_class = df[df["Class"] == class_num]

    n_cols = 4
    n_rows = len(df_class) // n_cols

    st.subheader(f"1-{class_num} 학생정보")
    for i in range(n_rows):
        row = st.columns(n_cols)
        for j, col in enumerate(row):
            student = df_class.iloc[i * n_cols + j]
            tile = col.container(height=140)
            tile.write(f"📌 {student['Name']}")


if __name__ == "__main__":
    load_page_config()

    class1, clss2, class3 = st.tabs(["1-1", "1-2", "1-3"])

    with class1:
        load_student_info(1)

    with clss2:
        load_student_info(2)

    with class3:
        load_student_info(3)