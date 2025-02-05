# **Python 課程筆記**

## **1. 字串格式化**
```python
name = " Lin"
age = 20
print(f"My name is {name.strip()}, I'm {age} years old")  # f-string
```
- `f-string` 可將變數或運算結果嵌入 `{}` 中，使輸出更直觀。
- `len(str)`：計算字串長度。
- `type(value)`：查看變數型態。

## **2. 型態與型態轉換**
```python
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type(True))  # <class 'bool'>
```
- `int()`、`float()`、`str()`、`bool()` 可進行型態轉換。
- **注意**：無法將非數字字串轉換為數字，例如 `int("hello")` 會產生錯誤。

## **3. 使用者輸入**
```python
a = input("請輸入數字: ")
print(int(a) + 10)  # 轉換為整數
```
- `input()`：接收使用者輸入，預設型態為 `str`，需轉換為適當型態。

## **4. 計算面積**
```python
a = int(input("請輸入正方形的邊長: "))
print(f"正方形的面積是 {a * a}")

r = int(input("請輸入圓的半徑: "))
print(f"圓的面積是 {3.14 * r**2}")
```
- `**` 為次方運算符。

## **5. 比較與邏輯運算**
### **比較運算子**
```python
print(1 == 1)  # True
print(1 != 2)  # True
print(1 < 2)   # True
print(1 >= 2)  # False
```
### **邏輯運算子**
```python
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```
### **運算優先順序**
1. `()` 括號
2. `**` 次方
3. `* / // %` 乘、除、整除、取餘數
4. `+ -` 加、減
5. `== != > < >= <=` 比較運算子
6. `and or not` 邏輯運算子

## **6. 條件判斷**
### **密碼檢查**
```python
password = input("請輸入密碼: ")
if password == "123456":
    print("hi john")
elif password == "12345":
    print("hi tim")
else:
    print("密碼錯誤")
```
- `if`、`elif`、`else` 可用於條件判斷。
- `elif` 能避免重複判斷，提高效率。

---

## **7. Streamlit 簡介**
- `st.write()` 可顯示文字、數字、Markdown、表格等。
- `st.title()` 設定標題。

```python
import streamlit as st

st.title("Python 筆記")
st.write("這是 Streamlit 的應用")
```
### **Markdown 支援**
```python
st.write("""
# 這是第一標題
- 這是項目 1
- 這是項目 2
""")
```

## **8. Streamlit 互動元件**
### **數字輸入**
```python
n = st.number_input(label="請輸入數字", value=0, step=1, min_value=0, max_value=100)
st.write(f"你輸入的數字是 {n}")
```

### **分級系統**
```python
score = st.number_input("請輸入分數", min_value=0, max_value=100, step=1)

if score >= 90:
    st.write("你的分級是 A")
elif score >= 80:
    st.write("你的分級是 B")
elif score >= 70:
    st.write("你的分級是 C")
elif score >= 60:
    st.write("你的分級是 D")
else:
    st.write("你的分級是 F")
```

### **按鈕互動**
```python
if st.button("點我放氣球"):
    st.balloons()
if st.button("點我下雪"):
    st.snow()
```

## **9. Streamlit 遊戲應用**
### **隨機數字遊戲**
```python
import random as r

if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)
    st.session_state.last = 0

n = st.number_input("請輸入 1-100 的數字", step=1, min_value=1, max_value=100)

if st.session_state.last >= 8:
    st.write(f"遊戲結束！答案是 {st.session_state.ans}")
else:
    if n < st.session_state.ans:
        st.write("再大一點")
    elif n > st.session_state.ans:
        st.write("再小一點")
    else:
        st.write(f"恭喜答對！答案是 {st.session_state.ans}")
        st.balloons()
    st.session_state.last += 1
```
- `st.session_state` 用於儲存變數，即使使用者更新頁面，變數仍保留。

