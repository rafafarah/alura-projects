from abc import ABCMeta, abstractmethod

class Account(metaclass=ABCMeta):
    def __init__(self, id):
        self._id = id
        self._balance = 0

    def __str__(self):
        return f">> id {self._id} balance {self._balance} <<"

    def __eq__(self, other):
        if type(other) != Account:
            return False
        return self._id == other._id

    def __lt__(self, other):
        return self._id < other._id

    def deposit(self, value):
        self._balance += value

    @abstractmethod
    def after_mount():
        pass


class CheckingAccount(Account):
    def after_mount(self):
        self._balance -= 2

class SavingAccount(Account):
    def after_mount(self):
        self._balance *= 1.01
        self._balance -= 3
