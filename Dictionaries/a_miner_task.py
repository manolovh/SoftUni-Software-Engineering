command = input()

line_count = 0
resources = {}
while command != 'stop':
    resource = command
    quantity = int(input())
    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity

    command = input()

for key, value in resources.items():
    print(f"{key} -> {value}")
    