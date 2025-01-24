# class Firsst_class:
#     def __init__(self, name) -> None:
#         self.name = name
#         print(name)

# instance1 = Firsst_class("John")
# str1 = "Hello"
# print(type(str1))


class ClassA:
    def __init__(self, name):
        self.name = name
    def message(self):
            pass

class ClassB(ClassA):
    def message(self):
            print("Hello, my name is " + self.name)
var = ClassB("John")
var.message()
