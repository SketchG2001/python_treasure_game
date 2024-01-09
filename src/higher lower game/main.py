import random

from art import logo,vs
from game_data import data

# format the account data into printable format.
def fromat_account(account):
    """Takes the account data returns the printable format."""
    account_name = account_a["name"]
    account_descr = account_a["description"]
    account_country = account_a["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"
def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display the art.
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    # generate the random account from the game data.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {fromat_account(account_a)}.")
    print(vs)
    print(f"Against B: {fromat_account(account_b)}.")

    # ask user for guess.
    guess = input("WHo has more followers? Type 'A' or 'B': ").lower()
    # check if user is correct.
    # get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess=guess, a_followers=a_follower_count, b_followers=b_follower_count)

    #  user if statement to check if user is correct.
    if is_correct:
        score += 1
        print(f"You're right! current score is {score}")
    else:
        game_should_continue = False
        print(f"Sorry, thst's wrong. Final score is {score}.")
    # give user feedback on their guess.
    # score keeping
    #  make the game repeatable
    # making account at position B become the next account at position A.
    # clear the screen between each rounds.
