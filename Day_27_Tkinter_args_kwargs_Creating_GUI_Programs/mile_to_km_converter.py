from tkinter import *

window = Tk()
window.minsize(width=400, height=300)
window.title("Mile to KM converter")

label_is_eq = Label(text="is equal to", font=("Arial", 18))
label_is_eq.place(x=50, y=100)

label_miles = Label(text="miles", font=("Arial", 18))
label_miles.place(x=250, y=50)

label_km = Label(text="km", font=("Arial", 18))
label_km.place(x=250, y=100)

field_of_km = Entry(width=10)
field_of_km.place(x=150, y=50)

display_result = Label(text="0", font=("Arial", 18))
display_result.place(x=150, y=100)


def converter():
    entering = field_of_km.get()
    int_ent = float(entering)
    result = int_ent * 1.609
    display_result.config(text=result)
    return result


button = Button(text="Calculate", command=converter)
button.place(x=150, y=150)

window.mainloop()
