# 1. DEFAULT CONSTRUCTOR

class Name :
    def  __init__(self):
        print("Hello Dhruv")

a = Name()

# 2. PARAMETERIZED CONSTRUCTOR

class Information:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Name: {self.name}, Age: {self.age}")

info = Information('Dhruv', 20)