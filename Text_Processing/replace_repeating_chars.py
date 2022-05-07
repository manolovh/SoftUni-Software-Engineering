text = input()

letter_list = ['']

for char in text:
    if letter_list[-1] != char:
        letter_list.append(char)

print(''.join(letter_list))