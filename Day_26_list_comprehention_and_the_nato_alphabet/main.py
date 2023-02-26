numbers = [1, 2, 3]

new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Angela"
new_list = [l * 2 for l in name]
print(new_list)

new_list_range = [n * 2 for n in range(1, 5)]
print(new_list_range)
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

sort_names = [name.upper() for name in names if len(name) > 5]
print(sort_names)

