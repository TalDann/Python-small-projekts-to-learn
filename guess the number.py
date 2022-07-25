import random

guessing_number = random.randint(1, 25)

times_guessed = 0

guess = 0

print("Guess the Number (1-25)")

while guess != guessing_number:

    guess = input()
    times_guessed += 1
    guess = int(guess)
    if guess < guessing_number:
        print("the number is too small")
    if guess > guessing_number:
        print("the number is too big")
print("You got it! Times guessed:" + str(times_guessed))
