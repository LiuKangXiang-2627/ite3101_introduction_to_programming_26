from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
guess = int(input("Your guess: "))
while guesses_left > 0 :
    print(random_number)
    if guess = random_number:
        print("You win!")
        break
    guesses_left = guesses_left - 1
    else:
        print()
