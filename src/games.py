import guessing_game

print("****************************")
print("*Welcome to Nostalgic Game!*")
print("****************************")

print("(1) Guessing game")

game = int(input("Select a game to play:"))

if (game == 1):
    print("Guessing game selected")
else:
    print("Invalid game")