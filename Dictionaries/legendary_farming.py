special_word = ''

key_materials = {}
junk = {}
while not special_word:
    material_case_sens = input().split(' ')
    materials = list(map(lambda x:x.lower(), material_case_sens))
    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i + 1]

        # if material == 'shards' or material == 'fragments' or material == 'motes':
        if material in ['shards', 'fragments', 'motes']:
            if material not in key_materials:
                key_materials[material] = quantity
            else:
                key_materials[material] += quantity

            key_list = list(key_materials.keys())
            val_list = list(key_materials.values())
            for val in key_materials.values():
                if val > 250:
                    special_word = key_list[val_list.index(val)]
                    break
                elif val == 250:
                    special_word = key_list[val_list.index(val)]
                    break
        else:
            if material not in junk:
                junk[material] = quantity
            else:
                junk[material] += quantity

if special_word == 'fragments':
    print("Valanyr obtained!")
    key_materials['fragments'] -= 250
elif special_word == 'shards':
    print("Shadowmourne obtained!")
    key_materials['shards'] -= 250
elif special_word == 'motes':
    print("Dragonwrath obtained!")
    key_materials['motes'] -= 250

shards = key_materials.get('shards')
fragments = key_materials.get('fragments')
motes = key_materials.get('motes')
if shards is None:
    print("shards: 0")
else:
    print(f"shards: {shards}")
if fragments is None:
    print("fragments: 0")
else:
    print(f"fragments: {fragments}")
if motes is None:
    print("motes: 0")
else:
    print(f"motes: {motes}")

for key, value in junk.items():
    print(f"{key}: {value}")
