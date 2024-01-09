from random import randint
from art import logo,high_logo,low_logo,great_logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0
def check_ans(guess,answer,turns):
    """checks answer against guess. returns the number of turns remaining."""
    if guess > answer:
        print(high_logo)
        print("Too High.")
        return turns - 1
    elif guess < answer:
        print(low_logo)
        print("Too Low.")
        return turns - 1
    else:
        print(great_logo)
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty Type 'easy' or 'hard': ").lower()
    if level == "easy":
        global turns
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def play_game():
    print(logo)
    print("welcome to the number guessing Gmae!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}.")
    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_ans(guess=guess, answer=answer,turns=turns)
        if turns == 0:
            print("you've run out of guesses!")
            return
        elif guess != answer:
            print("guess again.")

play_game()