import streamlit as st
import time

st.title("欄位元件")
col1, col2 = st.columns(2)  # 2columns
col1.button("按鈕1", key="button1")  # 在col1中建立一個按鈕類似st.button("按鈕1")
col2.button("按鈕2", key="button2")  # 在col2中建立一個按鈕類似st.button("按鈕2")

# 2columns,可以用比例來設定每個column的寬度,將比例放到list中
col1, col2 = st.columns([1, 2])
col1.button("按鈕1", key="button3")  # 在col1中建立一個按鈕類似st.button("按鈕1")
col2.button("按鈕2", key="button4")  # 在col2中建立一個按鈕類似st.button("按鈕2")

# 3columns
col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕1", key="button5")  # 在col1中建立一個按鈕類似st.button("按鈕1")
col2.button("按鈕2", key="button6")  # 在col2中建立一個按鈕類似st.button("按鈕2")
col3.button("按鈕3", key="button7")  # 在col3中建立一個按鈕類似st.button("按鈕3")


col1, col2 = st.columns(
    [
        1,
        2,
    ]
)
with col1:  # col1中建立一個按鈕類似
    if st.button("按鈕1", key="button8"):  # 在col1中建立一個按鈕
        st.balloons()  # 在col1中建立一個氣球
    st.write("這是col1")  # 在col1中建立一個文字
with col2:  # col2中建立一個按鈕類似
    st.button("按鈕2", key="button9")  # 在col2中建立一個按鈕
    st.write("這是col2")  # 在col2中建立一個文字


# 多個colmuns
col_mun = st.number_input("輸入欄位數量", min_value=1)
cols = st.columns(col_mun)  # colmuns,cols[0]...cols[col_mun-1]
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}", key=f"btn{i+1}")  # 在col1[i]中建立一個按鈕類似


st.write("---")
st.title("columns排列元件效果比較")
# 2columns
col1, col2 = st.columns([1, 2])
with col1:
    st.button("按鈕1", key="button10")
    st.button("按鈕2", key="button11")
    st.button("按鈕3", key="button12")
with col2:
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")


st.write("---")

for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}", key=f"btn{i+4}")
        with col2:
            st.write(f"這是col2_{i+1}")


st.write("---")
if st.button("重新開始", key="reset"):  # 如果按鈕按下
    st.sussess("重新開始")  # 顯示綠色訊息
    time.sleep(1)  # 等待1秒
    st.rerun()  # 重新整理整個頁面
