import streamlit as st
import menu

menu.menu()
st.title("數字金字塔")
n = st.number_input(label="請輸入一個整數(1,9)", step=1, min_value=1, max_value=9)
st.write("數字金字塔")
n = n + 1
for i in range(n):
    st.write(str(i) * i)


st.write("---")
st.title("文字輸入元件")
# st.text_input()指令格式 st.text_input(輸入欄位標題,value=""預設顯示文字"")
a = st.text_input("請輸入文字", value="這是一個預設顯示文字")
st.write(f"你輸入的文字是:{a}")
