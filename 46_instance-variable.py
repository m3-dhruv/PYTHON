# class variable

class MyClass:
    class_variable = 0

    def __init__(self):
        MyClass.class_variable += 1
        print(MyClass.class_variable)

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

print(obj1)
print(obj2)
print(obj3)

# instance variable

class My_Class:
    def __init__(self, name):
        self.name = name
        print(self.name)

objinstance1 = My_Class("dhruv")
objinstance2 = My_Class("tony")
objinstance3 = My_Class("captan")

print(objinstance1)
print(objinstance2)
print(objinstance3)