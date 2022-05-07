command = input()

course_dict = dict()
while command != 'end':
    course_name, student_name = command.split(' : ')
    if course_name not in course_dict:
        course_dict[course_name] = [student_name]
    else:
        course_dict[course_name] += [student_name]

    command = input()

for course in course_dict:
    print(f"{course}: {len(course_dict[course])}")
    for student in course_dict[course]:
        print(f"-- {student}")
