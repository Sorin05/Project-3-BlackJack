''' game of blackjack'''

import random
import os
from time import sleep
from art import LOGO
from rules import RULES


def deal_card():
    ''' Returns a  random card from the deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    '''Take a list of cards and return the score calculated from the cards'''

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    ''' Compares the score and determines a winner or a draw'''

    if user_score > 21 and computer_score > 21:
        return "You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "You lose, House has BlackJack 😱"
    elif user_score == 0:
        return "You have BlackJack, YOU WIN 😎"
    elif user_score > 21:
        return "You went over. BUST 😭"
    elif computer_score > 21:
        return "House went BUST. YOU WIN 😁"
    elif user_score > computer_score:
        return "YOU WIN 😃"
    else:
        return "YOU LOSE 😤"


def play_game():
    ''' It Plays the game'''

    print(LOGO)
    sleep(2.5)
    print(RULES)
    sleep(3)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        sleep(2)
        print(f" Your Cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to HIT, type 'n' to STAND: "
            )
            sleep(2)
            if user_should_deal == "y":
                user_cards.append(deal_card())
            elif user_should_deal == "n":
                while computer_score != 0 and computer_score < 17:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)
                if computer_score >= 17:
                    is_game_over = True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid option")

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"""  Computer's final hand: {computer_cards},
        final score: {computer_score}"""
    )
    print(compare(user_score, computer_score))


def validate_input(user_input):
    ''' It validates wrong user input'''
    y_n = ("y", "n")
    user_response = user_input.lower().strip()
    while (
        not user_response.isalpha()
        or user_response not in y_n
    ):
        print("Please input 'y' or 'n'")
        user_response = input().lower().strip()
        continue

    if user_response == "n":
        return False

    return True


def main():
    ''' main function'''
    user_answer = True
    while user_answer:
        sleep(1.5)
        response = input(
            "Do you want to play a game of BlackJack? Type 'y' or 'n':")
        sleep(2)
        result = validate_input(response)
        os.system('cls' if os.name == 'nt' else 'clear')
        if result:
            play_game()
        else:
            print("Goodbye")
            sleep(1.5)
            user_answer = False


main()
