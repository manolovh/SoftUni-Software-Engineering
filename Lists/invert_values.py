# MY SOLUTION
string = input()

string_list = string.split(' ')
new_list = []
for string in string_list:
    if '-' in string:
        stripped = string.strip('-')
        new_string = '+' + stripped
    else:
        new_string = '-' + string
    new_list.append(int(new_string))

print(new_list)


# LECTOR'S SOLUTION
string = input()

string_list = string.split(' ')
new_list = []

for string in string_list:
    if int(string) > 0:
        new_list.append(-int(string))
    else:
        new_list.append(abs(int(string)))

print(new_list)
