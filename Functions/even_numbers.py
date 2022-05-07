def even_numbers(number_string):
    split_string = number_string.split(' ')
    num_list = list()
    for number in split_string:
        num_list.append(int(number))
    evens = filter(lambda x: x % 2 == 0, num_list)
    return list(evens)


number_string = input()
print(even_numbers(number_string))
