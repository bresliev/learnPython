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
COUNTER_START = 5
count_downs = 0
checks = ''
after = ''


# ---------------------------- TIMER RESET ------------------------------- #
def action_start():
    count = WORK_MIN
    count_down(count)


def action_reset():
    print("Evo ga konstatuje")
    window.after_cancel(id=after)
    canvas.itemconfig(timer_text, text=f"00:00")
    global count_downs
    global checks
    check_marks = Label(text=checks, fg=GREEN, bg=YELLOW)
    check_marks.grid(column=1, row=4)


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global count_downs
    global checks
    global after

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        after = window.after(1000, count_down, count - 1)
    else:
        count_downs += 1
        print(f"count downs : {count_downs}")
        if count_downs == 0 or count_downs % 2 == 0:
            count = WORK_MIN
            checks += "✔"
            check_marks = Label(text=checks, fg=GREEN, bg=YELLOW)
            check_marks.grid(column=1, row=4)
        elif count_downs % 2 != 0 and count_downs != 7:
            count = SHORT_BREAK_MIN
        else:
            count = LONG_BREAK_MIN
            count_downs = 0
        after = window.after(1000, count_down, count)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
label.grid(column=1, row=0)

# calls action() when pressed
start_button = Button(text="Start", command=action_start)
start_button.grid(column=0, row=4)

# calls action() when pressed
reset_button = Button(text="Reset", command=action_reset)
reset_button.grid(column=2, row=4)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

window.mainloop()
