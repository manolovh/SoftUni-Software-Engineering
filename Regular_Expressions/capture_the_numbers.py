import re

pattern = r'\d+'

while True:
    inp = input()

    if not inp:
        break

    result = re.findall(pattern, inp)

    if len(result) > 0:
        print(' '.join(result), end=' ')
