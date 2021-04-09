class Account:
    total_accounts = 0
    operation_tax = None

    def __init__(self, client, ag, number):
        self.__balance = 0
        self.__ag = 0
        self.__number = 0

        self.client = client
        self.__set_ag(ag)
        self.__set_number(number)

        Account.total_accounts += 1
        Account.operation_tax = 30 / Account.total_accounts

    @property
    def ag(self):
        return self.__ag

    def __set_ag(self, ag):
        if (not isinstance(ag, int)):
            raise TypeError('Attribute must be an integer', ag)
        if (ag <=0):
            raise ValueError('Attribute must be greater than zero')

        self.__ag = ag

    @property
    def number(self):
        return self.__number

    def __set_number(self, number):
        if (not isinstance(number, int)):
            raise TypeError('Attribute must be an integer')
        if (number <=0):
            raise ValueError('Attribute must be greater than zero')

        self.__number = number

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance):
        if (not isinstance(balance, int)):
            raise TypeError('Attribute must be an integer')
        if (number <0):
            raise ValueError('Attribute must be positive')

        self.__balance = balance

    def transfer(self, value, dest):
        dest.deposit(value)

    def withdraw(self, value):
        self.__balance -= value

    def deposit(self, value):
        self.__balance += value

