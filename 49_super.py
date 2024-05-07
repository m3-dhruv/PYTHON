class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Manager(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

emp1 = Employee("Dhruv", 118)
emp2 = Manager("Ronny", 119, "Python")

print(emp1.name, emp1.id)
print(emp2.name, emp2.id, emp2.lang)