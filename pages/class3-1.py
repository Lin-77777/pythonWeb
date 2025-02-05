# for迴圈
# for會搭配 in 來使用， in 後面接一個有範圍的東西
# range(5) 會產生0,1,2,3,4，不包含5
# i 是迴圈的變數可以自己取名，迴圈變數只能在迴圈內使用
# 迴圈變數每回合會從範圍裡面取一個資料出來
for i in range(5):
    print(i)

# range可以設定起始值、結束值，但不包含結束值
# range(1,5) 會產生1,2,3,4
for i in range(1, 5):
    print(i)

# range可以設定起始值、結束值與間隔值，但不包含結束值
# range(1,10,2) 會產生1,3,5,7,9
for i in range(1, 10, 2):
    print(i)


# 補充random.randrange()函數
# random.randrange()函數可以隨機生成一個範圍內的整數
# ramdom.randrange()設定傳入的參數跟range()一樣
import random as r


for i in range(10):
    print(r.randrange(1, 10))


# list 列表\清單\陣列
print([])  # 這是空的list
print([1, 2, 3])  # 這是一個有三個元素的list
print([1, 2, 3, "a", "b", "c"])  # 這是一個有六個元素的list
print([1, 2, 3, ["a", "b", "c"]])  # 這是一個有四個元素的list
print([1, True, "a", 1.234])  # 這是一個有四個元素的list


# list 讀取元素，元素的index從0開始
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[1])  # 2
print(L[2])  # 3
print(L[3])  # "a"


# list 取長度，也就是list中有幾個元素，不是index的最大值
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 6


# list 走訪元素
# 可以透過取德index的方式來找到list中的資料
# 也可以直接把list當作一個範圍來取得資料
# 這兩種方式都可以，但是看使用的情境是否會需要index來決定要用哪一種方式
L = [1, 2, 3, "a", "b", "c"]

for i in range(len(L)):
    print(L[i])  # 1,2,3,"a","b","c"

for i in range(0, len(L), 2):  # 0,2,4
    print(L[i])  # 1,3,"b"

for i in L:
    print(i)  # 1,2,3,"a","b","c"


L = [1, 2, 3, "a", "b", "c"]
# 就是取index 0到最後，每次取兩個元素，所以是[1,3,"b"]
print(L[::2])
# 就是取index 一到三的元素，不包含index 4，所以是[2,3,"a"]
print(L[1:4])
# 就是取index 一到三的元素，不包含index 4，並且每次取2個元素，所以是[2,"a"]
print(L[1:4:2])
# 跟range一樣的用法，只是符號不同


# list修改元素
L = [1, 2, 3, "a", "b", "c"]
L[0] = 2
print(L)  # [2,2,3,"a","b","c"]
