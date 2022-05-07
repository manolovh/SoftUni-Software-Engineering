input_line = input().split('@')
input_line = list(map(int, input_line))
command = input()

last_position = 0
current_jump = 0

while command != 'Love!':
    jump_command = command.split(' ')
    jump = jump_command[0]
    jump_length = int(jump_command[1])

    current_jump += jump_length
    if current_jump >= len(input_line):
        current_jump = 0

    if input_line[current_jump] == 0:
        print(f"Place {current_jump} already had Valentine's day.")
    elif -1 < current_jump < len(input_line):
        input_line[current_jump] -= 2
        if input_line[current_jump] == 0:
            print(f"Place {current_jump} has Valentine's day.")

    last_position = current_jump
    command = input()

result = [x for x in input_line if x == 0]

print(f"Cupid's last position was {last_position}.")
if len(result) != len(input_line):
    diff = len(input_line) - len(result)
    print(f"Cupid has failed {diff} places.")
else:
    print("Mission was successful.")
