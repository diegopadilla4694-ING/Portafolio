import json

student_scores = {
    'Jonathan': 88,
    'Aron': 78,
    'Pepe': 95,
    'Navarro': 75,
    'Zeferino': 60,
    'Fernando' : 100,
    'Eustacio' : 95,
    'Pedro' : 89,
    'Xavier' : 91,
    'Frank' : 100
}

student_grades = {}

for student in student_scores:
    point = student_scores[student]

    if point >= 91 and point <= 100:
       student_grades[student] = "Outstanding"
    
    elif point >= 81 and point <= 90:
       student_grades[student] = "Exceeds Expectations"

    elif point >= 71 and point <= 80:
        student_grades[student] = "Acceptable"
    
    else:
        student_grades[student] = "Fail"

print(json.dumps(student_grades, indent=4))




