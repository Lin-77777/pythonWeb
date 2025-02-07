import streamlit as st
import random as r
import menu

menu.menu()

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
```python
print("Hello world!")
```
    """
)

st.write(
    """
# 這是第一標題
- 這是第一個項目
- 這是第二個項目
- 這是第三個項目

## 這是第二標題
### 這是第三標題
#### 這是第四標題
##### 這是第五標題
###### 這是第六標題
    """
)

# st.nuber_input()
# 可以讓使用者輸入數字，設定step=1可以讓使用者輸入整數
# min_value=0,max_value=100可以設定最小值和最大值
# value=0可以設定預設值
n = st.number_input(label="請輸入數字", value=0, step=1, min_value=0, max_value=100)
st.write(f"你輸入的數字是{n}")

# 分級器
st.write("---")
st.write("練習")
number = st.number_input(label="請輸入你的分數", step=1, min_value=0, max_value=100)

if number >= 90:
    st.write("你的分級是A")
elif number >= 80:
    st.write("你的分級是B")
elif number >= 70:
    st.write("你的分級是C")
elif number >= 60:
    st.write("你的分級是D")
elif number <= 59:
    st.write("你的分級是F")


st.write("---")
st.write("#### 按鈕練習")
if st.button("hahaha", key="button1"):
    st.balloons()
if st.button("hahaha", key="button2"):
    st.snow()


st.write("---")
st.write("隨機數字")
# random.randint(1, 100)可以產生一個1到100之間的隨機整數
# st.write(f"random.randint(1, 100) = {r.randint(1, 100)}")
if st.button("按我一下", key="random"):
    st.write(f"random.randint(1, 100) = {r.randint(1, 100)}")

# 透過session_state可以在將變數暫時存在瀏覽器當中，直到使用者重新整理整個網頁
# 按下元件、或是與元件互動，都不會讓session_state當中的變數消失
if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)

st.write(f"存在於session_state的隨機數字={st.session_state.ans}")
