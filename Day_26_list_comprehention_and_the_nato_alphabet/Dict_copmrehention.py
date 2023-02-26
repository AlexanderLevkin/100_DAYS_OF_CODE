import random
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# students_score = {new_key:new_value for item in list}
students_score = {student: random.randint(1, 100) for student in names}
print(students_score)

passed_students = {student: score for (student, score) in students_score.items() if score >= 70}
print(passed_students)
