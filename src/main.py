from account import Account, CheckingAccount, SavingAccount

def test_account_list():
    ac1 = Account(15)
    ac1.deposit(500)

    ac2 = Account(476585)
    ac2.deposit(1000)

    # list element refer to original object, i.e., accounts[0] == ac1, accounts[1] == ac2
    accounts = [ac1, ac2]
    for ac in accounts:
        print(ac)

def test_polymorphism():
    ac15 = CheckingAccount(15)
    ac15.deposit(1000)

    ac16 = SavingAccount(16)
    ac16.deposit(1000)

    acs = [ac15, ac16]

    for ac in acs:
        ac.after_mount()
        print(ac)

# avoid array unless performance is needed
def test_array():
    import array as arr
    ar = arr.array('d', [1, 1.5])
    print(ar)

def test_numpy():
    import numpy as np
    np_array = np.array([1, 1.3])
    print(np_array)
    np_array += 3
    print(np_array)

def test_position_in_list():
    ages = [15, 87, 32, 65, 56, 32, 49, 37]
    for i in range(len(ages)):
        print(i, ages[i])

    l = list(enumerate(ages))
    print(l)

    for index, age in enumerate(ages):
        print(index, age)


if __name__ == "__main__":
    test_position_in_list()