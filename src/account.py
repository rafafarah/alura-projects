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

    # private method
    def __has_enough_limit(self, value_to_withdraw):
        max_withdraw_value = self.balance + self.limit
        return (value_to_withdraw <= max_withdraw_value)

    def withdraw(self, value):
        if(self.__has_enough_limit(value)):
            self.__balance -= value
        else:
            print("Value {} is out of limit".format(value))

    def statement(self):
        print("Current balance for {} is {}".format(self.__holder, self.__balance))

    def transfer(self, dest, value):
        self.withdraw(value)
        dest.deposit(value)

    @property
    def number(self):
        return self.__number

    @property
    def holder(self):
        return self.__holder

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_code():
        return "001"
