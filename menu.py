import streamlit as st


def menu():
    st.sidebar.page_link("main.py", label="首頁", icon="🏠")

    st.sidebar.write("---")
    st.sidebar.page_link("pages/handbook.py", label="學習筆記", icon="📚")
    st.sidebar.page_link("pages/class2-2.py", label="Streamlit 基礎", icon="🎯")
    st.sidebar.page_link("pages/class2-3.py", label="猜數字遊戲1", icon="🎲")
    st.sidebar.page_link("pages/class2-4.py", label="猜數字遊戲2", icon="🎮")
    st.sidebar.page_link("pages/class3-2.py", label="數字金字塔", icon="🔢")
    st.sidebar.page_link("pages/class4-1.py", label="欄位元件", icon="📊")
    st.sidebar.page_link("pages/class4-2.py", label="點餐機", icon="🍽️")
    st.sidebar.page_link("pages/class5-2.py", label="聊天AI", icon="🤖")
    st.sidebar.page_link("pages/class5-3.py", label="AI猜謎遊戲", icon="🤖")
