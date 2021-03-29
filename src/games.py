import guessing_game

def select_game():
    print("****************************")
    print("*Welcome to Nostalgic Game!*")
    print("****************************")

    print("(1) Guessing game")

    game = int(input("Select a game to play: "))

    if (game == 1):
        print("Guessing game selected")
        guessing_game.play()
    else:
        print("Invalid game")

if (__name__ == "__main__"):
    select_game()