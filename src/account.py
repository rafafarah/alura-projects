class Account:
    def __init__(self, id):
        self._id = id
        self._balance = 0

    def __str__(self):
        return f">> id {self._id} balance {self._balance} <<"

    def deposit(self, value):
        self._balance += value


class CheckingAccount(Account):
    def after_mount(self):
        self._balance -= 2

class SavingAccount(Account):
    def after_mount(self):
        self._balance *= 1.01
        self._balance -= 3
