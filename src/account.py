class Account:
    total_accounts = 0
    operation_tax = None

    def __init__(self, client, ag, number):
        self.balance = 0
        self.client = client
        self.ag =  ag
        self.number = number
        Account.total_accounts += 1
        Account.operation_tax = 30 / Account.total_accounts

    def transfer(self, value, dest):
        dest.deposit(value)

    def withdraw(self, value):
        self.balance -= value

    def deposit(self, value):
        self.balance += value

cc = Account(None, '00', '101')
