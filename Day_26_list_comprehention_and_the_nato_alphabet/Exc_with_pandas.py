import pandas

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
