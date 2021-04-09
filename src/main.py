import sys
from cliente import Client
from account import Account

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


if(__name__ == '__main__'):
    main()