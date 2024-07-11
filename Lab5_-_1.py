import numpy as np

x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([0.0, 0.5, 0.86603, 1.0, 0.86603])

n = len(x) - 1
h = np.diff(x)
alpha = np.zeros(n)
for i in range(1, n):
    alpha[i] = 3 * (y[i+1] - y[i]) / h[i] - 3 * (y[i] - y[i-1]) / h[i-1]

l = np.zeros(n+1)
mu = np.zeros(n+1)
z = np.zeros(n+1)
l[0] = 1
mu[0] = 0
z[0] = 0

for i in range(1, n):
    l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
    mu[i] = h[i] / l[i]
    z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]

l[n] = 1
z[n] = 0
c = np.zeros(n+1)
b = np.zeros(n)
d = np.zeros(n)

for j in range(n-1, -1, -1):
    c[j] = z[j] - mu[j] * c[j+1]
    b[j] = (y[j+1] - y[j]) / h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
    d[j] = (c[j+1] - c[j]) / (3 * h[j])

def cubic_spline(x_eval, x, y, b, c, d):
    idx = np.searchsorted(x, x_eval) - 1
    if idx < 0:
        idx = 0
    elif idx >= len(x) - 1:
        idx = len(x) - 2

    dx = x_eval - x[idx]
    return y[idx] + b[idx] * dx + c[idx] * dx**2 + d[idx] * dx**3

x_eval = 1.5
spline_value = cubic_spline(x_eval, x, y, b, c, d)
print(f"Значение функции в точке x = {x_eval}: {spline_value}")
