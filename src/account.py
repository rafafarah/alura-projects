class Account:

    def __init__(self, number, holder, balance, limit = 1000.0):
        print("Building object.. {}".format(self))
        # declaring private attributes with __attribute
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        self.__balance -= value

    def statement(self):
        print("Current balance for {} is {}".format(self.__holder, self.__balance))

    def transfer(self, dest, value):
        self.withdraw(value)
        dest.deposit(value)
