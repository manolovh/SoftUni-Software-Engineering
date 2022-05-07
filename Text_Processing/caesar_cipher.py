input_text = input()

new_text = []
for char in input_text:
    new_text.append(chr(ord(char)+ 3))

new_string = ''
print(new_string.join(new_text))