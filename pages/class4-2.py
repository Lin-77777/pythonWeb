import streamlit as st
import menu

menu.menu()
# 初始化 session_state 變數 "l"，如果尚未定義則設為空列表
if "l" not in st.session_state:
    st.session_state.l = []

# 建立兩個欄位 a 和 b，用來佈局輸入框與按鈕
a, b = st.columns(2)

with a:
    # 建立文字輸入框，讓使用者輸入點餐機名稱，預設值為 "這是點餐機預設文字"
    x = st.text_input("請輸入點餐機名稱", value="這是點餐機預設文字")

with b:
    # 建立點餐按鈕，當按下按鈕時，將輸入的名稱添加到 session_state.l 清單中
    if st.button("點餐", key="button1"):
        st.session_state.l.append(x)

# 顯示購物籃標題
st.write("### 購物籃")

# 依據購物籃內容動態顯示已點選的品項
for i in range(len(st.session_state.l)):
    col1, col2 = st.columns(2)  # 建立兩個欄位，分別放商品名稱與刪除按鈕

    with col1:
        # 顯示購物籃中的點餐名稱
        st.write(st.session_state.l[i])

    with col2:
        # 建立刪除按鈕，按下後刪除對應的品項，並強制重新執行程式以更新畫面
        if st.button("刪除", key=f"btn{i+1}"):
            st.session_state.l.pop(i)  # 刪除對應索引的品項
            st.rerun()  # 重新執行程式以更新畫面
