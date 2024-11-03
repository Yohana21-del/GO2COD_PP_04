import random

random_number = random.randint(1, 100)

guess = None
attempts = 0

while guess != random_number:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess > random_number:
        print("Too high!")
    elif guess < random_number:
        print("Too low!")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
