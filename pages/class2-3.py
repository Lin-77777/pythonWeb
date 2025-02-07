import streamlit as st

import random as r


st.title("猜數字小遊戲")
st.write("---")
# 透過session_state可以在將變數暫時存在瀏覽器當中，直到使用者重新整理整個網頁
# 按下元件、或是與元件互動，都不會讓session_state當中的變數消失


if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)
if "last" not in st.session_state:
    st.session_state.last = 7
st.write(f"你還剩{st.session_state.last}次機會")
n = st.number_input(
    label="請輸入一個一到一百的數字", step=1, min_value=0, max_value=100
)
if st.session_state.last == 0:
    st.write(f"公布達案，答案是{st.session_state.ans}")
if n < st.session_state.ans:
    st.write("再大一點")
    st.session_state.last = st.session_state.last - 1
elif n > st.session_state.ans:
    st.write("再小一點")
    st.session_state.last = st.session_state.last - 1
else:
    st.write(f"恭喜答對，答案是，答案是{st.session_state.ans}")
    st.balloons()
