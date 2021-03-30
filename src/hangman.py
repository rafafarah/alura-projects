def play():
    print("***************************")
    print("Welcome to the Hangman Game")
    print("***************************")

    secret_word = "banana"
    hanged = False
    won = False

    while (not hanged and not won):
        guess = input("\nYour guess: ")

        for letter in secret_word:
            if (guess == letter):
                print(guess, end="")
            else:
                print("_", end="")


if (__name__ == "__main__"):
    play()