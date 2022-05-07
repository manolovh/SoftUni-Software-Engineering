items = input().split(', ')
command = input()

while command != 'Craft!':
    current_command = command.split(' - ')
    action = current_command[0]
    item = current_command[1]

    if action == 'Collect' and item not in items:
        items.append(item)
    elif action == 'Drop' and item in items:
        items.remove(item)
    elif action == 'Combine Items':
        item_to_swap = item.split(':')
        item_1 = item_to_swap[0]
        item_2 = item_to_swap[1]
        if item_1 in items:
            index = items.index(item_1)
            items.insert(index + 1, item_2)
    elif action == 'Renew':
        items.append(item)
        items.remove(item)

    command = input()

print(*items, sep=', ')
