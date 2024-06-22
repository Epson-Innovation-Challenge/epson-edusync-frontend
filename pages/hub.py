import dropbox
import streamlit as st
import fitz  # PyMuPDF
from datetime import datetime
from streamlit_javascript import st_javascript
import base64

# Dropbox 액세스 토큰과 폴더 경로 설정
ACCESS_TOKEN = ''

# Dropbox 클라이언트 초기화
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# 지정된 폴더의 파일 목록 반환 함수
def list_files(folder_path):
    """주어진 폴더의 파일 목록을 반환합니다."""
    files = []
    try:
        res = dbx.files_list_folder(folder_path)
        for entry in res.entries:
            files.append(entry.name)
    except dropbox.exceptions.ApiError as err:
        st.error(f"Failed to list files: {err}")
    return files

@st.cache_data
def download_file(file_path):
    """Dropbox에서 파일을 다운로드하여 바이트 데이터를 반환합니다."""
    try:
        metadata, res = dbx.files_download(file_path)
        return res.content
    except dropbox.exceptions.ApiError as err:
        st.error(f"Failed to download file: {err}")
        return None

# PDF 페이지 수 가져오는 함수
def get_pdf_page_count(pdf_content):
    with open("temp.pdf", "wb") as f:
        f.write(pdf_content)
    doc = fitz.open("temp.pdf")
    return doc.page_count

def display_pdf(file_bytes, ui_width):
    """주어진 바이트 데이터를 PDF로 디스플레이합니다."""
    base64_pdf = base64.b64encode(file_bytes).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width={str(ui_width)} height={str(ui_width*4/3)} type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Streamlit 앱
st.title("📑 문제 저장소")

# 지정된 폴더의 PDF 파일 목록 나열
folder_path = "/test"

files = list_files(folder_path)

if files:
    with st.sidebar:
        selected_file = st.selectbox("📌 문제지를 골라주세요", files)
        
        if selected_file:
            file_path = f"{folder_path}/{selected_file}"
            file_bytes = download_file(file_path)
            
            if file_bytes:
                # 다운로드 버튼 추가
                st.download_button(
                    label="📥 문제지 다운로드",
                    data=file_bytes,
                    file_name=selected_file,
                    mime="application/pdf"
                )
                
    ui_width = st_javascript("window.innerWidth")
    display_pdf(file_bytes, ui_width)
