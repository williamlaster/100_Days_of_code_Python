from tkinter import *


# Function called by button, this function converts the mile value to km and inputs the value to
# conversion_result label
def mile_to_km():
    mile = float(entry.get())
    value_in_km = mile * 1.609
    conversion_result.config(text=value_in_km)


window = Tk()
window.title("Mile/Kilometer Converter")
window.minsize(width=300, height=150)
window.config(padx=100, pady=50)

# Label just to make the layout easier for user to understand the conversion process
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

# Label to show the actual value of the conversion
conversion_result = Label(text="0")
conversion_result.grid(column=1, row=1)

# Label to show what unit we are converting to
converted_unit_label = Label(text="Km")
converted_unit_label.grid(column=2, row=1)

# Label to show what unit we are converting from
starting_unit_label = Label(text="Miles")
starting_unit_label.grid(column=2, row=0)

# Entry Box
entry = Entry(width=5)
entry.grid(column=1, row=0)
entry.insert(END, string="0")
# Gets text in entry
# print(entry.get())
entry.grid(column=1, row=0)


# calls miles_to_km() when pressed
button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)


window.mainloop()
