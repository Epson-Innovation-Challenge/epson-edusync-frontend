import streamlit as st
from utils import load_page_config

def show_upload(state):
    st.session_state.uploader_visible = state

def init_streamlit():
    load_page_config()
    st.header("EPSON EDUSYNC", divider="rainbow")

def init_chat():
    if "uploader_visible" not in st.session_state:
        st.session_state.uploader_visible = False

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if st.session_state.uploader_visible:
        st.session_state.messages = [{"role": "assistant", "content": "안녕하세요. 유사한 문제를 생성해드리겠습니다! 문제 파일을 올려주세요 :blush:"}]
    else:
        with st.chat_message("assistant"):
            cols = st.columns((4, 1))
            cols[0].write("안녕하세요! 문제를 생성하시고 싶은 경우이면 [생성]을 눌러주세요!")
            cols[1].button("생성", use_container_width=True, on_click=show_upload, args=[True])

    # if "messages" not in st.session_state:
    #     st.session_state.messages = [{"role": "assistant", "content": "안녕하세요. 유사한 문제를 생성해드리겠습니다! 문제 파일을 올려주세요 :blush:"}]

    for messages in st.session_state.messages:
        with st.chat_message(messages["role"]):
            st.write(messages["content"])
            uploaded_file = st.file_uploader("", key="file_uploader", label_visibility="collapsed")
            
def chat_main():
    if message := st.chat_input("여기에 입력해주세요!"):
        st.session_state.messages.append({"role": "user", "content": message})
        with st.chat_message("user"):
            st.markdown(message)

if __name__ == "__main__":
    init_streamlit()
    init_chat()
    chat_main()