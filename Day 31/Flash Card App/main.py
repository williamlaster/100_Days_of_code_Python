from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ------------------------- CSV DATA SETUP ---------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

# ------------------------ FRONT SIDE OF CARD ------------------------- #


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    timer = window.after(3000, func=flip_card)

# ------------------------ BACK SIDE OF CARD -------------------------- #


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526,
                background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
# Title text on the card
card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
# Word text on the card
card_word = canvas.create_text(
    400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# X Button
wrong_img = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong.grid(column=0, row=1)

# Check Button
right_img = PhotoImage(file="images/right.png")
correct = Button(image=right_img, highlightthickness=0, command=is_known)
correct.grid(column=1, row=1)

next_card()

window.mainloop()
