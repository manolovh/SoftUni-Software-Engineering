names = input().split(', ')

for name in range(len(names)):
    if not 3 <= len(names[name]) <= 16:
        names[name] = ''
    else:
        for char in names[name]:
            if char not in 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789-_':
                names[name] = ''
for name in names:
    if name != '':
        print(name)