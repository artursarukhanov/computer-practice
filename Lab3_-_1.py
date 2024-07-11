import numpy as np

def f1(x):
    return x**4 / (1 + x**2)

def rectangle_method(f, a, b, n):
    h = (b - a) / n
    result = sum(f(a + i*h) for i in range(n))
    return result * h

def trapezoidal_method(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b)) + sum(f(a + i*h) for i in range(1, n))
    return result * h

def simpson_method(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n, 2):
        result += 4 * f(a + i*h)
    for i in range(2, n-1, 2):
        result += 2 * f(a + i*h)
    return result * h / 3

a, b = 1, 2
n = 1000

rectangle_result = rectangle_method(f1, a, b, n)
trapezoidal_result = trapezoidal_method(f1, a, b, n)
simpson_result = simpson_method(f1, a, b, n)

print(f"Rectangle Method: {rectangle_result}")
print(f"Trapezoidal Method: {trapezoidal_result}")
print(f"Simpson Method: {simpson_result}")
