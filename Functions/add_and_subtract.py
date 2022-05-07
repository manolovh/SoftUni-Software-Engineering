def add_and_subtract(a, b, c):

    def sum_numbers():
        return a + b

    def subtract_numbers():
        return sum_numbers() - c

    return subtract_numbers()


first = int(input())
second = int(input())
third = int(input())

print(add_and_subtract(first, second, third))

