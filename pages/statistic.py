import streamlit as st
import plotly.figure_factory as ff
from streamlit.type_util import data_frame_to_bytes
from utils import load_page_config, load_data

def info_and_stat(class_num):
    # 학생 정보가 담긴 데이터 로드
    df = load_data("example.csv")
    # 특정 반의 학생만 추출
    df_class = df[df["Class"] == class_num]

    # 반 정보 표시 및 컨테이너 생성
    st.subheader(f"1학년 {class_num}반")
    container = st.container(border=True, height=700)
    col1, col2 = container.columns([2, 5])

    # 학생 정보를 나타내기 위한 부분
    with col1:
        st.markdown("##### 학생")
        for idx, row in df_class.iterrows():
            student_info = st.container(border=True, height=60)
            student_info.write(f'{row["Name"]} # {row["Email"]}')

    # 통계를 보여주기 위한 부분
    with col2:
        st.markdown ("##### 점수 통계")
        subject = st.radio(label="과목 선택", options=["Korean", "English", "Math"], horizontal= True, label_visibility="collapsed", key=class_num)
        df_subject = df_class[subject]
        fig = ff.create_distplot([df_subject], group_labels=[subject])
        st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    load_page_config()

    class1, class2, class3 = st.tabs(["1-1", "1-2", "1-3"])

    with class1:
        info_and_stat(1)
    with class2:
        info_and_stat(2)
    with class3:
        info_and_stat(3)