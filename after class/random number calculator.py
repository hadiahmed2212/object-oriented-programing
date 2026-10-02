import random
import math

ur_number = random.randint(1, 10)
print("Your lucky number is:", ur_number)

# PART 3: Turn a random number into a random choice
choices = ["Play a game", "snakes and ladders", "Read a book", "have a nap"]
random_activity = random.choice(choices)
print("activity for today", random_activity)

print("Guess the secret number from 1 to 5!")
sct_number = random.randint(1, 5)

while True:
    guess = int(input("Enter your guess: "))

    if guess == sct_number:
        print("Correct! lets goo")
    else:
        print("NOPE! try again!")