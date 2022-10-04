# import random, art and game_data
import random
import art
import game_data
# create a two elemnts array for the current competiotors
a_vs_b = []
score = 0
choice = ''
# write a function to select an element from the game data but not one of the already chosen
def select_an_element():
    element = game_data.data[random.randint(0, len(game_data.data))]
    while element in a_vs_b:
        select_an_element()
    return element

def check_the_result():
    if ((choice == 'A' and a_vs_b[0]['follower_count'] > a_vs_b[1]['follower_count']) or
       (choice == 'B' and a_vs_b[1]['follower_count'] > a_vs_b[0]['follower_count'])):
        return True
    else:
        return False
                
def print_competition():
    print(art.logo)
    if score != 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {a_vs_b[0]['name']}, a {a_vs_b[0]['description']}, from {a_vs_b[0]['country']}   {a_vs_b[0]['follower_count']}")
    print(art.vs)
    print(f"Against B: {a_vs_b[1]['name']}, a {a_vs_b[1]['description']}, from {a_vs_b[1]['country']} {a_vs_b[1]['follower_count']}")
    choice = input("Who has more followers? Type 'A' or 'B' :")

#at the begining of the game insert two elements in to the competitors array
a_vs_b.append(select_an_element())
a_vs_b.append(select_an_element())
print_competition()

# print the selection
while check_the_result():
    #ask the player to make a choice
    score += 1
    a_vs_b[0] = a_vs_b[1]
    a_vs_b[1] = select_an_element()
    print_competition()