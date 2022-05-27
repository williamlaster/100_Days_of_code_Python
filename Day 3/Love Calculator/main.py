# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name1_lowercase = name1.lower()
name2_lowercase = name2.lower()

count_L = (name1_lowercase.count("l") + name2_lowercase.count("l"))
count_O = (name1_lowercase.count("o") + name2_lowercase.count("o"))
count_V = (name1_lowercase.count("v") + name2_lowercase.count("v"))
count_E = (name1_lowercase.count("e") + name2_lowercase.count("e"))

count_love = (count_L + count_O + count_V + count_E)

count_T = (name1_lowercase.count("t") + name2_lowercase.count("t"))
count_R = (name1_lowercase.count("r") + name2_lowercase.count("r"))
count_U = (name1_lowercase.count("u") + name2_lowercase.count("u"))
count_E = (name1_lowercase.count("e") + name2_lowercase.count("e"))

count_true = (count_T + count_R + count_U + count_E)

score = int(str(count_true) + str(count_love))

if score >= 90 or score <= 10:
    print((f"Your score is {score}, you go together like coke and mentos."))
elif score >= 40 and score <= 50:
    print((f"Your score is {score}, you are alright together."))
else:
    print((f"Your score is {score}."))
