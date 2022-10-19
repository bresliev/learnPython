# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
import importlib

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
OUTPUT_FOLDER = "./Output/ReadyToSend"
INPUT_FOLDER = "./Input"

with open(F"{INPUT_FOLDER}/Names/invited_names.txt") as names_file:
    invated_lines = names_file.readlines()

invated_lines = [i.strip(chr(10)) for i in invated_lines]

with open(F"{INPUT_FOLDER}/Letters/starting_letter.txt") as output_file:
    text = output_file.read()

for line in invated_lines:
    text = text.replace(PLACEHOLDER, line)
    print(text)
    output_file = open(f"{OUTPUT_FOLDER}/Dear_{line}_invitation.txt", "w")
    output_file.write(text)

