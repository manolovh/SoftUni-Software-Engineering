def smallest_of_three(num_list):
    return min(num_list)


num_list = []
for i in range(3):
    current_num = int(input())
    num_list.append(current_num)

print(smallest_of_three(num_list))