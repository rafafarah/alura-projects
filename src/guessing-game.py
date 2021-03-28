print("****************************")
print("Welcome to the Guessing Game")
print("****************************")

secret_number = 42

guess = int(input("Insert number: "))

guessed_right   = guess == secret_number
is_higher       = guess > secret_number

if (guessed_right):
    print("Congrats")
else:
    if (is_higher):
        print("Not this time... Your guess is too high.")
    else:
        print("Not this time... Your guess is too low.")
