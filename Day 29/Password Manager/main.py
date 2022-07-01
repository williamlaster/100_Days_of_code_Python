from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def make_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(END, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        fields = messagebox.showinfo(
            title="Field Left Empty", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(
            title=website_entry.get(), message=f"These are the details entered: \nEmail: {email_entry.get()}\nPassword: {password_entry.get()}\n Is it ok to save?")

        if is_ok == True:
            data = open("data.txt", "a")
            data.write(
                f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            data.close()
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
background_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background_image)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

# Email/Username Label
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)

# Password Label
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

# Website Entry Box
website_entry = Entry(width=42)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

# Email/Username Entry Box
email_entry = Entry(width=42)
email_entry.insert(END, string="test@email.com")
email_entry.grid(column=1, row=2, columnspan=2)

# Password Entry
password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

# Password Generate Button
generate_password = Button(text="Generate Password",
                           command=make_password, width=14)
generate_password.grid(column=2, row=3)

# Add Button
add = Button(text="Add", command=save, width=36)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
