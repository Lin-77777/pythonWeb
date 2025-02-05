### 📚 Python 課程筆記

---

#### 1️⃣ **註解 (Comments)**

* **單行註解** ：使用`#` 開頭的文字不會被執行。
  ```python
  # 這是註解，不會被執行
  print("Hello world!")  # 這也是註解
  ```
* **快速註解/取消註解** ：按`Ctrl + ?` 可以快速註解或取消註解選中的程式碼。

---

#### 2️⃣ **輸出指令 (print)**

* 使用`print()` 來在終端機顯示訊息。
  ```python
  print("Hello world!")  # 輸出字串
  print(1)               # 輸出整數
  print(1.234)           # 輸出浮點數
  print(True)            # 輸出布林值
  ```

---

#### 3️⃣ **基本資料型態 (Data Types)**

* **整數 (`int`)** ：如`1`,`-1`,`0`
* **浮點數 (`float`)** ：如`1.0`,`1.234`
* **字串 (`str`)** ：如`"1"`,`"aaa"`
* **布林值 (`bool`)** ：`True`,`False`

---

#### 4️⃣ **變數 (Variables)**

* 使用`=` 來指定變數的值。
  ```python
  a = 10        # 將數字 10 存到變數 a
  print(a)      # 輸出變數 a 的值 -> 10

  a = "apple"   # 將字串 "apple" 存到變數 a
  print(a)      # 輸出變數 a 的值 -> apple
  ```

---

#### 5️⃣ **運算子 (Operators)**

* **數學運算子** ：
  ```python
  print(1 + 1)    # 加法 -> 2
  print(1 - 1)    # 減法 -> 0
  print(1 * 1)    # 乘法 -> 1
  print(1 / 1)    # 除法 -> 1.0
  print(1 // 1)   # 整數除法 -> 1
  print(1 % 1)    # 取餘數 -> 0
  print(2 ** 3)   # 次方 -> 8
  ```
* **運算優先順序** ：
  1. `()` 括號
  2. `**` 次方
  3. `*`,`/`,`//`,`%` 乘法、除法、整數除法、取餘數
  4. `+`,`-` 加法、減法

---

#### 6️⃣ **字串操作 (String Operations)**

* **字串相加 (`+`)** ：可以將兩個字串合併。
  ```python
  print("apple" + "pen")  # applepen
  ```
* **字串乘法 (`*`)** ：重複字串。
  ```python
  print("apple" * 3)  # appleappleapple
  ```

---

#### 7️⃣ **函式 (Functions)**

* `max()`：找出最大值。
  ```python
  print(max("1", "2", "3"))  # 輸出 '3'
  ```

---

#### 8️⃣ **執行 Streamlit 網頁應用程式**

* **Streamlit** 是一個快速建立網頁應用的 Python 套件。
* 使用以下指令來啟動：
  ```bash
  streamlit run main.py
  ```

---
