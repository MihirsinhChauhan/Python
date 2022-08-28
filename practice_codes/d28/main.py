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
    global timer,reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    time_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=("Courier", 32, "bold"))
    check_label.config(text="")
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    WORK_SEC = WORK_MIN * 60
    SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
    LONG_BREAK_SEC = LONG_BREAK_MIN * 60

    reps += 1
    if not reps % 2 == 0:
        time_label.config(text="Work", fg=GREEN, bg=YELLOW, font=("Courier", 32, "bold"))
        count_down(WORK_SEC)
        global check

    elif reps % 8 == 0:
        time_label.config(text="Long Break", fg=RED, bg=YELLOW, font=("Courier", 32, "bold"))
        count_down(LONG_BREAK_SEC)
    else:
        time_label.config(text="Break", fg=PINK, bg=YELLOW, font=("Courier", 32, "bold"))
        count_down(SHORT_BREAK_SEC)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        canvas.itemconfig(timer_text, text=f"{count_min}:{0}{count_sec}")
    else:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            global check
            check_label.config(text=check)
            check += "✔"


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

time_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Courier", 32, "bold"))
time_label.grid(row=0, column=1)

start_buttton = Button(text="Start", highlightthickness=0, command=start_timer)
start_buttton.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0 ,command=reset_timer)
reset_button.grid(row=2, column=2)

check = "✔"
check_label = Label(fg=GREEN, bg=YELLOW, font=("Courier", 12, "bold"))
check_label.grid(row=3, column=1)

window.mainloop()
