input_line = input()

phonebook = {}
while not input_line.isnumeric():
    details = input_line.split('-')
    name = details[0]
    phone = details[1]
    phonebook[name] = phone

    input_line = input()

for _ in range(int(input_line)):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f'Contact {name} does not exist.')
