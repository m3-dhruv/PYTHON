# Multiple inheritance
class Employee:
    def __init__(self, name):
        self.name = name

class Dancer:
    def __init__(self,dance):
        def __init__(self, Dance):
            self.dance = dance

class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance):
         self.name = name
         self.dance = dance

DE = DancerEmployee("Vaani", "Kathak")
print(DE.name)
print(DE.dance)