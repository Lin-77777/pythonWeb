# 算數指定運算子
a = 1
a += 1  # a=a+1
print(a)
a -= 1  # a=a-1
print(a)
a *= 1  # a=a*1
print(a)
a /= 1  # a=a/1
print(a)
a //= 1  # a=a//1
print(a)
a %= 1  # a=a%1
print(a)
a **= 1  # a=a**1
print(a)


# 優先順序
# 1.()括號
# 2.**次方
# 3.* / // % 乘 除 取商 取餘數
# 4.+ - 加 減
# 5.== != > < >= <= 比較運算子
# 6.and or not 邏輯運算子
# 7. = += -= *= /= //= %= **= 算數指定運算子
# 有儲存的東西都是最後執行


# while 迴圈
# while 會搭配一個條件式來使用
# 條件式為 True 時會一直執行迴圈
# 條件式為 False 時會結束迴圈
# 每次迴圈執行完都會重新檢查條件有沒有變成 false
i = 0
while i < 10:
    print(i)
    i += 1  # i = i +1

# break 可以強制跳出迴圈
# 先判斷break屬於哪個迴圈，然後跳出對應的迴圈
i = 0
while i < 5:
    print(i)

    for j in range(5):
        print(j)

    if i == 3:
        break  # 跳出迴圈，屬於while迴圈
    i = i + 1


# 字典
# dict是透過key-value的方式來儲存資料，key是唯一的，value可以重複
# dict是無序的，所以無法透過index來取得資料
# dict的key必須是不可變的資料型態，例如:str,int,float
# dict的value可以是任意資料型態
# dict的key-value是透過冒號來連結，key:value
# dict的key-value是透過逗號來分隔
d = {"a": 1, "b": 2, "c": 3}

# 取得dict的key
print(d.keys())  # dict_keys(['a', 'b', 'c'])
for key in d.keys():
    print(key)


# 取得dict的value
print(d.values())  # dict_values([1, 2, 3])
for value in d.values():
    print(value)


# 取得dict的key-value
print(d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])
for key, value in d.items():
    print(key, value)

# 新增/修改dict的key-value
d["d"] = 4  # 新增
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d["a"] = 5  # 修改
print(d)  # {'a': 5, 'b': 2, 'c': 3, 'd': 4}

# 檢查dict是否有某個key
# in不能檢查value
# 跟list比較，in可以檢查的是list的元素dict的key
print("a" in d)  # True
print("e" in d)  # false
# list 檢查元素
l = [1, 2, 3]
print(1 in l)  # True
print(4 in l)  # false


# 刪除dict的key-value,pop()方法
# 如果資料有存在，就刪除並回傳value
print(d.pop("a"))  # 5
# 如果資料不存在，就回傳預設值
print(d.pop("只要是字串都可以"))
# 如果資料不存在，也沒有預設值，就會報錯


# 比較複雜的dict
d = {"a": [1, 2, {"e": 40, "f": 50}], "b": {"c": 4, "d": 5}}
print(d["a"])  # [1,2,3]
print(d["a"][0])  # 1
print(d["b"])  # {'c': 4, 'd': 5}
print(d["b"]["c"])  # 4
print(d["a"][2]["f"])  # 50
