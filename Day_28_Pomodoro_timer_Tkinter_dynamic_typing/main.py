import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Text_timer.config(text="Timer", font=("Arial", 50), bg=YELLOW, fg=GREEN)
    Check_box.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        Text_timer.config(text="Break", font=("Arial", 50), bg=YELLOW, fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        Text_timer.config(text="Break", font=("Arial", 50), bg=YELLOW, fg=PINK)
    else:
        count_down(work_sec)
        Text_timer.config(text="Work", font=("Arial", 50), bg=YELLOW, fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✓"
            Check_box.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Arial", 35, "bold"))
canvas.grid(column=2, row=2)

button_start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
button_start.grid(column=0, row=3)

button_reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
button_reset.grid(column=3, row=3)

Check_box = Label(text="", font=("Arial", 50), bg=YELLOW, fg=GREEN)
Check_box.grid(column=2, row=4)

Text_timer = Label(text="Timer", font=("Arial", 50), bg=YELLOW, fg=GREEN)
Text_timer.grid(column=2, row=0)

window.mainloop()
