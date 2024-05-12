# Define the parent class
class Animal:
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, name, hair_color):
        super().__init__(name)
        self.hair_color = hair_color


class Carnivore(Mammal):
    def __init__(self, name, hair_color, diet):
        super().__init__(name, hair_color)
        self.diet = diet


class Herbivore(Mammal):
    def __init__(self, name, hair_color, diet):
        super().__init__(name, hair_color)
        self.diet = diet



lion = Carnivore("Lion", "Golden", "Meat")
cow = Herbivore("Cow", "Brown", "Grass")

print("Name: " + lion.name)
print("Name: " + cow.name)