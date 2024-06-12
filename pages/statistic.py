import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
from utils import load_page_config, load_data

# Load the data
df = pd.read_csv('example.csv')

def info_and_stat(df, class_num):
    # Filter students by class
    df_class = df[df["Class"] == class_num]

    # Display class information
    st.subheader(f"1학년 {class_num}반")
    container = st.container()
    col1, col2 = container.columns([1, 3])

    # Display student information
    with col1:
        st.markdown("##### 학생 명단")
        for idx, row in df_class.iterrows():
            with st.expander(f'{row["Name"]} ({row["Gender"]})'):
                st.image(row["ImageURL"], width=50)
                st.write(f'Email: {row["Email"]}')
                st.write(f'Korean: {row["Korean"]}')
                st.write(f'English: {row["English"]}')
                st.write(f'Math: {row["Math"]}')
                st.write(f'Progress: {row["Progress"]}')

    # Display score statistics and graph
    with col2:

        st.markdown("##### 점수 통계 및 분포")
        # Calculate statistics
        subjects = ["Korean", "English", "Math"]
        stats = {subject: {'mean': df_class[subject].mean(), 'std': df_class[subject].std()} for subject in subjects}
        # Display statistics
        for subject, stat in stats.items():
            st.write(f"{subject} = 평균: {stat['mean']:.2f}점, 표준편차: {stat['std']:.2f}점")
        # Create distribution plots
        hist_data = [df_class[subject] for subject in subjects]
        group_labels = subjects
        fig = ff.create_distplot(hist_data, group_labels, show_hist=False, show_rug=False)
        st.plotly_chart(fig)
        st.data_editor(
            df_class,
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


if __name__ == "__main__":
    st.set_page_config(page_title="학생 정보 및 통계", layout="wide")

    class1, class2, class3 = st.tabs(["1-1", "1-2", "1-3"])

    with class1:
        info_and_stat(df, 1)
    with class2:
        info_and_stat(df, 2)
    with class3:
        info_and_stat(df, 3)
