from account import Account

ac1 = Account(15)
ac1.deposit(500)

ac2 = Account(476585)
ac2.deposit(1000)

# list element refer to original object, i.e., accounts[0] == ac1, accounts[1] == ac2
accounts = [ac1, ac2]
for ac in accounts:
    print(ac)
