import streamlit as st

import random as r


import menu

menu.menu()
st.title("猜數字小遊戲")
st.write("---")
# 透過session_state可以在將變數暫時存在瀏覽器當中，直到使用者重新整理整個網頁
# 按下元件、或是與元件互動，都不會讓session_state當中的變數消失
if "min_value" not in st.session_state:
    st.session_state.min_value = 1
if "max" not in st.session_state:
    st.session_state.max = 100


if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)
if "last2" not in st.session_state:
    st.session_state.last2 = 7

st.write(f"你還剩{st.session_state.last2}次機會")
n = st.number_input(
    label="請輸入一個一到一百的數字", step=1, min_value=0, max_value=100
)

if st.session_state.last2 == 0:
    st.write(f"公布達案，答案是{st.session_state.ans}")

if n < st.session_state.ans:
    if n > st.session_state.min_value:
        st.session_state.min_value = n
    st.write(
        f"再大一點，答案在{st.session_state.min_value}到{st.session_state.max}間，你的答案是:{n}"
    )
elif n > st.session_state.ans:
    if n < st.session_state.max:
        st.session_state.max = n
    st.write(
        f"再小一點，答案在{st.session_state.min_value}到{st.session_state.max}間，你的答案是:{n}"
    )
else:
    st.write(f"恭喜答對，答案是，答案是{st.session_state.ans}")
    st.balloons()

if st.button("重新開始", key="reset"):
    st.session_state.min_value = 1
    st.session_state.max = 100
    st.session_state.last2 = 7
    st.session_state.ans = r.randint(1, 100)
    st.rerun()
