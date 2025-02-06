**Python 課程筆記**

---

## **1. Streamlit 欄位元件**

### **(1) 建立 Columns 欄位**
```python
import streamlit as st
st.title("欄位元件")
col1, col2 = st.columns(2)  # 建立兩個欄位
col1.button("按鈕1", key="button1")
col2.button("按鈕2", key="button2")
```

### **(2) 設定欄位比例**
```python
col1, col2 = st.columns([1, 2])  # 設定欄位比例
col1.button("按鈕1", key="button3")
col2.button("按鈕2", key="button4")
```

### **(3) 三個欄位**
```python
col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕1", key="button5")
col2.button("按鈕2", key="button6")
col3.button("按鈕3", key="button7")
```

### **(4) 使用 with 語法在欄位內建立按鈕與內容**
```python
col1, col2 = st.columns([1, 2])
with col1:
    if st.button("按鈕1", key="button8"):
        st.balloons()
    st.write("這是col1")
with col2:
    st.button("按鈕2", key="button9")
    st.write("這是col2")
```

### **(5) 動態建立欄位數量**
```python
col_mun = st.number_input("輸入欄位數量", min_value=1)
cols = st.columns(col_mun)
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}", key=f"btn{i+1}")
```

### **(6) 購物籃功能實作**
```python
if "l" not in st.session_state:
    st.session_state.l = []

a, b = st.columns(2)
with a:
    x = st.text_input("請輸入點餐機名稱", value="這是點餐機預設文字")
with b:
    if st.button("點餐", key="button1"):
        st.session_state.l.append(x)

st.write("### 購物籃")
for i in range(len(st.session_state.l)):
    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state.l[i])
    with col2:
        if st.button("刪除", key=f"btn{i+1}"):
            st.session_state.l.pop(i)
            st.rerun()
```

---

## **2. Python 運算子與迴圈**

### **(1) 算數指定運算子**
```python
a = 1
a += 1  # a = a + 1
a -= 1  # a = a - 1
a *= 1  # a = a * 1
a /= 1  # a = a / 1
a //= 1  # a = a // 1
a %= 1  # a = a % 1
a **= 1  # a = a ** 1
```

### **(2) 運算子優先順序**
1. `()` 括號
2. `**` 次方
3. `* / // %` 乘、除、取商、取餘數
4. `+ -` 加、減
5. `== != > < >= <=` 比較運算子
6. `and or not` 邏輯運算子
7. `= += -= *= /= //= %= **=` 算數指定運算子

### **(3) while 迴圈**
```python
i = 0
while i < 10:
    print(i)
    i += 1
```

### **(4) break 跳出迴圈**
```python
i = 0
while i < 5:
    print(i)
    for j in range(5):
        print(j)
    if i == 3:
        break  # 跳出 while 迴圈
    i += 1
```

---

## **3. Python 字典 (Dictionary)**

### **(1) 建立字典**
```python
d = {"a": 1, "b": 2, "c": 3}
```

### **(2) 取得鍵、值與鍵值對**
```python
print(d.keys())  # 取得鍵
print(d.values())  # 取得值
print(d.items())  # 取得鍵值對
```

### **(3) 新增/修改字典**
```python
d["d"] = 4  # 新增鍵值對
d["a"] = 5  # 修改鍵值對
```

### **(4) 檢查鍵是否存在**
```python
print("a" in d)  # True
print("e" in d)  # False
```

### **(5) 刪除字典鍵值對**
```python
print(d.pop("a"))  # 刪除鍵 'a'
```

### **(6) 複雜的字典結構**
```python
d = {"a": [1, 2, {"e": 40, "f": 50}], "b": {"c": 4, "d": 5}}
print(d["a"])  # [1, 2, {'e': 40, 'f': 50}]
print(d["a"][2]["f"])  # 50
```

---


