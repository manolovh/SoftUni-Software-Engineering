input_words = input().split(' ')

numbers = []
letters = []
for word in input_words:
    current_nums = []
    current_chars = []
    for char in word:
        if char.isdigit():
            current_nums.append(char)
        else:
            current_chars.append(char)
    numbers.append(current_nums)
    letters.append(current_chars)

for i in range(len(input_words)):
    letters[i][0], letters[i][-1] = letters[i][-1], letters[i][0]
    current_word = chr(int(''.join(numbers[i]))) + ''.join(letters[i])
    print(current_word, end=' ')
