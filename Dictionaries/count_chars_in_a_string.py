text = input().split(' ')

char_dict = {}
for word in text:
    for char in word:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

for char in char_dict:
    print(f"{char} -> {char_dict[char]}")