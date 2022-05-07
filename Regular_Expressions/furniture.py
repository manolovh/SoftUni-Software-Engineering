import re


def furniture_info():

    command = input()
    total_price = 0
    current_list = []

    while command != 'Purchase':
        pattern = r'>>([a-zA-z]+)<<(\d+|\d+\.\d+)!(\d+)'

        result = re.match(pattern, command)

        if result is not None:
            product = result[1]
            price = float(result[2])
            quantity = float(result[3])
            total_price += price * quantity
            current_list.append(product)

        command = input()

    print("Bought furniture:")
    if total_price > 0:
        print('\n'.join(current_list))
    print(f"Total money spend: {total_price:.2f}")

furniture_info()