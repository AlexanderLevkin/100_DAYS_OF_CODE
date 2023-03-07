from tkinter import *
from tkinter import messagebox
import random
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters + symbols + numbers) for char in range(nr_letters)]

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_field.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    value_pass = pass_field.get()
    value_username_field = username_field.get()
    value_website_field = website_field.get()

    is_ok = messagebox.askokcancel(title=value_website_field, message=f"These are the details entered: \nEmail:"
                                                                      f"{value_username_field}\nPassword:"
                                                                      f" {value_pass}\nIs"
                                                                      f"it ok to save?")
    if len(value_pass) == 0:
        messagebox.showinfo(title="Warning", message="Please fill the Password")
    elif len(value_website_field) == 0:
        messagebox.showinfo(title="Ooooops", message="Please fill the Website")
    else:
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{value_website_field} | {value_username_field} | {value_pass}\n")
            messagebox.showinfo(title="Success", message="Your credentials have saved")
            website_field.delete(0, END)
            pass_field.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Common

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0)

# Text
website_text = Label(text="Website:", font=("Arial", 18))
website_text.grid(column=0, row=1)

email_username_text = Label(text="Email/Username:", font=("Arial", 18))
email_username_text.grid(column=0, row=2)

password_text = Label(text="Password:", font=("Arial", 18))
password_text.grid(column=0, row=3)

# Fields
website_field = Entry(width=35)
website_field.grid(column=1, row=1, columnspan=2)
website_field.focus()

username_field = Entry(width=35)
username_field.grid(column=1, row=2, columnspan=2)
username_field.insert(0, "arterial888@gmail.com")

pass_field = Entry(width=18)
pass_field.grid(column=1, row=3)

# Buttons
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
