from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    title_text.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        title_text.config(text="Timer", fg=GREEN)
        count_down(work_sec)
    elif reps % 2 == 0 and reps % 8 != 0:
        title_text.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif reps % 8 == 0:
        title_text.config(text="Break", fg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        checkmark_place.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Application")
window.config(padx=100, pady=50, bg=YELLOW)

title_text = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 35, "bold"))
title_text.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_place = Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 15, "bold"))
checkmark_place.grid(row=3, column=1)

window.mainloop()