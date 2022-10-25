<<<<<<< HEAD
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
=======
import random
import time
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"


def flip_card():
    canvas.itemconfigure(language, text="English", fill="white")
    canvas.itemconfigure(word_text, text=word_to_guess["English"], fill="white")
    canvas.itemconfigure(canvas_image, image=card_back_img)


def next_card():
    global word_to_guess
    global flip_timer
    window.after_cancel(flip_timer)
    word_to_guess = random.choice(df_as_dict)
    canvas.itemconfigure(canvas_image, image=card_front_img)
    canvas.itemconfigure(word_text, text=word_to_guess["French"], fill="black")
    canvas.itemconfigure(language, text="French", fill="black")
    flip_timer = window.after(3000, flip_card)


def guess():
    df_as_dict.remove(word_to_guess)
    df_words_to_learn = pandas.DataFrame(df_as_dict)
    df_words_to_learn.to_csv("words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
window.title("Flash card")
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=562)
card_front_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_back_img = PhotoImage(file="images/card_back.png")
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

try:
    df = pandas.read_csv("words_to_learn.csv")
    print("ima obradjenihg")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
    print("citam original")

df_as_dict = df.to_dict(orient="records")

word_to_guess = {}

btn_wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=btn_wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

btn_right_image = PhotoImage(file="images/right.png")
btn_right = Button(image=btn_right_image, highlightthickness=0, command=guess)
btn_right.grid(column=1, row=1)

next_card()

window.mainloop()
>>>>>>> main
