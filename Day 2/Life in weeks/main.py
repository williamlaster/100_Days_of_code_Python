# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

Time_left_mo = (90 * 12 - int(age) * 12)
Time_left_wk = (90 * 52 - int(age) * 52)
Time_left_day = (90 * 365 - int(age) * 365)

Message = f"You have {Time_left_day} days, {Time_left_wk} weeks, and {Time_left_mo} months left."

print(Message)
