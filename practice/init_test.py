# init = initialize = 初始化

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name, 'can walk')
        print(self.name, 'is', self.age)

s1 = Student('Lin', '20')
s1.walk()


s2 = Student('Ace', '22')
s2.walk()
