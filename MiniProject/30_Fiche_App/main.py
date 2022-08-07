import tkinter
from tkinter import *
import pandas
import random

# ----------------- Data Managing --------------------- #

try:
    words = pandas.read_csv("Data/Progres_list.csv")
except FileNotFoundError:
    words = pandas.read_csv("Data/Polish_Words.csv")

try:
    en_words = words["English"]
    en_words = en_words.to_list()
except ValueError:
    words = pandas.read_csv("Data/Polish_Words.csv")
    en_words = words["English"]
    en_words = en_words.to_list()
pl_words = words["Polish"]
pl_words = pl_words.to_list()

# ----------------- Variables --------------------- #

BG_COLOR = "#B1DDC6"
chosen_word_pl = ""
chosen_word_en = ""
timer = 3
count_sec = timer * 1000

# ----------------- Word Choosing --------------------- #


def choose_word():
    if len(en_words) > 2:
        random_int = random.randint(0, (len(en_words) - 1))
        global chosen_word_pl
        chosen_word_pl = pl_words[random_int]
        global chosen_word_en
        chosen_word_en = en_words[random_int]
    else:
        chosen_word_pl = "Koniec"
        chosen_word_en = "End"
    global flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(lang, text="Polski")
    canvas.itemconfig(word, text=chosen_word_pl)
    canvas.itemconfig(card_bg, image=card_front)
    timer_mech()

# ----------------- Green Button --------------------- #


def you_know_that():
    if len(en_words) > 2:
        pl_words.remove(chosen_word_pl)
        en_words.remove(chosen_word_en)
    choose_word()


# ----------------- Text Change --------------------- #


def translate():
    canvas.itemconfig(lang, text="English")
    canvas.itemconfig(word, text=chosen_word_en)
    canvas.itemconfig(card_bg, image=card_back)


# ----------------- Timer --------------------- #


def timer_mech():
    global flip_timer
    flip_timer = window.after(count_sec, translate)


# ----------------- Basic Window Conf --------------------- #

window = Tk()
window.title("Learn Polish!!!")
window.config(padx=50, pady=50, bg=BG_COLOR)

# ----------------- Image --------------------- #

wrong = PhotoImage(file="Graphics/wrong.png")
right = PhotoImage(file="Graphics/right.png")
card_front = PhotoImage(file="Graphics/card_front.png")
card_back = PhotoImage(file="Graphics/card_back.png")

# ----------------- UI conf --------------------- #

canvas = tkinter.Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
card_bg = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

lang = canvas.create_text(400, 150, text="Polski", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text=chosen_word_pl, font=("Ariel", 60, "bold"))
flip_timer = window.after(count_sec, translate)

wrong_button = Button(image=wrong, highlightthickness=0, command=choose_word)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right, highlightthickness=0, command=you_know_that)
right_button.grid(row=1, column=1)

choose_word()

window.mainloop()

if len(en_words) > 2:
    words = {"English": en_words, "Polish": pl_words}
    words = pandas.DataFrame(words)
else:
    words = pandas.read_csv("Data/Polish_Words.csv")
words.to_csv("Data/Progress_List.csv", index=False)
