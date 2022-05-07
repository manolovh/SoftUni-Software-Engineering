command = input()
side_dict = dict()
side_name = []
while command != 'Lumpawaroo':
    if '|' in command:
        info = command.split(' | ')
        force_side = info[0]
        force_user = info[1]

        if force_side not in side_dict and force_user not in side_dict.values():
            side_dict[force_side] = [force_user]
            side_name += [force_side]
        elif [force_user] not in side_dict.values():
            side_dict[force_side] += [force_user]

    elif '->' in command:
        info = command.split(' -> ')
        force_user = info[0]
        force_side = info[1]
        if force_side not in side_dict[force_side] and force_user not in side_dict.values():
            side_dict[force_side] = [force_user]

        if force_user not in side_dict.values():
            side_dict[force_side].append(force_user)
        else:

            if force_user in side_dict[side_name[0]]:
                side_dict[side_name[1]].append(force_user)
                side_dict[side_name[0]].remove(force_user)
            else:
                side_dict[side_name[0]].append(force_user)
                side_dict[side_name[1]].remove(force_user)

        print(f"{force_user} joins the {force_side} side!")

    command = input()

for side in side_dict:
    if len(side_dict[side]) > 0:
        print(f"Side: {side}, Members: {len(side_dict[side])}")
    for user in side_dict[side]:
        print(f"! {user}")
