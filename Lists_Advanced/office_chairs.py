number_of_rooms = int(input())

free_chairs = 0
room_number = 0
for room in range(number_of_rooms):
    current_room = input().split(' ')
    current_chairs = len(current_room[0])
    current_visitors = int(current_room[1])
    room_number += 1

    if current_chairs >= current_visitors:
        free_chairs += current_chairs - current_visitors
    else:
        print(f'{current_visitors - current_chairs} more chairs needed in room {room_number}')
        free_chairs -= current_visitors - current_chairs

if free_chairs >= 0:
    print(f'Game On, {free_chairs} free chairs left')