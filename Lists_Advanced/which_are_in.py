first_sequence = input().split(', ')
second_sequence = input().split(', ')

substrings = []
for string in first_sequence:
    if any(string in str for str in second_sequence):
        substrings.append(string)
print(substrings)
