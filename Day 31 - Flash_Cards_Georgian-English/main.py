import pandas as pd
from tkinter import *
from random import choice

BG_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    all_data = pd.read_csv("data/ge.csv")
    to_learn = all_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(title, text="Georgian", fill="#000")
    canvas.itemconfig(word, text=current_card["Georgian"], fill="#000")
    canvas.itemconfig(card_bg, image=font_bg)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title, text="English", fill="#fff")
    canvas.itemconfig(word, text=current_card["English"], fill="#fff")
    canvas.itemconfig(card_bg, image=back_bg)

def done():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash Cards - Georgian-English")
window.config(padx=50, pady=50, bg=BG_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=562)
font_bg = PhotoImage(file="images/card_front.png")
back_bg = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=font_bg)
canvas.config(bg=BG_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, text="Title", font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text="text", font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)
# Buttons
left_img = PhotoImage(file="images/wrong.png")
left_btn = Button(image=left_img, highlightthickness=0, cursor="hand1", command=next_card)
left_btn.grid(column=0, row=1)
right_img = PhotoImage(file="images/right.png")
checkmark = Button(image=right_img, highlightthickness=0, cursor="hand1", command=done)
checkmark.grid(column=1, row=1)

next_card()
window.mainloop()