import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


grey_squirrels = len(data[data["Primary Fur Colors"] == "Gray"])

red_squirrels = len(data[data["Primary Fur Colors"] == "Cinnamon"])

black_squirrels = len(data[data["Primary Fur Colors"] == "Black"])

print(red_squirrels)
print(black_squirrels)
print(grey_squirrels)


data_dictionary = {
    "Fur Color": ["Grey", "Black", "Red"],
    "Count": [grey_squirrels, black_squirrels, red_squirrels]
}

df = pandas.DataFrame(data_dictionary)

df.to_csv("squirrel_count.csv")
