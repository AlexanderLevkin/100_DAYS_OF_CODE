import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])

new_data = data.to_dict()
print(new_data)

convert_to_list = data["temp"].to_list()
print(len(convert_to_list))


# Calculate the average when we use python without padnas
def average(list):
    av = sum(list) / len(list)
    return av


average_list = average(convert_to_list)

print(round(average_list, 2))

# Calculate the average when we use python with padnas

print(data["temp"].mean())


# Find the max value when using python without pandas
def max_value_from_list(lists):
    list_max = 0
    for item in lists:
        if item > list_max:
            list_max = item
    print(list_max)


max_value_from_list(convert_to_list)

# Find the max value when using python with pandas

print(data["temp"].max())

# Get data in columns

print(data["condition"])
print(data.condition)

# Get data in row
print(data[data["day"] == "Monday"])

# Find the row with max value of "temp"
max_day = data["temp"].max()

print(data[data["temp"] == max_day])

# Find the temp in "monday" row *
monday = data[data["day"] == "Monday"]
temp_of_monday_far = int(monday["temp"]) * 9/5 + 32
print(temp_of_monday_far)

# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [75, 56, 65]
}

data_fr = pandas.DataFrame(data_dict)
print(data_fr)
data_fr.to_csv("new_data_2.csv")

