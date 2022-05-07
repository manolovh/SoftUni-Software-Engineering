gift_names = input()
command = input()

gifts = gift_names.split(' ')
while command != 'No Money':
    command_list = command.split(' ')

    if 'OutOfStock' == command_list[0]:
        for i in range(len(gifts)):
            if gifts[i] == command_list[1]:
                gifts[i] = 'None'
    elif 'Required' == command_list[0]:
        if len(command_list) > 2 and int(command_list[2]) < len(gifts):
            gifts[int(command_list[2])] = command_list[1]
    elif 'JustInCase' == command_list[0]:
        gifts[-1] = command_list[1]
    command = input()

for gift in gifts:
    if gift == 'None':
        gifts.remove(gift)

print(*gifts)
