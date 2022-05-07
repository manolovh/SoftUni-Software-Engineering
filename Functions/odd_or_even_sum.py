def odd_and_even_sum(num):
    odd_sum = 0
    even_sum = 0
    for char in num:
        if int(char) % 2 == 0:
            even_sum += int(char)
        else:
            odd_sum += int(char)
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


num = input()
print(odd_and_even_sum(num))