student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

student_dict = {
    "students": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries

# for (key, value) in student_dict.items():
#     print(value)

student_date_frame = pandas.DataFrame(student_dict)
print(student_date_frame)


for (index, row) in student_date_frame.iterrows():
    print(row.students)

for (index, row) in student_date_frame.iterrows():
    if row.students == "Angela":
        print(row.score)
# TODO 1. Create a dictionary in this format:

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row["letter"]: row["code"] for (index, row) in nato_data.iterrows()}
print(nato_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Give me some word: ").upper()
print(user_word)

result = [nato_dict[letter] for letter in user_word]

print(result)