def palindrome_check(integers_list):
    for num in integers_list:
        if num == num[::-1]:
            print('True')
        else:
            print('False')


integers_list = input().split(', ')

palindrome_check(integers_list)