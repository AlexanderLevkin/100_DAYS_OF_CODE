from tkinter import *
import pandas
import random

# --------------------------- Functions -------------------------------- #
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_word, text=f"{current_card['French']}")


# --------------------------- Common things ----------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashcard project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

# --------------------------- Canvases ----------------------------------- #
image_card_back = PhotoImage(file="images/card_back.png")
image_card_front = PhotoImage(file="images/card_front.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
back_ground = canvas.create_image(400, 263, image=image_card_back)
front = canvas.create_image(400, 263, image=image_card_front)
canvas.grid(column=0, row=0, columnspan=2)

# --------------------------- Texts ----------------------------------- #
card_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="GG", font=("Arial", 60, "bold"), fill="black")

# --------------------------- Buttons ----------------------------------- #
image_right_button = PhotoImage(file="images/right.png")
button_right = Button(image=image_right_button, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=next_card)
button_right.grid(column=1, row=1)

image_wrong_button = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong_button, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=next_card)
button_wrong.grid(column=0, row=1)

next_card()

window.mainloop()
