import sys
from cliente import Client
from account import Account
from exceptions import NotEnoughBlanceError

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
    try:
        acc1 = Account(None, 111, 222)
        acc2 = Account(None, 112, 223)

        acc1.deposit(50)
        acc1.transfer(-50, acc2)
        print('Balance acc1: ', acc1.balance)
        print('Balance acc2: ', acc2.balance)

    except NotEnoughBlanceError as E:
        print(E.args)
    except ValueError as E:
        print(E)


if(__name__ == '__main__'):
    main()