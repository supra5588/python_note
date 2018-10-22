


#if 語句

a = 10
b = 20

if a>b:

    print("a的值小於B")

if b>a:

    print("b的值大於a")


age = int(input("Please enter your age: "))

print(type(age))


if age<21:
    print("You can not smoke")

elif age == 21:
    print("You can smole too")

elif age == 100:
    print("You are too old do not smoke")

else:
    print("You can smoke")
