import random
import art
from game_data import data
import os


def pick_random_number():
    """Picks a random number between 0 and 49 to be passed to choose a random choice out of game data."""
    number = random.randint(0, 49)
    return number


def game():
    stop_playing = False
    correct = False
    score = 0
    # Initial Picks from game data
    pick1 = data[pick_random_number()]
    pick2 = data[pick_random_number()]
    while stop_playing == False:
        A = str(
            f"Compare A: {pick1['name']}, a {pick1['description']}, from {pick1['country']}.")
        B = str(
            f"Against B: {pick2['name']}, a {pick2['description']}, from {pick2['country']}.")

        # If both picks are the same pick again for pick2.
        while pick1 == pick2:
            pick2 = data[pick_random_number()]

        if pick1 != pick2:
            # Pick one, showing name, description, and country.
            print(art.logo)
            if correct == True:
                print((f"You're right! Current score is: {score}"))
            print(A)
            print(art.vs)
            # Pick two, showing name, description, and country.
            print(B)
            guess = input(
                "Who has more followers? Type 'A' or 'B': ").capitalize()
        # Get scores for picks from follower count
        pick1_score = pick1['follower_count']
        pick2_score = pick2['follower_count']

        if guess == "A" and pick1_score > pick2_score:
            os.system('cls')
            score += 1
            pick2 = data[pick_random_number()]
            correct = True

        elif guess == "B" and pick2_score > pick1_score:
            os.system('cls')
            score += 1
            # Change B to A
            pick1 = pick2
            # Draw a new value for B
            pick2 = data[pick_random_number()]
            correct = True
        # Guessed wrong, game is over
        else:
            os.system('cls')
            print(art.logo)
            print(f"Your score was: {score}")
            stop_playing = True
            return


game()
