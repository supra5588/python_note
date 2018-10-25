# inheritance        繼承

class Fater:
    def eat(self):
        print("I can eat")


class Mother():
    def walk(self):
        print("Walk like son")


class Son(Fater, Mother):  # inheritance => 繼承Father屬性
    def eat(self):
        print("eat like son")


littleLin = Son()
littleLin.walk()
