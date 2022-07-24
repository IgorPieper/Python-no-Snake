import pandas

panda_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in panda_alphabet.iterrows()}

word = input("Enter a word: ").upper()

result = [nato_alphabet[letter] for letter in word]

print(result)
