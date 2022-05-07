def chars_in_range(first, second):
    range1 = ord(first)
    range2 = ord(second)
    char_string = ''
    for i in range(range1 + 1, range2):
        char_string += chr(i) + ' '
    return char_string


first = input()
second = input()
print(chars_in_range(first, second))
