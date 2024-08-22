import random

def guessing_game():
    num1 = random.randint(0,1000)
    attempts= 0
    user_guess = 9999
    while num1 != user_guess :
        user_guess = int(input("Guess the Number: "))

        attempts = attempts + 1

        if user_guess < num1 :
            print("low , try again")
        elif user_guess > num1:
            print("high , try again")
        else:
            print("Congratulations, you have successfully guessed the number")
            print("You have taken",attempts,"attempts to guess the number")

guessing_game()
