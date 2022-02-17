class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        self.balance += money
    def withdraw(self, money):
        if self.balance < money:
            print("insuffcient funds")
        else:
            self.balance -= money
    def show(self):
        print(self.owner + " " + str(self.balance))
    
p1 = Account("MyName", 500)
p1.show()
p1.deposit(1500)
p1.show()
p1.withdraw(600)
p1.withdraw(1000)
p1.show()
p1.withdraw(1000)
        