energy = 100
coins = 100

events = input()
event_types = events.split('|')

day_done = True
for event in event_types:
    event_contents = event.split('-')
    event_type = event_contents[0]
    event_value = int(event_contents[1])

    if event_type == 'rest':
        if energy < 100:
            if 100 - energy <= event_value:
                energy = 100
            else:
                energy += event_value
            print(f'You gained {100 - (energy + event_value)} energy.')
        else:
            print(f'You gained 0 energy.')
        print(f'Current energy: {energy}.')
    elif event_type == 'order':
        if energy - 30 >= 0:
            coins += event_value
            energy -= 30
            print(f'You earned {event_value} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins >= event_value:
            print(f'You bought {event_type}.')
            coins -= event_value
        else:
            print(f"Closed! Cannot afford {event_type}.")
            day_done = False
            break

if day_done:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
