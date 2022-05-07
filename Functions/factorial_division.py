import math


def factorial_division(x, y):
    x_factorial = math.factorial(x)
    y_factorial = math.factorial(y)
    return x_factorial / y_factorial


x = int(input())
y = int(input())
print(f'{factorial_division(x, y):.2f}')
