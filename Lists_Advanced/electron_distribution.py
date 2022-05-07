input_electron_num = int(input())

electron_list = []
total_electrons = input_electron_num
for i in range(1, total_electrons + 1):
    if 2 * i ** 2 <= total_electrons:
        electron_list.append(2 * i ** 2)
        total_electrons -= 2 * i ** 2
    else:
        electron_list.append(total_electrons)
        break

print(electron_list)