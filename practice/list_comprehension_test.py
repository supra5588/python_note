"""
list comprehesion   列表解析式

從0~10的數字分別乘2,然後放到新的list

"""

newList = []
for i in range(11):
    newList.append(i * 2)

print(newList)

print([i * 2 for i in range(11)])  # i*2需要做的邏輯，再加上迴圈，簡化寫法

list = ['a', 'a1', 'a2', 'b1', 'b2', 'd1', 'd2', 'e1', 'e2', 'f1']
emptyList = []
for name in list:
    if name.startswith('a'):
        emptyList.append(name)
print(emptyList)

print([name for name in list if name.startswith('a')])  # 簡化寫法
