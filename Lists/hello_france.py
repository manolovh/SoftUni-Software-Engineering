items = input()
budget = float(input())

budget_copy = budget
items_list = items.split('|')
bought_items_price = 0
bought_items = []

for item in items_list:
    split_item = item.split('->')
    item_type = split_item[0]
    item_value = float(split_item[1])
    if budget_copy >= item_value:
        if (item_type == 'Clothes' and item_value <= 50) or (item_type == 'Shoes' and item_value <= 35) \
                or (item_type == 'Accessories' and item_value <= 20.5):
            budget_copy -= item_value
            bought_items_price += item_value
            bought_items.append(item_value)

for value in bought_items:
    print(f"{float(value) * 1.4:.2f}", end=' ')
print()

final_money = bought_items_price * 1.4 + budget_copy
profit = abs(final_money - budget)

print(f'Profit: {profit:.2f}')
if final_money >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')