### Python 課程筆記  

#### **1. for 迴圈**  
- `for` 迴圈搭配 `in` 使用，`in` 後面接可迭代的物件，如 `range()`。  
- `range(5)` 會產生 `0,1,2,3,4`，不包含 `5`。  
- 變數 `i` 為迴圈變數，只能在迴圈內使用，每次執行時取範圍內一個值。  

**範例**：
```python
for i in range(5):  # 產生 0,1,2,3,4
    print(i)
```

- `range(start, end)`：設定起始與結束值（不包含 `end`）。
```python
for i in range(1, 5):  # 產生 1,2,3,4
    print(i)
```

- `range(start, end, step)`：設定起始、結束與間隔值。
```python
for i in range(1, 10, 2):  # 產生 1,3,5,7,9
    print(i)
```

#### **2. `random.randrange()` 函數**  
- 產生範圍內的隨機整數，語法與 `range()` 相同。  

**範例**：
```python
import random as r

for i in range(10):
    print(r.randrange(1, 10))  # 隨機輸出 1~9 之間的數字
```

---

#### **3. List (列表、陣列)**
- `list` 用 `[]` 表示，可存放不同類型的元素。  

**範例**：
```python
print([])  # 空 list
print([1, 2, 3])  # 整數 list
print([1, 2, 3, "a", "b", "c"])  # 混合型 list
print([1, 2, 3, ["a", "b", "c"]])  # 巢狀 list
print([1, True, "a", 1.234])  # 混合型 list
```

##### **讀取 List 元素**
- **索引從 `0` 開始**。
- 使用 `len()` 取得 list 長度。

**範例**：
```python
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(len(L))  # 6
```

##### **遍歷 List**
- 使用 `range(len(L))` 或直接 `for i in L` 來走訪元素。

```python
L = [1, 2, 3, "a", "b", "c"]
for i in range(len(L)):  
    print(L[i])  # 逐一輸出元素
for i in L:  
    print(i)  # 直接輸出元素
```

##### **List 切片 (Slicing)**
```python
L = [1, 2, 3, "a", "b", "c"]
print(L[::2])  # 取得 index 0,2,4 => [1,3,"b"]
print(L[1:4])  # 取得 index 1,2,3 => [2,3,"a"]
print(L[1:4:2])  # 取得 index 1,3 => [2,"a"]
```

##### **修改 List**
```python
L = [1, 2, 3, "a", "b", "c"]
L[0] = 2
print(L)  # [2,2,3,"a","b","c"]
```

---

#### **4. Call by Value 與 Call by Reference**
##### **值傳遞 (Call by Value)**
```python
a = 1
b = a  # 複製 a 的值
b = 2
print(a, b)  # 1, 2
```

##### **引用傳遞 (Call by Reference)**
```python
a = [1, 2, 3]
b = a  # `b` 指向與 `a` 相同的記憶體位置
b[0] = 2
print(a)  # [2,2,3]，`a` 也被改變
```

##### **使用 `copy()` 複製 List**
```python
a = [1, 2, 3]
b = a.copy()  # `b` 為 `a` 的副本
b[0] = 2
print(a, b)  # [1,2,3] [2,2,3]，`a` 不受影響
```

---

#### **5. List 方法**
##### **`append()`**
- 在 `list` 末尾新增元素。

```python
L = [1, 2, 3]
L.append(4)
print(L)  # [1,2,3,4]
```

##### **刪除元素**
1. **`remove()`**：移除第一個符合條件的元素。
```python
L = ["a", "b", "c", "d", "a"]
L.remove("a")  # 移除第一個 "a"
print(L)  # ["b","c","d","a"]
```

2. **`pop(index)`**：移除指定 `index` 的元素，若無指定則移除最後一個。
```python
L = ["a", "b", "c", "d", "a"]
L.pop(0)  # 移除 index 0 的元素
L.pop()  # 移除最後一個元素
print(L)
```

---

#### **6. `streamlit` 相關應用**
##### **數字金字塔**
```python
import streamlit as st

st.title("數字金字塔")
n = st.number_input(label="請輸入一個整數(1,9)", step=1, min_value=1, max_value=9)
st.write("數字金字塔")

for i in range(n + 1):
    st.write(str(i) * i)
```

##### **文字輸入元件**
```python
st.write("---")
st.title("文字輸入元件")
a = st.text_input("請輸入文字", value="這是一個預設顯示文字")
st.write(f"你輸入的文字是:{a}")
```

##### **顯示 Markdown 檔案內容**
```python
import os

hd_book_files = os.listdir("markdown")

for file_name in hd_book_files:
    with st.expander(file_name[:-3]):  # 去掉 .md 副檔名
        with open(f"markdown/{file_name}", "r", encoding="utf-8") as file:
            text = file.read()
            st.write(text)
```

---

這份筆記涵蓋了 `for 迴圈`、`random`、`list` 操作、`call by value/reference`、`list 方法` 以及 `streamlit` 相關應用，可以作為學習 Python 的基礎指南！🚀