print("****************************")
print("Welcome to the Guessing Game")
print("****************************")

secret_number = 42

total_of_guess = 3
guess_round = 1

while (total_of_guess >= guess_round):
    print("Round", guess_round, "of", total_of_guess)
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

    guess_round += 1
