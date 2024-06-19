import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def check_if_11_or_1(cards):
    """Decides if we should count '11' as '1'."""
    if 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1
    return cards


def find_probability(array, cards):
    """Finds probability of occurrence for each card in the deck."""
    probability_dict = {}
    if sum(cards) > 10:
        array[0] = 1
    for card in set(array):
        probability = round((array.count(card)/len(array))*100)
        probability_dict[card] = probability
    return probability_dict


def computer_logic(computer_cards):
    """Defines how computer decides it should take a card."""
    probability_to_lose = 0
    computer_score = sum(computer_cards)
    if computer_score <= 11:
        return True
    elif 11 < computer_score < 21:
        probability_dict = find_probability(cards, computer_cards)
        for number in probability_dict.keys():
            if number > 21 - computer_score:
                probability_to_lose += probability_dict[number]
    if probability_to_lose < 70:
        return True
    return False


def user_logic(your_cards):
    """Defines whether we can offer a user another card."""
    gimme_more = True
    while sum(your_cards) <= 21 and gimme_more:
        should_continue = input(
            "Type 'y' to get another card, type 'n' to pass: "
        ).lower()
        if should_continue == "y":
            if sum(your_cards) > 10:
                cards[0] = 1
            your_cards.append(random.choice(cards))
            your_cards = check_if_11_or_1(your_cards)
            print(f"Your_cards: {your_cards}")
        elif should_continue == "n":
            gimme_more = False
        else:
            print("You've typed the wrong letter.")
    return your_cards


def compare_cards(computer_cards, player_hand):
    """Compares computer and user final card sets."""
    if sum(player_hand) > 21 and sum(computer_cards) > 21:
        return "Both of you have lost."
    elif sum(player_hand) > 21:
        return "You've lost."
    elif sum(computer_cards) > 21:
        return "You win! Congrats!"
    elif sum(player_hand) == sum(computer_cards):
        return "It's a draw"
    elif sum(player_hand) > sum(computer_cards):
        return "You win! Congrats!"
    return "You've lost."


def black_jack(cards):
    """Main black jack function. Contains all the logic of the game."""
    decision = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': "
    ).lower()
    if decision == 'y':
        print(logo)
        your_cards = [random.choice(cards) for _ in range(2)]
        print(f"Your_cards: {your_cards}")
        computer_cards = [random.choice(cards) for _ in range(2)]
        print(f"Opponent's first card: {computer_cards[0]}")
        while computer_logic(computer_cards):
            computer_cards.append(random.choice(cards))
            computer_cards = check_if_11_or_1(computer_cards)
        player_hand = user_logic(your_cards)
        print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
        print(f"Computer final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print(compare_cards(computer_cards, player_hand))
        black_jack(cards)
    elif decision == "n":
        return
    else:
        print("You've typed the wrong letter.")
        black_jack(cards)



if __name__ == '__main__':
    black_jack(cards)

