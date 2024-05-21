# Create account class with 2 attributes - balance and account no,
# create method for debit, credit and printing the balance.

class Account():
    def __init__(self, bal, acc):
        self.balance = bal
        self.acc_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount,"Was debited")
        print("Total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount,"Was credited")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 118)
acc1.debit(1000)
acc1.credit(3000)
acc1.credit(50000)