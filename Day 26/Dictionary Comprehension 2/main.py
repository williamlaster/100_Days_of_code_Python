weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

# Temp C to F conversion is C * 9/5 + 32 = F
weather_f = {day: temperature * 9/5 +
             32 for (day, temperature) in weather_c.items()}


print(weather_f)
