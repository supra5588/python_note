


condition = 1
while condition<=5:

    print(condition)
    condition = condition +1

    for i in range(1,6):
        print(i)

        while True:

            a = int(input("Please enter number a : "))
            b = int(input("Please enter number b : "))

            print("a + b = " + str(a+b))
            break