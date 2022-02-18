
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

import pandas
import time

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
time.sleep(9999)
#the sleep function is to stop the console from closing after encoding the plain text
