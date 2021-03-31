def play():
    print("***************************")
    print("Welcome to the Hangman Game")
    print("***************************")

    secret_word = "banana"
    guessed_right = ["_", "_", "_", "_", "_", "_"]

    hanged = False
    won = False
    misses = 0

    print(guessed_right)
    while (not hanged and not won):
        guess = input("\nYour guess: ")
        guess = guess.strip().upper()

        if (guess in secret_word):
            index = 0
            for letter in secret_word:
                if (guess == letter):
                    guessed_right[index] = letter
                index += 1
        else:
            misses += 1
            print("Opps, you missed! {} guesses remaining.".format(6-misses))

        hanged = (misses == 6)

        won = ("_" not in guessed_right)

        print(guessed_right)

    if (hanged):
        print("Game Over!")
    else:
        print("You won!")


if (__name__ == "__main__"):
    play()