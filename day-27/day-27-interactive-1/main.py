from tkinter import *
import playground

def button_clicked():
    my_label.config(text=input.get())
    # my_label.pack()

window = Tk()
window.title("My first tkinter")
window.minsize(width=500, height=300)

playground.calculate(2, add=3, miulti=6)

my_car = playground.Car(make="Mazda", model="CX-30", color="Soul red")
print(my_car.make)
print(my_car.model)
print(my_car.color)

my_label = Label(text=f"The value is {playground.add(1, 2, 3, 4)}", font=("Arial", 24, "bold italic"))
my_label.config(text="New Text")
my_label.pack()

input = Entry(width=20)
print(input.get())
input.pack()

button = Button(text="Click me", command=button_clicked)
button.pack()

window.mainloop()
