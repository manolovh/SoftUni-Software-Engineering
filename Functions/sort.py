def sort_nums(numbers):
    nums = numbers.split(' ')
    number_list = []
    for i in nums:
        number_list.append(int(i))
    return sorted(number_list)


numbers = input()
print(sort_nums(numbers))
