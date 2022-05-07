integer_string = input()
beggars_count = int(input())

number_list = integer_string.split(', ')

number_int_list = []
for num in number_list:
    number_int_list.append(int(num))

final_list = []
for i in range(beggars_count):
    current_index = i
    if current_index > len(number_int_list) - 1:
        current_value = 0
        final_list.append(current_value)
        continue
    current_value = number_int_list[i]
    current_index += beggars_count
    while current_index < len(number_int_list):
        current_value += number_int_list[current_index]
        current_index += beggars_count
    final_list.append(current_value)

print(final_list)
