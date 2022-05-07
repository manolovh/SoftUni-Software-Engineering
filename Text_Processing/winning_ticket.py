tickets = input().split(', ')

is_valid = False
for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
    else:
        for char in ['@', '#', '$', '^']:
            if char * 6 in ticket[:len(ticket) / 2] and char * 6 in ticket[len(ticket) / 2:]:
                is_valid = True
                break
            else:
                is_valid = False
