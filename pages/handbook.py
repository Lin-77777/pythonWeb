import streamlit as st

st.code(
    """
# 這是註解<不會被執行>
# 用ctrl+?框起來的地方可以快速加入註解/取消註解

print("Hello world!")  # print是在終端顯示文字的指令
# 基本資料型態
print(1)  # int這是整數,-1,0,1,2...等
print(1.0)  # float這是浮點數
print(1.234)  # float這是浮點數
print("1")  # str這是字串
print("aaa")  # str這是字串
print(True)  # bool這是布林值
print(False)  # bool這是布林值


print(1 + 1)  # 2
print("1" + "1")  # "11",這是字串的串接=字串相加


print(max("1", "2", "3"))


# 變數

a = 10  # 新增一個變數並命名為a
# "="的功能是將右邊的10加到左邊的a
print(a)  # 在終端機顯示a所存的值
a = "apple"  # 將a的值改成apple
print(a)  # 在終端機顯示a所存的值


# 運算子

print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1)  # 整數除法
print(1 % 1)  # 取餘數
print(2**3)  # 次方

# 優先順序
# 1.()括號
# 2.**次方
# 3.* / // % 乘 除 取商 取餘數
# 4.+ - 加 減

# 字串運算、+、*

print("apple" + "pen")  # 字串相加
print("apple" * 3)  # 字串乘法

#用streamlit run main.py網頁




"""
)
