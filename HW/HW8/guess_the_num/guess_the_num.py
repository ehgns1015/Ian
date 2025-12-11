import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {number}.")
                print(f"You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

guess_the_number()
