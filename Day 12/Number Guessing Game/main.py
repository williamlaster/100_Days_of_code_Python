import random
import art
import os

# Number Guessing Game Objectives:


def pick_random_number():
    return random.randint(1, 100)


def evaluate_guess(player_guess, random_number, number_of_lives):
    if player_guess > random_number:
        print("Too high")
        return number_of_lives - 1
    elif player_guess < random_number:
        print("Too low")
        return number_of_lives - 1
    else:
        print(f"You got it! The answer was: {random_number}")
        return number_of_lives * 0


def game():
    lives = 0
    picked_number = pick_random_number()
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    # Use line below to see answer to help debugging issues
    print(f"The correct answer is {picked_number}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    else:
        lives = 0

    while lives != 0:
        print(f"You have {lives} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        lives = evaluate_guess(
            player_guess=guess, random_number=picked_number, number_of_lives=lives)

    if lives == 0 and guess != picked_number:
        print(f"You lost! The correct answer was: {picked_number}")
        play_again = input("Would you like to play again? Type 'y' or 'n': ")
        if play_again == "y":
            os.system('cls')
            game()
        else:
            os.system('cls')
    elif lives == 0 and guess == picked_number:
        play_again = input("Would you like to play again? Type 'y' or 'n': ")
        if play_again == "y":
            os.system('cls')
            game()
    else:
        os.system('cls')


game()
