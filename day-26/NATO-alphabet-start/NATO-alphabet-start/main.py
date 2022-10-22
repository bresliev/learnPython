
import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

word = list(input("Enter the word, please: "))

df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)
nato_alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}
nato_coded = ''
for letter in word:
    nato_coded += '-'
    nato_coded += nato_alphabet_dict[letter.upper()]
nato_coded = nato_coded.lstrip('-').rstrip('-')

print(nato_coded)


# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#
