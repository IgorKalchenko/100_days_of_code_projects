from random import choice

from .art import logo, vs
from .game_data import data

your_score = 0
first_account = choice(data)


def compare_followers(first_account, second_account, your_choice):
    """
    Takes two accounts and user's choice.
    Returns 'True' if user guessed right and 'False' if not.
    """
    if first_account["follower_count"] > second_account["follower_count"]:
        return your_choice == "A"
    else:
        return your_choice == "B"


def format_data(account):
    """Format the account data into printable format."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description} from {country}"


def main_game(first_account):
    """Contains main logic of the game."""
    print(logo)
    print(f"Compare A: {format_data(first_account)}.")
    print(vs)
    second_account = choice(data)
    while second_account == first_account:
        second_account = choice(data)
    print(f"Against B: {format_data(second_account)}.")
    your_choice = input("Who has more followers? Type A or B: ").capitalize()
    while your_choice not in ["A", "B"]:
        your_choice = input(
            "You've typed in the wrong letter. Please, type A or B: "
        ).capitalize()
    if compare_followers(first_account, second_account, your_choice):
        global your_score
        your_score += 1
        print(f"You're right. Current score: {your_score}")
        main_game(second_account)
    else:
        print(f"Sorry, that's wrong. Final score: {your_score}")
        return

if __name__ == "__main__":
    main_game(first_account)
