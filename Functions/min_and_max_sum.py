def min_max_and_sum(numbers):
    nums = numbers.split(' ')
    num_list = list()
    for n in nums:
        num_list.append(int(n))
    return f'The minimum number is {min(num_list)}\n' \
           f'The maximum number is {max(num_list)}\n' \
           f'The sum number is: {sum(num_list)}'


numbers = input()
print(min_max_and_sum(numbers))
