import streamlit as st

def init_streamlit():
    st.header("EPSON EDUSYNC", divider="rainbow")

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"}]

    for messages in st.session_state.messages:
        with st.chat_message(messages["role"]):
            st.write(messages["content"])

def chat_main():
    if message := st.chat_input("여기에 입력해주세요!"):
        st.session_state.messages.append({"role": "user", "content": message})
        with st.chat_message("user"):
            st.markdown(message)

if __name__ == "__main__":
    init_streamlit()
    chat_main()