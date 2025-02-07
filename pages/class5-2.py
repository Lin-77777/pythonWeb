import streamlit as st

st.title("猜謎遊戲")
if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    if message["role"] != "developer":
        with st.chat_message(message["role"]):
            st.write(message["content"])

message = st.chat_input("請輸入文字")  # 聊天輸入框元件

if message:
    st.session_state.history.append({"role": "user", "content": message})
    st.session_state.history.append(
        {"role": "assistant", "content": f"你輸入的內容是:{message}"}
    )
    st.rerun()  # 重新整理頁面
