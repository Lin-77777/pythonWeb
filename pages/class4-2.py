import streamlit as st

if "l" not in st.session_state:
    st.session_state.l = []

a, b = st.columns(2)
with a:
    x = st.text_input("請輸入點餐機名稱", value="這是點餐機預設文字")
with b:
    if st.button("點餐", key="button1"):
        st.session_state.l.append(x)
st.write("### 購物籃")

for i in range(len(st.session_state.l)):
    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state.l[i])
    with col2:
        if st.button("刪除", key=f"btn{i+1}"):
            st.session_state.l.remove(st.session_state.l[i])
            st.rerun()
