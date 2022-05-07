command = input()

products = dict()
product_price = dict()
while command != 'buy':
    name, price, quantity = command.split(' ')
    price = float(price)
    quantity = int(quantity)
    if name not in products:
        products[name] = quantity
        product_price[name] = price
    else:
        products[name] += quantity
        product_price[name] = price

    command = input()

for product, quantity in products.items():
    print(f"{product} -> {quantity * product_price[product]:.2f}")

