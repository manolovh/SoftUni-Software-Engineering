import re

text = input()

user_pattern = r'( |^)[a-zA-Z0-9]+((\.|\_\-)[A-Za-z0-9]+)*'
host_pattern = r'[A-Za-z]+(-[a-zA-z]+)*(\.[A-Za-z]+(-[a-zA-Z]+)*)+'

pattern = rf'{user_pattern}@{host_pattern}'

emails = re.finditer(pattern, text)

for email in emails:
    print(email[0])
