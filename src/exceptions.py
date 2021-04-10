class NotEnoughBlanceError(Exception):
    def __init__(self, message='', balance=None, value=None):
        # # debbugger
        # import pdb
        # pdb.set_trace()
        self.balance = balance
        self.value = value
        msg = 'Not enough balance for the operation\n' \
            f'Current balance: {self.balance}, Value to withdraw: {self.value}'
        super(NotEnoughBlanceError, self).__init__(message or msg)
