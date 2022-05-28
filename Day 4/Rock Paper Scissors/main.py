import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
player_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

elements = [rock, paper, scissors]

computer_choice = random.randint(0, 2)

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print("You chose:")
    print(elements[player_choice])

    print("Computer chose:")
    print(elements[computer_choice])

    if player_choice == 0 and computer_choice == 2:
        print("you won!")
    elif player_choice == 1 and computer_choice == 0:
        print("you won!")
    elif player_choice == 2 and computer_choice == 1:
        print("you won!")
    elif player_choice == computer_choice:
        print("It's a draw")
    else:
        print("you lost!")
