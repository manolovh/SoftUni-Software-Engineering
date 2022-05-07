string = input()
# dash_count = 0
# for char in string:
#     if char == '>':
#         dash_count += 1
explosion_power = 0
for i in range(len(string)):
    if string[i] == '>':
        explosion_power += int(string[i + 1])
        explosion_range = explosion_power

        if '>' not in string[i + 1: i + explosion_power + 1]:
            string = string.replace(string[i + 1: i + explosion_power + 1], ' ', 1)
            explosion_power = 0
        else:
            for char in string[i + 1:]:
                index = i + 1
                if char != '>':
                    string = string.replace(string[index], ' ', 1)
                    explosion_power -= 1
                else:
                    break
    if '>' not in string[i:]:
        break

string = string.split(' ')
print(''.join(string))
