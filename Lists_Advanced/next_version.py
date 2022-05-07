input_version = input().split('.')
first_num = int(input_version[0])
second_num = int(input_version[1])
third_num = int(input_version[2])

new_first_num = first_num
new_second_num = second_num
new_third_num = third_num

if third_num < 9:
    new_third_num += 1
elif second_num < 9:
    new_third_num = 0
    new_second_num += 1
else:
    new_second_num = 0
    new_third_num = 0
    new_first_num += 1

next_num = str(new_first_num) + '. '.join(str(new_second_num)) + '. '.join(str(new_third_num))
print(f'{new_first_num}.{new_second_num}.{new_third_num}')