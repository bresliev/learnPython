from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if not ws_entry.get() or not email_entry.get() or not password_entry.get() is None:
        messagebox.showerror(title="Error", message="All the fields are mandatory. Please, enter value for each field.")
    else:
        is_ok = messagebox.askokcancel(title=ws_entry.get(),
                                       message=f"These are details entered: \nEmail: {email_entry.get()} "
                                               f"\nPassword: {password_entry.get()} \nIsi it OK to save?")
        if is_ok:
            with open("data.txt", "a") as passwords:
                passwords.writelines(f"{ws_entry.get()} |{email_entry.get()} | {password_entry.get()}\n")
                ws_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            ws_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manger")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0)

label_ws = Label(text="Website:")
label_ws.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

ws_entry = Entry(width=35)
ws_entry.grid(column=1, row=1, columnspan=2, sticky="w")
ws_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "nikola.bresliev@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w")

button_generate = Button(text="Generate Password", command=gen_pass)
button_generate.grid(column=2, row=3, sticky="w")

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
