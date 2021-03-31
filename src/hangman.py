def play():
    print("***************************")
    print("Welcome to the Hangman Game")
    print("***************************")

    secret_word = "banana"
    guessed_right = ["_", "_", "_", "_", "_", "_"]

    hanged = False
    won = False

    print(guessed_right)
    while (not hanged and not won):
        guess = input("\nYour guess: ")
        guess = guess.strip()

        index = 0
        for letter in secret_word:
            if (guess.upper() == letter.upper()):
                guessed_right[index] = letter
            index += 1

        print(guessed_right)


if (__name__ == "__main__"):
    play()