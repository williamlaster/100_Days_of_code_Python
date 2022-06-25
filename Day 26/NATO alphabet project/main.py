import pandas

data = pandas.read_csv("NATO alphabet project/nato_phonetic_alphabet.csv")

nato_alphabet = pandas.DataFrame(data)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# Take nato_alphabet and create new dictionary with key as the letter,
# and value as the nato code for that letter
nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Take user input and make it caplitalized to be used against the Key in nato_dict
user_input = input("Enter a word: ").upper()
# Take each letter in the user_input and use it as the key to pull the value from nato_dict
nato_output = [nato_dict[letter] for letter in user_input]
# Print user_input with each letter converted to nato phonetic alphabet
print(nato_output)
