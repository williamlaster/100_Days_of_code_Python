import pandas

data = pandas.read_csv("NATO alphabet project/nato_phonetic_alphabet.csv")

nato_alphabet = pandas.DataFrame(data)

nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


def input_to_nato_alphabet():
    # Take user input and make it caplitalized to be used against the Key in nato_dict
    user_input = input("Enter a word: ").upper()
    # Take each letter in the user_input and use it as the key to pull the value from nato_dict
    try:
        nato_output = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Only letters in the alphabet please.")
        input_to_nato_alphabet()
    else:
        # Print user_input with each letter converted to nato phonetic alphabet
        print(nato_output)


input_to_nato_alphabet()
