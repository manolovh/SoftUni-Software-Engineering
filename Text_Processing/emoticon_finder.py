input_text = input()

for i in range(len(input_text)):
    if input_text[i] == ':':
        print(f":{input_text[i + 1]}")
