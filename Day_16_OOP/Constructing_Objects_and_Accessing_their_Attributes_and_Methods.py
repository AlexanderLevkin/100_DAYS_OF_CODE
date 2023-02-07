from prettytable import PrettyTable

# from turtle import Turtle, Screen
# import tkinter as TK
#
# timmy = Turtle()
# print(timmy)
#
# timmy.shape("turtle")
# timmy.color("DarkSeaGreen")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
