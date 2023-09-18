from art import logo
import random

EASY_LEVEL_TURN=10
HARD_LEVEL_TURN=5

print(logo)

def check_answer(guess,answer,turn):

    if(guess > answer):
        print("high")
        return turn-1
    elif(guess < answer):
        print("low")
        return turn-1
    else:
        print(f"You have got it! The answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if(level=="easy"):
        return EASY_LEVEL_TURN
    elif(level=="hard"):
        return HARD_LEVEL_TURN
    else:
        print("Wrong input, Try again")
    
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    actual_number=random.randint(1,100)

    turns=set_difficulty()
    guess=0

    while guess!=actual_number:

        print(f"You have {turns} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))
        
        turns=check_answer(guess,actual_number,turns)

        if turns==0:
            print("You've run out of guesses, you lose.")
            return
        elif guess!=actual_number:
            print("Guess again.")


game()