import tkinter

window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(600, 600)

#Lable

my_lable = tkinter.Label(text="I am a lable", font=("Arial", 24, "bold"))

my_lable.pack()




window.mainloop()