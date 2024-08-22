import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100.")

    user_guess = 0
    while user_guess != number_to_guess:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess and (number_to_guess - user_guess)>15:
            print("Too low! Try again.")
        elif user_guess < number_to_guess and (number_to_guess - user_guess)<15:
            print("low! Try again")
        elif user_guess > number_to_guess and(user_guess - number_to_guess)>15:
            print("Too high! Try again.")
        elif user_guess > number_to_guess and(user_guess - number_to_guess)<15:
            print("high! Try again")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            
guess_number()
