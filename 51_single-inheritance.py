class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Bark !!")

a = Animal("Dog")
a.sound()

d = Dog("Dog", "haskey")
d.sound()