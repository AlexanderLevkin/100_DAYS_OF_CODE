import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_number = random.randint(0, len(names))
print(f"{names[random_number]} is going to buy the meal today!")

# fruits = ["Strawberries", "Nectarines", "Apples"]
# vegetables = ["Spinach", "Kale", "Tomatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[0][0], dirty_dozen[0][1], dirty_dozen[0][2])

