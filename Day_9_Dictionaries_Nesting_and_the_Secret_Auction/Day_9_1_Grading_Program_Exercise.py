student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

    """Code below is exactly the same as code above  """
    # if 91 <= student_scores[student] <= 100:
    #     student_grades[student] = "Outstanding"
    # elif 81 <= student_scores[student] <= 90:
    #     student_grades[student] = "Exceeds Expectations"
    # elif 71 <= student_scores[student] <= 80:
    #     student_grades[student] = "Acceptable"
    # else:
    #     student_grades[student] = "Fail"

print(student_grades)
