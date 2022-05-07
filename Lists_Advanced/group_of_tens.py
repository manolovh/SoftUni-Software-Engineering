input_line = input().split(', ')

initial_group = 10
while len(input_line) > 0:
    current_list = [int(i) for i in input_line if int(i) <= initial_group]
    current_group = []
    for element in current_list:
        if int(element) <= initial_group:
            current_group.append(int(element))
            input_line.remove(str(element))
    print(f"Group of {initial_group}'s: {current_group}")
    initial_group += 10
