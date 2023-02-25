import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_prim = len(data[data["Primary Fur Color"] == "Gray"])
red_prim = len(data[data["Primary Fur Color"] == "Red"])
black_prim = len(data[data["Primary Fur Color"] == "Black"])
print(gray_prim)
print(red_prim)
print(black_prim)


data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_prim, red_prim, black_prim],
}

data_fr = pandas.DataFrame(data_dict)
data_fr.to_csv("colors_from_challenge_2.csv")
