# Treasure Island Game

from turtle import right


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
# into to game
print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")
# first question, left continues game, right is game over.
step1 = input(
    'You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()


if step1 == "left":
    # second question, wait continues game, swim is game over
    step2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    # second question handling of input
    if step2 == "wait":
        # third question, yellow door wins game, anything else loses
        step3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        # third question handling of input
        if step3 == "yellow":
            print("You Won!")
        # third question game over
        elif step3 == "red":
            print("you lose")
            exit()
        # third question game over
        else:
            print("You Lost")
            exit()
    # second question game over
    else:
        print("game over")
        exit()
# first question game over
else:
    print("game over")
    exit()
