# Create place holder to be replaced by a name later.
name_place_holder = '[name]'

# Create a list of names from a text file
with open(r'Input\Names\invited_names.txt') as names:
    names = names.readlines()

# Create the starting letter, so we can replace the name place holder with a name from the list we created
with open('Input\Letters\starting_letter.txt') as letter:
    starting_letter = letter.read()
    for name in names:
        # Clean the names to ensure they go into the letter properly
        stripped_name = name.strip()
        # Replace the place holder with the cleaned name, and save each name to its own text file.
        output_letter = starting_letter.replace('[name]', stripped_name)
        with open(f'Output\ReadyToSend\letter_{stripped_name}.txt', mode="w") as output:
            output.write(output_letter)
        # After this line a text file for every name should've been created inside \Output\ReadyToSend\
        # Example \Output\ReadyToSend\letter_Matthew.txt
