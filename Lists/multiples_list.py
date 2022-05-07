# MY SOLUTION
factor = int(input())
count = int(input())

number_list = []
current_number = factor
for number in range(count):
    if current_number >= 0:
        number_list.append(current_number)
    current_number += factor
print(number_list)


# LECTOR'S SOLUTION
factor = int(input())
count = int(input())
number_list = []

for number in range(1, count + 1):
    number_list.append(number * factor)

print(number_list)