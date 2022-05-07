command = input()

exam_dict = dict()
submission_count_dict = dict()
while command != 'exam finished':
    info = command.split('-')
    is_banned = False
    points = 0
    language = ''
    username = ''

    if len(info) == 2:
        username = info[0]
        is_banned = True
    else:
        username = info[0]
        language = info[1]
        points = int(info[2])

    if not is_banned:
        if username not in exam_dict:
            exam_dict[username] = points
            if language not in submission_count_dict:
                submission_count_dict[language] = 1
            else:
                submission_count_dict[language] += 1
        else:
            if exam_dict[username] < points:
                exam_dict[username] = points
            submission_count_dict[language] += 1
    else:
        exam_dict.pop(username)

    command = input()

print('Results:')
for name in exam_dict:
    print(f"{name} | {exam_dict[name]}")
print("Submissions:")
for language in submission_count_dict:
    print(f"{language} - {submission_count_dict[language]}")