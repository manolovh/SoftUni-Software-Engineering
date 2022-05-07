target_sequence = input().split(' ')
target_sequence = list(map(int, target_sequence))
command = input()

while command != 'End':
    current_command = command.split(' ')
    action = current_command[0]
    index = int(current_command[1])
    value = int(current_command[2])

    if action == 'Shoot':
        if index < len(target_sequence):
            target_sequence[index] -= value
            if target_sequence[index] <= 0:
                target_sequence.pop(index)

    elif action == 'Add':
        if index < len(target_sequence):
            target_sequence.insert(index, value)
        else:
            print('Invalid placement!')

    elif action == 'Strike':
        if index < len(target_sequence) and (index + 2 * value) < len(target_sequence):
            for i in range(1 + 2 * value):
                target_sequence.pop(index - value)
        else:
            print('Strike missed!')

    command = input()

print(*target_sequence, sep='|')

