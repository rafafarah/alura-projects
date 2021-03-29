import random

def play():
    print("****************************")
    print("Welcome to the Guessing Game")
    print("****************************")

    secret_number = random.randrange(1, 101) # generate numbers between 1 and 101
    total_of_guess = 10
    score = 1000

    print("Select a difficulty level:")
    print("(1) Easy, (2) Normal, (3) Hard")

    level = int(input("Difficulty level: "))

    if (level == 1):
        total_of_guess = 20
    elif (level == 2):
        total_of_guess = 10
    elif (level == 3):
        total_of_guess = 5

    for guess_round in range(1, total_of_guess+1):
        print("Round {} of {}".format(guess_round, total_of_guess))
        guess = int(input("Insert number between 1 and 100: "))

        if (guess < 1 or guess > 100):
            print("Guesses must be between 1 and 100")
            continue

        guessed_right   = guess == secret_number
        is_higher       = guess > secret_number

        if (guessed_right):
            print("Congrats")
            print("Final score: {}".format(score))
            break
        else:
            if (is_higher):
                print("Not this time... Your guess is too high.")
            else:
                print("Not this time... Your guess is too low.")
            score -= (abs(secret_number - guess)) # penalty level is the distance from secret number

    if (guessed_right):
        print("Good job!")
    else:
        print("The secret number was {}. Good luck next time".format(secret_number))

if (__name__ == "__main__"):
    play()