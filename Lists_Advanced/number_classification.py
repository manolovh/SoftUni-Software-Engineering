input_line = input().split(', ')
input_line = list(map(int, input_line))

positives = [num for num in input_line if num >= 0]
negatives = [num for num in input_line if num < 0]
evens = [num for num in input_line if num % 2 == 0]
odds = [num for num in input_line if num % 2 != 0]

print('Positive: ', end='')
print(*positives, sep=', ')
print('Negative: ', end='')
print(*negatives, sep=', ')
print('Even: ', end='')
print(*evens, sep=', ')
print('Odd: ', end='')
print(*odds, sep=', ')
