import random
print("Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("correct! You guessed the number :D")
        break
    elif guess > secret_number:
        print("too high :(")
    else:
        print("Too low :(")

    attempts -= 1
    print("Attempts left:", attempts)
if attempts == 0: 
    print("Game Over")
    print("and the number was...", secret_number)
