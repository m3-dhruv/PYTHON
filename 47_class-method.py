class Employee:
    company = "India Tech"

    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

    @classmethod
    def newCompany(cls, newc):
        cls.company = newc

e1 = Employee()
e1.name = "Dhruv"
e1.show()
e1.newCompany("India cs")
e1.show()
print(Employee.company)