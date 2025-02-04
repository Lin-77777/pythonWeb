# 字串格式化
name = " Lin"
age = 20

print(f"my name is  {name}, I 'm {age}years old")  # f-string
# 可以將變數或其他型態的資料放到f字串裡面的{},這樣可以在字串中顯示


print(len("hello"))  # len()是一個函式,可以計算字串的長度
print(len("，"))  # len()是一個函式,可以計算字串的長度
# type( ) #可以查看型態
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type(True))  # <class 'bool'>
# 型態轉換
print(int(1.0))  # float轉int
print(float(1))  # int轉float
print(str(1))  # int轉str
print(bool(1))  # int轉bool
print(int(1.234))  # float轉int
print(float("1.234"))  # str轉float
print(str(1.234))  # float轉str
print(bool(1.234))  # float轉bool
# print(int("hello"))#這行會error，因為字串裡面有非數字字元，所以不能轉換成數字

print("輸入開始")
# input()是一個函式,可以讓使用者輸入文字
# ()裡面的文字是提示訊息會先顯示在終端機才會等待使用者輸入
a = input("請輸入文字:")
print("輸入結束")
print(int(a) + 10)
print(type(a))  # 證明input()被輸入的字都是字串
a = int(a)
print(type(a))  # 這時候a已經是整數了


# 正方形的面積計算機
a = input("請輸入正方形的邊常")
a = int(a)
b = a * a
print(f"正方形的面積是{b}")

# 圓形的面積計算機
a = input("請輸入半徑")
a = int(a)
b = 3.14 * a**2
print(f"半徑為{a}的圓的面積是{b}")

# 比較運算子
print(1 == 1)  # True
print(1 == 2)  # False
print(1 != 2)  # True
print(1 != 1)  # False
print(1 < 2)  # True
print(1 > 2)  # False
print(1 <= 2)  # True
print(1 >= 2)  # False
print(1 < 1)  # False
print(1 > 1)  # False
print(1 <= 1)  # True
print(1 >= 1)  # True

# 邏輯運算子
# and 運算子
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
# or 運算子
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
# not 運算子
print(not True)  # False
print(not False)  # True


# 優先順序
# 1.()括號
# 2.**次方
# 3.* / // % 乘 除 取商 取餘數
# 4.+ - 加 減
# 5.== != > < >= <= 比較運算子
# 6.and or not 邏輯運算子
