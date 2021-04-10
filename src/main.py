import sys
from cliente import Client
from account import Account
from exceptions import NotEnoughBalanceError, FinanceOperationError
from filereader import FileReader

def main():

    accounts = []
    while(True):
        try:
            name = input('Client name:\n')
            ag = int(input('Client ag:\n'))
            # debbugger
            # import pdb
            # pdb.set_trace()
            number = int(input('Client number:\n'))
            client = Client(name, None, None)
            acc = Account(client, ag, number)
            accounts.append(acc)
        except KeyboardInterrupt:
            print(f'\n\n{len(accounts)}(s) accounts created')
            sys.exit()


def test_account_operations():
    acc1 = Account(None, 111, 222)
    acc2 = Account(None, 112, 223)
    try:
        acc1.withdraw(10)
        acc1.deposit(50)
        acc1.transfer(-50, acc2)
        print('Balance acc1: ', acc1.balance)
        print('Balance acc2: ', acc2.balance)

    except FinanceOperationError as E:
        print(E)
    except ValueError as E:
        print(E)


def test_file_reader():
    # try:
    #     reader = FileReader('file.txt')
    #     reader.read_next_line()
    #     reader.read_next_line()
    #     reader.read_next_line()
    # # except IOError:
    # #     print('IOError exception')
    # finally:
    #     # check if variable reader exists
    #     # this might be dangerous if other reader
    #     # has been declared before
    #     if ('reader' in locals()):
    #         reader.close()

    # ensure that resources will be freed properly
    with FileReader('file.txt') as reader:
        reader.read_next_line()

if(__name__ == '__main__'):
    main()