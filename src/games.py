import guessing_game
import hangman

def select_game():
    print("****************************")
    print("*Welcome to Nostalgic Game!*")
    print("****************************")

    print("(1) Guessing game, (2) Hangman")

    game = int(input("Select a game to play: "))

    if (1 == game):
        print("Guessing game selected")
        guessing_game.play()
    elif (2 == game):
        print("Hangman game selected")
        hangman.play()
    else:
        print("Invalid game")

if (__name__ == "__main__"):
    select_game()