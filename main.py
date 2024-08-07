import random
from art import logo, vs
from game_data import data


def items_set(item):
    """Function will return two different items from the game directory"""
    new_set = []
    item_a = item
    new_set.append(item_a)
    item_b = random.choice(data)
    while item_a == item_b:
        item_b = random.choice(data)
    new_set.append(item_b)
    return new_set


def higher_lower(items):
    """Function will check the higher score and return A or B"""
    if items[0]['follower_count'] > items[1]['follower_count']:
        return 'a'
    else:
        return 'b'


def higher_lower_game():
    # Set up starting score
    score = 0
    # Random choose the first item
    first_item = random.choice(data)
    while True:
        # Get the items to compare from data directory
        items = items_set(first_item)
        # Check the higher count of followers
        more_followers = higher_lower(items)
        # Testing code
        # for item in items:
        #     print(item)
        # print(f"Winner: {more_followers}")
        # Game stage
        print(logo)
        print(f"Compare A: {items[0]['name']}, a {items[0]['description']}, "
              f"from {items[0]['country']}")
        print(vs)
        print(f"Against B: {items[1]['name']}, a {items[1]['description']}, "
              f"from {items[1]['country']}")
        answer = input("Who has nore followers? Type 'A' or 'B: ")
        if answer.lower() == more_followers:
            score += 1
            if more_followers == "b":
                first_item = items[1]
            print(f"You're right! Current Score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final Score: {score}.")
            return


higher_lower_game()
while input("Want play again? Type 'y'") == 'y':
    higher_lower_game()
