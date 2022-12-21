import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
Timer = None

def reset():
    global reps
    window.after_cancel(Timer)
    canvas.itemconfig(timer, text="00:00")
    title.config(text="Work")
    checkmark.config(text="")
    reps = 0
    
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break)
        title.config(text="20min Break", fg=PINK)
    elif reps % 2 == 0: 
        count_down(short_break)
        title.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)

def count_down(count):
    mins = math.floor(count / 60)
    secs = count % 60
    if mins < 10:
        mins = f"0{mins}"
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(timer, text=f"{mins}:{secs}")
    if count > 0:
        global Timer
        Timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        checkmark.config(text=mark)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 140, text="00:00", fill="#fff", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start",bg=YELLOW, highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset)
reset_btn.grid(column=2, row=2)

checkmark = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36))
checkmark.grid(column=1, row=3)

window.mainloop()