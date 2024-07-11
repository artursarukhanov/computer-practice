import numpy as np

def f2(x, y):
    return y**(-2*x) * np.sin(x)

def rectangle_method(f, a, b, n, y):
    h = (b - a) / n
    result = sum(f(a + i*h, y) for i in range(n))
    return result * h

def trapezoidal_method(f, a, b, n, y):
    h = (b - a) / n
    result = 0.5 * (f(a, y) + f(b, y)) + sum(f(a + i*h, y) for i in range(1, n))
    return result * h

def simpson_method(f, a, b, n, y):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    result = f(a, y) + f(b, y)
    for i in range(1, n, 2):
        result += 4 * f(a + i*h, y)
    for i in range(2, n-1, 2):
        result += 2 * f(a + i*h, y)
    return result * h / 3

a, b = 0, 100
n = 100000
y = 2

rectangle_result = rectangle_method(f2, a, b, n, y)
trapezoidal_result = trapezoidal_method(f2, a, b, n, y)
simpson_result = simpson_method(f2, a, b, n, y)

print(f"Rectangle Method: {rectangle_result}")
print(f"Trapezoidal Method: {trapezoidal_result}")
print(f"Simpson Method: {simpson_result}")
