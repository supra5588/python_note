#重量轉換例子

def converter(weight):
    ponds = weight/0.45         #公斤轉磅數
    print(ponds)

converter(100)


def converter2(weight = 100):
    pond = weight/0.45
    print(pond)


converter2()
