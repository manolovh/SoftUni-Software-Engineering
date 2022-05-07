number_of_commands = int(input())

database_dict = dict()
for _ in range(number_of_commands):
    command = input().split(' ')
    action = command[0]
    name = command[1]
    reg_number = ''
    if len(command) > 2:
        reg_number = command[2]

    if action == 'register':
        if name in database_dict:
            print(f"ERROR: already registered with plate number {database_dict[name]}")
        else:
            database_dict[name] = reg_number
            print(f"{name} registered {database_dict[name]} successfully")

    elif action == 'unregister':
        if name not in database_dict:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            database_dict.pop(name)

for user in database_dict:
    print(f"{user} => {database_dict[user]}")