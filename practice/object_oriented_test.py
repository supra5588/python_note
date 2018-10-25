#object_oriented_ = 面向對象


class Student():                                   #Student is an object  ＝ 物件
    def eat(self):
        print("Student can eat")                   #eat(self) 僅代表Student底下的eat
    def study(self):
        print("Student can study")


qq = Student()
qq.study()


friut = "apple"
print(friut.upper())        #小寫轉大寫