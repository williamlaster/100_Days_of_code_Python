import turtle
import pandas


screen = turtle.Screen()
screen.title("Name the States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Pull all the states data from CSV file and place them in 'all_states' list
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
# Create empty list that will be filled by a user guessing a correct state
guessed_states = []

# Keep game running until all states have been guessed, or user types "Exit"
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="What's another State's name?").title()

    # Do nothing if guessing a state that has already been guessed
    if answer_state in guessed_states:
        pass

    # Draw State name on the map
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    # Exit the game and create a csv file with any missed states inside
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missed_States.csv")
        break
