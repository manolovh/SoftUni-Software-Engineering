import re

pattern = r'\b_([A-Za-z0-9]+)\b'

inp = input()

result = re.findall(pattern, inp)

print(','.join(result))
