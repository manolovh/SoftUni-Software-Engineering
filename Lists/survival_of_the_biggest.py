# MY SOLUTION
numbers = input()
numbers_to_remove = int(input())

new_list = [int(n) for n in numbers.split(' ')]

sorted_list = sorted(new_list)
index = 0
for n in range(numbers_to_remove):
    new_list.remove(sorted_list[index])
    index += 1

print(*new_list, sep=', ')


# LECTOR'S SOLUTION
nums = input().split(' ')
copy_nums = list(map(int, nums))
count = int(input())

for _ in range(count):
    current_min_element = min(copy_nums)
    nums.remove(str(current_min_element))
    copy_nums.remove(current_min_element)

print(', '.join(nums))