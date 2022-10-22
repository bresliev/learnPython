import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Games")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = Turtle()
writer.hideturtle()
writer.penup()

score = 0

df = pandas.read_csv("50_states.csv")
no_of_states = df["state"].count()


def get_mouse_click_coor(x, y):
    global score

    answare_state = screen.textinput(title=f"Guess the State {score}/{no_of_states}",
                                     prompt="What's another state name?").capitalize()
    data_row = df[df.state == answare_state]
    print(x, y)
    print(data_row)
    if data_row.empty:
        print("No such a state. Clikg again!")
    else:
        if x + 20 > int(data_row.x) > x - 20 and y + 20 > int(data_row.y) > y - 20:
            writer.goto(int(data_row.x), int(data_row.y))
            writer.pendown()
            writer.write(answare_state)
            writer.penup()
            score += 1
        else:
            print("No territory marked there. Clik again!")


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
