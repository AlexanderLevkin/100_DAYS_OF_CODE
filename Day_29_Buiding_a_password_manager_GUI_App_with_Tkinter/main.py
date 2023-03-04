from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:", font=("Arial", 18))
website_text.grid(column=0, row=1)

email_username_text = Label(text="Email/Username:", font=("Arial", 18))
email_username_text.grid(column=0, row=2)

password_text = Label(text="Password:", font=("Arial", 18))
password_text.grid(column=0, row=3)

website_field = Entry(width=35)
website_field.grid(column=1, row=1, columnspan=2)
website_field.focus()

username_field = Entry(width=35)
username_field.grid(column=1, row=2, columnspan=2)
username_field.insert(0, "arterial888@gmail.com")

pass_field = Entry(width=18)
pass_field.grid(column=1, row=3)

generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()
