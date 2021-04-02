import random

def play():
    print_welcome_message()
    secret_word = load_secret_word()

    guessed_right = initialize_guessed_right(secret_word)
    print(guessed_right)

    hanged = False
    won = False
    misses = 0

    while (not hanged and not won):
        guess = read_guess()

        if (guess in secret_word):
            fill_guessed_right(guess, secret_word, guessed_right)
        else:
            misses += 1
            print("Opps, you missed! {} guesses remaining.".format(6-misses))

        hanged = (misses == 6)
        won = ("_" not in guessed_right)
        print(guessed_right)

    if (hanged):
        print_game_over()
    else:
        print_win_message()

def print_welcome_message():
    print("***************************")
    print("Welcome to the Hangman Game")
    print("***************************")

def load_secret_word():
    fileword = open("words.txt", "r")
    words = []

    for line in fileword:
        words.append(line.strip())

    fileword.close()
    fileindex = random.randrange(0, len(words))
    secret_word = words[fileindex].upper()
    return secret_word

def initialize_guessed_right(secret):
    return ["_" for letter in secret]

def read_guess():
    guess = input("\nYour guess: ")
    return guess.strip().upper()

def fill_guessed_right(guess, secret_word, guessed_right):
    index = 0
    for letter in secret_word:
        if (guess == letter):
            guessed_right[index] = letter
        index += 1


def print_game_over(secret_word):
    print("Game Over!")
    print("The secret word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def print_win_message():
    print("You won!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def draw_hangman(misses):
    print("  _______     ")
    print(" |/      |    ")

    if(misses == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(misses == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(misses == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(misses == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(misses == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(misses == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (misses == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    play()
