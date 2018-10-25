"""
what is *args
"""


# def add(n1, n2, n3):
#     print(n1 + n2 + n3)
#
#
# add(1, 1, 1)


# def add(*args):
#     print(sum(args))
#     print(type(args))
#
#
# add(1, 2)

def add(*args):  # 不用擔心日後增加數值
    for name in args:
        print('ha ha', name)


add('a', 'b', 'c')
