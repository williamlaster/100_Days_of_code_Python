import art
import random
import os
############### Blackjack Project #####################


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(destination):
    dealt_card = random.choice(cards)
    return destination.append(dealt_card)


def score(cards):
    total = 0
    for card in cards:
        total += card
    if total == 21:
        total = 0
    elif total > 21:
        for card in cards:
            if card == 11:
                cards.remove(11)
                cards.append(1)
                total += card
    return total


def game():
    game_over = False
    players_cards = []
    computers_cards = []
    play = input(
        "Would you like to play a game of BlackJack? Type 'y' or 'n': ").lower()
    if play == "y":
        for _ in range(2):
            deal_card(players_cards)
            deal_card(computers_cards)
        print(art.logo)
    else:
        return

    while not game_over:

        if score(players_cards) == 0 or score(computers_cards) == 0 or score(players_cards) > 21 or score(computers_cards) > 21:
            game_over = True

        if game_over == False:
            print(
                f"    You're cards {players_cards} current score: {score(players_cards)}")
            print(
                f"    Computer's first {computers_cards[0]}")
            draw_card = input(
                "Type 'y' to get another card, type 'n' to pass: ").lower()
            if draw_card == "y":
                deal_card(players_cards)
                os.system('cls')
                print(art.logo)
            if draw_card == "n":
                while score(computers_cards) < 17 and not 0:
                    if score(computers_cards):
                        deal_card(computers_cards)
                game_over = True

    if game_over == True:
        os.system('cls')
        print(art.logo)
        print(
            f"    You're cards {players_cards} final score: {score(players_cards)}")
        print(
            f"    Computer's cards {computers_cards} final score: {score(computers_cards)}")
        if score(computers_cards) == score(players_cards):
            print("It's a tie!")
        if score(computers_cards) == 0:
            print("You lose, Computer has blackjack")
        if score(players_cards) == 0:
            print("You win, you have blackjack")
        if score(computers_cards) > 21:
            print("You win, Computer Bust!")
        if score(players_cards) > 21:
            print("You Bust! You Lose")
        if score(computers_cards) > score(players_cards) and score(computers_cards) < 21:
            print("Computer Wins")
        if score(players_cards) > score(computers_cards) and score(players_cards) < 21:
            print("You Win!")

    play_agian = input("Would you like to play again? Type'y' or 'n': ")

    if play_agian == "y" and game_over == True:
        os.system('cls')
        return game()
    else:
        os.system('cls')


game()
