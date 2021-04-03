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

    def get_number(self):
        return self.__number

    def get_holder(self):
        return self.__holder

    def get_balance(self):
        return self.__balance

    def get_limit(self):
        return self.__limit

    def set_limit(self, limit):
        self.__limit = limit
