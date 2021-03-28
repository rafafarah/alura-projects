print("****************************")
print("Welcome to the Guessing Game")
print("****************************")

secret_number = 42

guess = int(input("Insert number: "))

if (secret_number == guess):
    print("Congrats")
else:
    if (guess > secret_number):
        print("Not this time... Your guess is too high.")
    else:
        print("Not this time... Your guess is too low.")
