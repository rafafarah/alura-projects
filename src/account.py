class Account:

    def __init__(self, number, holder, balance, limit = 1000.0):
        print("Building object.. {}".format(self))
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value

    def statement(self):
        print("Current balance for {} is {}".format(self.holder, self.balance))