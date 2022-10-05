# import turtle
#
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("triangle")
# timmy.color("DarkOliveGreen4")
#
# my_screen = turtle.Screen()
# timmy.forward(75)
# print(my_screen.getshapes())
# my_screen.exitonclick()
#

from prettytable import PrettyTable

table = PrettyTable()
# # table.field_names = [
# #     "Pokemon name",
# #     "Style"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)

