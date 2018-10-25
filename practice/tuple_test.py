

#list

mylist = [1, 2, 3, 4, 5]

#tuple

mytuple = (1, 2, 3, 4, 5)

print(type(mylist))         #印出型別

print(type(mytuple))        #印出型別

print(len(mylist))
print(len(mytuple))

print(mylist[0])
print(mytuple[0])


print(dir(mylist))

print(".............")

print(dir(mytuple))


"""

list is mutable  可改變
tuple is inmutable  無法改變

"""

mylist.remove(2);           #移除mylist內的2
print(mylist)
                            #mytuple無法remove

                            #不想被用戶更改時使用tuple,tuple運算速度也較list快