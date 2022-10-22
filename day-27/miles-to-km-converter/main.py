from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")


# Entries
entry = Entry(width=30)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

# Labels Miles
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

# Labels is equal to
label_eq = Label(text="is equal to ")
label_eq.grid(column=0, row=1)

# Labels is equal to
label_result = Label(text="0")
label_result.grid(column=1, row=1)

# Labels km
label = Label(text="Km")
label.grid(column=2, row=1)


def action():
    print(entry.get())
    print(type(entry.get()))
    label_result.config(text=float(entry.get())*1.6)


# calls action() when pressed
new_button = Button(text="Click Me New", command=action)
new_button.grid(column=1, row=2)

window.mainloop()
