import time 
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from utils import load_page_config, save_to_word
from llm import generate_question
import fitz  # PyMuPDF
from io import BytesIO

def init_streamlit():
    load_page_config()
    st.header("EPSON EDUSYNC", divider="rainbow")

def extract_text_from_pdf(file):
    # Read the PDF file into a BytesIO object
    pdf_bytes = file.read()
    pdf_stream = BytesIO(pdf_bytes)
    
    # Open the provided PDF file
    document = fitz.open(stream=pdf_stream, filetype="pdf")
    text = ""
    # Iterate over each page and extract text
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()

    return text

def init_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "안녕하세요. 유사한 문제를 생성해드리겠습니다! 문제 파일을 올려주세요 :blush:"}]

    if "count" not in st.session_state:
        st.session_state.count = 0
    
    for messages in st.session_state.messages:
        with st.chat_message(messages["role"]):
            st.markdown(messages["content"])

def chat_main():
    # if message := st.chat_input("여기에 입력해주세요!"):
    #     st.session_state.messages.append({"role": "user", "content": message})
    #     with st.chat_message("user"):
    #         st.markdown(message)

    if file := st.file_uploader("pdf", key=st.session_state.count, type="pdf", label_visibility="collapsed"):
        st.session_state.count += 1

        bytes_data = file.read()
        file.seek(0) 
        text = extract_text_from_pdf(file)
        pdf_viewer(input=bytes_data, width=700)

        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                question = generate_question(text)
                message_placeholder = st.empty()
                full_question = ""
                for lines in question.split("\n"):
                    for chunk in lines.split():
                        full_question += chunk + " "
                        time.sleep(0.05)
                        message_placeholder.write(full_question)
                    full_question += "\n"
                message_placeholder.write(full_question)

                # 워드 파일로 저장
                file_path = "./generations/generated.docx"
                save_to_word(full_question, file_path)

                # 워드 파일 다운로드 버튼 추가
                with open(file_path, "rb") as f:
                    st.download_button(
                        label="Download Generated Question",
                        data=f,
                        file_name="generated.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )

        st.session_state.messages.append({"role": "assistant", "content": question})
        st.session_state.messages = [{"role": "assistant", "content": "안녕하세요. 유사한 문제를 생성해드리겠습니다! 문제 파일을 올려주세요 :blush:"}]
                
if __name__ == "__main__":
    init_streamlit()
    init_chat()
    chat_main()