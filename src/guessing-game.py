print("****************************")
print("Welcome to the Guessing Game")
print("****************************")

secret_number = 42

total_of_guess = 3

for guess_round in range(1, total_of_guess+1):
    print("Round {} of {}".format(guess_round, total_of_guess))
    guess = int(input("Insert number: "))

    guessed_right   = guess == secret_number
    is_higher       = guess > secret_number

    if (guessed_right):
        print("Congrats")
        break
    else:
        if (is_higher):
            print("Not this time... Your guess is too high.")
        else:
            print("Not this time... Your guess is too low.")
