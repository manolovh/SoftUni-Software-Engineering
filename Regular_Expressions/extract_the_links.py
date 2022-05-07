# SOLVED IT 80/100, I AM MESSING UP THE UNDERSCORE CASES
# SOMEWHERE, TRIED 2-3 WAYS TO CHANGE IT BUT IT DID NOT WORK

import re

while True:
    text = input()
    if text == '':
        break
    pattern = r'(www.)(([^_]-?[a-zA-z0-9+]+)+)((\.+[a-zA-z]+)+)'

    emails = re.finditer(pattern, text)
    for email in emails:
        pattern1 = rf'{email[1]}{email[2]}{email[4]}'
        if email[4] is not None:
            print(pattern1)
            