import streamlit as st

st.title("數字金字塔")
n = st.number_input(label="請輸入一個整數(1,9)", step=1, min_value=1, max_value=9)
st.write("數字金字塔")
n = n + 1
for i in range(n):
    st.write(str(i) * i)
