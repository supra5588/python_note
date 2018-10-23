class Student:
    def eat(self, name, age):
        print(name, ' can eat and he is ', age, ' years old')

    @staticmethod  # 靜態功能，方法
    def walk():  # 不使用self的寫法

        print('Student can walk')  # 此處無法調用name and age


Student.walk()
Student().eat('Lin', str(20))

student1 = Student()  # creat object name is student1
student1.eat('Lin1', str(20))
student1.walk()

student2 = Student()  # creat object name is student2
student2.eat('Lin2', str(20))
student2.walk()
