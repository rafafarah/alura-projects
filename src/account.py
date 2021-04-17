class Account:
    def __init__(self, id):
        self.id = id
        self.balance = 0

    def __str__(self):
        return f">> id {self.id} balance {self.balance} <<"

    def deposit(self, value):
        self.balance += value
