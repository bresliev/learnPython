# import random, art and game_data
import random
import art
import game_data
#show the logo
print(art.logo)
# create a two elemnts array for the current competiotors
a_vs_b = []
# write a function to select an element from the game data but not one of the already chosen
def chose_an_element():
    element = random.randint(0, len(game_data.data))
    while element in a_vs_b:
        chose_an_element()
        return game_data.data[element]

#at the begining of the game insert two elements in to the competitors array
a_vs_b.append(chose_an_element())
a_vs_b.append(chose_an_element())

print(a_vs_b)