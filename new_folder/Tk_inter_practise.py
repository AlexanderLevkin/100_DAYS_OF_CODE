from tkinter import *

window = Tk()
window.title("My first GUI programm")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label

my_label = Label(text="I am a lable", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text", padx=50, pady=50)


# Button


# Entry

input = Entry(width=50)
input.grid(column=3, row=3)


def button_click():
    my_label["text"] = input.get()


button = Button(text="click me", command=button_click)
button.grid(column=1, row=1)

new_button = Button(text="New_button", command=button_click)
new_button.grid(column=2, row=0)


window.mainloop()
