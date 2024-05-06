class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
P = Person("Dhruv", 20)
print(P.__dict__)