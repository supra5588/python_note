"""
what is **kwargs
"""


def m1(*args, **kwargs):
    print(type(args))
    print(type(kwargs))


# dic_lin = {'name': 'lin', 'age': '20 years old', 'height': '180cm', 'weight': '80kg'}
#
#
# def someone(dic_someone):
#     for k, v in dic_someone.items():
#         print(k, ':', v)
#
#
# someone(dic_lin)

"""
How to use **kwargs
"""

dic_lin = {'name': 'lin', 'age': '20 years old', 'height': '180cm', 'weight': '80kg'}


def someone(**kwargs):
    for k, v in kwargs.items():
        print(k, ':', v)


someone(name="ha ha ha", age="20 years old", height="180cm")
