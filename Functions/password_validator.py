def password_validator(password):
    is_valid_length = False
    is_alnum = True
    is_enough_nums = False
    nums = 0
    if 6 <= len(password) <= 10:
        is_valid_length = True

    for char in password:
        if not char.isalnum():
            is_alnum = False
        if char.isnumeric():
            nums += 1

    if nums >= 2:
        is_enough_nums = True

    if is_valid_length and is_alnum and is_enough_nums:
        print("Password is valid")
    else:
        if not is_valid_length:
            print("Password must be between 6 and 10 characters")
        if not is_alnum:
            print("Password must consist only of letters and digits")
        if not is_enough_nums:
            print("Password must have at least 2 digits")


password = input()

password_validator(password)