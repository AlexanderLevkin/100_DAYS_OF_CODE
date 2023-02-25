import turtle
import pandas

screen = turtle.Screen()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()


def paint_the_word(x_coord, y_coord):
    pen.hideturtle()
    pen.penup()
    pen.goto(x=x, y=y)
    pen.pendown()
    pen.write(answer_state, True, align="center", font=("Arial", 14, "normal"))

data_states = pandas.read_csv("50_states.csv")
data_states_name = data_states["state"].to_list()
guessed_list = []

save_states = {
    "Save states": guessed_list
}

while len(guessed_list) < 50:
    answer_state = screen.textinput(title=f"Guess the State {len(guessed_list)}/"
                                          f"50", prompt="What's another state's name?").capitalize()
    if answer_state == "Exit":
        missing_state = []
        for state in data_states_name:
            if state not in guessed_list:
                missing_state.append(state)
        print(missing_state)
        data = pandas.DataFrame(save_states)
        data.to_csv("Save_data_of_States_game.csv")
        break

    data_states = pandas.read_csv("50_states.csv")
    data_states_name = data_states["state"].to_list()

    for name in data_states_name:
        if answer_state == name:
            guessed_list.append(answer_state)
            coord = data_states[data_states["state"] == str(answer_state)]
            x = int(coord["x"])
            y = int(coord["y"])
            paint_the_word(x_coord=x, y_coord=y)


