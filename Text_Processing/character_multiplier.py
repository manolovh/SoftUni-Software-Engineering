strings = input().split()

str1 = strings[0]
str2 = strings[1]

total_sum = 0
index = 0
if len(str1) <= len(str2):
    while index + 1 <= len(str1):
        total_sum += ord(str1[index]) * ord(str2[index])
        index += 1
    else:
        while len(str2) > index:
            total_sum += ord(str2[index])
            index += 1
else:
    while index + 1 <= len(str2):
        total_sum += ord(str1[index]) * ord(str2[index])
        index += 1
    else:
        while len(str1) > index:
            total_sum += ord(str1[index])
            index += 1

print(total_sum)