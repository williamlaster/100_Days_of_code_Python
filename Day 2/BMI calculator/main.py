# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

BMI = float(weight) / float(height) ** 2
BMI_int = int(BMI)

print("Your BMI is " + str(BMI_int))
