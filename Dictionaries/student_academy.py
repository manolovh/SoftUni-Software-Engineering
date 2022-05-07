grade_pair_count = int(input())

grades_dict = dict()
grades_per_person = dict()
for _ in range(grade_pair_count):
    name = input()
    grade = float(input())
    if name not in grades_dict:
        grades_dict[name] = grade
        grades_per_person[name] = 1
    else:
        grades_dict[name] += grade
        grades_per_person[name] += 1

final_grades = grades_dict.copy()
for student, grade in grades_dict.items():
    if grades_dict[student] / grades_per_person[student] < 4.5:
        final_grades.pop(student)

for student, grade in final_grades.items():
    print(f"{student} -> {grade / grades_per_person[student]:.2f}")