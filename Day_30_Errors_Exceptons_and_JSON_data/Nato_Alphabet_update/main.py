import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


def nato_alph():
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    print(phonetic_dict)

    word = input("Enter a word: ").upper()
    output_list = [phonetic_dict[letter] for letter in word]
    print(output_list)


var_catch = True

while var_catch:
    try:
        nato_alph()
        var_catch = False

    except KeyError:
        print("Sorry, only letters in alphabet please!")

