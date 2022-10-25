import pandas

def encode():
    word = list(input("Enter the word, please: "))
    print(word)
    df = pandas.read_csv("nato_phonetic_alphabet.csv")
    nato_alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}
    print(nato_alphabet_dict)
    nato_coded = ''
    for letter in word:
        print(f"Das ist word: {word}")
        try:
            code = nato_alphabet_dict[letter.upper()]
            print(f"Letter is {letter.upper()} and the code is {code}")
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
            nato_coded = ''
            word.clear()
            encode()
        else:
            print(f"Working for letter {letter.upper()} and the code is {code}")
            nato_coded += code
            nato_coded += '-'
            print(f"So, it is added {nato_coded}")
    final_string = nato_coded.strip('-').rstrip('-')
    print(f"Abd the final string is {final_string}")
    return final_string


print(f"evo printamo {encode()}")

