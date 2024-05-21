# Creat a student class that takes name & marks of 3 subject as arguments in constructor.
# then creat a method to print the everage.

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def everage(self):
        sum = 0
        for i in self.marks:
            sum += i
            ave = sum / 3
        print("hello", self.name, "Your average score is :", ave)
    
S1 = Student("Dhruv", [80, 90, 100])
S1.everage()

S2 = Student("krishna", [88, 91, 79])
S2.everage()