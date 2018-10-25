try:
    print(10 / 0)
except:
    print("you can not do it")

try:
    print(10 / 2)
    print(10 + 'o')
except ArithmeticError as e:
    print(e)
except TypeError as e:
    print(e)
except Exception:
    print("There is something wrong")
