sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
list_of_words = sentence.split()

print(list_of_words)

list_of_dict = {word: len(word) for word in list_of_words}

print(list_of_dict)
# print(result)
