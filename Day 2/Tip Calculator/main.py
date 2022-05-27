# Tip Calculator

print("Welcome to the tip calculator.")

# Get Bill total from user as a floating point number
Totalbill = float(input("What was the total bill? $"))

# Ask user desired tip percentage and save as a float
Tip_Percentage = float(
    input("What percentage tip would you like to give? 10, 12, or 15? "))

# Ask how many ways the bill is being split. Save as an integer
Split = int(input("How many people splitting the bill? "))

# Convert Tip from percentage to value to multiply Totalbill by.
Tip = (0.01 * Tip_Percentage + 1)

# Calculate amount owed with tip by each person, round to 2 decimal places
Amount_owed = "{:.2f}".format(Totalbill * Tip / Split)

# Print the amount each person should pay
print(f"Each person should pay: ${Amount_owed}")
