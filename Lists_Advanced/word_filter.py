input_line = input().split(' ')

final_list = [word for word in input_line if len(word) % 2 == 0]
for word in final_list:
    print(word)