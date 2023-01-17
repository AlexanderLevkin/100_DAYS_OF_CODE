row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0]) #Элемент во вложенном списке
vertical = int(position[1]) #вложенный список

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
# if position[0] == "1" and position[1] == "1":
#     row1 = ["X", row1[1], row1[2]]
# elif position[0] == "1" and position[1] == "2":
#     row2 = ["X", row1[1], row1[2]]
# elif position[0] == "1" and position[1] == "3":
#     row3 = ["X", row1[1], row1[2]]
# if position[0] == "2" and position[1] == "1":
#     row1 = [row1[0], "X", row1[2]]
# elif position[0] == "2" and position[1] == "2":
#     row2 = [row1[0], "X", row1[2]]
# elif position[0] == "2" and position[1] == "3":
#     row3 = [row1[0], "X", row1[2]]
# if position[0] == "3" and position[1] == "1":
#     row1 = [row1[0], row1[1], "X"]
# elif position[0] == "3" and position[1] == "2":
#     row2 = [row1[0], row1[1], "X"]
# elif position[0] == "3" and position[1] == "3":
#     row3 = [row1[0], row1[1], "X"]
# print(f"{row1}\n{row2}\n{row3}")
