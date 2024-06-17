import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
from utils import load_page_config, load_data

# Load the data
df = pd.read_csv('example.csv')

# Define GPA calculation
def calculate_gpa(row):
    total_score = row['Korean'] + row['English'] + row['Math']
    gpa = total_score / 3
    return gpa

# Add GPA to DataFrame
df['GPA'] = df.apply(calculate_gpa, axis=1)

# Calculate ranks within class and overall
df['Class Rank'] = df.groupby('Class')['GPA'].rank(ascending=False, method='min')
df['Overall Rank'] = df['GPA'].rank(ascending=False, method='min')

# Define grade boundaries based on overall rank
def assign_grade(rank):
    if rank <= 4:
        return '1등급'
    elif rank <= 11:
        return '2등급'
    elif rank <= 23:
        return '3등급'
    elif rank <= 40:
        return '4등급'
    elif rank <= 60:
        return '5등급'
    elif rank <= 77:
        return '6등급'
    elif rank <= 89:
        return '7등급'
    elif rank <= 96:
        return '8등급'
    else:
        return '9등급'

# Assign grades for each subject
df['Korean Rank'] = df['Korean'].rank(ascending=False, method='min')
df['English Rank'] = df['English'].rank(ascending=False, method='min')
df['Math Rank'] = df['Math'].rank(ascending=False, method='min')

df['Korean Grade'] = df['Korean Rank'].apply(assign_grade)
df['English Grade'] = df['English Rank'].apply(assign_grade)
df['Math Grade'] = df['Math Rank'].apply(assign_grade)

def student_detail(row):
    st.image(row["ImageURL"], width=100)
    details = {
        "Name": row["Name"],
        "Gender": row["Gender"],
        "Email": row["Email"],
        "Korean": row["Korean"],
        "Korean Grade": row["Korean Grade"],
        "English": row["English"],
        "English Grade": row["English Grade"],
        "Math": row["Math"],
        "Math Grade": row["Math Grade"],
        "Progress": row["Progress"],
        "GPA": f'{row["GPA"]:.2f}',
        "Class Rank": f'{row["Class Rank"]:.0f}',
        "Overall Rank": f'{row["Overall Rank"]:.0f}'
    }
    st.table(pd.DataFrame(details.items(), columns=['Attribute', 'Value']))

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
                if st.button(f'상세 정보 보기', key=idx):
                    st.session_state.selected_student = row["Email"]

    # Display score statistics and graph
    with col2:
        st.markdown("##### 점수 통계 및 분포")
        # Calculate statistics
        subjects = ["Korean", "English", "Math"]
        stats = {subject: {'mean': df_class[subject].mean(), 'std': df_class[subject].std()} for subject in subjects}
        # Create distribution plots
        hist_data = [df_class[subject] for subject in subjects]
        group_labels = subjects
        fig = ff.create_distplot(hist_data, group_labels, show_hist=False, show_rug=False)
        st.plotly_chart(fig)

def main():
    load_page_config()

    if 'selected_student' in st.session_state:
        selected_student = df[df["Email"] == st.session_state.selected_student].iloc[0]
        st.subheader(f"{selected_student['Name']}의 상세 정보")
        student_detail(selected_student)

        if st.button("반으로 돌아가기"):
            del st.session_state.selected_student
    else:
        class1, class2, class3 = st.tabs(["1-1", "1-2", "1-3"])

        with class1:
            info_and_stat(df, 1)
        with class2:
            info_and_stat(df, 2)
        with class3:
            info_and_stat(df, 3)

if __name__ == "__main__":
    main()