def perfect_number(number):
    sum_of_nums = 0
    for num in range(1, number):
        if number % num == 0:
            sum_of_nums += num
    if number == sum_of_nums:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_number(number))
