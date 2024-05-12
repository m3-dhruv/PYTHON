class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Meow!")

roger = Dog("Roger", "Golden Retriever")
whiskers = Cat("Whiskers", "Siamese")

print("Name: " + roger.name)
roger.make_sound()

print("Name: " + whiskers.name)
whiskers.make_sound()