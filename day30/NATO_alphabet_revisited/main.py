import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

def get_phonetic():
    word = input("Please enter a word: ")
    try:
        word_nato = [nato_dict[letter] for letter in word.upper()]
    except KeyError:
        print("Error: word contains non-alphabetic characters")
        get_phonetic()
    else:
        print(word_nato)
        entering_word = False

get_phonetic()