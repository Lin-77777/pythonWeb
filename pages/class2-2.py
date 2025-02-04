import streamlit as st


st.title("class2-2")
st.write(
    "這是一個用`st.write`顯示的字串，可以處理很多種格式，例如:數字，文字，Markdown，數據框等。"
)
st.write(
    """
這是一個'st.write'顯示的字串，可以處理 Markdown 語法。
例如:
* **粗體字**
* *斜體字*
* ~~刪除線~~
* [首頁連結](http://localhost:8501/)
* 代碼塊:
'''python
print("Hello world!")


'''
    """
)
