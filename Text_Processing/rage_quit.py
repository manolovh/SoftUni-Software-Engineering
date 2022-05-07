input_string = input()

previous_index = 0
symbols = []
for symbol in input_string:
    if not symbol.isnumeric() and symbol.lower() not in symbols:
        symbols.append(symbol.lower())
print(f"Unique symbols used: {len(symbols)}")

for i in range(len(input_string)):
    if input_string[i].isnumeric():
        print((input_string[previous_index:i] * int(input_string[i])).upper(), end='')
        previous_index = i + 1
